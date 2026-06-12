"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListLifecycleExecutionResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_execution_id
    import aws_sdk_imagebuilder.types.lifecycle_execution_resource_list
    import aws_sdk_imagebuilder.types.lifecycle_execution_state
    import aws_sdk_imagebuilder.types.pagination_token


class ListLifecycleExecutionResourcesResponse(TypedDict):
    lifecycle_execution_id: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId"
    ]
    """<p>Runtime details for the specified runtime instance of the lifecycle policy.</p>"""
    lifecycle_execution_state: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_execution_state.LifecycleExecutionState"
    ]
    """<p>The current state of the lifecycle runtime instance.</p>"""
    resources: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_execution_resource_list.LifecycleExecutionResourceList"
    ]
    """<p>A list of resources that were identified for lifecycle actions.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLifecycleExecutionResourcesResponse) -> dict:
    out: dict = {}
    if "lifecycle_execution_id" in value:
        out["lifecycleExecutionId"] = value["lifecycle_execution_id"]
    if "lifecycle_execution_state" in value:
        import aws_sdk_imagebuilder.types.lifecycle_execution_state

        out["lifecycleExecutionState"] = (
            aws_sdk_imagebuilder.types.lifecycle_execution_state.serialize_json(
                value["lifecycle_execution_state"]
            )
        )
    if "resources" in value:
        import aws_sdk_imagebuilder.types.lifecycle_execution_resource_list

        out["resources"] = (
            aws_sdk_imagebuilder.types.lifecycle_execution_resource_list.serialize_json(
                value["resources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLifecycleExecutionResourcesResponse:
    out: ListLifecycleExecutionResourcesResponse = {}  # type: ignore[typeddict-item]
    if "lifecycleExecutionId" in data:
        out["lifecycle_execution_id"] = data["lifecycleExecutionId"]
    if "lifecycleExecutionState" in data:
        import aws_sdk_imagebuilder.types.lifecycle_execution_state

        out["lifecycle_execution_state"] = (
            aws_sdk_imagebuilder.types.lifecycle_execution_state.deserialize_json(
                data["lifecycleExecutionState"]
            )
        )
    if "resources" in data:
        import aws_sdk_imagebuilder.types.lifecycle_execution_resource_list

        out["resources"] = (
            aws_sdk_imagebuilder.types.lifecycle_execution_resource_list.deserialize_json(
                data["resources"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
