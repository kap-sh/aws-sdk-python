"""Generated from Smithy shape ``com.amazonaws.glue#GroupFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.group_filters

GroupFiltersList: TypeAlias = list["aws_sdk_glue.types.group_filters.GroupFilters"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupFiltersList) -> list:
    import aws_sdk_glue.types.group_filters

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.group_filters.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GroupFiltersList:
    import aws_sdk_glue.types.group_filters

    out: GroupFiltersList = []
    for item in data:
        out.append(aws_sdk_glue.types.group_filters.deserialize_aws_json_1_1(item))
    return out
