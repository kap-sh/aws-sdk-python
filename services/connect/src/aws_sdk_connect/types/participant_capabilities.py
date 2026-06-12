"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantCapabilities``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.screen_share_capability
    import aws_sdk_connect.types.video_capability


class ParticipantCapabilities(TypedDict):
    video: NotRequired["aws_sdk_connect.types.video_capability.VideoCapability"]
    """<p>The configuration having the video and screen sharing capabilities for participants over the call.</p>"""
    screen_share: NotRequired[
        "aws_sdk_connect.types.screen_share_capability.ScreenShareCapability"
    ]
    """<p>The screen sharing capability that is enabled for the participant. <code>SEND</code> indicates the participant can share their screen.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantCapabilities) -> dict:
    out: dict = {}
    if "video" in value:
        import aws_sdk_connect.types.video_capability

        out["Video"] = aws_sdk_connect.types.video_capability.serialize_json(
            value["video"]
        )
    if "screen_share" in value:
        import aws_sdk_connect.types.screen_share_capability

        out["ScreenShare"] = (
            aws_sdk_connect.types.screen_share_capability.serialize_json(
                value["screen_share"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParticipantCapabilities:
    out: ParticipantCapabilities = {}  # type: ignore[typeddict-item]
    if "Video" in data:
        import aws_sdk_connect.types.video_capability

        out["video"] = aws_sdk_connect.types.video_capability.deserialize_json(
            data["Video"]
        )
    if "ScreenShare" in data:
        import aws_sdk_connect.types.screen_share_capability

        out["screen_share"] = (
            aws_sdk_connect.types.screen_share_capability.deserialize_json(
                data["ScreenShare"]
            )
        )
    return out
