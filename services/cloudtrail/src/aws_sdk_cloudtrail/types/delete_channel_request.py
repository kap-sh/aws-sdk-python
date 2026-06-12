"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DeleteChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.channel_arn


class DeleteChannelRequest(TypedDict):
    channel: "aws_sdk_cloudtrail.types.channel_arn.ChannelArn"
    """<p>The ARN or the <code>UUID</code> value of the channel that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteChannelRequest) -> dict:
    out: dict = {}
    out["Channel"] = value["channel"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteChannelRequest:
    out: DeleteChannelRequest = {}  # type: ignore[typeddict-item]
    if "Channel" in data:
        out["channel"] = data["Channel"]
    else:
        raise DeserializationError("DeleteChannelRequest.channel required")
    return out
