"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MetricDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.metric_definition

MetricDefinitionList: TypeAlias = list[
    "capo_cleanroomsml.types.metric_definition.MetricDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDefinitionList) -> list:
    import capo_cleanroomsml.types.metric_definition

    out: list = []
    for item in value:
        out.append(capo_cleanroomsml.types.metric_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricDefinitionList:
    import capo_cleanroomsml.types.metric_definition

    out: MetricDefinitionList = []
    for item in data:
        out.append(capo_cleanroomsml.types.metric_definition.deserialize_json(item))
    return out
