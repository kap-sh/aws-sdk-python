"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactFlowModuleStatus: TypeAlias = Literal[
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


def serialize_json(value: ContactFlowModuleStatus) -> str:
    return value


def deserialize_json(data: str) -> ContactFlowModuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactFlowModuleStatus value: {data!r}")
    return cast(ContactFlowModuleStatus, data)
