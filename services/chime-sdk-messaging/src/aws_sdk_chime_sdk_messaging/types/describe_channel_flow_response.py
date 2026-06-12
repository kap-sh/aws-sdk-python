"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelFlowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_flow


class DescribeChannelFlowResponse(TypedDict):
    channel_flow: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_flow.ChannelFlow"
    ]
    """<p>The channel flow details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelFlowResponse) -> dict:
    out: dict = {}
    if "channel_flow" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_flow

        out["ChannelFlow"] = (
            aws_sdk_chime_sdk_messaging.types.channel_flow.serialize_json(
                value["channel_flow"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeChannelFlowResponse:
    out: DescribeChannelFlowResponse = {}  # type: ignore[typeddict-item]
    if "ChannelFlow" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_flow

        out["channel_flow"] = (
            aws_sdk_chime_sdk_messaging.types.channel_flow.deserialize_json(
                data["ChannelFlow"]
            )
        )
    return out
