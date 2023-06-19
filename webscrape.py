import requests
from bs4 import BeautifulSoup

# Dictionary mapping options to URLs
urls = {
    "G-Button cleaning and use.": "https://uihc.org/childrens/educational-resources/use-and-care-g-button",
    "How to clean a trach.": "https://uihc.org/educational-resources/how-clean-tracheostomy-tube",
    "How to change a trach.": "https://uihc.org/educational-resources/how-change-tracheostomy-tube",
    "How to suction a trach.": "https://uihc.org/educational-resources/suctioning-tracheostomy",
    "How to set up feed tube machine.": "https://www.mskcc.org/cancer-care/patient-education/tube-feeding-pump",
    "Basic rehab exercises": "https://healthwire.pk/healthcare/exercises-for-bed-bound-patients/"
}

while True:
    # Prompt the user to select an option
    print("Select a query:")
    for i, option in enumerate(urls.keys()):
        print(f"{i + 1}. {option}")

    selected_option = input("Enter the number of your selection (or 'exit' to quit): ")

    if selected_option.lower() == "exit":
        print("Exiting the program.")
        break

    # Scrape and display the selected option
    try:
        index = int(selected_option) - 1
        options = list(urls.keys())
        if 0 <= index < len(options):
            url = urls[options[index]]
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            sections = soup.find(class_="wysiwyg").find_all(["h2", "h3", "p", "ul", "li", "ol"])

            print(f"\nHere is the information for '{options[index]}':\n")

            indentation = ""
            current_heading = None

            for section in sections:
                if section.name == "h2":
                    if current_heading is not None:
                        print(f"{current_heading}\n")
                    current_heading = section.text

                elif section.name in ["h3", "h4"]:
                    print(f"{section.text}\n")

                elif section.name == "p":
                    print(f"> {section.text}\n")

                elif section.name in ["ol", "ul"]:
                    lis = section.find_all("li")
                    for li in lis:
                        print(f"- {li.text}")

            print("\n---\n")  # Add a separator after displaying the information

        else:
            print("Invalid selection.")

    except ValueError:
        print("Invalid input. Please enter a number or 'exit' to quit.")
