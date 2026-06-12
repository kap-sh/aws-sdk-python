"""Generated from Smithy shape ``com.amazonaws.appsync#MergeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

MergeType: TypeAlias = Literal[
    "MANUAL_MERGE",
    "AUTO_MERGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANUAL_MERGE",
        "AUTO_MERGE",
    )
)


def serialize_json(value: MergeType) -> str:
    return value


def deserialize_json(data: str) -> MergeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MergeType value: {data!r}")
    return cast(MergeType, data)
