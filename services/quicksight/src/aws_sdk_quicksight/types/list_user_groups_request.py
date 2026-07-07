"""Generated from Smithy shape ``com.amazonaws.quicksight#ListUserGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.max_results
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.user_name


class ListUserGroupsRequest(TypedDict, closed=True):
    user_name: "aws_sdk_quicksight.types.user_name.UserName"
    """<p>The Amazon Quick Sight user name that you want to list group memberships for.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID that the user is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace. Currently, you should set this to <code>default</code>.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return from this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUserGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListUserGroupsRequest:
    out: ListUserGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
