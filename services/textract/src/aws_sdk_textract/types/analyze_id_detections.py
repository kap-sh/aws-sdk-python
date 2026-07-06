"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeIDDetections``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.normalized_value
    import aws_sdk_textract.types.percent
    import aws_sdk_textract.types.string


class AnalyzeIDDetections(TypedDict, closed=True):
    text: "aws_sdk_textract.types.string.String"
    """<p>Text of either the normalized field or value associated with it.</p>"""
    normalized_value: NotRequired[
        "aws_sdk_textract.types.normalized_value.NormalizedValue"
    ]
    """<p>Only returned for dates, returns the type of value detected and the date written in a more machine readable way.</p>"""
    confidence: NotRequired["aws_sdk_textract.types.percent.Percent"]
    """<p>The confidence score of the detected text.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeIDDetections) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    if "normalized_value" in value:
        import aws_sdk_textract.types.normalized_value

        out["NormalizedValue"] = (
            aws_sdk_textract.types.normalized_value.serialize_aws_json_1_1(
                value["normalized_value"]
            )
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyzeIDDetections:
    out: AnalyzeIDDetections = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("AnalyzeIDDetections.text required")
    if "NormalizedValue" in data:
        import aws_sdk_textract.types.normalized_value

        out["normalized_value"] = (
            aws_sdk_textract.types.normalized_value.deserialize_aws_json_1_1(
                data["NormalizedValue"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
