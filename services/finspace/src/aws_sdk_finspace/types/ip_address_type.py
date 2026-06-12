"""Generated from Smithy shape ``com.amazonaws.finspace#IPAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

IPAddressType: TypeAlias = Literal["IP_V4",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("IP_V4",))


def serialize_json(value: IPAddressType) -> str:
    return value


def deserialize_json(data: str) -> IPAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IPAddressType value: {data!r}")
    return cast(IPAddressType, data)
