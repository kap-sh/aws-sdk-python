"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonDeploymentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_deployment_list
    import capo_ecs.types.failures


class DescribeDaemonDeploymentsResponse(TypedDict, closed=True):
    failures: NotRequired["capo_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
    daemon_deployments: NotRequired[
        "capo_ecs.types.daemon_deployment_list.DaemonDeploymentList"
    ]
    """<p>The list of daemon deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonDeploymentsResponse) -> dict:
    out: dict = {}
    if "failures" in value:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    if "daemon_deployments" in value:
        import capo_ecs.types.daemon_deployment_list

        out["daemonDeployments"] = (
            capo_ecs.types.daemon_deployment_list.serialize_aws_json_1_1(
                value["daemon_deployments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonDeploymentsResponse:
    out: DescribeDaemonDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "failures" in data:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    if "daemonDeployments" in data:
        import capo_ecs.types.daemon_deployment_list

        out["daemon_deployments"] = (
            capo_ecs.types.daemon_deployment_list.deserialize_aws_json_1_1(
                data["daemonDeployments"]
            )
        )
    return out
