"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CreatePresetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.preset
    import aws_sdk_elastic_transcoder.types.string


class CreatePresetResponse(TypedDict, closed=True):
    preset: NotRequired["aws_sdk_elastic_transcoder.types.preset.Preset"]
    """<p>A section of the response body that provides information about the preset that is created.</p>"""
    warning: NotRequired["aws_sdk_elastic_transcoder.types.string.String"]
    """<p>If the preset settings don't comply with the standards for the video codec but Elastic Transcoder created the preset, this message explains the reason the preset settings don't meet the standard. Elastic Transcoder created the preset because the settings might produce acceptable output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePresetResponse) -> dict:
    out: dict = {}
    if "preset" in value:
        import aws_sdk_elastic_transcoder.types.preset

        out["Preset"] = aws_sdk_elastic_transcoder.types.preset.serialize_json(
            value["preset"]
        )
    if "warning" in value:
        out["Warning"] = value["warning"]
    return out


def deserialize_json(data: dict) -> CreatePresetResponse:
    out: CreatePresetResponse = {}  # type: ignore[typeddict-item]
    if "Preset" in data:
        import aws_sdk_elastic_transcoder.types.preset

        out["preset"] = aws_sdk_elastic_transcoder.types.preset.deserialize_json(
            data["Preset"]
        )
    if "Warning" in data:
        out["warning"] = data["Warning"]
    return out
