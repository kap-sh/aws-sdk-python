"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.configuration_item

ConfigurationItemList: TypeAlias = list[
    "capo_config_service.types.configuration_item.ConfigurationItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationItemList) -> list:
    import capo_config_service.types.configuration_item

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.configuration_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigurationItemList:
    import capo_config_service.types.configuration_item

    out: ConfigurationItemList = []
    for item in data:
        out.append(
            capo_config_service.types.configuration_item.deserialize_aws_json_1_1(item)
        )
    return out
