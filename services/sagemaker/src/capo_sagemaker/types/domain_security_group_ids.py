"""Generated from Smithy shape ``com.amazonaws.sagemaker#DomainSecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.security_group_id

DomainSecurityGroupIds: TypeAlias = list[
    "capo_sagemaker.types.security_group_id.SecurityGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainSecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DomainSecurityGroupIds:
    return list(data)
