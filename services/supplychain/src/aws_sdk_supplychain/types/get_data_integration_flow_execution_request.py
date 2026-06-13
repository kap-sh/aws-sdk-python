"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataIntegrationFlowExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_name
    import aws_sdk_supplychain.types.uuid


class GetDataIntegrationFlowExecutionRequest(TypedDict):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    flow_name: (
        "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    )
    """<p>The flow name.</p>"""
    execution_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The flow execution identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataIntegrationFlowExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataIntegrationFlowExecutionRequest:
    out: GetDataIntegrationFlowExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
