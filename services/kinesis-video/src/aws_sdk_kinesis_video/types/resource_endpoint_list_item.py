"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ResourceEndpointListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.channel_protocol
    import aws_sdk_kinesis_video.types.resource_endpoint


class ResourceEndpointListItem(TypedDict):
    protocol: NotRequired[
        "aws_sdk_kinesis_video.types.channel_protocol.ChannelProtocol"
    ]
    """<p>The protocol of the signaling channel returned by the <code>GetSignalingChannelEndpoint</code> API.</p>"""
    resource_endpoint: NotRequired[
        "aws_sdk_kinesis_video.types.resource_endpoint.ResourceEndpoint"
    ]
    """<p>The endpoint of the signaling channel returned by the <code>GetSignalingChannelEndpoint</code> API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceEndpointListItem) -> dict:
    out: dict = {}
    if "protocol" in value:
        import aws_sdk_kinesis_video.types.channel_protocol

        out["Protocol"] = aws_sdk_kinesis_video.types.channel_protocol.serialize_json(
            value["protocol"]
        )
    if "resource_endpoint" in value:
        out["ResourceEndpoint"] = value["resource_endpoint"]
    return out


def deserialize_json(data: dict) -> ResourceEndpointListItem:
    out: ResourceEndpointListItem = {}  # type: ignore[typeddict-item]
    if "Protocol" in data:
        import aws_sdk_kinesis_video.types.channel_protocol

        out["protocol"] = aws_sdk_kinesis_video.types.channel_protocol.deserialize_json(
            data["Protocol"]
        )
    if "ResourceEndpoint" in data:
        out["resource_endpoint"] = data["ResourceEndpoint"]
    return out
