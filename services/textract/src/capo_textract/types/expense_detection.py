"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.geometry
    import capo_textract.types.percent
    import capo_textract.types.string


class ExpenseDetection(TypedDict, closed=True):
    text: NotRequired["capo_textract.types.string.String"]
    """<p>The word or line of text recognized by Amazon Textract</p>"""
    geometry: NotRequired["capo_textract.types.geometry.Geometry"]
    confidence: NotRequired["capo_textract.types.percent.Percent"]
    """<p>The confidence in detection, as a percentage</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseDetection) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "geometry" in value:
        import capo_textract.types.geometry

        out["Geometry"] = capo_textract.types.geometry.serialize_aws_json_1_1(
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
        import capo_textract.types.geometry

        out["geometry"] = capo_textract.types.geometry.deserialize_aws_json_1_1(
            data["Geometry"]
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
