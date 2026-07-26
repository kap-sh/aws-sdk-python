"""Generated from Smithy shape ``com.amazonaws.rekognition#Emotion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.emotion_name
    import capo_rekognition.types.percent


class Emotion(TypedDict, closed=True):
    type: NotRequired["capo_rekognition.types.emotion_name.EmotionName"]
    """<p>Type of emotion detected.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Level of confidence in the determination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Emotion) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_rekognition.types.emotion_name

        out["Type"] = capo_rekognition.types.emotion_name.serialize_aws_json_1_1(
            value["type"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Emotion:
    out: Emotion = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_rekognition.types.emotion_name

        out["type"] = capo_rekognition.types.emotion_name.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
