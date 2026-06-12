"""Generated from Smithy shape ``com.amazonaws.rekognition#TextTypes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

TextTypes: TypeAlias = Literal[
    "LINE",
    "WORD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINE",
        "WORD",
    )
)


def serialize_aws_json_1_1(value: TextTypes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TextTypes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TextTypes value: {data!r}")
    return cast(TextTypes, data)
