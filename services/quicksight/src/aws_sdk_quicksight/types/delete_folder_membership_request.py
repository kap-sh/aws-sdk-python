"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteFolderMembershipRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.member_type
    import aws_sdk_quicksight.types.restrictive_resource_id


class DeleteFolderMembershipRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the folder.</p>"""
    folder_id: "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The Folder ID.</p>"""
    member_id: "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The ID of the asset that you want to delete.</p>"""
    member_type: "aws_sdk_quicksight.types.member_type.MemberType"
    """<p>The member type of the asset that you want to delete from a folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFolderMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFolderMembershipRequest:
    out: DeleteFolderMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
