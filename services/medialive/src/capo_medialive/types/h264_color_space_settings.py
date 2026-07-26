"""Generated from Smithy shape ``com.amazonaws.medialive#H264ColorSpaceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.color_space_passthrough_settings
    import capo_medialive.types.rec601_settings
    import capo_medialive.types.rec709_settings


class H264ColorSpaceSettings(TypedDict, closed=True):
    color_space_passthrough_settings: NotRequired[
        "capo_medialive.types.color_space_passthrough_settings.ColorSpacePassthroughSettings"
    ]
    rec601_settings: NotRequired["capo_medialive.types.rec601_settings.Rec601Settings"]
    rec709_settings: NotRequired["capo_medialive.types.rec709_settings.Rec709Settings"]


# --- restJson1 ser/de ---
def serialize_json(value: H264ColorSpaceSettings) -> dict:
    out: dict = {}
    if "color_space_passthrough_settings" in value:
        import capo_medialive.types.color_space_passthrough_settings

        out["colorSpacePassthroughSettings"] = (
            capo_medialive.types.color_space_passthrough_settings.serialize_json(
                value["color_space_passthrough_settings"]
            )
        )
    if "rec601_settings" in value:
        import capo_medialive.types.rec601_settings

        out["rec601Settings"] = capo_medialive.types.rec601_settings.serialize_json(
            value["rec601_settings"]
        )
    if "rec709_settings" in value:
        import capo_medialive.types.rec709_settings

        out["rec709Settings"] = capo_medialive.types.rec709_settings.serialize_json(
            value["rec709_settings"]
        )
    return out


def deserialize_json(data: dict) -> H264ColorSpaceSettings:
    out: H264ColorSpaceSettings = {}  # type: ignore[typeddict-item]
    if "colorSpacePassthroughSettings" in data:
        import capo_medialive.types.color_space_passthrough_settings

        out["color_space_passthrough_settings"] = (
            capo_medialive.types.color_space_passthrough_settings.deserialize_json(
                data["colorSpacePassthroughSettings"]
            )
        )
    if "rec601Settings" in data:
        import capo_medialive.types.rec601_settings

        out["rec601_settings"] = capo_medialive.types.rec601_settings.deserialize_json(
            data["rec601Settings"]
        )
    if "rec709Settings" in data:
        import capo_medialive.types.rec709_settings

        out["rec709_settings"] = capo_medialive.types.rec709_settings.deserialize_json(
            data["rec709Settings"]
        )
    return out
