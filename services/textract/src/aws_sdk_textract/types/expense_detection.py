"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseDetection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.geometry
    import aws_sdk_textract.types.percent
    import aws_sdk_textract.types.string


class ExpenseDetection(TypedDict):
    text: NotRequired["aws_sdk_textract.types.string.String"]
    """<p>The word or line of text recognized by Amazon Textract</p>"""
    geometry: NotRequired["aws_sdk_textract.types.geometry.Geometry"]
    confidence: NotRequired["aws_sdk_textract.types.percent.Percent"]
    """<p>The confidence in detection, as a percentage</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseDetection) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "geometry" in value:
        import aws_sdk_textract.types.geometry

        out["Geometry"] = aws_sdk_textract.types.geometry.serialize_aws_json_1_1(
            value["geometry"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpenseDetection:
    out: ExpenseDetection = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Geometry" in data:
        import aws_sdk_textract.types.geometry

        out["geometry"] = aws_sdk_textract.types.geometry.deserialize_aws_json_1_1(
            data["Geometry"]
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
