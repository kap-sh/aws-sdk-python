"""Generated from Smithy shape ``com.amazonaws.ssm#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.tag

TagList: TypeAlias = list["aws_sdk_ssm.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagList) -> list:
    import aws_sdk_ssm.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagList:
    import aws_sdk_ssm.types.tag

    out: TagList = []
    for item in data:
        out.append(aws_sdk_ssm.types.tag.deserialize_aws_json_1_1(item))
    return out
