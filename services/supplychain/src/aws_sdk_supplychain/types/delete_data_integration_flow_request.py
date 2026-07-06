"""Generated from Smithy shape ``com.amazonaws.supplychain#DeleteDataIntegrationFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_name
    import aws_sdk_supplychain.types.uuid


class DeleteDataIntegrationFlowRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    """<p>The name of the DataIntegrationFlow to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataIntegrationFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataIntegrationFlowRequest:
    out: DeleteDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
    return out
