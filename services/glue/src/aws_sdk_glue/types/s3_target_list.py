"""Generated from Smithy shape ``com.amazonaws.glue#S3TargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.s3_target

S3TargetList: TypeAlias = list["aws_sdk_glue.types.s3_target.S3Target"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TargetList) -> list:
    import aws_sdk_glue.types.s3_target

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.s3_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> S3TargetList:
    import aws_sdk_glue.types.s3_target

    out: S3TargetList = []
    for item in data:
        out.append(aws_sdk_glue.types.s3_target.deserialize_aws_json_1_1(item))
    return out
