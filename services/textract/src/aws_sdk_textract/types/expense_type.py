"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.percent
    import aws_sdk_textract.types.string


class ExpenseType(TypedDict, closed=True):
    text: NotRequired["aws_sdk_textract.types.string.String"]
    """<p>The word or line of text detected by Amazon Textract.</p>"""
    confidence: NotRequired["aws_sdk_textract.types.percent.Percent"]
    """<p>The confidence of accuracy, as a percentage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseType) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpenseType:
    out: ExpenseType = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
