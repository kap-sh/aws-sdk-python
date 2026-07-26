"""Generated from Smithy shape ``com.amazonaws.medialive#MotionGraphicsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.motion_graphics_insertion
    import capo_medialive.types.motion_graphics_settings


class MotionGraphicsConfiguration(TypedDict, closed=True):
    motion_graphics_insertion: NotRequired[
        "capo_medialive.types.motion_graphics_insertion.MotionGraphicsInsertion"
    ]
    motion_graphics_settings: NotRequired[
        "capo_medialive.types.motion_graphics_settings.MotionGraphicsSettings"
    ]
    """Motion Graphics Settings"""


# --- restJson1 ser/de ---
def serialize_json(value: MotionGraphicsConfiguration) -> dict:
    out: dict = {}
    if "motion_graphics_insertion" in value:
        import capo_medialive.types.motion_graphics_insertion

        out["motionGraphicsInsertion"] = (
            capo_medialive.types.motion_graphics_insertion.serialize_json(
                value["motion_graphics_insertion"]
            )
        )
    if "motion_graphics_settings" in value:
        import capo_medialive.types.motion_graphics_settings

        out["motionGraphicsSettings"] = (
            capo_medialive.types.motion_graphics_settings.serialize_json(
                value["motion_graphics_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MotionGraphicsConfiguration:
    out: MotionGraphicsConfiguration = {}  # type: ignore[typeddict-item]
    if "motionGraphicsInsertion" in data:
        import capo_medialive.types.motion_graphics_insertion

        out["motion_graphics_insertion"] = (
            capo_medialive.types.motion_graphics_insertion.deserialize_json(
                data["motionGraphicsInsertion"]
            )
        )
    if "motionGraphicsSettings" in data:
        import capo_medialive.types.motion_graphics_settings

        out["motion_graphics_settings"] = (
            capo_medialive.types.motion_graphics_settings.deserialize_json(
                data["motionGraphicsSettings"]
            )
        )
    return out
