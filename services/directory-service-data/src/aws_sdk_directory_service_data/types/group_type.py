"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#GroupType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service_data.errors import DeserializationError

GroupType: TypeAlias = Literal[
    "Distribution",
    "Security",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Distribution",
        "Security",
    )
)


def serialize_json(value: GroupType) -> str:
    return value


def deserialize_json(data: str) -> GroupType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupType value: {data!r}")
    return cast(GroupType, data)
