"""Generated from Smithy shape ``com.amazonaws.ram#ResourceOwner``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

ResourceOwner: TypeAlias = Literal[
    "SELF",
    "OTHER-ACCOUNTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELF",
        "OTHER-ACCOUNTS",
    )
)


def serialize_json(value: ResourceOwner) -> str:
    return value


def deserialize_json(data: str) -> ResourceOwner:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceOwner value: {data!r}")
    return cast(ResourceOwner, data)
