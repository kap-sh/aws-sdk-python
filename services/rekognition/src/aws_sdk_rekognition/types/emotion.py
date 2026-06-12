"""Generated from Smithy shape ``com.amazonaws.rekognition#Emotion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.emotion_name
    import aws_sdk_rekognition.types.percent


class Emotion(TypedDict):
    type: NotRequired["aws_sdk_rekognition.types.emotion_name.EmotionName"]
    """<p>Type of emotion detected.</p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Level of confidence in the determination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Emotion) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_rekognition.types.emotion_name

        out["Type"] = aws_sdk_rekognition.types.emotion_name.serialize_aws_json_1_1(
            value["type"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Emotion:
    out: Emotion = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_rekognition.types.emotion_name

        out["type"] = aws_sdk_rekognition.types.emotion_name.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
