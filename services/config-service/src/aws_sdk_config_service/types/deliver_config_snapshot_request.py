"""Generated from Smithy shape ``com.amazonaws.configservice#DeliverConfigSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.channel_name


class DeliverConfigSnapshotRequest(TypedDict):
    delivery_channel_name: "aws_sdk_config_service.types.channel_name.ChannelName"
    """<p>The name of the delivery channel through which the snapshot is delivered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverConfigSnapshotRequest) -> dict:
    out: dict = {}
    out["deliveryChannelName"] = value["delivery_channel_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliverConfigSnapshotRequest:
    out: DeliverConfigSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "deliveryChannelName" in data:
        out["delivery_channel_name"] = data["deliveryChannelName"]
    else:
        raise DeserializationError(
            "DeliverConfigSnapshotRequest.delivery_channel_name required"
        )
    return out
