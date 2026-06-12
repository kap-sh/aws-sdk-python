"""Generated from Smithy shape ``com.amazonaws.textract#Prediction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.non_empty_string
    import aws_sdk_textract.types.percent


class Prediction(TypedDict):
    value: NotRequired["aws_sdk_textract.types.non_empty_string.NonEmptyString"]
    """<p>The predicted value of a detected object.</p>"""
    confidence: NotRequired["aws_sdk_textract.types.percent.Percent"]
    """<p>Amazon Textract's confidence in its predicted value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Prediction) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Prediction:
    out: Prediction = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
