"""Generated from Smithy shape ``com.amazonaws.quicksight#ListGroupMembershipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.group_name
    import aws_sdk_quicksight.types.max_results
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.string


class ListGroupMembershipsRequest(TypedDict, closed=True):
    group_name: "aws_sdk_quicksight.types.group_name.GroupName"
    """<p>The name of the group that you want to see a membership list of.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return from this request.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the group is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace of the group that you want a list of users from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupMembershipsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGroupMembershipsRequest:
    out: ListGroupMembershipsRequest = {}  # type: ignore[typeddict-item]
    return out
