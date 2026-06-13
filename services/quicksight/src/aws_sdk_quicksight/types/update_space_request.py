"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSpaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.public_space_id
    import aws_sdk_quicksight.types.space_description
    import aws_sdk_quicksight.types.space_name


class UpdateSpaceRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the space.</p>"""
    space_id: "aws_sdk_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space that you want to update.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.space_name.SpaceName"]
    """<p>A new display name for the space.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.space_description.SpaceDescription"
    ]
    """<p>A new description for the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpaceRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateSpaceRequest:
    out: UpdateSpaceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
