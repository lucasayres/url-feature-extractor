from get_database_phishtank import update_db
import argparse
import extract


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="File of URLs to be analyzed")
    parser.add_argument("output", help="Output File")
    args = parser.parse_args()

    if args.input and args.output:
        # Update phishtank database
        print('Download and update phishtank database...')
        update_db()
        # Starts extraction
        print('Starts extraction...')
        extract.main(args.input, args.output)
        print('''
#######################################
#   Dataset generated successfully!   #
#######################################
            ''')


if __name__ == "__main__":
    main()
