"""Generated from Smithy shape ``com.amazonaws.ecs#ListServiceDeploymentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_deployments_brief
    import aws_sdk_ecs.types.string


class ListServiceDeploymentsResponse(TypedDict, closed=True):
    service_deployments: NotRequired[
        "aws_sdk_ecs.types.service_deployments_brief.ServiceDeploymentsBrief"
    ]
    """<p>An overview of the service deployment, including the following properties:</p> <ul> <li> <p>The ARN of the service deployment.</p> </li> <li> <p>The ARN of the service being deployed.</p> </li> <li> <p>The ARN of the cluster that hosts the service in the service deployment.</p> </li> <li> <p>The time that the service deployment started.</p> </li> <li> <p>The time that the service deployment completed.</p> </li> <li> <p>The service deployment status.</p> </li> <li> <p>Information about why the service deployment is in the current state.</p> </li> <li> <p>The ARN of the service revision that is being deployed.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListServiceDeployments</code> request. When the results of a <code>ListServiceDeployments</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServiceDeploymentsResponse) -> dict:
    out: dict = {}
    if "service_deployments" in value:
        import aws_sdk_ecs.types.service_deployments_brief

        out["serviceDeployments"] = (
            aws_sdk_ecs.types.service_deployments_brief.serialize_aws_json_1_1(
                value["service_deployments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServiceDeploymentsResponse:
    out: ListServiceDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "serviceDeployments" in data:
        import aws_sdk_ecs.types.service_deployments_brief

        out["service_deployments"] = (
            aws_sdk_ecs.types.service_deployments_brief.deserialize_aws_json_1_1(
                data["serviceDeployments"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
