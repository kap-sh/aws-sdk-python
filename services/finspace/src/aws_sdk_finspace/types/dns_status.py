"""Generated from Smithy shape ``com.amazonaws.finspace#dnsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

dnsStatus: TypeAlias = Literal[
    "NONE",
    "UPDATE_REQUESTED",
    "UPDATING",
    "FAILED_UPDATE",
    "SUCCESSFULLY_UPDATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "UPDATE_REQUESTED",
        "UPDATING",
        "FAILED_UPDATE",
        "SUCCESSFULLY_UPDATED",
    )
)


def serialize_json(value: dnsStatus) -> str:
    return value


def deserialize_json(data: str) -> dnsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown dnsStatus value: {data!r}")
    return cast(dnsStatus, data)
