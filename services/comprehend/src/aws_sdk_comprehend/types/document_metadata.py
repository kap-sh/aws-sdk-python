"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.list_of_extracted_characters


class DocumentMetadata(TypedDict, closed=True):
    pages: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Number of pages in the document.</p>"""
    extracted_characters: NotRequired[
        "aws_sdk_comprehend.types.list_of_extracted_characters.ListOfExtractedCharacters"
    ]
    """<p>List of pages in the document, with the number of characters extracted from each page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentMetadata) -> dict:
    out: dict = {}
    if "pages" in value:
        out["Pages"] = value["pages"]
    if "extracted_characters" in value:
        import aws_sdk_comprehend.types.list_of_extracted_characters

        out["ExtractedCharacters"] = (
            aws_sdk_comprehend.types.list_of_extracted_characters.serialize_aws_json_1_1(
                value["extracted_characters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentMetadata:
    out: DocumentMetadata = {}  # type: ignore[typeddict-item]
    if "Pages" in data:
        out["pages"] = data["Pages"]
    if "ExtractedCharacters" in data:
        import aws_sdk_comprehend.types.list_of_extracted_characters

        out["extracted_characters"] = (
            aws_sdk_comprehend.types.list_of_extracted_characters.deserialize_aws_json_1_1(
                data["ExtractedCharacters"]
            )
        )
    return out
