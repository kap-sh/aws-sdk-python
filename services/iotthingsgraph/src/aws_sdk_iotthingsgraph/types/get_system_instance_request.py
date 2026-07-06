"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetSystemInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.urn


class GetSystemInstanceRequest(TypedDict, closed=True):
    id: "aws_sdk_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the system deployment instance. This value is returned by <code>CreateSystemInstance</code>.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:deployment:DEPLOYMENTNAME</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSystemInstanceRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSystemInstanceRequest:
    out: GetSystemInstanceRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetSystemInstanceRequest.id required")
    return out
