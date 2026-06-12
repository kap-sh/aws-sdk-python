"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#MetricNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.metric_name

MetricNames: TypeAlias = list["aws_sdk_bcm_dashboards.types.metric_name.MetricName"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricNames) -> list:
    import aws_sdk_bcm_dashboards.types.metric_name

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_dashboards.types.metric_name.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MetricNames:
    import aws_sdk_bcm_dashboards.types.metric_name

    out: MetricNames = []
    for item in data:
        out.append(
            aws_sdk_bcm_dashboards.types.metric_name.deserialize_aws_json_1_0(item)
        )
    return out
