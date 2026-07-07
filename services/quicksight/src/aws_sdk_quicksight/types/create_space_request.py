"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateSpaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.public_space_id
    import aws_sdk_quicksight.types.space_description
    import aws_sdk_quicksight.types.space_name


class CreateSpaceRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the space.</p>"""
    space_id: "aws_sdk_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    name: "aws_sdk_quicksight.types.space_name.SpaceName"
    """<p>A display name for the space.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.space_description.SpaceDescription"
    ]
    """<p>A description of the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSpaceRequest) -> dict:
    out: dict = {}
    out["SpaceId"] = value["space_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateSpaceRequest:
    out: CreateSpaceRequest = {}  # type: ignore[typeddict-item]
    if "SpaceId" in data:
        out["space_id"] = data["SpaceId"]
    else:
        raise DeserializationError("CreateSpaceRequest.space_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateSpaceRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    return out
