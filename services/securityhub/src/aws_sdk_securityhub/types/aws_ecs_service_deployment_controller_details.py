"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceDeploymentControllerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsServiceDeploymentControllerDetails(TypedDict, closed=True):
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The rolling update (<code>ECS</code>) deployment type replaces the current running version of the container with the latest version.</p> <p>The blue/green (<code>CODE_DEPLOY</code>) deployment type uses the blue/green deployment model that is powered by CodeDeploy. This deployment model a new deployment of a service can be verified before production traffic is sent to it.</p> <p>The external (<code>EXTERNAL</code>) deployment type allows the use of any third-party deployment controller for full control over the deployment process for an Amazon ECS service.</p> <p>Valid values: <code>ECS</code> | <code>CODE_DEPLOY</code> | <code>EXTERNAL</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServiceDeploymentControllerDetails) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsEcsServiceDeploymentControllerDetails:
    out: AwsEcsServiceDeploymentControllerDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
