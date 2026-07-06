"""Generated from Smithy shape ``com.amazonaws.supplychain#DeleteDataIntegrationFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_name
    import aws_sdk_supplychain.types.uuid


class DeleteDataIntegrationFlowResponse(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    """<p>The name of the DataIntegrationFlow deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataIntegrationFlowResponse) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteDataIntegrationFlowResponse:
    out: DeleteDataIntegrationFlowResponse = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError(
            "DeleteDataIntegrationFlowResponse.instance_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteDataIntegrationFlowResponse.name required")
    return out
