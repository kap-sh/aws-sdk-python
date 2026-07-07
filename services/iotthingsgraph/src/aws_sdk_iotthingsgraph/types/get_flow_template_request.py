"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetFlowTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.urn
    import aws_sdk_iotthingsgraph.types.version


class GetFlowTemplateRequest(TypedDict, closed=True):
    id: "aws_sdk_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the workflow.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME</code> </p>"""
    revision_number: NotRequired["aws_sdk_iotthingsgraph.types.version.Version"]
    """<p>The number of the workflow revision to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFlowTemplateRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "revision_number" in value:
        out["revisionNumber"] = value["revision_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFlowTemplateRequest:
    out: GetFlowTemplateRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetFlowTemplateRequest.id required")
    if "revisionNumber" in data:
        out["revision_number"] = data["revisionNumber"]
    return out
