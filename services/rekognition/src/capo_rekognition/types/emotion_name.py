"""Generated from Smithy shape ``com.amazonaws.rekognition#EmotionName``."""

from typing import Literal, TypeAlias, cast

EmotionName: TypeAlias = Literal[
    "HAPPY",
    "SAD",
    "ANGRY",
    "CONFUSED",
    "DISGUSTED",
    "SURPRISED",
    "CALM",
    "UNKNOWN",
    "FEAR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmotionName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EmotionName:
    return cast(EmotionName, data)
