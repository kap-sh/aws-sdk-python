"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UpdatePresetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.preset


class UpdatePresetResponse(TypedDict):
    preset: NotRequired["aws_sdk_mediaconvert.types.preset.Preset"]
    """A preset is a collection of preconfigured media conversion settings that you want MediaConvert to apply to the output during the conversion process."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePresetResponse) -> dict:
    out: dict = {}
    if "preset" in value:
        import aws_sdk_mediaconvert.types.preset

        out["preset"] = aws_sdk_mediaconvert.types.preset.serialize_json(
            value["preset"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePresetResponse:
    out: UpdatePresetResponse = {}  # type: ignore[typeddict-item]
    if "preset" in data:
        import aws_sdk_mediaconvert.types.preset

        out["preset"] = aws_sdk_mediaconvert.types.preset.deserialize_json(
            data["preset"]
        )
    return out
