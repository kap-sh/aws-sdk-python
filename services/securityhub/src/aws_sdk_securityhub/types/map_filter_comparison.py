"""Generated from Smithy shape ``com.amazonaws.securityhub#MapFilterComparison``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

MapFilterComparison: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "CONTAINS",
    "NOT_CONTAINS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "NOT_EQUALS",
        "CONTAINS",
        "NOT_CONTAINS",
    )
)


def serialize_json(value: MapFilterComparison) -> str:
    return value


def deserialize_json(data: str) -> MapFilterComparison:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MapFilterComparison value: {data!r}")
    return cast(MapFilterComparison, data)
