"""Generated from Smithy shape ``com.amazonaws.odb#characterSetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

characterSetType: TypeAlias = Literal[
    "DATABASE",
    "NATIONAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATABASE",
        "NATIONAL",
    )
)


def serialize_aws_json_1_0(value: characterSetType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> characterSetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown characterSetType value: {data!r}")
    return cast(characterSetType, data)
