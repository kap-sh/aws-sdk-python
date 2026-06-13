"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListDeploymentEventsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_launch_wizard.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_id
    import aws_sdk_launch_wizard.types.max_deployment_event_results
    import aws_sdk_launch_wizard.types.next_token


class ListDeploymentEventsInput(TypedDict):
    deployment_id: "aws_sdk_launch_wizard.types.deployment_id.DeploymentId"
    """<p>The ID of the deployment.</p>"""
    max_results: NotRequired[
        "aws_sdk_launch_wizard.types.max_deployment_event_results.MaxDeploymentEventResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["aws_sdk_launch_wizard.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentEventsInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDeploymentEventsInput:
    out: ListDeploymentEventsInput = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("ListDeploymentEventsInput.deployment_id required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
