"""Generated from Smithy shape ``com.amazonaws.rum#MetricDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rum.types.metric_definition

MetricDefinitions: TypeAlias = list["capo_rum.types.metric_definition.MetricDefinition"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDefinitions) -> list:
    import capo_rum.types.metric_definition

    out: list = []
    for item in value:
        out.append(capo_rum.types.metric_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricDefinitions:
    import capo_rum.types.metric_definition

    out: MetricDefinitions = []
    for item in data:
        out.append(capo_rum.types.metric_definition.deserialize_json(item))
    return out
