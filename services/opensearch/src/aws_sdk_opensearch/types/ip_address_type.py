"""Generated from Smithy shape ``com.amazonaws.opensearch#IPAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

IPAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "dualstack",
    )
)


def serialize_json(value: IPAddressType) -> str:
    return value


def deserialize_json(data: str) -> IPAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IPAddressType value: {data!r}")
    return cast(IPAddressType, data)
