"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#QueryGranularity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

QueryGranularity: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOURLY",
        "DAILY",
    )
)


def serialize_json(value: QueryGranularity) -> str:
    return value


def deserialize_json(data: str) -> QueryGranularity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryGranularity value: {data!r}")
    return cast(QueryGranularity, data)
