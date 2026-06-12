"""Generated from Smithy shape ``com.amazonaws.codedeploy#TagFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.tag_filter

TagFilterList: TypeAlias = list["aws_sdk_codedeploy.types.tag_filter.TagFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilterList) -> list:
    import aws_sdk_codedeploy.types.tag_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_codedeploy.types.tag_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagFilterList:
    import aws_sdk_codedeploy.types.tag_filter

    out: TagFilterList = []
    for item in data:
        out.append(aws_sdk_codedeploy.types.tag_filter.deserialize_aws_json_1_1(item))
    return out
