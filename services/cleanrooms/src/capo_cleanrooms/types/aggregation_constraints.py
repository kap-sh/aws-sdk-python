"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AggregationConstraints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.aggregation_constraint

AggregationConstraints: TypeAlias = list[
    "capo_cleanrooms.types.aggregation_constraint.AggregationConstraint"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationConstraints) -> list:
    import capo_cleanrooms.types.aggregation_constraint

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.aggregation_constraint.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregationConstraints:
    import capo_cleanrooms.types.aggregation_constraint

    out: AggregationConstraints = []
    for item in data:
        out.append(capo_cleanrooms.types.aggregation_constraint.deserialize_json(item))
    return out
