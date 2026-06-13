"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSpaceResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.public_space_id
    import aws_sdk_quicksight.types.space_resource_operations


class UpdateSpaceResourcesRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the space.</p>"""
    space_id: "aws_sdk_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space that you want to update resources for.</p>"""
    add_resources: NotRequired[
        "aws_sdk_quicksight.types.space_resource_operations.SpaceResourceOperations"
    ]
    """<p>A list of resources to add to the space.</p>"""
    remove_resources: NotRequired[
        "aws_sdk_quicksight.types.space_resource_operations.SpaceResourceOperations"
    ]
    """<p>A list of resources to remove from the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpaceResourcesRequest) -> dict:
    out: dict = {}
    if "add_resources" in value:
        import aws_sdk_quicksight.types.space_resource_operations

        out["AddResources"] = (
            aws_sdk_quicksight.types.space_resource_operations.serialize_json(
                value["add_resources"]
            )
        )
    if "remove_resources" in value:
        import aws_sdk_quicksight.types.space_resource_operations

        out["RemoveResources"] = (
            aws_sdk_quicksight.types.space_resource_operations.serialize_json(
                value["remove_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSpaceResourcesRequest:
    out: UpdateSpaceResourcesRequest = {}  # type: ignore[typeddict-item]
    if "AddResources" in data:
        import aws_sdk_quicksight.types.space_resource_operations

        out["add_resources"] = (
            aws_sdk_quicksight.types.space_resource_operations.deserialize_json(
                data["AddResources"]
            )
        )
    if "RemoveResources" in data:
        import aws_sdk_quicksight.types.space_resource_operations

        out["remove_resources"] = (
            aws_sdk_quicksight.types.space_resource_operations.deserialize_json(
                data["RemoveResources"]
            )
        )
    return out
