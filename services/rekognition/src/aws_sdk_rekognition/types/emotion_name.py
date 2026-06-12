"""Generated from Smithy shape ``com.amazonaws.rekognition#EmotionName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "HAPPY",
        "SAD",
        "ANGRY",
        "CONFUSED",
        "DISGUSTED",
        "SURPRISED",
        "CALM",
        "UNKNOWN",
        "FEAR",
    )
)


def serialize_aws_json_1_1(value: EmotionName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EmotionName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmotionName value: {data!r}")
    return cast(EmotionName, data)
