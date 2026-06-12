"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationAggregatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_aggregator

ConfigurationAggregatorList: TypeAlias = list[
    "aws_sdk_config_service.types.configuration_aggregator.ConfigurationAggregator"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationAggregatorList) -> list:
    import aws_sdk_config_service.types.configuration_aggregator

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.configuration_aggregator.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigurationAggregatorList:
    import aws_sdk_config_service.types.configuration_aggregator

    out: ConfigurationAggregatorList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.configuration_aggregator.deserialize_aws_json_1_1(
                item
            )
        )
    return out
