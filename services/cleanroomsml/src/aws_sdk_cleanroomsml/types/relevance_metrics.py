"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#RelevanceMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.relevance_metric

RelevanceMetrics: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.relevance_metric.RelevanceMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: RelevanceMetrics) -> list:
    import aws_sdk_cleanroomsml.types.relevance_metric

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanroomsml.types.relevance_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> RelevanceMetrics:
    import aws_sdk_cleanroomsml.types.relevance_metric

    out: RelevanceMetrics = []
    for item in data:
        out.append(aws_sdk_cleanroomsml.types.relevance_metric.deserialize_json(item))
    return out
