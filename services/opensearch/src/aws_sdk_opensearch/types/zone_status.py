"""Generated from Smithy shape ``com.amazonaws.opensearch#ZoneStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

ZoneStatus: TypeAlias = Literal[
    "Active",
    "StandBy",
    "NotAvailable",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "StandBy",
        "NotAvailable",
    )
)


def serialize_json(value: ZoneStatus) -> str:
    return value


def deserialize_json(data: str) -> ZoneStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ZoneStatus value: {data!r}")
    return cast(ZoneStatus, data)
