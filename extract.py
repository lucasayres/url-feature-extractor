from lib.functions import *
import posixpath
import csv


def attributes():
    """Output file attributes."""
    lexical = [
        'qtd_ponto_url', 'qtd_hifen_url', 'qtd_underline_url',
        'qtd_barra_url', 'qtd_interrogacao_url', 'qtd_igual_url',
        'qtd_arroba_url', 'qtd_comercial_url', 'qtd_exclamacao_url',
        'qtd_espaco_url', 'qtd_til_url', 'qtd_virgula_url',
        'qtd_mais_url', 'qtd_asterisco_url', 'qtd_hashtag_url',
        'qtd_cifrao_url', 'qtd_porcento_url', 'qtd_tld_url',
        'comprimento_url', 'qtd_ponto_dominio', 'qtd_hifen_dominio',
        'qtd_underline_dominio', 'qtd_barra_dominio', 'qtd_interrogacao_dominio',
        'qtd_igual_dominio', 'qtd_arroba_dominio', 'qtd_comercial_dominio',
        'qtd_exclamacao_dominio', 'qtd_espaco_dominio', 'qtd_til_dominio',
        'qtd_virgula_dominio', 'qtd_mais_dominio', 'qtd_asterisco_dominio',
        'qtd_hashtag_dominio', 'qtd_cifrao_dominio', 'qtd_porcento_dominio',
        'qtd_vogais_dominio', 'comprimento_dominio', 'formato_ip_dominio',
        'server_client_dominio', 'qtd_ponto_diretorio', 'qtd_hifen_diretorio',
        'qtd_underline_diretorio', 'qtd_barra_diretorio', 'qtd_interrogacao_diretorio',
        'qtd_igual_diretorio', 'qtd_arroba_diretorio', 'qtd_comercial_diretorio',
        'qtd_exclamacao_diretorio', 'qtd_espaco_diretorio', 'qtd_til_diretorio',
        'qtd_virgula_diretorio', 'qtd_mais_diretorio', 'qtd_asterisco_diretorio',
        'qtd_hashtag_diretorio', 'qtd_cifrao_diretorio', 'qtd_porcento_diretorio',
        'comprimento_diretorio', 'qtd_ponto_arquivo', 'qtd_hifen_arquivo',
        'qtd_underline_arquivo', 'qtd_barra_arquivo', 'qtd_interrogacao_arquivo',
        'qtd_igual_arquivo', 'qtd_arroba_arquivo', 'qtd_comercial_arquivo',
        'qtd_exclamacao_arquivo', 'qtd_espaco_arquivo', 'qtd_til_arquivo',
        'qtd_virgula_arquivo', 'qtd_mais_arquivo', 'qtd_asterisco_arquivo',
        'qtd_hashtag_arquivo', 'qtd_cifrao_arquivo', 'qtd_porcento_arquivo',
        'comprimento_arquivo', 'qtd_ponto_parametros', 'qtd_hifen_parametros',
        'qtd_underline_parametros', 'qtd_barra_parametros', 'qtd_interrogacao_parametros',
        'qtd_igual_parametros', 'qtd_arroba_parametros', 'qtd_comercial_parametros',
        'qtd_exclamacao_parametros', 'qtd_espaco_parametros', 'qtd_til_parametros',
        'qtd_virgula_parametros', 'qtd_mais_parametros', 'qtd_asterisco_parametros',
        'qtd_hashtag_parametros', 'qtd_cifrao_parametros', 'qtd_porcento_parametros',
        'comprimento_parametros', 'presenca_tld_argumentos', 'qtd_parametros',
        'email_na_url', 'extensao_arquivo'
    ]

    blacklist = ['url_presente_em_blacklists', 'presenca_ip_blacklists', 'dominio_presente_em_blacklists']

    host = ['dominio_presente_em_rbl', 'tempo_resposta', 'possui_spf', 'localizacao_geografica_ip',
            'numero_as_ip', 'ptr_ip', 'tempo_ativacao_dominio', 'tempo_expiracao_dominio',
            'qtd_ip_resolvido', 'qtd_nameservers', 'qtd_servidores_mx', 'valor_ttl_associado']

    others = ['certificado_tls_ssl', 'qtd_redirecionamentos', 'url_indexada_no_google', 'dominio_indexado_no_google', 'url_encurtada']

    list_attributes = []
    list_attributes.extend(lexical)
    list_attributes.extend(blacklist)
    list_attributes.extend(host)
    list_attributes.extend(others)
    list_attributes.extend(['phishing'])

    return list_attributes


