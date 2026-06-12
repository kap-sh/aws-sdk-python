"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#RotationOverridePreviewMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.member

RotationOverridePreviewMemberList: TypeAlias = list[
    "aws_sdk_ssm_contacts.types.member.Member"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationOverridePreviewMemberList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RotationOverridePreviewMemberList:
    return list(data)
