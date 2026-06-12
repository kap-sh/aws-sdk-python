"""Generated from Smithy shape ``com.amazonaws.gamelift#MetricGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.metric_group

MetricGroupList: TypeAlias = list["aws_sdk_gamelift.types.metric_group.MetricGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricGroupList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MetricGroupList:
    return list(data)
