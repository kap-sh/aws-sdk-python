"""Generated from Smithy shape ``com.amazonaws.finspace#ChangesetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

ChangesetStatus: TypeAlias = Literal[
    "PENDING",
    "PROCESSING",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "PROCESSING",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_json(value: ChangesetStatus) -> str:
    return value


def deserialize_json(data: str) -> ChangesetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangesetStatus value: {data!r}")
    return cast(ChangesetStatus, data)
