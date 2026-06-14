"""Generated from Smithy shape ``com.amazonaws.datazone#GroupProfileStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

GroupProfileStatus: TypeAlias = Literal[
    "ASSIGNED",
    "NOT_ASSIGNED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSIGNED",
        "NOT_ASSIGNED",
    )
)


def serialize_json(value: GroupProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupProfileStatus value: {data!r}")
    return cast(GroupProfileStatus, data)
