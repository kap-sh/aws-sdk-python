"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sfn.types.state_machine_alias_list_item

StateMachineAliasList: TypeAlias = list[
    "aws_sdk_sfn.types.state_machine_alias_list_item.StateMachineAliasListItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateMachineAliasList) -> list:
    import aws_sdk_sfn.types.state_machine_alias_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sfn.types.state_machine_alias_list_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StateMachineAliasList:
    import aws_sdk_sfn.types.state_machine_alias_list_item

    out: StateMachineAliasList = []
    for item in data:
        out.append(
            aws_sdk_sfn.types.state_machine_alias_list_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
