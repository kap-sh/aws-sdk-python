"""Generated from Smithy shape ``com.amazonaws.configservice#DeliveryChannelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.delivery_channel

DeliveryChannelList: TypeAlias = list[
    "capo_config_service.types.delivery_channel.DeliveryChannel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryChannelList) -> list:
    import capo_config_service.types.delivery_channel

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.delivery_channel.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeliveryChannelList:
    import capo_config_service.types.delivery_channel

    out: DeliveryChannelList = []
    for item in data:
        out.append(
            capo_config_service.types.delivery_channel.deserialize_aws_json_1_1(item)
        )
    return out
