"""Generated from Smithy shape ``com.amazonaws.rum#MetricDefinitionIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rum.types.metric_definition_id

MetricDefinitionIds: TypeAlias = list[
    "capo_rum.types.metric_definition_id.MetricDefinitionId"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDefinitionIds) -> list:
    return list(value)


def deserialize_json(data: list) -> MetricDefinitionIds:
    return list(data)
