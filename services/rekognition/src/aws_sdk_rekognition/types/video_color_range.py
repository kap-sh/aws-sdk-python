"""Generated from Smithy shape ``com.amazonaws.rekognition#VideoColorRange``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

VideoColorRange: TypeAlias = Literal[
    "FULL",
    "LIMITED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL",
        "LIMITED",
    )
)


def serialize_aws_json_1_1(value: VideoColorRange) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VideoColorRange:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoColorRange value: {data!r}")
    return cast(VideoColorRange, data)
