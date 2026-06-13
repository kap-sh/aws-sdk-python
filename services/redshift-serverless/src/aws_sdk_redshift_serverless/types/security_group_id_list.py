"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#SecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.security_group_id

SecurityGroupIdList: TypeAlias = list[
    "aws_sdk_redshift_serverless.types.security_group_id.SecurityGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecurityGroupIdList:
    return list(data)
