"""Generated from Smithy shape ``com.amazonaws.geoplaces#PhonemeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.address_component_phonemes
    import capo_geo_places.types.phoneme_transcription_list


class PhonemeDetails(TypedDict, closed=True):
    title: NotRequired[
        "capo_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>List of <code>PhonemeTranscription</code>. See <code>PhonemeTranscription</code> for fields.</p>"""
    address: NotRequired[
        "capo_geo_places.types.address_component_phonemes.AddressComponentPhonemes"
    ]
    """<p>How to pronounce the address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhonemeDetails) -> dict:
    out: dict = {}
    if "title" in value:
        import capo_geo_places.types.phoneme_transcription_list

        out["Title"] = capo_geo_places.types.phoneme_transcription_list.serialize_json(
            value["title"]
        )
    if "address" in value:
        import capo_geo_places.types.address_component_phonemes

        out["Address"] = (
            capo_geo_places.types.address_component_phonemes.serialize_json(
                value["address"]
            )
        )
    return out


def deserialize_json(data: dict) -> PhonemeDetails:
    out: PhonemeDetails = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        import capo_geo_places.types.phoneme_transcription_list

        out["title"] = (
            capo_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["Title"]
            )
        )
    if "Address" in data:
        import capo_geo_places.types.address_component_phonemes

        out["address"] = (
            capo_geo_places.types.address_component_phonemes.deserialize_json(
                data["Address"]
            )
        )
    return out
