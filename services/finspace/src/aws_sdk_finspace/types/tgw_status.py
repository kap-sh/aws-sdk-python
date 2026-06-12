"""Generated from Smithy shape ``com.amazonaws.finspace#tgwStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

tgwStatus: TypeAlias = Literal[
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


def serialize_json(value: tgwStatus) -> str:
    return value


def deserialize_json(data: str) -> tgwStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown tgwStatus value: {data!r}")
    return cast(tgwStatus, data)
