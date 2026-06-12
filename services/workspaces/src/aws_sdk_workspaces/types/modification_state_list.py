"""Generated from Smithy shape ``com.amazonaws.workspaces#ModificationStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.modification_state

ModificationStateList: TypeAlias = list[
    "aws_sdk_workspaces.types.modification_state.ModificationState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModificationStateList) -> list:
    import aws_sdk_workspaces.types.modification_state

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.modification_state.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModificationStateList:
    import aws_sdk_workspaces.types.modification_state

    out: ModificationStateList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.modification_state.deserialize_aws_json_1_1(item)
        )
    return out
