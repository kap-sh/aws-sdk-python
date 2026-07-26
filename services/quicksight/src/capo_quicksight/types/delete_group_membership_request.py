"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteGroupMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.group_member_name
    import capo_quicksight.types.group_name
    import capo_quicksight.types.namespace


class DeleteGroupMembershipRequest(TypedDict, closed=True):
    member_name: "capo_quicksight.types.group_member_name.GroupMemberName"
    """<p>The name of the user that you want to delete from the group membership.</p>"""
    group_name: "capo_quicksight.types.group_name.GroupName"
    """<p>The name of the group that you want to delete the user from.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the group is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace of the group that you want to remove a user from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGroupMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGroupMembershipRequest:
    out: DeleteGroupMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
