"""Generated from Smithy shape ``com.amazonaws.medialive#Av1ColorSpaceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.color_space_passthrough_settings
    import aws_sdk_medialive.types.hdr10_settings
    import aws_sdk_medialive.types.hlg2020_settings
    import aws_sdk_medialive.types.rec601_settings
    import aws_sdk_medialive.types.rec709_settings


class Av1ColorSpaceSettings(TypedDict, closed=True):
    color_space_passthrough_settings: NotRequired[
        "aws_sdk_medialive.types.color_space_passthrough_settings.ColorSpacePassthroughSettings"
    ]
    hdr10_settings: NotRequired["aws_sdk_medialive.types.hdr10_settings.Hdr10Settings"]
    rec601_settings: NotRequired[
        "aws_sdk_medialive.types.rec601_settings.Rec601Settings"
    ]
    rec709_settings: NotRequired[
        "aws_sdk_medialive.types.rec709_settings.Rec709Settings"
    ]
    hlg2020_settings: NotRequired[
        "aws_sdk_medialive.types.hlg2020_settings.Hlg2020Settings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Av1ColorSpaceSettings) -> dict:
    out: dict = {}
    if "color_space_passthrough_settings" in value:
        import aws_sdk_medialive.types.color_space_passthrough_settings

        out["colorSpacePassthroughSettings"] = (
            aws_sdk_medialive.types.color_space_passthrough_settings.serialize_json(
                value["color_space_passthrough_settings"]
            )
        )
    if "hdr10_settings" in value:
        import aws_sdk_medialive.types.hdr10_settings

        out["hdr10Settings"] = aws_sdk_medialive.types.hdr10_settings.serialize_json(
            value["hdr10_settings"]
        )
    if "rec601_settings" in value:
        import aws_sdk_medialive.types.rec601_settings

        out["rec601Settings"] = aws_sdk_medialive.types.rec601_settings.serialize_json(
            value["rec601_settings"]
        )
    if "rec709_settings" in value:
        import aws_sdk_medialive.types.rec709_settings

        out["rec709Settings"] = aws_sdk_medialive.types.rec709_settings.serialize_json(
            value["rec709_settings"]
        )
    if "hlg2020_settings" in value:
        import aws_sdk_medialive.types.hlg2020_settings

        out["hlg2020Settings"] = (
            aws_sdk_medialive.types.hlg2020_settings.serialize_json(
                value["hlg2020_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Av1ColorSpaceSettings:
    out: Av1ColorSpaceSettings = {}  # type: ignore[typeddict-item]
    if "colorSpacePassthroughSettings" in data:
        import aws_sdk_medialive.types.color_space_passthrough_settings

        out["color_space_passthrough_settings"] = (
            aws_sdk_medialive.types.color_space_passthrough_settings.deserialize_json(
                data["colorSpacePassthroughSettings"]
            )
        )
    if "hdr10Settings" in data:
        import aws_sdk_medialive.types.hdr10_settings

        out["hdr10_settings"] = aws_sdk_medialive.types.hdr10_settings.deserialize_json(
            data["hdr10Settings"]
        )
    if "rec601Settings" in data:
        import aws_sdk_medialive.types.rec601_settings

        out["rec601_settings"] = (
            aws_sdk_medialive.types.rec601_settings.deserialize_json(
                data["rec601Settings"]
            )
        )
    if "rec709Settings" in data:
        import aws_sdk_medialive.types.rec709_settings

        out["rec709_settings"] = (
            aws_sdk_medialive.types.rec709_settings.deserialize_json(
                data["rec709Settings"]
            )
        )
    if "hlg2020Settings" in data:
        import aws_sdk_medialive.types.hlg2020_settings

        out["hlg2020_settings"] = (
            aws_sdk_medialive.types.hlg2020_settings.deserialize_json(
                data["hlg2020Settings"]
            )
        )
    return out
