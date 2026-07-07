"""Generated from Smithy shape ``com.amazonaws.groundstation#TrackingOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.program_track_settings


class TrackingOverrides(TypedDict, closed=True):
    program_track_settings: NotRequired[
        "aws_sdk_groundstation.types.program_track_settings.ProgramTrackSettings"
    ]
    """<p>Program track settings to override for antenna tracking during the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrackingOverrides) -> dict:
    out: dict = {}
    if "program_track_settings" in value:
        import aws_sdk_groundstation.types.program_track_settings

        out["programTrackSettings"] = (
            aws_sdk_groundstation.types.program_track_settings.serialize_json(
                value["program_track_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> TrackingOverrides:
    out: TrackingOverrides = {}  # type: ignore[typeddict-item]
    if "programTrackSettings" in data:
        import aws_sdk_groundstation.types.program_track_settings

        out["program_track_settings"] = (
            aws_sdk_groundstation.types.program_track_settings.deserialize_json(
                data["programTrackSettings"]
            )
        )
    return out
