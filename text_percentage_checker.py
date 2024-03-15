import os
import shutil
import fitz

def get_text_percentage_and_move(file_name: str, destination_folder: str = "img", threshold: float = 0.02) -> float:
    """
    Calculate the percentage of the document covered by searchable text.
    If the text percentage is below the threshold, move the file to the destination folder.
    """
    total_page_area = 0.0
    total_text_area = 0.0
    doc = fitz.open(file_name)

    for page in doc:
        total_page_area += abs(page.rect)
        text_area = 0.0
        for pages in page.getTextBlocks():
            block_text_rectange = fitz.Rect(pages[:4])  # rectangle where block text appears
            text_area += abs(block_text_rectange)
        total_text_area += text_area

    doc.close()
    text_percentage = total_text_area / total_page_area

    if text_percentage < threshold:
        # Move the file to the destination folder
        destination_path = os.path.join(destination_folder, os.path.basename(file_name))
        shutil.move(file_name, destination_path)
        print(f"Moved {os.path.basename(file_name)} to {destination_folder}")

    return text_percentage

if __name__ == "__main__":
    source_folder = "data/pdf's/"
    destination_folder = "data/pdf's/image_based_pdf/"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(source_folder, filename)
            text_percentage = get_text_percentage_and_move(file_path, destination_folder)
            if text_percentage < 0.01:
                print(f"{filename} is a fully scanned PDF - no relevant text")
            else:
                print(f"{filename} is not a fully scanned PDF - text is present")