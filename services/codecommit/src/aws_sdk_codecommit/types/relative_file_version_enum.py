"""Generated from Smithy shape ``com.amazonaws.codecommit#RelativeFileVersionEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

RelativeFileVersionEnum: TypeAlias = Literal[
    "BEFORE",
    "AFTER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BEFORE",
        "AFTER",
    )
)


def serialize_aws_json_1_1(value: RelativeFileVersionEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelativeFileVersionEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelativeFileVersionEnum value: {data!r}")
    return cast(RelativeFileVersionEnum, data)
