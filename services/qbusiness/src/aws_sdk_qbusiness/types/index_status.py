"""Generated from Smithy shape ``com.amazonaws.qbusiness#IndexStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

IndexStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
        "UPDATING",
    )
)


def serialize_json(value: IndexStatus) -> str:
    return value


def deserialize_json(data: str) -> IndexStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IndexStatus value: {data!r}")
    return cast(IndexStatus, data)
