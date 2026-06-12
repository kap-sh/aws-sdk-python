"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DeploySystemInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.urn


class DeploySystemInstanceRequest(TypedDict):
    id: NotRequired["aws_sdk_iotthingsgraph.types.urn.Urn"]
    """<p>The ID of the system instance. This value is returned by the <code>CreateSystemInstance</code> action.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:deployment:DEPLOYMENTNAME</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploySystemInstanceRequest) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploySystemInstanceRequest:
    out: DeploySystemInstanceRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
