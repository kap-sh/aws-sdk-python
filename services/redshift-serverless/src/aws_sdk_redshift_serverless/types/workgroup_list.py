"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#WorkgroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.workgroup

WorkgroupList: TypeAlias = list["aws_sdk_redshift_serverless.types.workgroup.Workgroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkgroupList) -> list:
    import aws_sdk_redshift_serverless.types.workgroup

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_serverless.types.workgroup.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkgroupList:
    import aws_sdk_redshift_serverless.types.workgroup

    out: WorkgroupList = []
    for item in data:
        out.append(
            aws_sdk_redshift_serverless.types.workgroup.deserialize_aws_json_1_1(item)
        )
    return out
