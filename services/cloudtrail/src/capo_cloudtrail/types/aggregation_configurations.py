"""Generated from Smithy shape ``com.amazonaws.cloudtrail#AggregationConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.aggregation_configuration

AggregationConfigurations: TypeAlias = list[
    "capo_cloudtrail.types.aggregation_configuration.AggregationConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregationConfigurations) -> list:
    import capo_cloudtrail.types.aggregation_configuration

    out: list = []
    for item in value:
        out.append(
            capo_cloudtrail.types.aggregation_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AggregationConfigurations:
    import capo_cloudtrail.types.aggregation_configuration

    out: AggregationConfigurations = []
    for item in data:
        out.append(
            capo_cloudtrail.types.aggregation_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
