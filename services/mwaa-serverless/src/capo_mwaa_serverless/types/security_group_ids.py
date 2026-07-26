"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#SecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.security_group_string

SecurityGroupIds: TypeAlias = list[
    "capo_mwaa_serverless.types.security_group_string.SecurityGroupString"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SecurityGroupIds:
    return list(data)
