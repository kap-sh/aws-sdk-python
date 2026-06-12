"""Generated from Smithy shape ``com.amazonaws.rekognition#GenderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

GenderType: TypeAlias = Literal[
    "Male",
    "Female",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Male",
        "Female",
    )
)


def serialize_aws_json_1_1(value: GenderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GenderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GenderType value: {data!r}")
    return cast(GenderType, data)
