"""Generated from Smithy shape ``com.amazonaws.workspaces#AccountModificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.account_modification

AccountModificationList: TypeAlias = list[
    "capo_workspaces.types.account_modification.AccountModification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountModificationList) -> list:
    import capo_workspaces.types.account_modification

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.account_modification.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccountModificationList:
    import capo_workspaces.types.account_modification

    out: AccountModificationList = []
    for item in data:
        out.append(
            capo_workspaces.types.account_modification.deserialize_aws_json_1_1(item)
        )
    return out
