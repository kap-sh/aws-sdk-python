"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#InvitationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.invitation_status

InvitationStatusList: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.invitation_status.InvitationStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvitationStatusList) -> list:
    import aws_sdk_partnercentral_selling.types.invitation_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.invitation_status.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InvitationStatusList:
    import aws_sdk_partnercentral_selling.types.invitation_status

    out: InvitationStatusList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.invitation_status.deserialize_aws_json_1_0(
                item
            )
        )
    return out
