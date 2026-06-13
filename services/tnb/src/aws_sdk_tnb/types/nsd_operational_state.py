"""Generated from Smithy shape ``com.amazonaws.tnb#NsdOperationalState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

NsdOperationalState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: NsdOperationalState) -> str:
    return value


def deserialize_json(data: str) -> NsdOperationalState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NsdOperationalState value: {data!r}")
    return cast(NsdOperationalState, data)
