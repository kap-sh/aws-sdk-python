"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sfn.types.execution_list_item

ExecutionList: TypeAlias = list[
    "aws_sdk_sfn.types.execution_list_item.ExecutionListItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionList) -> list:
    import aws_sdk_sfn.types.execution_list_item

    out: list = []
    for item in value:
        out.append(aws_sdk_sfn.types.execution_list_item.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ExecutionList:
    import aws_sdk_sfn.types.execution_list_item

    out: ExecutionList = []
    for item in data:
        out.append(aws_sdk_sfn.types.execution_list_item.deserialize_aws_json_1_0(item))
    return out
