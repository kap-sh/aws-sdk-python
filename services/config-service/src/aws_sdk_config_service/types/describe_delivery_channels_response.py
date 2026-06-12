"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeDeliveryChannelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.delivery_channel_list


class DescribeDeliveryChannelsResponse(TypedDict):
    delivery_channels: NotRequired[
        "aws_sdk_config_service.types.delivery_channel_list.DeliveryChannelList"
    ]
    """<p>A list that contains the descriptions of the specified delivery channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveryChannelsResponse) -> dict:
    out: dict = {}
    if "delivery_channels" in value:
        import aws_sdk_config_service.types.delivery_channel_list

        out["DeliveryChannels"] = (
            aws_sdk_config_service.types.delivery_channel_list.serialize_aws_json_1_1(
                value["delivery_channels"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveryChannelsResponse:
    out: DescribeDeliveryChannelsResponse = {}  # type: ignore[typeddict-item]
    if "DeliveryChannels" in data:
        import aws_sdk_config_service.types.delivery_channel_list

        out["delivery_channels"] = (
            aws_sdk_config_service.types.delivery_channel_list.deserialize_aws_json_1_1(
                data["DeliveryChannels"]
            )
        )
    return out
