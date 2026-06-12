"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#AssociateChannelFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class AssociateChannelFlowRequest(TypedDict):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    channel_flow_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel flow.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateChannelFlowRequest) -> dict:
    out: dict = {}
    out["ChannelFlowArn"] = value["channel_flow_arn"]
    return out


def deserialize_json(data: dict) -> AssociateChannelFlowRequest:
    out: AssociateChannelFlowRequest = {}  # type: ignore[typeddict-item]
    if "ChannelFlowArn" in data:
        out["channel_flow_arn"] = data["ChannelFlowArn"]
    else:
        raise DeserializationError(
            "AssociateChannelFlowRequest.channel_flow_arn required"
        )
    return out
