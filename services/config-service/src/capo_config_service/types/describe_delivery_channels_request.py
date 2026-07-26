"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeDeliveryChannelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.delivery_channel_name_list


class DescribeDeliveryChannelsRequest(TypedDict, closed=True):
    delivery_channel_names: NotRequired[
        "capo_config_service.types.delivery_channel_name_list.DeliveryChannelNameList"
    ]
    """<p>A list of delivery channel names.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveryChannelsRequest) -> dict:
    out: dict = {}
    if "delivery_channel_names" in value:
        import capo_config_service.types.delivery_channel_name_list

        out["DeliveryChannelNames"] = (
            capo_config_service.types.delivery_channel_name_list.serialize_aws_json_1_1(
                value["delivery_channel_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveryChannelsRequest:
    out: DescribeDeliveryChannelsRequest = {}  # type: ignore[typeddict-item]
    if "DeliveryChannelNames" in data:
        import capo_config_service.types.delivery_channel_name_list

        out["delivery_channel_names"] = (
            capo_config_service.types.delivery_channel_name_list.deserialize_aws_json_1_1(
                data["DeliveryChannelNames"]
            )
        )
    return out
