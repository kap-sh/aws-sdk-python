"""Generated from Smithy shape ``com.amazonaws.rekognition#BodyPart``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

BodyPart: TypeAlias = Literal[
    "FACE",
    "HEAD",
    "LEFT_HAND",
    "RIGHT_HAND",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FACE",
        "HEAD",
        "LEFT_HAND",
        "RIGHT_HAND",
    )
)


def serialize_aws_json_1_1(value: BodyPart) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BodyPart:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BodyPart value: {data!r}")
    return cast(BodyPart, data)
