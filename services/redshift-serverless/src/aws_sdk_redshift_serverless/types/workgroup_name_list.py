"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#WorkgroupNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.workgroup_name

WorkgroupNameList: TypeAlias = list[
    "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkgroupNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkgroupNameList:
    return list(data)
