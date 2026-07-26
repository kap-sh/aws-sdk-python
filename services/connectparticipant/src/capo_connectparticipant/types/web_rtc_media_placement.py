"""Generated from Smithy shape ``com.amazonaws.connectparticipant#WebRTCMediaPlacement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.uri


class WebRTCMediaPlacement(TypedDict, closed=True):
    audio_host_url: NotRequired["capo_connectparticipant.types.uri.URI"]
    """<p>The audio host URL.</p>"""
    audio_fallback_url: NotRequired["capo_connectparticipant.types.uri.URI"]
    """<p>The audio fallback URL.</p>"""
    signaling_url: NotRequired["capo_connectparticipant.types.uri.URI"]
    """<p>The signaling URL.</p>"""
    event_ingestion_url: NotRequired["capo_connectparticipant.types.uri.URI"]
    """<p>The event ingestion URL to which you send client meeting events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebRTCMediaPlacement) -> dict:
    out: dict = {}
    if "audio_host_url" in value:
        out["AudioHostUrl"] = value["audio_host_url"]
    if "audio_fallback_url" in value:
        out["AudioFallbackUrl"] = value["audio_fallback_url"]
    if "signaling_url" in value:
        out["SignalingUrl"] = value["signaling_url"]
    if "event_ingestion_url" in value:
        out["EventIngestionUrl"] = value["event_ingestion_url"]
    return out


def deserialize_json(data: dict) -> WebRTCMediaPlacement:
    out: WebRTCMediaPlacement = {}  # type: ignore[typeddict-item]
    if "AudioHostUrl" in data:
        out["audio_host_url"] = data["AudioHostUrl"]
    if "AudioFallbackUrl" in data:
        out["audio_fallback_url"] = data["AudioFallbackUrl"]
    if "SignalingUrl" in data:
        out["signaling_url"] = data["SignalingUrl"]
    if "EventIngestionUrl" in data:
        out["event_ingestion_url"] = data["EventIngestionUrl"]
    return out
