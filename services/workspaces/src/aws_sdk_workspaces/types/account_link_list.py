"""Generated from Smithy shape ``com.amazonaws.workspaces#AccountLinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.account_link

AccountLinkList: TypeAlias = list["aws_sdk_workspaces.types.account_link.AccountLink"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountLinkList) -> list:
    import aws_sdk_workspaces.types.account_link

    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces.types.account_link.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AccountLinkList:
    import aws_sdk_workspaces.types.account_link

    out: AccountLinkList = []
    for item in data:
        out.append(aws_sdk_workspaces.types.account_link.deserialize_aws_json_1_1(item))
    return out
