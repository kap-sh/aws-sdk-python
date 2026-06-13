"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#OriginationIdentityMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.origination_identity_metadata

OriginationIdentityMetadataList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.origination_identity_metadata.OriginationIdentityMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OriginationIdentityMetadataList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.origination_identity_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.origination_identity_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> OriginationIdentityMetadataList:
    import aws_sdk_pinpoint_sms_voice_v2.types.origination_identity_metadata

    out: OriginationIdentityMetadataList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.origination_identity_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out
