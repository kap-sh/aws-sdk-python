"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MetricsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.shared_audience_metrics

MetricsList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.shared_audience_metrics.SharedAudienceMetrics"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricsList) -> list:
    import aws_sdk_cleanroomsml.types.shared_audience_metrics

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.shared_audience_metrics.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MetricsList:
    import aws_sdk_cleanroomsml.types.shared_audience_metrics

    out: MetricsList = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.shared_audience_metrics.deserialize_json(item)
        )
    return out
