"""Generated from Smithy shape ``com.amazonaws.quicksight#BarsArrangement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

BarsArrangement: TypeAlias = Literal[
    "CLUSTERED",
    "STACKED",
    "STACKED_PERCENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLUSTERED",
        "STACKED",
        "STACKED_PERCENT",
    )
)


def serialize_json(value: BarsArrangement) -> str:
    return value


def deserialize_json(data: str) -> BarsArrangement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BarsArrangement value: {data!r}")
    return cast(BarsArrangement, data)
