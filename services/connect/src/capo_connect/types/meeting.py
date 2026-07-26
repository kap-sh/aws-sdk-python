"""Generated from Smithy shape ``com.amazonaws.connect#Meeting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.media_placement
    import capo_connect.types.media_region
    import capo_connect.types.meeting_features_configuration
    import capo_connect.types.meeting_id


class Meeting(TypedDict, closed=True):
    media_region: NotRequired["capo_connect.types.media_region.MediaRegion"]
    """<p>The Amazon Web Services Region in which you create the meeting.</p>"""
    media_placement: NotRequired["capo_connect.types.media_placement.MediaPlacement"]
    """<p>The media placement for the meeting.</p>"""
    meeting_features: NotRequired[
        "capo_connect.types.meeting_features_configuration.MeetingFeaturesConfiguration"
    ]
    """<p>The configuration settings of the features available to a meeting.</p>"""
    meeting_id: NotRequired["capo_connect.types.meeting_id.MeetingId"]
    """<p>The Amazon Chime SDK meeting ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Meeting) -> dict:
    out: dict = {}
    if "media_region" in value:
        out["MediaRegion"] = value["media_region"]
    if "media_placement" in value:
        import capo_connect.types.media_placement

        out["MediaPlacement"] = capo_connect.types.media_placement.serialize_json(
            value["media_placement"]
        )
    if "meeting_features" in value:
        import capo_connect.types.meeting_features_configuration

        out["MeetingFeatures"] = (
            capo_connect.types.meeting_features_configuration.serialize_json(
                value["meeting_features"]
            )
        )
    if "meeting_id" in value:
        out["MeetingId"] = value["meeting_id"]
    return out


def deserialize_json(data: dict) -> Meeting:
    out: Meeting = {}  # type: ignore[typeddict-item]
    if "MediaRegion" in data:
        out["media_region"] = data["MediaRegion"]
    if "MediaPlacement" in data:
        import capo_connect.types.media_placement

        out["media_placement"] = capo_connect.types.media_placement.deserialize_json(
            data["MediaPlacement"]
        )
    if "MeetingFeatures" in data:
        import capo_connect.types.meeting_features_configuration

        out["meeting_features"] = (
            capo_connect.types.meeting_features_configuration.deserialize_json(
                data["MeetingFeatures"]
            )
        )
    if "MeetingId" in data:
        out["meeting_id"] = data["MeetingId"]
    return out
