"""Generated from Smithy shape ``com.amazonaws.mwaa#MetricData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.metric_datum

MetricData: TypeAlias = list["aws_sdk_mwaa.types.metric_datum.MetricDatum"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricData) -> list:
    import aws_sdk_mwaa.types.metric_datum

    out: list = []
    for item in value:
        out.append(aws_sdk_mwaa.types.metric_datum.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricData:
    import aws_sdk_mwaa.types.metric_datum

    out: MetricData = []
    for item in data:
        out.append(aws_sdk_mwaa.types.metric_datum.deserialize_json(item))
    return out
