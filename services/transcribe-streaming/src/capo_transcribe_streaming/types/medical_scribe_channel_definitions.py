"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeChannelDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_scribe_channel_definition

MedicalScribeChannelDefinitions: TypeAlias = list[
    "capo_transcribe_streaming.types.medical_scribe_channel_definition.MedicalScribeChannelDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeChannelDefinitions) -> list:
    import capo_transcribe_streaming.types.medical_scribe_channel_definition

    out: list = []
    for item in value:
        out.append(
            capo_transcribe_streaming.types.medical_scribe_channel_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MedicalScribeChannelDefinitions:
    import capo_transcribe_streaming.types.medical_scribe_channel_definition

    out: MedicalScribeChannelDefinitions = []
    for item in data:
        out.append(
            capo_transcribe_streaming.types.medical_scribe_channel_definition.deserialize_json(
                item
            )
        )
    return out
