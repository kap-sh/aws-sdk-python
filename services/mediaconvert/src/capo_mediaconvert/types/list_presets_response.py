"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ListPresetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_preset
    import capo_mediaconvert.types.__string


class ListPresetsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Use this string to request the next batch of presets."""
    presets: NotRequired["capo_mediaconvert.types.__list_of_preset.__listOfPreset"]
    """List of presets"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPresetsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "presets" in value:
        import capo_mediaconvert.types.__list_of_preset

        out["presets"] = capo_mediaconvert.types.__list_of_preset.serialize_json(
            value["presets"]
        )
    return out


def deserialize_json(data: dict) -> ListPresetsResponse:
    out: ListPresetsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "presets" in data:
        import capo_mediaconvert.types.__list_of_preset

        out["presets"] = capo_mediaconvert.types.__list_of_preset.deserialize_json(
            data["presets"]
        )
    return out
