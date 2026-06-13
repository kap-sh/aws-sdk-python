"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeGroupMembershipRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.group_member_name
    import aws_sdk_quicksight.types.group_name
    import aws_sdk_quicksight.types.namespace


class DescribeGroupMembershipRequest(TypedDict):
    member_name: "aws_sdk_quicksight.types.group_member_name.GroupMemberName"
    """<p>The user name of the user that you want to search for.</p>"""
    group_name: "aws_sdk_quicksight.types.group_name.GroupName"
    """<p>The name of the group that you want to search.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the group is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace that includes the group you are searching within.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGroupMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGroupMembershipRequest:
    out: DescribeGroupMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
