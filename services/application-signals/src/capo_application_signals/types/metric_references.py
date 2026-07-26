"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.metric_reference

MetricReferences: TypeAlias = list[
    "capo_application_signals.types.metric_reference.MetricReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricReferences) -> list:
    import capo_application_signals.types.metric_reference

    out: list = []
    for item in value:
        out.append(capo_application_signals.types.metric_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricReferences:
    import capo_application_signals.types.metric_reference

    out: MetricReferences = []
    for item in data:
        out.append(
            capo_application_signals.types.metric_reference.deserialize_json(item)
        )
    return out
