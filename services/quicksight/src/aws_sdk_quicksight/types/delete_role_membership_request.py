"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteRoleMembershipRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.group_name
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.role


class DeleteRoleMembershipRequest(TypedDict):
    member_name: "aws_sdk_quicksight.types.group_name.GroupName"
    """<p>The name of the group.</p>"""
    role: "aws_sdk_quicksight.types.role.Role"
    """<p>The role that you want to remove permissions from.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to create a group in. The Amazon Web Services account ID that you provide must be the same Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace that contains the role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRoleMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRoleMembershipRequest:
    out: DeleteRoleMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
