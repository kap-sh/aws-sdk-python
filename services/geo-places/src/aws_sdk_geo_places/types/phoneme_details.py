"""Generated from Smithy shape ``com.amazonaws.geoplaces#PhonemeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.address_component_phonemes
    import aws_sdk_geo_places.types.phoneme_transcription_list


class PhonemeDetails(TypedDict):
    title: NotRequired[
        "aws_sdk_geo_places.types.phoneme_transcription_list.PhonemeTranscriptionList"
    ]
    """<p>List of <code>PhonemeTranscription</code>. See <code>PhonemeTranscription</code> for fields.</p>"""
    address: NotRequired[
        "aws_sdk_geo_places.types.address_component_phonemes.AddressComponentPhonemes"
    ]
    """<p>How to pronounce the address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhonemeDetails) -> dict:
    out: dict = {}
    if "title" in value:
        import aws_sdk_geo_places.types.phoneme_transcription_list

        out["Title"] = (
            aws_sdk_geo_places.types.phoneme_transcription_list.serialize_json(
                value["title"]
            )
        )
    if "address" in value:
        import aws_sdk_geo_places.types.address_component_phonemes

        out["Address"] = (
            aws_sdk_geo_places.types.address_component_phonemes.serialize_json(
                value["address"]
            )
        )
    return out


def deserialize_json(data: dict) -> PhonemeDetails:
    out: PhonemeDetails = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        import aws_sdk_geo_places.types.phoneme_transcription_list

        out["title"] = (
            aws_sdk_geo_places.types.phoneme_transcription_list.deserialize_json(
                data["Title"]
            )
        )
    if "Address" in data:
        import aws_sdk_geo_places.types.address_component_phonemes

        out["address"] = (
            aws_sdk_geo_places.types.address_component_phonemes.deserialize_json(
                data["Address"]
            )
        )
    return out
