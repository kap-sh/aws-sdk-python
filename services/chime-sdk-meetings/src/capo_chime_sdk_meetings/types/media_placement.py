"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#MediaPlacement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.string


class MediaPlacement(TypedDict, closed=True):
    audio_host_url: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The audio host URL.</p>"""
    audio_fallback_url: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The audio fallback URL.</p>"""
    signaling_url: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The signaling URL.</p>"""
    turn_control_url: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The turn control URL.</p> <important> <p> <b>This parameter is deprecated and no longer used by the Amazon Chime SDK.</b> </p> </important>"""
    screen_data_url: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The screen data URL.</p> <important> <p> <b>This parameter is deprecated and no longer used by the Amazon Chime SDK.</b> </p> </important>"""
    screen_viewing_url: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The screen viewing URL.</p> <important> <p> <b>This parameter is deprecated and no longer used by the Amazon Chime SDK.</b> </p> </important>"""
    screen_sharing_url: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The screen sharing URL.</p> <important> <p> <b>This parameter is deprecated and no longer used by the Amazon Chime SDK.</b> </p> </important>"""
    event_ingestion_url: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The event ingestion URL.</p>"""


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
    if "screen_data_url" in value:
        out["ScreenDataUrl"] = value["screen_data_url"]
    if "screen_viewing_url" in value:
        out["ScreenViewingUrl"] = value["screen_viewing_url"]
    if "screen_sharing_url" in value:
        out["ScreenSharingUrl"] = value["screen_sharing_url"]
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
    if "ScreenDataUrl" in data:
        out["screen_data_url"] = data["ScreenDataUrl"]
    if "ScreenViewingUrl" in data:
        out["screen_viewing_url"] = data["ScreenViewingUrl"]
    if "ScreenSharingUrl" in data:
        out["screen_sharing_url"] = data["ScreenSharingUrl"]
    if "EventIngestionUrl" in data:
        out["event_ingestion_url"] = data["EventIngestionUrl"]
    return out
