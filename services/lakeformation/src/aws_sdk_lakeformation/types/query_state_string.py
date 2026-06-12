"""Generated from Smithy shape ``com.amazonaws.lakeformation#QueryStateString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

QueryStateString: TypeAlias = Literal[
    "PENDING",
    "WORKUNITS_AVAILABLE",
    "ERROR",
    "FINISHED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "WORKUNITS_AVAILABLE",
        "ERROR",
        "FINISHED",
        "EXPIRED",
    )
)


def serialize_json(value: QueryStateString) -> str:
    return value


def deserialize_json(data: str) -> QueryStateString:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryStateString value: {data!r}")
    return cast(QueryStateString, data)
