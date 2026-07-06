"""Generated from Smithy shape ``com.amazonaws.textract#SplitDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.page_list
    import aws_sdk_textract.types.u_integer


class SplitDocument(TypedDict, closed=True):
    index: NotRequired["aws_sdk_textract.types.u_integer.UInteger"]
    """<p>The index for a given document in a DocumentGroup of a specific Type.</p>"""
    pages: NotRequired["aws_sdk_textract.types.page_list.PageList"]
    """<p>An array of page numbers for a for a given document, ordered by logical boundary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitDocument) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "pages" in value:
        import aws_sdk_textract.types.page_list

        out["Pages"] = aws_sdk_textract.types.page_list.serialize_aws_json_1_1(
            value["pages"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SplitDocument:
    out: SplitDocument = {}  # type: ignore[typeddict-item]
    if "Index" in data:
        out["index"] = data["Index"]
    if "Pages" in data:
        import aws_sdk_textract.types.page_list

        out["pages"] = aws_sdk_textract.types.page_list.deserialize_aws_json_1_1(
            data["Pages"]
        )
    return out
