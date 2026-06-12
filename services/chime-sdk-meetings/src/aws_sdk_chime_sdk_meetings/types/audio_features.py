"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#AudioFeatures``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.meeting_feature_status


class AudioFeatures(TypedDict):
    echo_reduction: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.meeting_feature_status.MeetingFeatureStatus"
    ]
    """<p>Makes echo reduction available to clients who connect to the meeting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioFeatures) -> dict:
    out: dict = {}
    if "echo_reduction" in value:
        import aws_sdk_chime_sdk_meetings.types.meeting_feature_status

        out["EchoReduction"] = (
            aws_sdk_chime_sdk_meetings.types.meeting_feature_status.serialize_json(
                value["echo_reduction"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioFeatures:
    out: AudioFeatures = {}  # type: ignore[typeddict-item]
    if "EchoReduction" in data:
        import aws_sdk_chime_sdk_meetings.types.meeting_feature_status

        out["echo_reduction"] = (
            aws_sdk_chime_sdk_meetings.types.meeting_feature_status.deserialize_json(
                data["EchoReduction"]
            )
        )
    return out
