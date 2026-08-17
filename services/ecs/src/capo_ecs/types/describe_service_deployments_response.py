"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServiceDeploymentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.failures
    import capo_ecs.types.service_deployments


class DescribeServiceDeploymentsResponse(TypedDict, closed=True):
    service_deployments: NotRequired[
        "capo_ecs.types.service_deployments.ServiceDeployments"
    ]
    """<p>The list of service deployments described.</p>"""
    failures: NotRequired["capo_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p> <p>If you decsribe a deployment with a service revision created before October 25, 2024, the call fails. The failure includes the service revision ARN and the reason set to <code>MISSING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceDeploymentsResponse) -> dict:
    out: dict = {}
    if "service_deployments" in value:
        import capo_ecs.types.service_deployments

        out["serviceDeployments"] = (
            capo_ecs.types.service_deployments.serialize_aws_json_1_1(
                value["service_deployments"]
            )
        )
    if "failures" in value:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceDeploymentsResponse:
    out: DescribeServiceDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("serviceDeployments") is not None:
        import capo_ecs.types.service_deployments

        out["service_deployments"] = (
            capo_ecs.types.service_deployments.deserialize_aws_json_1_1(
                data["serviceDeployments"]
            )
        )
    if data.get("failures") is not None:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
