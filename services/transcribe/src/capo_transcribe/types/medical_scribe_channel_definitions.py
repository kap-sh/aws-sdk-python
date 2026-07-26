"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeChannelDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.medical_scribe_channel_definition

MedicalScribeChannelDefinitions: TypeAlias = list[
    "capo_transcribe.types.medical_scribe_channel_definition.MedicalScribeChannelDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeChannelDefinitions) -> list:
    import capo_transcribe.types.medical_scribe_channel_definition

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.medical_scribe_channel_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MedicalScribeChannelDefinitions:
    import capo_transcribe.types.medical_scribe_channel_definition

    out: MedicalScribeChannelDefinitions = []
    for item in data:
        out.append(
            capo_transcribe.types.medical_scribe_channel_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
