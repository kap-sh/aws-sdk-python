"""Generated from Smithy shape ``com.amazonaws.emr#MetricDimensionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.metric_dimension

MetricDimensionList: TypeAlias = list["capo_emr.types.metric_dimension.MetricDimension"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDimensionList) -> list:
    import capo_emr.types.metric_dimension

    out: list = []
    for item in value:
        out.append(capo_emr.types.metric_dimension.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricDimensionList:
    import capo_emr.types.metric_dimension

    out: MetricDimensionList = []
    for item in data:
        out.append(capo_emr.types.metric_dimension.deserialize_aws_json_1_1(item))
    return out
