"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerServiceDeploymentsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_deployment_list


class GetContainerServiceDeploymentsResult(TypedDict):
    deployments: NotRequired[
        "aws_sdk_lightsail.types.container_service_deployment_list.ContainerServiceDeploymentList"
    ]
    """<p>An array of objects that describe deployments for a container service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerServiceDeploymentsResult) -> dict:
    out: dict = {}
    if "deployments" in value:
        import aws_sdk_lightsail.types.container_service_deployment_list

        out["deployments"] = (
            aws_sdk_lightsail.types.container_service_deployment_list.serialize_aws_json_1_1(
                value["deployments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerServiceDeploymentsResult:
    out: GetContainerServiceDeploymentsResult = {}  # type: ignore[typeddict-item]
    if "deployments" in data:
        import aws_sdk_lightsail.types.container_service_deployment_list

        out["deployments"] = (
            aws_sdk_lightsail.types.container_service_deployment_list.deserialize_aws_json_1_1(
                data["deployments"]
            )
        )
    return out
