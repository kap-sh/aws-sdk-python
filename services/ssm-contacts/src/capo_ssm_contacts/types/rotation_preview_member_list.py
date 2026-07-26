"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#RotationPreviewMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_contacts.types.member

RotationPreviewMemberList: TypeAlias = list["capo_ssm_contacts.types.member.Member"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationPreviewMemberList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RotationPreviewMemberList:
    return list(data)
