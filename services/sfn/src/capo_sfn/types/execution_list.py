"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sfn.types.execution_list_item

ExecutionList: TypeAlias = list["capo_sfn.types.execution_list_item.ExecutionListItem"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionList) -> list:
    import capo_sfn.types.execution_list_item

    out: list = []
    for item in value:
        out.append(capo_sfn.types.execution_list_item.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ExecutionList:
    import capo_sfn.types.execution_list_item

    out: ExecutionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_sfn.types.execution_list_item.deserialize_aws_json_1_0(item))
    return out
