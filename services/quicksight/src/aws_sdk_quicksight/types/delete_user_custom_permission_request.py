"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteUserCustomPermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.user_name


class DeleteUserCustomPermissionRequest(TypedDict):
    user_name: "aws_sdk_quicksight.types.user_name.UserName"
    """<p>The username of the user that you want to remove custom permissions from.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the custom permission configuration that you want to delete.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace that the user belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserCustomPermissionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUserCustomPermissionRequest:
    out: DeleteUserCustomPermissionRequest = {}  # type: ignore[typeddict-item]
    return out
