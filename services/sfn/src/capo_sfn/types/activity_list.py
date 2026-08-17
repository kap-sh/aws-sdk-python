"""Generated from Smithy shape ``com.amazonaws.sfn#ActivityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sfn.types.activity_list_item

ActivityList: TypeAlias = list["capo_sfn.types.activity_list_item.ActivityListItem"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityList) -> list:
    import capo_sfn.types.activity_list_item

    out: list = []
    for item in value:
        out.append(capo_sfn.types.activity_list_item.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ActivityList:
    import capo_sfn.types.activity_list_item

    out: ActivityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_sfn.types.activity_list_item.deserialize_aws_json_1_0(item))
    return out
