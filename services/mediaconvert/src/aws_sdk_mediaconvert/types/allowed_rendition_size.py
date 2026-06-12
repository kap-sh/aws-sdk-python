"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AllowedRenditionSize``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min32_max8192
    import aws_sdk_mediaconvert.types.required_flag


class AllowedRenditionSize(TypedDict):
    height: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8192.__integerMin32Max8192"
    ]
    """Use Height to define the video resolution height, in pixels, for this rule."""
    required: NotRequired["aws_sdk_mediaconvert.types.required_flag.RequiredFlag"]
    """Set to ENABLED to force a rendition to be included."""
    width: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8192.__integerMin32Max8192"
    ]
    """Use Width to define the video resolution width, in pixels, for this rule."""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedRenditionSize) -> dict:
    out: dict = {}
    if "height" in value:
        out["height"] = value["height"]
    if "required" in value:
        import aws_sdk_mediaconvert.types.required_flag

        out["required"] = aws_sdk_mediaconvert.types.required_flag.serialize_json(
            value["required"]
        )
    if "width" in value:
        out["width"] = value["width"]
    return out


def deserialize_json(data: dict) -> AllowedRenditionSize:
    out: AllowedRenditionSize = {}  # type: ignore[typeddict-item]
    if "height" in data:
        out["height"] = data["height"]
    if "required" in data:
        import aws_sdk_mediaconvert.types.required_flag

        out["required"] = aws_sdk_mediaconvert.types.required_flag.deserialize_json(
            data["required"]
        )
    if "width" in data:
        out["width"] = data["width"]
    return out
