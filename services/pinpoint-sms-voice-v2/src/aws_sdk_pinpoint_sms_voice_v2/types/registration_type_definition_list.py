"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationTypeDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition

RegistrationTypeDefinitionList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition.RegistrationTypeDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationTypeDefinitionList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationTypeDefinitionList:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition

    out: RegistrationTypeDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition.deserialize_aws_json_1_0(
                item
            )
        )
    return out
