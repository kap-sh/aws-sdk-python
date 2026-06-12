"""Generated from Smithy shape ``com.amazonaws.finspace#KxDataviewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxDataviewStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "FAILED",
        "DELETING",
    )
)


def serialize_json(value: KxDataviewStatus) -> str:
    return value


def deserialize_json(data: str) -> KxDataviewStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KxDataviewStatus value: {data!r}")
    return cast(KxDataviewStatus, data)
