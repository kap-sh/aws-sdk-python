"""Generated from Smithy shape ``com.amazonaws.resiliencehub#FieldAggregationType``."""

from typing import Literal, TypeAlias, cast

FieldAggregationType: TypeAlias = Literal[
    "Min",
    "Max",
    "Sum",
    "Avg",
    "Count",
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldAggregationType) -> str:
    return value


def deserialize_json(data: str) -> FieldAggregationType:
    return cast(FieldAggregationType, data)
