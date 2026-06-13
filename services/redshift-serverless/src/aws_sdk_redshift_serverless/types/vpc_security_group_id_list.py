"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#VpcSecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.vpc_security_group_id

VpcSecurityGroupIdList: TypeAlias = list[
    "aws_sdk_redshift_serverless.types.vpc_security_group_id.VpcSecurityGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcSecurityGroupIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VpcSecurityGroupIdList:
    return list(data)
