"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeChannelDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.medical_scribe_channel_definition

MedicalScribeChannelDefinitions: TypeAlias = list[
    "aws_sdk_connecthealth.types.medical_scribe_channel_definition.MedicalScribeChannelDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeChannelDefinitions) -> list:
    import aws_sdk_connecthealth.types.medical_scribe_channel_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connecthealth.types.medical_scribe_channel_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MedicalScribeChannelDefinitions:
    import aws_sdk_connecthealth.types.medical_scribe_channel_definition

    out: MedicalScribeChannelDefinitions = []
    for item in data:
        out.append(
            aws_sdk_connecthealth.types.medical_scribe_channel_definition.deserialize_json(
                item
            )
        )
    return out
