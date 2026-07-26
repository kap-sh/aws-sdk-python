"""Generated from Smithy shape ``com.amazonaws.medialive#AudioDolbyEDecode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.dolby_e_program_selection


class AudioDolbyEDecode(TypedDict, closed=True):
    program_selection: NotRequired[
        "capo_medialive.types.dolby_e_program_selection.DolbyEProgramSelection"
    ]
    """Applies only to Dolby E. Enter the program ID (according to the metadata in the audio) of the Dolby E program to extract from the specified track. One program extracted per audio selector. To select multiple programs, create multiple selectors with the same Track and different Program numbers. “All channels” means to ignore the program IDs and include all the channels in this selector; useful if metadata is known to be incorrect."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioDolbyEDecode) -> dict:
    out: dict = {}
    if "program_selection" in value:
        import capo_medialive.types.dolby_e_program_selection

        out["programSelection"] = (
            capo_medialive.types.dolby_e_program_selection.serialize_json(
                value["program_selection"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioDolbyEDecode:
    out: AudioDolbyEDecode = {}  # type: ignore[typeddict-item]
    if "programSelection" in data:
        import capo_medialive.types.dolby_e_program_selection

        out["program_selection"] = (
            capo_medialive.types.dolby_e_program_selection.deserialize_json(
                data["programSelection"]
            )
        )
    return out
