"""Generated from Smithy shape ``com.amazonaws.configservice#PutDeliveryChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.delivery_channel


class PutDeliveryChannelRequest(TypedDict, closed=True):
    delivery_channel: "aws_sdk_config_service.types.delivery_channel.DeliveryChannel"
    """<p>An object for the delivery channel. A delivery channel sends notifications and updated configuration states. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDeliveryChannelRequest) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.delivery_channel

    out["DeliveryChannel"] = (
        aws_sdk_config_service.types.delivery_channel.serialize_aws_json_1_1(
            value["delivery_channel"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDeliveryChannelRequest:
    out: PutDeliveryChannelRequest = {}  # type: ignore[typeddict-item]
    if "DeliveryChannel" in data:
        import aws_sdk_config_service.types.delivery_channel

        out["delivery_channel"] = (
            aws_sdk_config_service.types.delivery_channel.deserialize_aws_json_1_1(
                data["DeliveryChannel"]
            )
        )
    else:
        raise DeserializationError(
            "PutDeliveryChannelRequest.delivery_channel required"
        )
    return out
