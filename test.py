from pathlib import Path
import sys
import warnings

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from bs4 import XMLParsedAsHTMLWarning
from sec2md.core import convert_to_markdown
from sec2md.sections import extract_sections, get_section

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)


URL = "https://www.sec.gov/Archives/edgar/data/789019/000119312526027207/msft-20251231.htm"
USER = "Rahul (rahul@example.com)"


def main() -> None:
    pages = convert_to_markdown(URL, user_agent=USER, return_pages=True)
    sections = extract_sections(pages, filing_type="10-Q")

    id = 0
    for i in sections:
        i.item = str(id)
        print(f"{i.item}\t{i.item_title}\t{i.page_range}")
        # print(i.item_title, i.item)
        id += 1

    print(get_section(sections, item="4", filing_type="10-Q", item_class="generic"))


if __name__ == "__main__":
    main()
