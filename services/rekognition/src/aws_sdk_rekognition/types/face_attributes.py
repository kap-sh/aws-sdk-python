"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceAttributes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

FaceAttributes: TypeAlias = Literal[
    "DEFAULT",
    "ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "ALL",
    )
)


def serialize_aws_json_1_1(value: FaceAttributes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FaceAttributes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FaceAttributes value: {data!r}")
    return cast(FaceAttributes, data)
