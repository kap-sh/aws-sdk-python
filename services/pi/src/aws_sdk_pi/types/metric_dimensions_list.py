"""Generated from Smithy shape ``com.amazonaws.pi#MetricDimensionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.metric_dimension_groups

MetricDimensionsList: TypeAlias = list[
    "aws_sdk_pi.types.metric_dimension_groups.MetricDimensionGroups"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDimensionsList) -> list:
    import aws_sdk_pi.types.metric_dimension_groups

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pi.types.metric_dimension_groups.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MetricDimensionsList:
    import aws_sdk_pi.types.metric_dimension_groups

    out: MetricDimensionsList = []
    for item in data:
        out.append(
            aws_sdk_pi.types.metric_dimension_groups.deserialize_aws_json_1_1(item)
        )
    return out
