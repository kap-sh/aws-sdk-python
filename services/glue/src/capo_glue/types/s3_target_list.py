"""Generated from Smithy shape ``com.amazonaws.glue#S3TargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.s3_target

S3TargetList: TypeAlias = list["capo_glue.types.s3_target.S3Target"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TargetList) -> list:
    import capo_glue.types.s3_target

    out: list = []
    for item in value:
        out.append(capo_glue.types.s3_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> S3TargetList:
    import capo_glue.types.s3_target

    out: S3TargetList = []
    for item in data:
        out.append(capo_glue.types.s3_target.deserialize_aws_json_1_1(item))
    return out
