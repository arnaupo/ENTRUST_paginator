import logging


def load_document(file_path: str) -> str:
    """Load the content of a document from a file."""

    with open(file_path, 'r') as file:
        return file.read().strip()


def paginate_and_save_document(doc: str, output_path: str, max_len: int = 80, lines_pp: int = 25) -> None:
    """ 
    Paginates the documents so that each line contains a maximum of max_len characters.
    Every lines_pp lines, it adds a page separator. Also, saves the paginated content to a new file.
    """

    words = doc.split()
    paginated_lines = []
    current_line = ''
    nlines = 0
    page_number = 1

    for word in words:
        if len(current_line) + len(word) + 1 <= max_len:
            current_line += (' ' if current_line else '') + word # Add space if not the first word
        else:
            paginated_lines.append(current_line)
            nlines += 1
            if nlines == lines_pp:
                separator = f'--- Page {page_number} ---'
                centered_separator = separator.center(max_len)
                paginated_lines.append(f'{centered_separator}')
                page_number += 1
                nlines = 0
            current_line = word
        
    #check if pending line is not empty and add the page number
    if current_line:
        paginated_lines.append(current_line)
        separator = f'--- Page {page_number} ---'
        centered_separator = separator.center(max_len)
        paginated_lines.append(f'{centered_separator}')


    with open(output_path, 'w') as file:
        for line in paginated_lines:
            file.write(line + '\n')


def main() -> None:

    # Set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Load the document
    file_path = './document.txt'
    logger.info(f'Loading document from {file_path}')
    doc = load_document(file_path)
    logger.info('Document loaded successfully')


    # Paginate the document
    output_path = './paginated_document.txt'
    logger.info(f'Paginating document and saving to {output_path}')
    paginate_and_save_document(doc, output_path)
    logger.info('Document paginated and saved successfully')


    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)

if __name__ == "__main__":
    main()
