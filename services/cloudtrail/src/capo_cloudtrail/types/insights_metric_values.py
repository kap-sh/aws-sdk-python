"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InsightsMetricValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.double

InsightsMetricValues: TypeAlias = list["capo_cloudtrail.types.double.Double"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsightsMetricValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InsightsMetricValues:
    return list(data)
