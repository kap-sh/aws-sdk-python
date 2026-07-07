"""Generated from Smithy shape ``com.amazonaws.connect#MediaPlacement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.uri


class MediaPlacement(TypedDict, closed=True):
    audio_host_url: NotRequired["aws_sdk_connect.types.uri.URI"]
    """<p>The audio host URL.</p>"""
    audio_fallback_url: NotRequired["aws_sdk_connect.types.uri.URI"]
    """<p>The audio fallback URL.</p>"""
    signaling_url: NotRequired["aws_sdk_connect.types.uri.URI"]
    """<p>The signaling URL.</p>"""
    turn_control_url: NotRequired["aws_sdk_connect.types.uri.URI"]
    """<p>The turn control URL.</p>"""
    event_ingestion_url: NotRequired["aws_sdk_connect.types.uri.URI"]
    """<p>The event ingestion URL to which you send client meeting events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaPlacement) -> dict:
    out: dict = {}
    if "audio_host_url" in value:
        out["AudioHostUrl"] = value["audio_host_url"]
    if "audio_fallback_url" in value:
        out["AudioFallbackUrl"] = value["audio_fallback_url"]
    if "signaling_url" in value:
        out["SignalingUrl"] = value["signaling_url"]
    if "turn_control_url" in value:
        out["TurnControlUrl"] = value["turn_control_url"]
    if "event_ingestion_url" in value:
        out["EventIngestionUrl"] = value["event_ingestion_url"]
    return out


def deserialize_json(data: dict) -> MediaPlacement:
    out: MediaPlacement = {}  # type: ignore[typeddict-item]
    if "AudioHostUrl" in data:
        out["audio_host_url"] = data["AudioHostUrl"]
    if "AudioFallbackUrl" in data:
        out["audio_fallback_url"] = data["AudioFallbackUrl"]
    if "SignalingUrl" in data:
        out["signaling_url"] = data["SignalingUrl"]
    if "TurnControlUrl" in data:
        out["turn_control_url"] = data["TurnControlUrl"]
    if "EventIngestionUrl" in data:
        out["event_ingestion_url"] = data["EventIngestionUrl"]
    return out
