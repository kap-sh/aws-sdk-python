"""Generated from Smithy shape ``com.amazonaws.odb#CloneType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

CloneType: TypeAlias = Literal[
    "FULL",
    "METADATA",
    "PARTIAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL",
        "METADATA",
        "PARTIAL",
    )
)


def serialize_aws_json_1_0(value: CloneType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CloneType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CloneType value: {data!r}")
    return cast(CloneType, data)
