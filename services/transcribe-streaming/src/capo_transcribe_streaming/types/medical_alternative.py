"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalAlternative``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_entity_list
    import capo_transcribe_streaming.types.medical_item_list
    import capo_transcribe_streaming.types.string


class MedicalAlternative(TypedDict, closed=True):
    transcript: NotRequired["capo_transcribe_streaming.types.string.String"]
    """<p>Contains transcribed text.</p>"""
    items: NotRequired[
        "capo_transcribe_streaming.types.medical_item_list.MedicalItemList"
    ]
    """<p>Contains words, phrases, or punctuation marks in your transcription output.</p>"""
    entities: NotRequired[
        "capo_transcribe_streaming.types.medical_entity_list.MedicalEntityList"
    ]
    """<p>Contains entities identified as personal health information (PHI) in your transcription output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalAlternative) -> dict:
    out: dict = {}
    if "transcript" in value:
        out["Transcript"] = value["transcript"]
    if "items" in value:
        import capo_transcribe_streaming.types.medical_item_list

        out["Items"] = capo_transcribe_streaming.types.medical_item_list.serialize_json(
            value["items"]
        )
    if "entities" in value:
        import capo_transcribe_streaming.types.medical_entity_list

        out["Entities"] = (
            capo_transcribe_streaming.types.medical_entity_list.serialize_json(
                value["entities"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalAlternative:
    out: MedicalAlternative = {}  # type: ignore[typeddict-item]
    if "Transcript" in data:
        out["transcript"] = data["Transcript"]
    if "Items" in data:
        import capo_transcribe_streaming.types.medical_item_list

        out["items"] = (
            capo_transcribe_streaming.types.medical_item_list.deserialize_json(
                data["Items"]
            )
        )
    if "Entities" in data:
        import capo_transcribe_streaming.types.medical_entity_list

        out["entities"] = (
            capo_transcribe_streaming.types.medical_entity_list.deserialize_json(
                data["Entities"]
            )
        )
    return out
