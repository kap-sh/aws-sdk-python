"""Generated from Smithy shape ``com.amazonaws.rum#MetricDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rum.types.metric_definition_request

MetricDefinitionsRequest: TypeAlias = list[
    "capo_rum.types.metric_definition_request.MetricDefinitionRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDefinitionsRequest) -> list:
    import capo_rum.types.metric_definition_request

    out: list = []
    for item in value:
        out.append(capo_rum.types.metric_definition_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricDefinitionsRequest:
    import capo_rum.types.metric_definition_request

    out: MetricDefinitionsRequest = []
    for item in data:
        out.append(capo_rum.types.metric_definition_request.deserialize_json(item))
    return out
