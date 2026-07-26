"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#AttendeeCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.media_capabilities


class AttendeeCapabilities(TypedDict, closed=True):
    audio: "capo_chime_sdk_meetings.types.media_capabilities.MediaCapabilities"
    """<p>The audio capability assigned to an attendee.</p>"""
    video: "capo_chime_sdk_meetings.types.media_capabilities.MediaCapabilities"
    """<p>The video capability assigned to an attendee.</p>"""
    content: "capo_chime_sdk_meetings.types.media_capabilities.MediaCapabilities"
    """<p>The content capability assigned to an attendee.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttendeeCapabilities) -> dict:
    out: dict = {}
    import capo_chime_sdk_meetings.types.media_capabilities

    out["Audio"] = capo_chime_sdk_meetings.types.media_capabilities.serialize_json(
        value["audio"]
    )
    import capo_chime_sdk_meetings.types.media_capabilities

    out["Video"] = capo_chime_sdk_meetings.types.media_capabilities.serialize_json(
        value["video"]
    )
    import capo_chime_sdk_meetings.types.media_capabilities

    out["Content"] = capo_chime_sdk_meetings.types.media_capabilities.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> AttendeeCapabilities:
    out: AttendeeCapabilities = {}  # type: ignore[typeddict-item]
    if "Audio" in data:
        import capo_chime_sdk_meetings.types.media_capabilities

        out["audio"] = (
            capo_chime_sdk_meetings.types.media_capabilities.deserialize_json(
                data["Audio"]
            )
        )
    else:
        raise DeserializationError("AttendeeCapabilities.audio required")
    if "Video" in data:
        import capo_chime_sdk_meetings.types.media_capabilities

        out["video"] = (
            capo_chime_sdk_meetings.types.media_capabilities.deserialize_json(
                data["Video"]
            )
        )
    else:
        raise DeserializationError("AttendeeCapabilities.video required")
    if "Content" in data:
        import capo_chime_sdk_meetings.types.media_capabilities

        out["content"] = (
            capo_chime_sdk_meetings.types.media_capabilities.deserialize_json(
                data["Content"]
            )
        )
    else:
        raise DeserializationError("AttendeeCapabilities.content required")
    return out
