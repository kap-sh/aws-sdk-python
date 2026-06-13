"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.actions_list_member_string

ActionsList: TypeAlias = list[
    "aws_sdk_quicksight.types.actions_list_member_string.ActionsListMemberString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionsList) -> list:
    return list(value)


def deserialize_json(data: list) -> ActionsList:
    return list(data)
