"""Generated from Smithy shape ``com.amazonaws.textract#Warning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.error_code
    import capo_textract.types.pages


class Warning(TypedDict, closed=True):
    error_code: NotRequired["capo_textract.types.error_code.ErrorCode"]
    """<p>The error code for the warning.</p>"""
    pages: NotRequired["capo_textract.types.pages.Pages"]
    """<p>A list of the pages that the warning applies to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Warning) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "pages" in value:
        import capo_textract.types.pages

        out["Pages"] = capo_textract.types.pages.serialize_aws_json_1_1(value["pages"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Warning:
    out: Warning = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Pages" in data:
        import capo_textract.types.pages

        out["pages"] = capo_textract.types.pages.deserialize_aws_json_1_1(data["Pages"])
    return out
