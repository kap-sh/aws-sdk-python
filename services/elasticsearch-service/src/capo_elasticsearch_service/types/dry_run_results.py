"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DryRunResults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.deployment_type
    import capo_elasticsearch_service.types.message


class DryRunResults(TypedDict, closed=True):
    deployment_type: NotRequired[
        "capo_elasticsearch_service.types.deployment_type.DeploymentType"
    ]
    """<p> Specifies the deployment mechanism through which the update shall be applied on the domain. Possible responses are <code>Blue/Green</code> (The update will require a blue/green deployment.) <code>DynamicUpdate</code> (The update can be applied in-place without a Blue/Green deployment required.) <code>Undetermined</code> (The domain is undergoing an update which needs to complete before the deployment type can be predicted.) <code>None</code> (The configuration change matches the current configuration and will not result in any update.) </p>"""
    message: NotRequired["capo_elasticsearch_service.types.message.Message"]
    """<p>Contains an optional message associated with the DryRunResults.</p>"""


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
