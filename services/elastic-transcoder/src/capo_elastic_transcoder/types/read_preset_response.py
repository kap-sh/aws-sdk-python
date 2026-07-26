"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ReadPresetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.preset


class ReadPresetResponse(TypedDict, closed=True):
    preset: NotRequired["capo_elastic_transcoder.types.preset.Preset"]
    """<p>A section of the response body that provides information about the preset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadPresetResponse) -> dict:
    out: dict = {}
    if "preset" in value:
        import capo_elastic_transcoder.types.preset

        out["Preset"] = capo_elastic_transcoder.types.preset.serialize_json(
            value["preset"]
        )
    return out


def deserialize_json(data: dict) -> ReadPresetResponse:
    out: ReadPresetResponse = {}  # type: ignore[typeddict-item]
    if "Preset" in data:
        import capo_elastic_transcoder.types.preset

        out["preset"] = capo_elastic_transcoder.types.preset.deserialize_json(
            data["Preset"]
        )
    return out
