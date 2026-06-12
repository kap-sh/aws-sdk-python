"""Generated from Smithy shape ``com.amazonaws.rekognition#SegmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

SegmentType: TypeAlias = Literal[
    "TECHNICAL_CUE",
    "SHOT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TECHNICAL_CUE",
        "SHOT",
    )
)


def serialize_aws_json_1_1(value: SegmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SegmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SegmentType value: {data!r}")
    return cast(SegmentType, data)
