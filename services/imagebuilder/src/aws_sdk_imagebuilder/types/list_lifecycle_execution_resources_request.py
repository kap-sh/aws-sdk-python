"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListLifecycleExecutionResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_execution_id
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.restricted_integer


class ListLifecycleExecutionResourcesRequest(TypedDict):
    lifecycle_execution_id: (
        "aws_sdk_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId"
    )
    """<p>Use the unique identifier for a runtime instance of the lifecycle policy to get runtime details.</p>"""
    parent_resource_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>You can leave this empty to get a list of Image Builder resources that were identified for lifecycle actions.</p> <p>To get a list of associated resources that are impacted for an individual resource (the parent), specify its Amazon Resource Name (ARN). Associated resources are produced from your image and distributed when you run a build, such as AMIs or container images stored in ECR repositories.</p>"""
    max_results: NotRequired[
        "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>Specify the maximum number of items to return in a request.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLifecycleExecutionResourcesRequest) -> dict:
    out: dict = {}
    out["lifecycleExecutionId"] = value["lifecycle_execution_id"]
    if "parent_resource_id" in value:
        out["parentResourceId"] = value["parent_resource_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLifecycleExecutionResourcesRequest:
    out: ListLifecycleExecutionResourcesRequest = {}  # type: ignore[typeddict-item]
    if "lifecycleExecutionId" in data:
        out["lifecycle_execution_id"] = data["lifecycleExecutionId"]
    else:
        raise DeserializationError(
            "ListLifecycleExecutionResourcesRequest.lifecycle_execution_id required"
        )
    if "parentResourceId" in data:
        out["parent_resource_id"] = data["parentResourceId"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
