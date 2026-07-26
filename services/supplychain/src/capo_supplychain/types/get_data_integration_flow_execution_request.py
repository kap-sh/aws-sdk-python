"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataIntegrationFlowExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_name
    import capo_supplychain.types.uuid


class GetDataIntegrationFlowExecutionRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    flow_name: (
        "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    )
    """<p>The flow name.</p>"""
    execution_id: "capo_supplychain.types.uuid.UUID"
    """<p>The flow execution identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataIntegrationFlowExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataIntegrationFlowExecutionRequest:
    out: GetDataIntegrationFlowExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
