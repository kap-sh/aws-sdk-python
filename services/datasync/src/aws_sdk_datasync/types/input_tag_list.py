"""Generated from Smithy shape ``com.amazonaws.datasync#InputTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datasync.types.tag_list_entry

InputTagList: TypeAlias = list["aws_sdk_datasync.types.tag_list_entry.TagListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputTagList) -> list:
    import aws_sdk_datasync.types.tag_list_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_datasync.types.tag_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InputTagList:
    import aws_sdk_datasync.types.tag_list_entry

    out: InputTagList = []
    for item in data:
        out.append(aws_sdk_datasync.types.tag_list_entry.deserialize_aws_json_1_1(item))
    return out
