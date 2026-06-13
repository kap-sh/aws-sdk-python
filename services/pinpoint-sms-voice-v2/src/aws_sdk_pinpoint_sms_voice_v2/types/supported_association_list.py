"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SupportedAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.supported_association

SupportedAssociationList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.supported_association.SupportedAssociation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupportedAssociationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.supported_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.supported_association.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SupportedAssociationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.supported_association

    out: SupportedAssociationList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.supported_association.deserialize_aws_json_1_0(
                item
            )
        )
    return out
