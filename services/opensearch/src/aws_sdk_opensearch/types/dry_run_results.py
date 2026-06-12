"""Generated from Smithy shape ``com.amazonaws.opensearch#DryRunResults``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.deployment_type
    import aws_sdk_opensearch.types.message


class DryRunResults(TypedDict):
    deployment_type: NotRequired[
        "aws_sdk_opensearch.types.deployment_type.DeploymentType"
    ]
    """<p> Specifies the way in which OpenSearch Service will apply an update. Possible values are:</p> <ul> <li> <p> <b>Blue/Green</b> - The update requires a blue/green deployment.</p> </li> <li> <p> <b>DynamicUpdate</b> - No blue/green deployment required</p> </li> <li> <p> <b>Undetermined</b> - The domain is in the middle of an update and can't predict the deployment type. Try again after the update is complete.</p> </li> <li> <p> <b>None</b> - The request doesn't include any configuration changes.</p> </li> </ul>"""
    message: NotRequired["aws_sdk_opensearch.types.message.Message"]
    """<p>A message corresponding to the deployment type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DryRunResults) -> dict:
    out: dict = {}
    if "deployment_type" in value:
        out["DeploymentType"] = value["deployment_type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DryRunResults:
    out: DryRunResults = {}  # type: ignore[typeddict-item]
    if "DeploymentType" in data:
        out["deployment_type"] = data["DeploymentType"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
