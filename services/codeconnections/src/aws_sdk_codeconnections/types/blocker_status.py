"""Generated from Smithy shape ``com.amazonaws.codeconnections#BlockerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeconnections.errors import DeserializationError

BlockerStatus: TypeAlias = Literal[
    "ACTIVE",
    "RESOLVED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "RESOLVED",
    )
)


def serialize_aws_json_1_0(value: BlockerStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BlockerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlockerStatus value: {data!r}")
    return cast(BlockerStatus, data)
