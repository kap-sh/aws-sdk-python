"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonDeploymentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_list
    import aws_sdk_ecs.types.failures


class DescribeDaemonDeploymentsResponse(TypedDict):
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
    daemon_deployments: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_list.DaemonDeploymentList"
    ]
    """<p>The list of daemon deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonDeploymentsResponse) -> dict:
    out: dict = {}
    if "failures" in value:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    if "daemon_deployments" in value:
        import aws_sdk_ecs.types.daemon_deployment_list

        out["daemonDeployments"] = (
            aws_sdk_ecs.types.daemon_deployment_list.serialize_aws_json_1_1(
                value["daemon_deployments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonDeploymentsResponse:
    out: DescribeDaemonDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "failures" in data:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    if "daemonDeployments" in data:
        import aws_sdk_ecs.types.daemon_deployment_list

        out["daemon_deployments"] = (
            aws_sdk_ecs.types.daemon_deployment_list.deserialize_aws_json_1_1(
                data["daemonDeployments"]
            )
        )
    return out
