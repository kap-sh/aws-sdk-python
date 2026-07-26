"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MetricsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.shared_audience_metrics

MetricsList: TypeAlias = list[
    "capo_cleanroomsml.types.shared_audience_metrics.SharedAudienceMetrics"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricsList) -> list:
    import capo_cleanroomsml.types.shared_audience_metrics

    out: list = []
    for item in value:
        out.append(capo_cleanroomsml.types.shared_audience_metrics.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricsList:
    import capo_cleanroomsml.types.shared_audience_metrics

    out: MetricsList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.shared_audience_metrics.deserialize_json(item)
        )
    return out
