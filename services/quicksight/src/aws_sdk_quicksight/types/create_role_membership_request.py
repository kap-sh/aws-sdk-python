"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateRoleMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.group_name
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.role


class CreateRoleMembershipRequest(TypedDict, closed=True):
    member_name: "aws_sdk_quicksight.types.group_name.GroupName"
    """<p>The name of the group that you want to add to the role.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to create a group in. The Amazon Web Services account ID that you provide must be the same Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace that the role belongs to.</p>"""
    role: "aws_sdk_quicksight.types.role.Role"
    """<p>The role that you want to add a group to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoleMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateRoleMembershipRequest:
    out: CreateRoleMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
