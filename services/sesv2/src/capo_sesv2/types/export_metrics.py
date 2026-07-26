"""Generated from Smithy shape ``com.amazonaws.sesv2#ExportMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.export_metric

ExportMetrics: TypeAlias = list["capo_sesv2.types.export_metric.ExportMetric"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportMetrics) -> list:
    import capo_sesv2.types.export_metric

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.export_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportMetrics:
    import capo_sesv2.types.export_metric

    out: ExportMetrics = []
    for item in data:
        out.append(capo_sesv2.types.export_metric.deserialize_json(item))
    return out
