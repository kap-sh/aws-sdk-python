"""Generated from Smithy shape ``com.amazonaws.glacier#ActionCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glacier.errors import DeserializationError

ActionCode: TypeAlias = Literal[
    "ArchiveRetrieval",
    "InventoryRetrieval",
    "Select",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ArchiveRetrieval",
        "InventoryRetrieval",
        "Select",
    )
)


def serialize_json(value: ActionCode) -> str:
    return value


def deserialize_json(data: str) -> ActionCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionCode value: {data!r}")
    return cast(ActionCode, data)
