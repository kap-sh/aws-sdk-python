"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ContentFeatures``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.content_resolution


class ContentFeatures(TypedDict, closed=True):
    max_resolution: NotRequired[
        "capo_chime_sdk_meetings.types.content_resolution.ContentResolution"
    ]
    """<p>The maximum resolution for the meeting content.</p> <note> <p>Defaults to <code>FHD</code>. To use <code>UHD</code>, you must also provide a <code>MeetingFeatures:Attendee:MaxCount</code> value and override the default size limit of 250 attendees.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentFeatures) -> dict:
    out: dict = {}
    if "max_resolution" in value:
        import capo_chime_sdk_meetings.types.content_resolution

        out["MaxResolution"] = (
            capo_chime_sdk_meetings.types.content_resolution.serialize_json(
                value["max_resolution"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContentFeatures:
    out: ContentFeatures = {}  # type: ignore[typeddict-item]
    if "MaxResolution" in data:
        import capo_chime_sdk_meetings.types.content_resolution

        out["max_resolution"] = (
            capo_chime_sdk_meetings.types.content_resolution.deserialize_json(
                data["MaxResolution"]
            )
        )
    return out
