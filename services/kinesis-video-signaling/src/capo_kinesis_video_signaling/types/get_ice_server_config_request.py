"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#GetIceServerConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_signaling.types.client_id
    import capo_kinesis_video_signaling.types.resource_arn
    import capo_kinesis_video_signaling.types.service
    import capo_kinesis_video_signaling.types.username


class GetIceServerConfigRequest(TypedDict, closed=True):
    channel_arn: NotRequired[
        "capo_kinesis_video_signaling.types.resource_arn.ResourceARN"
    ]
    """<p>The ARN of the signaling channel to be used for the peer-to-peer connection between configured peers. </p>"""
    client_id: NotRequired["capo_kinesis_video_signaling.types.client_id.ClientId"]
    """<p>Unique identifier for the viewer. Must be unique within the signaling channel.</p>"""
    service: NotRequired["capo_kinesis_video_signaling.types.service.Service"]
    """<p>Specifies the desired service. Currently, <code>TURN</code> is the only valid value.</p>"""
    username: NotRequired["capo_kinesis_video_signaling.types.username.Username"]
    """<p>An optional user ID to be associated with the credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIceServerConfigRequest) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelARN"] = value["channel_arn"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "service" in value:
        import capo_kinesis_video_signaling.types.service

        out["Service"] = capo_kinesis_video_signaling.types.service.serialize_json(
            value["service"]
        )
    if "username" in value:
        out["Username"] = value["username"]
    return out


def deserialize_json(data: dict) -> GetIceServerConfigRequest:
    out: GetIceServerConfigRequest = {}  # type: ignore[typeddict-item]
    if "ChannelARN" in data:
        out["channel_arn"] = data["ChannelARN"]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    if "Service" in data:
        import capo_kinesis_video_signaling.types.service

        out["service"] = capo_kinesis_video_signaling.types.service.deserialize_json(
            data["Service"]
        )
    if "Username" in data:
        out["username"] = data["Username"]
    return out
