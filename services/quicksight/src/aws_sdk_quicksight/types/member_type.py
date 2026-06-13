"""Generated from Smithy shape ``com.amazonaws.quicksight#MemberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

MemberType: TypeAlias = Literal[
    "DASHBOARD",
    "ANALYSIS",
    "DATASET",
    "DATASOURCE",
    "TOPIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DASHBOARD",
        "ANALYSIS",
        "DATASET",
        "DATASOURCE",
        "TOPIC",
    )
)


def serialize_json(value: MemberType) -> str:
    return value


def deserialize_json(data: str) -> MemberType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemberType value: {data!r}")
    return cast(MemberType, data)
