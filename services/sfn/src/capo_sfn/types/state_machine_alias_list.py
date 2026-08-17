"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sfn.types.state_machine_alias_list_item

StateMachineAliasList: TypeAlias = list[
    "capo_sfn.types.state_machine_alias_list_item.StateMachineAliasListItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateMachineAliasList) -> list:
    import capo_sfn.types.state_machine_alias_list_item

    out: list = []
    for item in value:
        out.append(
            capo_sfn.types.state_machine_alias_list_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StateMachineAliasList:
    import capo_sfn.types.state_machine_alias_list_item

    out: StateMachineAliasList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sfn.types.state_machine_alias_list_item.deserialize_aws_json_1_0(item)
        )
    return out
