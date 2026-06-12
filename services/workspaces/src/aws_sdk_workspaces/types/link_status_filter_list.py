"""Generated from Smithy shape ``com.amazonaws.workspaces#LinkStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.account_link_status_enum

LinkStatusFilterList: TypeAlias = list[
    "aws_sdk_workspaces.types.account_link_status_enum.AccountLinkStatusEnum"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LinkStatusFilterList) -> list:
    import aws_sdk_workspaces.types.account_link_status_enum

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.account_link_status_enum.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LinkStatusFilterList:
    import aws_sdk_workspaces.types.account_link_status_enum

    out: LinkStatusFilterList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.account_link_status_enum.deserialize_aws_json_1_1(
                item
            )
        )
    return out
