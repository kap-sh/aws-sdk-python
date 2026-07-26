"""Generated from Smithy shape ``com.amazonaws.medialive#FrameCaptureSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1_max3600000
    import capo_medialive.types.frame_capture_interval_unit
    import capo_medialive.types.timecode_burnin_settings


class FrameCaptureSettings(TypedDict, closed=True):
    capture_interval: NotRequired[
        "capo_medialive.types.__integer_min1_max3600000.__integerMin1Max3600000"
    ]
    """The frequency at which to capture frames for inclusion in the output. May be specified in either seconds or milliseconds, as specified by captureIntervalUnits."""
    capture_interval_units: NotRequired[
        "capo_medialive.types.frame_capture_interval_unit.FrameCaptureIntervalUnit"
    ]
    """Unit for the frame capture interval."""
    timecode_burnin_settings: NotRequired[
        "capo_medialive.types.timecode_burnin_settings.TimecodeBurninSettings"
    ]
    """Timecode burn-in settings"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameCaptureSettings) -> dict:
    out: dict = {}
    if "capture_interval" in value:
        out["captureInterval"] = value["capture_interval"]
    if "capture_interval_units" in value:
        import capo_medialive.types.frame_capture_interval_unit

        out["captureIntervalUnits"] = (
            capo_medialive.types.frame_capture_interval_unit.serialize_json(
                value["capture_interval_units"]
            )
        )
    if "timecode_burnin_settings" in value:
        import capo_medialive.types.timecode_burnin_settings

        out["timecodeBurninSettings"] = (
            capo_medialive.types.timecode_burnin_settings.serialize_json(
                value["timecode_burnin_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> FrameCaptureSettings:
    out: FrameCaptureSettings = {}  # type: ignore[typeddict-item]
    if "captureInterval" in data:
        out["capture_interval"] = data["captureInterval"]
    if "captureIntervalUnits" in data:
        import capo_medialive.types.frame_capture_interval_unit

        out["capture_interval_units"] = (
            capo_medialive.types.frame_capture_interval_unit.deserialize_json(
                data["captureIntervalUnits"]
            )
        )
    if "timecodeBurninSettings" in data:
        import capo_medialive.types.timecode_burnin_settings

        out["timecode_burnin_settings"] = (
            capo_medialive.types.timecode_burnin_settings.deserialize_json(
                data["timecodeBurninSettings"]
            )
        )
    return out
