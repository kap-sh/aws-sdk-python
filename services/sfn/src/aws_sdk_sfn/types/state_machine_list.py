"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sfn.types.state_machine_list_item

StateMachineList: TypeAlias = list[
    "aws_sdk_sfn.types.state_machine_list_item.StateMachineListItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateMachineList) -> list:
    import aws_sdk_sfn.types.state_machine_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sfn.types.state_machine_list_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StateMachineList:
    import aws_sdk_sfn.types.state_machine_list_item

    out: StateMachineList = []
    for item in data:
        out.append(
            aws_sdk_sfn.types.state_machine_list_item.deserialize_aws_json_1_0(item)
        )
    return out
