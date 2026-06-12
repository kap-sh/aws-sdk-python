"""Generated from Smithy shape ``com.amazonaws.configservice#BaseConfigurationItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.base_configuration_item

BaseConfigurationItems: TypeAlias = list[
    "aws_sdk_config_service.types.base_configuration_item.BaseConfigurationItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BaseConfigurationItems) -> list:
    import aws_sdk_config_service.types.base_configuration_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.base_configuration_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BaseConfigurationItems:
    import aws_sdk_config_service.types.base_configuration_item

    out: BaseConfigurationItems = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.base_configuration_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
