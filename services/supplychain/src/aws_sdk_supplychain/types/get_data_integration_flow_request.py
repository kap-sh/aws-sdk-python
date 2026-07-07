"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataIntegrationFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_name
    import aws_sdk_supplychain.types.uuid


class GetDataIntegrationFlowRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    """<p>The name of the DataIntegrationFlow created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataIntegrationFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataIntegrationFlowRequest:
    out: GetDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
    return out
