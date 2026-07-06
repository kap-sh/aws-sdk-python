"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateFolderMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.member_type
    import aws_sdk_quicksight.types.restrictive_resource_id


class CreateFolderMembershipRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the folder.</p>"""
    folder_id: "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The ID of the folder.</p>"""
    member_id: "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The ID of the asset that you want to add to the folder.</p>"""
    member_type: "aws_sdk_quicksight.types.member_type.MemberType"
    """<p>The member type of the asset that you want to add to a folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFolderMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateFolderMembershipRequest:
    out: CreateFolderMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
