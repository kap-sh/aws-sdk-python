"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeDeliveryChannelStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.delivery_channel_name_list


class DescribeDeliveryChannelStatusRequest(TypedDict):
    delivery_channel_names: NotRequired[
        "aws_sdk_config_service.types.delivery_channel_name_list.DeliveryChannelNameList"
    ]
    """<p>A list of delivery channel names.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveryChannelStatusRequest) -> dict:
    out: dict = {}
    if "delivery_channel_names" in value:
        import aws_sdk_config_service.types.delivery_channel_name_list

        out["DeliveryChannelNames"] = (
            aws_sdk_config_service.types.delivery_channel_name_list.serialize_aws_json_1_1(
                value["delivery_channel_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveryChannelStatusRequest:
    out: DescribeDeliveryChannelStatusRequest = {}  # type: ignore[typeddict-item]
    if "DeliveryChannelNames" in data:
        import aws_sdk_config_service.types.delivery_channel_name_list

        out["delivery_channel_names"] = (
            aws_sdk_config_service.types.delivery_channel_name_list.deserialize_aws_json_1_1(
                data["DeliveryChannelNames"]
            )
        )
    return out
