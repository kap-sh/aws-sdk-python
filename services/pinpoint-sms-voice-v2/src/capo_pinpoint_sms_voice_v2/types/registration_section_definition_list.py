"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationSectionDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_section_definition

RegistrationSectionDefinitionList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.registration_section_definition.RegistrationSectionDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationSectionDefinitionList) -> list:
    import capo_pinpoint_sms_voice_v2.types.registration_section_definition

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_section_definition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationSectionDefinitionList:
    import capo_pinpoint_sms_voice_v2.types.registration_section_definition

    out: RegistrationSectionDefinitionList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_section_definition.deserialize_aws_json_1_0(
                item
            )
        )
    return out
