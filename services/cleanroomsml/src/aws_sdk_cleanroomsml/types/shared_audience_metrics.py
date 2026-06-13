"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#SharedAudienceMetrics``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

SharedAudienceMetrics: TypeAlias = Literal[
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "NONE",
    )
)


def serialize_json(value: SharedAudienceMetrics) -> str:
    return value


def deserialize_json(data: str) -> SharedAudienceMetrics:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SharedAudienceMetrics value: {data!r}")
    return cast(SharedAudienceMetrics, data)
