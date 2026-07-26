"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteRoleMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.group_name
    import capo_quicksight.types.namespace
    import capo_quicksight.types.role


class DeleteRoleMembershipRequest(TypedDict, closed=True):
    member_name: "capo_quicksight.types.group_name.GroupName"
    """<p>The name of the group.</p>"""
    role: "capo_quicksight.types.role.Role"
    """<p>The role that you want to remove permissions from.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to create a group in. The Amazon Web Services account ID that you provide must be the same Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace that contains the role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRoleMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRoleMembershipRequest:
    out: DeleteRoleMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