def main(urls, dataset):
    with open(dataset, "w") as output:
        writer = csv.writer(output)
        writer.writerow(attributes())
        count_url = 0
        for url in read_file(urls):
            print(url)
            count_url = count_url + 1
            dict_url = start_url(url)

            """LEXICAL"""
            # URL
            dot_url = str(count(dict_url['url'], '.'))
            hyphe_url = str(count(dict_url['url'], '-'))
            underline_url = str(count(dict_url['url'], '_'))
            bar_url = str(count(dict_url['url'], '/'))
            question_url = str(count(dict_url['url'], '?'))
            equal_url = str(count(dict_url['url'], '='))
            arroba_url = str(count(dict_url['url'], '@'))
            ampersand_url = str(count(dict_url['url'], '&'))
            exclamation_url = str(count(dict_url['url'], '!'))
            blank_url = str(count(dict_url['url'], ' '))
            til_url = str(count(dict_url['url'], '~'))
            comma_url = str(count(dict_url['url'], ','))
            plus_url = str(count(dict_url['url'], '+'))
            asterisk_url = str(count(dict_url['url'], '*'))
            hashtag_url = str(count(dict_url['url'], '#'))
            money_sign_url = str(count(dict_url['url'], '$'))
            percentage_url = str(count(dict_url['url'], '%'))
            len_url = str(length(dict_url['url']))
            email_exist = str(valid_email(dict_url['url']))
            count_tld_url = str(count_tld(dict_url['url']))
            # DOMAIN
            dot_host = str(count(dict_url['host'], '.'))
            hyphe_host = str(count(dict_url['host'], '-'))
            underline_host = str(count(dict_url['host'], '_'))
            bar_host = str(count(dict_url['host'], '/'))
            question_host = str(count(dict_url['host'], '?'))
            equal_host = str(count(dict_url['host'], '='))
            arroba_host = str(count(dict_url['host'], '@'))
            ampersand_host = str(count(dict_url['host'], '&'))
            exclamation_host = str(count(dict_url['host'], '!'))
            blank_host = str(count(dict_url['host'], ' '))
            til_host = str(count(dict_url['host'], '~'))
            comma_host = str(count(dict_url['host'], ','))
            plus_host = str(count(dict_url['host'], '+'))
            asterisk_host = str(count(dict_url['host'], '*'))
            hashtag_host = str(count(dict_url['host'], '#'))
            money_sign_host = str(count(dict_url['host'], '$'))
            percentage_host = str(count(dict_url['host'], '%'))
            vowels_host = str(count_vowels(dict_url['host']))
            len_host = str(length(dict_url['host']))
            ip_exist = str(valid_ip(dict_url['host']))
            server_client = str(check_word_server_client(dict_url['host']))
            # DIRECTORY
            if dict_url['path']:
                dot_path = str(count(dict_url['path'], '.'))
                hyphe_path = str(count(dict_url['path'], '-'))
                underline_path = str(count(dict_url['path'], '_'))
                bar_path = str(count(dict_url['path'], '/'))
                question_path = str(count(dict_url['path'], '?'))
                equal_path = str(count(dict_url['path'], '='))
                arroba_path = str(count(dict_url['path'], '@'))
                ampersand_path = str(count(dict_url['path'], '&'))
                exclamation_path = str(count(dict_url['path'], '!'))
                blank_path = str(count(dict_url['path'], ' '))
                til_path = str(count(dict_url['path'], '~'))
                comma_path = str(count(dict_url['path'], ','))
                plus_path = str(count(dict_url['path'], '+'))
                asterisk_path = str(count(dict_url['path'], '*'))
                hashtag_path = str(count(dict_url['path'], '#'))
                money_sign_path = str(count(dict_url['path'], '$'))
                percentage_path = str(count(dict_url['path'], '%'))
                len_path = str(length(dict_url['path']))
            else:
                dot_path = '?'
                hyphe_path = '?'
                underline_path = '?'
                bar_path = '?'
                question_path = '?'
                equal_path = '?'
                arroba_path = '?'
                ampersand_path = '?'
                exclamation_path = '?'
                blank_path = '?'
                til_path = '?'
                comma_path = '?'
                plus_path = '?'
                asterisk_path = '?'
                hashtag_path = '?'
                money_sign_path = '?'
                percentage_path = '?'
                len_path = '?'
            # FILE
            if dict_url['path']:
                dot_file = str(count(posixpath.basename(dict_url['path']), '.'))
                hyphe_file = str(count(posixpath.basename(dict_url['path']), '-'))
                underline_file = str(
                    count(posixpath.basename(dict_url['path']), '_'))
                bar_file = str(count(posixpath.basename(dict_url['path']), '/'))
                question_file = str(
                    count(posixpath.basename(dict_url['path']), '?'))
                equal_file = str(count(posixpath.basename(dict_url['path']), '='))
                arroba_file = str(count(posixpath.basename(dict_url['path']), '@'))
                ampersand_file = str(
                    count(posixpath.basename(dict_url['path']), '&'))
                exclamation_file = str(
                    count(posixpath.basename(dict_url['path']), '!'))
                blank_file = str(count(posixpath.basename(dict_url['path']), ' '))
                til_file = str(count(posixpath.basename(dict_url['path']), '~'))
                comma_file = str(count(posixpath.basename(dict_url['path']), ','))
                plus_file = str(count(posixpath.basename(dict_url['path']), '+'))
                asterisk_file = str(
                    count(posixpath.basename(dict_url['path']), '*'))
                hashtag_file = str(
                    count(posixpath.basename(dict_url['path']), '#'))
                money_sign_file = str(
                    count(posixpath.basename(dict_url['path']), '$'))
                percentage_file = str(
                    count(posixpath.basename(dict_url['path']), '%'))
                len_file = str(length(posixpath.basename(dict_url['path'])))
                extension = str(extract_extension(
                    posixpath.basename(dict_url['path'])))
            else:
                dot_file = '?'
                hyphe_file = '?'
                underline_file = '?'
                bar_file = '?'
                question_file = '?'
                equal_file = '?'
                arroba_file = '?'
                ampersand_file = '?'
                exclamation_file = '?'
                blank_file = '?'
                til_file = '?'
                comma_file = '?'
                plus_file = '?'
                asterisk_file = '?'
                hashtag_file = '?'
                money_sign_file = '?'
                percentage_file = '?'
                len_file = '?'
                extension = '?'
            # PARAMETERS
            if dict_url['query']:
                dot_params = str(count(dict_url['query'], '.'))
                hyphe_params = str(count(dict_url['query'], '-'))
                underline_params = str(count(dict_url['query'], '_'))
                bar_params = str(count(dict_url['query'], '/'))
                question_params = str(count(dict_url['query'], '?'))
                equal_params = str(count(dict_url['query'], '='))
                arroba_params = str(count(dict_url['query'], '@'))
                ampersand_params = str(count(dict_url['query'], '&'))
                exclamation_params = str(count(dict_url['query'], '!'))
                blank_params = str(count(dict_url['query'], ' '))
                til_params = str(count(dict_url['query'], '~'))
                comma_params = str(count(dict_url['query'], ','))
                plus_params = str(count(dict_url['query'], '+'))
                asterisk_params = str(count(dict_url['query'], '*'))
                hashtag_params = str(count(dict_url['query'], '#'))
                money_sign_params = str(count(dict_url['query'], '$'))
                percentage_params = str(count(dict_url['query'], '%'))
                len_params = str(length(dict_url['query']))
                tld_params = str(check_tld(dict_url['query']))
                number_params = str(count_params(dict_url['query']))
            else:
                dot_params = '?'
                hyphe_params = '?'
                underline_params = '?'
                bar_params = '?'
                question_params = '?'
                equal_params = '?'
                arroba_params = '?'
                ampersand_params = '?'
                exclamation_params = '?'
                blank_params = '?'
                til_params = '?'
                comma_params = '?'
                plus_params = '?'
                asterisk_params = '?'
                hashtag_params = '?'
                money_sign_params = '?'
                percentage_params = '?'
                len_params = '?'
                tld_params = '?'
                number_params = '?'

            """BLACKLIST"""
            blacklist_url = str(check_blacklists(dict_url['protocol'] + '://' + dict_url['url']))
            blacklist_ip = str(check_blacklists_ip(dict_url))
            blacklist_domain = str(check_blacklists(dict_url['protocol'] + '://' + dict_url['host']))

            """HOST"""
            spf = str(valid_spf(dict_url['host']))
            rbl = str(check_rbl(dict_url['host']))
            time_domain = str(check_time_response(dict_url['protocol'] + '://' + dict_url['host']))
            asn = str(get_asn_number(dict_url))
            country = str(get_country(dict_url))
            ptr = str(get_ptr(dict_url))
            activation_time = str(time_activation_domain(dict_url))
            expiration_time = str(expiration_date_register(dict_url))
            count_ip = str(count_ips(dict_url))
            count_ns = str(count_name_servers(dict_url))
            count_mx = str(count_mx_servers(dict_url))
            ttl = str(extract_ttl(dict_url))

            """OTHERS"""
            ssl = str(check_ssl('https://' + dict_url['url']))
            count_redirect = str(count_redirects(
                dict_url['protocol'] + '://' + dict_url['url']))
            google_url = str(google_search(dict_url['url']))
            google_domain = str(google_search(dict_url['host']))
            shortener = str(check_shortener(dict_url))

            _lexical = [
                dot_url, hyphe_url, underline_url, bar_url, question_url,
                equal_url, arroba_url, ampersand_url, exclamation_url,
                blank_url, til_url, comma_url, plus_url, asterisk_url, hashtag_url,
                money_sign_url, percentage_url, count_tld_url, len_url, dot_host,
                hyphe_host, underline_host, bar_host, question_host, equal_host,
                arroba_host, ampersand_host, exclamation_host, blank_host, til_host,
                comma_host, plus_host, asterisk_host, hashtag_host, money_sign_host,
                percentage_host, vowels_host, len_host, ip_exist, server_client,
                dot_path, hyphe_path, underline_path, bar_path, question_path,
                equal_path, arroba_path, ampersand_path, exclamation_path,
                blank_path, til_path, comma_path, plus_path, asterisk_path,
                hashtag_path, money_sign_path, percentage_path, len_path, dot_file,
                hyphe_file, underline_file, bar_file, question_file, equal_file,
                arroba_file, ampersand_file, exclamation_file, blank_file,
                til_file, comma_file, plus_file, asterisk_file, hashtag_file,
                money_sign_file, percentage_file, len_file, dot_params,
                hyphe_params, underline_params, bar_params, question_params,
                equal_params, arroba_params, ampersand_params, exclamation_params,
                blank_params, til_params, comma_params, plus_params, asterisk_params,
                hashtag_params, money_sign_params, percentage_params, len_params,
                tld_params, number_params, email_exist, extension
            ]

            _blacklist = [blacklist_url, blacklist_ip, blacklist_domain]

            _host = [rbl, time_domain, spf, country, asn, ptr, activation_time,
                     expiration_time, count_ip, count_ns, count_mx, ttl]

            _others = [ssl, count_redirect, google_url, google_domain, shortener]

            result = []
            result.extend(_lexical)
            result.extend(_blacklist)
            result.extend(_host)
            result.extend(_others)
            result.extend([''])

            writer.writerow(result)
