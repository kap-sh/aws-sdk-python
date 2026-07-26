"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationFieldDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_field_definition

RegistrationFieldDefinitionList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.registration_field_definition.RegistrationFieldDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationFieldDefinitionList) -> list:
    import capo_pinpoint_sms_voice_v2.types.registration_field_definition

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_field_definition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationFieldDefinitionList:
    import capo_pinpoint_sms_voice_v2.types.registration_field_definition

    out: RegistrationFieldDefinitionList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_field_definition.deserialize_aws_json_1_0(
                item
            )
        )
    return out
