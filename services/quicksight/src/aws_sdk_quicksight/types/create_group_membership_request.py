"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateGroupMembershipRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.group_member_name
    import aws_sdk_quicksight.types.group_name
    import aws_sdk_quicksight.types.namespace


class CreateGroupMembershipRequest(TypedDict):
    member_name: "aws_sdk_quicksight.types.group_member_name.GroupMemberName"
    """<p>The name of the user that you want to add to the group membership.</p>"""
    group_name: "aws_sdk_quicksight.types.group_name.GroupName"
    """<p>The name of the group that you want to add the user to.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the group is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace that you want the user to be a part of.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateGroupMembershipRequest:
    out: CreateGroupMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
