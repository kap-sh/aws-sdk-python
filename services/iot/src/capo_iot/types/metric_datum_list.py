"""Generated from Smithy shape ``com.amazonaws.iot#MetricDatumList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.metric_datum

MetricDatumList: TypeAlias = list["capo_iot.types.metric_datum.MetricDatum"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDatumList) -> list:
    import capo_iot.types.metric_datum

    out: list = []
    for item in value:
        out.append(capo_iot.types.metric_datum.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricDatumList:
    import capo_iot.types.metric_datum

    out: MetricDatumList = []
    for item in data:
        out.append(capo_iot.types.metric_datum.deserialize_json(item))
    return out
