"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareAssociationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

ResourceShareAssociationType: TypeAlias = Literal[
    "PRINCIPAL",
    "RESOURCE",
    "SOURCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRINCIPAL",
        "RESOURCE",
        "SOURCE",
    )
)


def serialize_json(value: ResourceShareAssociationType) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareAssociationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceShareAssociationType value: {data!r}"
        )
    return cast(ResourceShareAssociationType, data)
