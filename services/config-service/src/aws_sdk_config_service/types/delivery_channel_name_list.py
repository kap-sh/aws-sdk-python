"""Generated from Smithy shape ``com.amazonaws.configservice#DeliveryChannelNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.channel_name

DeliveryChannelNameList: TypeAlias = list[
    "aws_sdk_config_service.types.channel_name.ChannelName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryChannelNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeliveryChannelNameList:
    return list(data)
