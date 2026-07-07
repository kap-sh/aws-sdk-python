"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_option
    import aws_sdk_codedeploy.types.deployment_type


class DeploymentStyle(TypedDict, closed=True):
    deployment_type: NotRequired[
        "aws_sdk_codedeploy.types.deployment_type.DeploymentType"
    ]
    """<p>Indicates whether to run an in-place deployment or a blue/green deployment.</p>"""
    deployment_option: NotRequired[
        "aws_sdk_codedeploy.types.deployment_option.DeploymentOption"
    ]
    """<p>Indicates whether to route deployment traffic behind a load balancer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStyle) -> dict:
    out: dict = {}
    if "deployment_type" in value:
        import aws_sdk_codedeploy.types.deployment_type

        out["deploymentType"] = (
            aws_sdk_codedeploy.types.deployment_type.serialize_aws_json_1_1(
                value["deployment_type"]
            )
        )
    if "deployment_option" in value:
        import aws_sdk_codedeploy.types.deployment_option

        out["deploymentOption"] = (
            aws_sdk_codedeploy.types.deployment_option.serialize_aws_json_1_1(
                value["deployment_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentStyle:
    out: DeploymentStyle = {}  # type: ignore[typeddict-item]
    if "deploymentType" in data:
        import aws_sdk_codedeploy.types.deployment_type

        out["deployment_type"] = (
            aws_sdk_codedeploy.types.deployment_type.deserialize_aws_json_1_1(
                data["deploymentType"]
            )
        )
    if "deploymentOption" in data:
        import aws_sdk_codedeploy.types.deployment_option

        out["deployment_option"] = (
            aws_sdk_codedeploy.types.deployment_option.deserialize_aws_json_1_1(
                data["deploymentOption"]
            )
        )
    return out
