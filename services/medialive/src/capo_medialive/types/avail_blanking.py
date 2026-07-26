"""Generated from Smithy shape ``com.amazonaws.medialive#AvailBlanking``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.avail_blanking_state
    import capo_medialive.types.input_location


class AvailBlanking(TypedDict, closed=True):
    avail_blanking_image: NotRequired[
        "capo_medialive.types.input_location.InputLocation"
    ]
    """Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported."""
    state: NotRequired["capo_medialive.types.avail_blanking_state.AvailBlankingState"]
    """When set to enabled, causes video, audio and captions to be blanked when insertion metadata is added."""


# --- restJson1 ser/de ---
def serialize_json(value: AvailBlanking) -> dict:
    out: dict = {}
    if "avail_blanking_image" in value:
        import capo_medialive.types.input_location

        out["availBlankingImage"] = capo_medialive.types.input_location.serialize_json(
            value["avail_blanking_image"]
        )
    if "state" in value:
        import capo_medialive.types.avail_blanking_state

        out["state"] = capo_medialive.types.avail_blanking_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> AvailBlanking:
    out: AvailBlanking = {}  # type: ignore[typeddict-item]
    if "availBlankingImage" in data:
        import capo_medialive.types.input_location

        out["avail_blanking_image"] = (
            capo_medialive.types.input_location.deserialize_json(
                data["availBlankingImage"]
            )
        )
    if "state" in data:
        import capo_medialive.types.avail_blanking_state

        out["state"] = capo_medialive.types.avail_blanking_state.deserialize_json(
            data["state"]
        )
    return out
