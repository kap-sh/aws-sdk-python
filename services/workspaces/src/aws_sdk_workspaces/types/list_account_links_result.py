"""Generated from Smithy shape ``com.amazonaws.workspaces#ListAccountLinksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.account_link_list
    import aws_sdk_workspaces.types.pagination_token


class ListAccountLinksResult(TypedDict, closed=True):
    account_links: NotRequired[
        "aws_sdk_workspaces.types.account_link_list.AccountLinkList"
    ]
    """<p>Information about the account links.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountLinksResult) -> dict:
    out: dict = {}
    if "account_links" in value:
        import aws_sdk_workspaces.types.account_link_list

        out["AccountLinks"] = (
            aws_sdk_workspaces.types.account_link_list.serialize_aws_json_1_1(
                value["account_links"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountLinksResult:
    out: ListAccountLinksResult = {}  # type: ignore[typeddict-item]
    if "AccountLinks" in data:
        import aws_sdk_workspaces.types.account_link_list

        out["account_links"] = (
            aws_sdk_workspaces.types.account_link_list.deserialize_aws_json_1_1(
                data["AccountLinks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
