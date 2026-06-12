"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactFlowStatus: TypeAlias = Literal[
    "PUBLISHED",
    "SAVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISHED",
        "SAVED",
    )
)


def serialize_json(value: ContactFlowStatus) -> str:
    return value


def deserialize_json(data: str) -> ContactFlowStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactFlowStatus value: {data!r}")
    return cast(ContactFlowStatus, data)
