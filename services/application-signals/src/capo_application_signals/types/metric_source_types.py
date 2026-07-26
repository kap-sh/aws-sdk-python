"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricSourceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.metric_source_type

MetricSourceTypes: TypeAlias = list[
    "capo_application_signals.types.metric_source_type.MetricSourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricSourceTypes) -> list:
    import capo_application_signals.types.metric_source_type

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.metric_source_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MetricSourceTypes:
    import capo_application_signals.types.metric_source_type

    out: MetricSourceTypes = []
    for item in data:
        out.append(
            capo_application_signals.types.metric_source_type.deserialize_json(item)
        )
    return out
