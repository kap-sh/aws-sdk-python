"""Generated from Smithy shape ``com.amazonaws.resiliencehub#CostFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

CostFrequency: TypeAlias = Literal[
    "Hourly",
    "Daily",
    "Monthly",
    "Yearly",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Hourly",
        "Daily",
        "Monthly",
        "Yearly",
    )
)


def serialize_json(value: CostFrequency) -> str:
    return value


def deserialize_json(data: str) -> CostFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CostFrequency value: {data!r}")
    return cast(CostFrequency, data)
