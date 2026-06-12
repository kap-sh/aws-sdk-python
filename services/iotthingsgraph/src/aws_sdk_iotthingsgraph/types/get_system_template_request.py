"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetSystemTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.urn
    import aws_sdk_iotthingsgraph.types.version


class GetSystemTemplateRequest(TypedDict):
    id: "aws_sdk_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the system to get. This ID must be in the user's namespace.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME</code> </p>"""
    revision_number: NotRequired["aws_sdk_iotthingsgraph.types.version.Version"]
    """<p>The number that specifies the revision of the system to get.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSystemTemplateRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "revision_number" in value:
        out["revisionNumber"] = value["revision_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSystemTemplateRequest:
    out: GetSystemTemplateRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetSystemTemplateRequest.id required")
    if "revisionNumber" in data:
        out["revision_number"] = data["revisionNumber"]
    return out
