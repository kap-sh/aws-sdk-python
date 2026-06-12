"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DeleteSystemTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.urn


class DeleteSystemTemplateRequest(TypedDict):
    id: "aws_sdk_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the system to be deleted.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSystemTemplateRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSystemTemplateRequest:
    out: DeleteSystemTemplateRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteSystemTemplateRequest.id required")
    return out
