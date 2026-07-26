"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeRoleCustomPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace
    import capo_quicksight.types.role


class DescribeRoleCustomPermissionRequest(TypedDict, closed=True):
    role: "capo_quicksight.types.role.Role"
    """<p>The name of the role whose permissions you want described.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to create a group in. The Amazon Web Services account ID that you provide must be the same Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace that contains the role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRoleCustomPermissionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRoleCustomPermissionRequest:
    out: DescribeRoleCustomPermissionRequest = {}  # type: ignore[typeddict-item]
    return out
