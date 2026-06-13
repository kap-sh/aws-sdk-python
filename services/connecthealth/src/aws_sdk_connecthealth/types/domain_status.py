"""Generated from Smithy shape ``com.amazonaws.connecthealth#DomainStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

DomainStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: DomainStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainStatus value: {data!r}")
    return cast(DomainStatus, data)
