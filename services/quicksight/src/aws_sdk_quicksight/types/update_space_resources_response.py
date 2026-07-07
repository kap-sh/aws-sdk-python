"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSpaceResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.failed_space_resource_operations
    import aws_sdk_quicksight.types.public_space_arn
    import aws_sdk_quicksight.types.public_space_id


class UpdateSpaceResourcesResponse(TypedDict, closed=True):
    space_id: "aws_sdk_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space.</p>"""
    space_arn: NotRequired["aws_sdk_quicksight.types.public_space_arn.PublicSpaceArn"]
    """<p>The ARN of the space.</p>"""
    failed_resource_operations: NotRequired[
        "aws_sdk_quicksight.types.failed_space_resource_operations.FailedSpaceResourceOperations"
    ]
    """<p>A list of resource operations that failed.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpaceResourcesResponse) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "space_arn" in value:
        out["spaceArn"] = value["space_arn"]
    if "failed_resource_operations" in value:
        import aws_sdk_quicksight.types.failed_space_resource_operations

        out["FailedResourceOperations"] = (
            aws_sdk_quicksight.types.failed_space_resource_operations.serialize_json(
                value["failed_resource_operations"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateSpaceResourcesResponse:
    out: UpdateSpaceResourcesResponse = {}  # type: ignore[typeddict-item]
    if "spaceId" in data:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("UpdateSpaceResourcesResponse.space_id required")
    if "spaceArn" in data:
        out["space_arn"] = data["spaceArn"]
    if "FailedResourceOperations" in data:
        import aws_sdk_quicksight.types.failed_space_resource_operations

        out["failed_resource_operations"] = (
            aws_sdk_quicksight.types.failed_space_resource_operations.deserialize_json(
                data["FailedResourceOperations"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
