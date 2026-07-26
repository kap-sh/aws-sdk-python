"""Generated from Smithy shape ``com.amazonaws.sagemaker#WorkforceSecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.workforce_security_group_id

WorkforceSecurityGroupIds: TypeAlias = list[
    "capo_sagemaker.types.workforce_security_group_id.WorkforceSecurityGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkforceSecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkforceSecurityGroupIds:
    return list(data)
