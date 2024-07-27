import argparse


def summary_text():
    pass

def main():

    parser = argparse.ArgumentParser(description="This is new Command-line Tool for summrizing text")

    parser_group = parser.add_argument_group('input_options', 'Enter one of the input options')
    parser_group.add_argument('--file', type=str, help='path to the text file')
    parser_group.add_argument('--text', type=str, help='text')
    
    args = parser.parse_args()
    
    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        parser.error("Provide valid input")
    
    summary = summary_text(text)
    print(summary)
    
if __name__ == '__main__':
    main()
    