"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonDeploymentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_summary_list
    import aws_sdk_ecs.types.string


class ListDaemonDeploymentsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListDaemonDeployments</code> request. When the results of a <code>ListDaemonDeployments</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results.</p>"""
    daemon_deployments: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_summary_list.DaemonDeploymentSummaryList"
    ]
    """<p>The list of daemon deployment summaries.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDaemonDeploymentsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "daemon_deployments" in value:
        import aws_sdk_ecs.types.daemon_deployment_summary_list

        out["daemonDeployments"] = (
            aws_sdk_ecs.types.daemon_deployment_summary_list.serialize_aws_json_1_1(
                value["daemon_deployments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDaemonDeploymentsResponse:
    out: ListDaemonDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "daemonDeployments" in data:
        import aws_sdk_ecs.types.daemon_deployment_summary_list

        out["daemon_deployments"] = (
            aws_sdk_ecs.types.daemon_deployment_summary_list.deserialize_aws_json_1_1(
                data["daemonDeployments"]
            )
        )
    return out
