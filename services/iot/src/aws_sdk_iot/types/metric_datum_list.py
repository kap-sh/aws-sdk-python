"""Generated from Smithy shape ``com.amazonaws.iot#MetricDatumList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.metric_datum

MetricDatumList: TypeAlias = list["aws_sdk_iot.types.metric_datum.MetricDatum"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDatumList) -> list:
    import aws_sdk_iot.types.metric_datum

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.metric_datum.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricDatumList:
    import aws_sdk_iot.types.metric_datum

    out: MetricDatumList = []
    for item in data:
        out.append(aws_sdk_iot.types.metric_datum.deserialize_json(item))
    return out
