"""Generated from Smithy shape ``com.amazonaws.costexplorer#MetricNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.metric_name

MetricNames: TypeAlias = list["aws_sdk_cost_explorer.types.metric_name.MetricName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MetricNames:
    return list(data)
