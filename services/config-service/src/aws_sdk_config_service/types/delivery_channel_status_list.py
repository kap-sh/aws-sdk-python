"""Generated from Smithy shape ``com.amazonaws.configservice#DeliveryChannelStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.delivery_channel_status

DeliveryChannelStatusList: TypeAlias = list[
    "aws_sdk_config_service.types.delivery_channel_status.DeliveryChannelStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryChannelStatusList) -> list:
    import aws_sdk_config_service.types.delivery_channel_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.delivery_channel_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeliveryChannelStatusList:
    import aws_sdk_config_service.types.delivery_channel_status

    out: DeliveryChannelStatusList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.delivery_channel_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
