"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#RawMetricDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_metrics.types.raw_metric_data

RawMetricDataList: TypeAlias = list[
    "capo_sagemaker_metrics.types.raw_metric_data.RawMetricData"
]


# --- restJson1 ser/de ---
def serialize_json(value: RawMetricDataList) -> list:
    import capo_sagemaker_metrics.types.raw_metric_data

    out: list = []
    for item in value:
        out.append(capo_sagemaker_metrics.types.raw_metric_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> RawMetricDataList:
    import capo_sagemaker_metrics.types.raw_metric_data

    out: RawMetricDataList = []
    for item in data:
        out.append(capo_sagemaker_metrics.types.raw_metric_data.deserialize_json(item))
    return out
