"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeDeliveryChannelStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.delivery_channel_status_list


class DescribeDeliveryChannelStatusResponse(TypedDict, closed=True):
    delivery_channels_status: NotRequired[
        "aws_sdk_config_service.types.delivery_channel_status_list.DeliveryChannelStatusList"
    ]
    """<p>A list that contains the status of a specified delivery channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveryChannelStatusResponse) -> dict:
    out: dict = {}
    if "delivery_channels_status" in value:
        import aws_sdk_config_service.types.delivery_channel_status_list

        out["DeliveryChannelsStatus"] = (
            aws_sdk_config_service.types.delivery_channel_status_list.serialize_aws_json_1_1(
                value["delivery_channels_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveryChannelStatusResponse:
    out: DescribeDeliveryChannelStatusResponse = {}  # type: ignore[typeddict-item]
    if "DeliveryChannelsStatus" in data:
        import aws_sdk_config_service.types.delivery_channel_status_list

        out["delivery_channels_status"] = (
            aws_sdk_config_service.types.delivery_channel_status_list.deserialize_aws_json_1_1(
                data["DeliveryChannelsStatus"]
            )
        )
    return out
