"""Generated from Smithy shape ``com.amazonaws.cloudtrail#AggregationConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.aggregation_configuration

AggregationConfigurations: TypeAlias = list[
    "aws_sdk_cloudtrail.types.aggregation_configuration.AggregationConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregationConfigurations) -> list:
    import aws_sdk_cloudtrail.types.aggregation_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudtrail.types.aggregation_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AggregationConfigurations:
    import aws_sdk_cloudtrail.types.aggregation_configuration

    out: AggregationConfigurations = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.aggregation_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
