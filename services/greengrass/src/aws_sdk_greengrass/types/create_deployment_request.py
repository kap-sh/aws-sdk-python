"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.deployment_type


class CreateDeploymentRequest(TypedDict):
    amzn_client_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    deployment_id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the deployment if you wish to redeploy a previous deployment."""
    deployment_type: NotRequired[
        "aws_sdk_greengrass.types.deployment_type.DeploymentType"
    ]
    """The type of deployment. When used for ''CreateDeployment'', only ''NewDeployment'' and ''Redeployment'' are valid."""
    group_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""
    group_version_id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the group version to be deployed."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentRequest) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    if "deployment_type" in value:
        import aws_sdk_greengrass.types.deployment_type

        out["DeploymentType"] = aws_sdk_greengrass.types.deployment_type.serialize_json(
            value["deployment_type"]
        )
    if "group_version_id" in value:
        out["GroupVersionId"] = value["group_version_id"]
    return out


def deserialize_json(data: dict) -> CreateDeploymentRequest:
    out: CreateDeploymentRequest = {}  # type: ignore[typeddict-item]
    if "DeploymentId" in data:
        out["deployment_id"] = data["DeploymentId"]
    if "DeploymentType" in data:
        import aws_sdk_greengrass.types.deployment_type

        out["deployment_type"] = (
            aws_sdk_greengrass.types.deployment_type.deserialize_json(
                data["DeploymentType"]
            )
        )
    if "GroupVersionId" in data:
        out["group_version_id"] = data["GroupVersionId"]
    return out
