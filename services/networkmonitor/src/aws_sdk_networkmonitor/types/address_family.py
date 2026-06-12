"""Generated from Smithy shape ``com.amazonaws.networkmonitor#AddressFamily``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmonitor.errors import DeserializationError

AddressFamily: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "IPV6",
    )
)


def serialize_json(value: AddressFamily) -> str:
    return value


def deserialize_json(data: str) -> AddressFamily:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AddressFamily value: {data!r}")
    return cast(AddressFamily, data)
