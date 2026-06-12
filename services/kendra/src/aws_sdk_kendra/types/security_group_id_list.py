"""Generated from Smithy shape ``com.amazonaws.kendra#SecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.vpc_security_group_id

SecurityGroupIdList: TypeAlias = list[
    "aws_sdk_kendra.types.vpc_security_group_id.VpcSecurityGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecurityGroupIdList:
    return list(data)
