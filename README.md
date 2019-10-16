# URL Feature Extractor

Extracting features from URLs to build a data set for machine learning. The purpose is to find a machine learning model to predict phishing URLs, which are targeted to the Brazilian population.

This repo includes the implementation of our paper:

Lucas Dantas Gama Ayres, Italo Valcy S Brito and Rodrigo Rocha Gomes e Souza. Using Machine Learning to Automatically Detect Malicious URLs in Brazil. In Simpósio Brasileiro de Redes de Computadores e Sistemas Distribuídos (SBRC 2019) - 2019, Gramado - RS - Brazil.

The paper is available here: https://sol.sbc.org.br/index.php/sbrc/article/view/7416
DOI: https://doi.org/10.5753/sbrc.2019.7416

## Install

```bash
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install virtualenv python3 python3-dev python-dev gcc libpq-dev libssl-dev libffi-dev build-essentials
$ virtualenv -p /usr/bin/python3 .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

## How to use

Before running the software, add the API Keys to the Google Safe Browsing, Phishtank, and MyWot in the ```config.ini``` file.

Now, run:

```bash
$ python run.py <input-urls> <output-dataset>
```

## Features implemented

<table>
    <tr>
        <th style="text-align:center" colspan="4">
            <b>LEXICAL</b>
        </th>
    </tr>
    <tr>
        <td>Count (.) in URL</td>
        <td>Count (-) in URL</td>
        <td>Count (_) in URL</td>
        <td>Count (/) in URL</td>
    </tr>
    <tr>
        <td>Count (?) in URL</td>
        <td>Count (=) in URL</td>
        <td>Count (@) in URL</td>
        <td>Count (&) in URL</td>
    </tr>
    <tr>
        <td>Count (!) in URL</td>
        <td>Count ( ) in URL</td>
        <td>Count (~) in URL</td>
        <td>Count (,) in URL</td>
    </tr>
    <tr>
        <td>Count (+) in URL</td>
        <td>Count (*) in URL</td>
        <td>Count (#) in URL</td>
        <td>Count ($) in URL</td>
    </tr>
    <tr>
        <td>Count (%) in URL</td>
        <td>URL LengthL</td>
        <td>TLD amount in URL</td>
        <td>Count (.) in Domain</td>
    </tr>
    <tr>
        <td>Count (-) in Domain</td>
        <td>Count (_) in Domain</td>
        <td>Count (/) in Domain</td>
        <td>Count (?) in Domain</td>
    </tr>
    <tr>
        <td>Count (=) in Domain</td>
        <td>Count (@) in Domain</td>
        <td>Count (&) in Domain</td>
        <td>Count (!) in Domain</td>
    </tr>
    <tr>
        <td>Count ( ) in Domain</td>
        <td>Count (~) in Domain</td>
        <td>Count (,) in Domain</td>
        <td>Count (+) in Domain</td>
    </tr>
    <tr>
        <td>Count (*) in Domain</td>
        <td>Count (#) in Domain</td>
        <td>Count ($) in Domain</td>
        <td>Count (%) in Domain</td>
    </tr>
    <tr>
        <td>Domain Length</td>
        <td>Quantidade de vogais in Domain</td>
        <td>URL domain in IP address format</td>
        <td>Domain contains the key words "server" or "client"</td>
    </tr>
    <tr>
        <td>Count (.) in Directory</td>
        <td>Count (-) in Directory</td>
        <td>Count (_) in Directory</td>
        <td>Count (/) in Directory</td>
    </tr>
    <tr>
        <td>Count (?) in Directory</td>
        <td>Count (=) in Directory</td>
        <td>Count (@) in Directory</td>
        <td>Count (&) in Directory</td>
    </tr>
    <tr>
        <td>Count (!) in Directory</td>
        <td>Count ( ) in Directory</td>
        <td>Count (~) in Directory</td>
        <td>Count (,) in Directory</td>
    </tr>
    <tr>
        <td>Count (+) in Directory</td>
        <td>Count (*) in Directory</td>
        <td>Count (#) in Directory</td>
        <td>Count ($) in Directory</td>
    </tr>
    <tr>
        <td>Count (%) in Directory</td>
        <td>Directory Length</td>
        <td>Count (.) in file</td>
        <td>Count (-) in file</td>
    </tr>
    <tr>
        <td>Count (_) in file</td>
        <td>Count (/) in file</td>
        <td>Count (?) in file</td>
        <td>Count (=) in file</td>
    </tr>
    <tr>
        <td>Count (@) in file</td>
        <td>Count (&) in file</td>
        <td>Count (!) in file</td>
        <td>Count ( ) in file</td>
    </tr>
    <tr>
        <td>Count (~) in file</td>
        <td>Count (,) in file</td>
        <td>Count (+) in file</td>
        <td>Count (*) in file</td>
    </tr>
    <tr>
        <td>Count (#) in file</td>
        <td>Count ($) in file</td>
        <td>Count (%) in file</td>
        <td>File length</td>
    </tr>
    <tr>
        <td>Count (.) in parameters</td>
        <td>Count (-) in parameters</td>
        <td>Count (_) in parameters</td>
        <td>Count (/) in parameters</td>
    </tr>
    <tr>
        <td>Count (?) in parameters</td>
        <td>Count (=) in parameters</td>
        <td>Count (@) in parameters</td>
        <td>Count (&) in parameters</td>
    </tr>
    <tr>
        <td>Count (!) in parameters</td>
        <td>Count ( ) in parameters</td>
        <td>Count (~) in parameters</td>
        <td>Count (,) in parameters</td>
    </tr>
    <tr>
        <td>Count (+) in parameters</td>
        <td>Count (*) in parameters</td>
        <td>Count (#) in parameters</td>
        <td>Count ($) in parameters</td>
    </tr>
    <tr>
        <td>Count (%) in parameters</td>
        <td>Length of parameters</td>
        <td>TLD presence in arguments</td>
        <td>Number of parameters</td>
    </tr>
    <tr>
        <td>Email present at URL</td>
        <td>File extension</td>
    </tr>
</table>

<table>
    <tr>
        <th style="text-align:center" colspan="4">
            <b>BLACKLIST</b>
        </th>
    </tr>
    <tr>
        <td>Presence of the URL in blacklists</td>
        <td>Presence of the IP Address in blacklists</td>
        <td>Presence of the domain in Blacklists</td>
    </tr>
</table>

<table>
    <tr>
        <th style="text-align:center" colspan="4">
            <b>HOST</b>
        </th>
    </tr>
    <tr>
        <td>Presence of the domain in RBL (Real-time Blackhole List)</td>
        <td>Search time (response) domain (lookup)</td>
        <td>Domain has SPF?</td>
        <td>Geographical location of IP</td>
    </tr>
    <tr>
        <td>AS Number (or ASN)</td>
        <td>PTR of IP</td>
        <td>Time (in days) of domain activation</td>
        <td>Time (in days) of domain expiration</td>
    </tr>
    <tr>
        <td>Number of resolved IPs</td>
        <td>Number of resolved name servers (NameServers - NS)</td>
        <td>Number of MX Servers</td>
        <td>Time-to-live (TTL) value associated with hostname</td>
    </tr>
</table>

<table>
    <tr>
        <th style="text-align:center" colspan="4">
            <b>OTHERS</b>
        </th>
    </tr>
    <tr>
        <td>Valid TLS / SSL Certificate</td>
        <td>Number of redirects</td>
        <td>Check if URL is indexed on Google</td>
        <td>Check if domain is indexed on Google</td>
    </tr>
    <tr>
        <td>Uses URL shortener service</td>
    </tr>
</table>

## Contributing

Any contribution is appreciated.

#### Submitting a Pull Request (PR)

1. Clone the project:
  ```
  $ git clone https://github.com/lucasayres/url-feature-extractor.git
  ```

2. Make your changes in a new git branch:
  ```
  $ git checkout -b my-branch master
  ```

3. Add your changes.

4. Push your branch to Github.

5. Create a PR to master.
