"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteDeliveryChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.channel_name


class DeleteDeliveryChannelRequest(TypedDict, closed=True):
    delivery_channel_name: "aws_sdk_config_service.types.channel_name.ChannelName"
    """<p>The name of the delivery channel that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeliveryChannelRequest) -> dict:
    out: dict = {}
    out["DeliveryChannelName"] = value["delivery_channel_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeliveryChannelRequest:
    out: DeleteDeliveryChannelRequest = {}  # type: ignore[typeddict-item]
    if "DeliveryChannelName" in data:
        out["delivery_channel_name"] = data["DeliveryChannelName"]
    else:
        raise DeserializationError(
            "DeleteDeliveryChannelRequest.delivery_channel_name required"
        )
    return out
