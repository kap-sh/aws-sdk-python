"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#SingleMasterChannelEndpointConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.channel_role
    import aws_sdk_kinesis_video.types.list_of_protocols


class SingleMasterChannelEndpointConfiguration(TypedDict):
    protocols: NotRequired[
        "aws_sdk_kinesis_video.types.list_of_protocols.ListOfProtocols"
    ]
    """<p>This property is used to determine the nature of communication over this <code>SINGLE_MASTER</code> signaling channel. If <code>WSS</code> is specified, this API returns a websocket endpoint. If <code>HTTPS</code> is specified, this API returns an <code>HTTPS</code> endpoint.</p>"""
    role: NotRequired["aws_sdk_kinesis_video.types.channel_role.ChannelRole"]
    """<p>This property is used to determine messaging permissions in this <code>SINGLE_MASTER</code> signaling channel. If <code>MASTER</code> is specified, this API returns an endpoint that a client can use to receive offers from and send answers to any of the viewers on this signaling channel. If <code>VIEWER</code> is specified, this API returns an endpoint that a client can use only to send offers to another <code>MASTER</code> client on this signaling channel. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingleMasterChannelEndpointConfiguration) -> dict:
    out: dict = {}
    if "protocols" in value:
        import aws_sdk_kinesis_video.types.list_of_protocols

        out["Protocols"] = aws_sdk_kinesis_video.types.list_of_protocols.serialize_json(
            value["protocols"]
        )
    if "role" in value:
        import aws_sdk_kinesis_video.types.channel_role

        out["Role"] = aws_sdk_kinesis_video.types.channel_role.serialize_json(
            value["role"]
        )
    return out


def deserialize_json(data: dict) -> SingleMasterChannelEndpointConfiguration:
    out: SingleMasterChannelEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if "Protocols" in data:
        import aws_sdk_kinesis_video.types.list_of_protocols

        out["protocols"] = (
            aws_sdk_kinesis_video.types.list_of_protocols.deserialize_json(
                data["Protocols"]
            )
        )
    if "Role" in data:
        import aws_sdk_kinesis_video.types.channel_role

        out["role"] = aws_sdk_kinesis_video.types.channel_role.deserialize_json(
            data["Role"]
        )
    return out
