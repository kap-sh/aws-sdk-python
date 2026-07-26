"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationAggregatorNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.configuration_aggregator_name

ConfigurationAggregatorNameList: TypeAlias = list[
    "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationAggregatorNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConfigurationAggregatorNameList:
    return list(data)
