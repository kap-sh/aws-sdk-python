"""Generated from Smithy shape ``com.amazonaws.resiliencehub#FieldAggregationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

FieldAggregationType: TypeAlias = Literal[
    "Min",
    "Max",
    "Sum",
    "Avg",
    "Count",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Min",
        "Max",
        "Sum",
        "Avg",
        "Count",
    )
)


def serialize_json(value: FieldAggregationType) -> str:
    return value


def deserialize_json(data: str) -> FieldAggregationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FieldAggregationType value: {data!r}")
    return cast(FieldAggregationType, data)
