"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeAccountModificationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.account_modification_list
    import aws_sdk_workspaces.types.pagination_token


class DescribeAccountModificationsResult(TypedDict):
    account_modifications: NotRequired[
        "aws_sdk_workspaces.types.account_modification_list.AccountModificationList"
    ]
    """<p>The list of modifications to the configuration of BYOL.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountModificationsResult) -> dict:
    out: dict = {}
    if "account_modifications" in value:
        import aws_sdk_workspaces.types.account_modification_list

        out["AccountModifications"] = (
            aws_sdk_workspaces.types.account_modification_list.serialize_aws_json_1_1(
                value["account_modifications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountModificationsResult:
    out: DescribeAccountModificationsResult = {}  # type: ignore[typeddict-item]
    if "AccountModifications" in data:
        import aws_sdk_workspaces.types.account_modification_list

        out["account_modifications"] = (
            aws_sdk_workspaces.types.account_modification_list.deserialize_aws_json_1_1(
                data["AccountModifications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
