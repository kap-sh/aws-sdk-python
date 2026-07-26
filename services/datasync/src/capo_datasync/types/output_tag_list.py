"""Generated from Smithy shape ``com.amazonaws.datasync#OutputTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.tag_list_entry

OutputTagList: TypeAlias = list["capo_datasync.types.tag_list_entry.TagListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputTagList) -> list:
    import capo_datasync.types.tag_list_entry

    out: list = []
    for item in value:
        out.append(capo_datasync.types.tag_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OutputTagList:
    import capo_datasync.types.tag_list_entry

    out: OutputTagList = []
    for item in data:
        out.append(capo_datasync.types.tag_list_entry.deserialize_aws_json_1_1(item))
    return out
