"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#RelevanceMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.relevance_metric

RelevanceMetrics: TypeAlias = list[
    "capo_cleanroomsml.types.relevance_metric.RelevanceMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: RelevanceMetrics) -> list:
    import capo_cleanroomsml.types.relevance_metric

    out: list = []
    for item in value:
        out.append(capo_cleanroomsml.types.relevance_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> RelevanceMetrics:
    import capo_cleanroomsml.types.relevance_metric

    out: RelevanceMetrics = []
    for item in data:
        out.append(capo_cleanroomsml.types.relevance_metric.deserialize_json(item))
    return out
