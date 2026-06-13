"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListDeploymentsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_filter_list
    import aws_sdk_launch_wizard.types.max_deployment_results
    import aws_sdk_launch_wizard.types.next_token


class ListDeploymentsInput(TypedDict):
    filters: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_filter_list.DeploymentFilterList"
    ]
    """<p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>WORKLOAD_NAME</code> - The name used in deployments.</p> </li> <li> <p> <code>DEPLOYMENT_STATUS</code> - <code>COMPLETED</code> | <code>CREATING</code> | <code>DELETE_IN_PROGRESS</code> | <code>DELETE_INITIATING</code> | <code>DELETE_FAILED</code> | <code>DELETED</code> | <code>FAILED</code> | <code>IN_PROGRESS</code> | <code>VALIDATING</code> </p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_launch_wizard.types.max_deployment_results.MaxDeploymentResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["aws_sdk_launch_wizard.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentsInput) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_launch_wizard.types.deployment_filter_list

        out["filters"] = (
            aws_sdk_launch_wizard.types.deployment_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDeploymentsInput:
    out: ListDeploymentsInput = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_launch_wizard.types.deployment_filter_list

        out["filters"] = (
            aws_sdk_launch_wizard.types.deployment_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
