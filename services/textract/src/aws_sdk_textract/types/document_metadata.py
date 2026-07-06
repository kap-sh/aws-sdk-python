"""Generated from Smithy shape ``com.amazonaws.textract#DocumentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.u_integer


class DocumentMetadata(TypedDict, closed=True):
    pages: NotRequired["aws_sdk_textract.types.u_integer.UInteger"]
    """<p>The number of pages that are detected in the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentMetadata) -> dict:
    out: dict = {}
    if "pages" in value:
        out["Pages"] = value["pages"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentMetadata:
    out: DocumentMetadata = {}  # type: ignore[typeddict-item]
    if "Pages" in data:
        out["pages"] = data["Pages"]
    return out
