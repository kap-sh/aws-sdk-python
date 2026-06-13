"""Generated from Smithy shape ``com.amazonaws.pcs#SecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pcs.types.security_group_id

SecurityGroupIdList: TypeAlias = list[
    "aws_sdk_pcs.types.security_group_id.SecurityGroupId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SecurityGroupIdList:
    return list(data)
