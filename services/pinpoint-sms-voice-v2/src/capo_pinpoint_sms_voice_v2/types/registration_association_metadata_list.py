"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationAssociationMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_association_metadata

RegistrationAssociationMetadataList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.registration_association_metadata.RegistrationAssociationMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationAssociationMetadataList) -> list:
    import capo_pinpoint_sms_voice_v2.types.registration_association_metadata

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_association_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationAssociationMetadataList:
    import capo_pinpoint_sms_voice_v2.types.registration_association_metadata

    out: RegistrationAssociationMetadataList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_association_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out
