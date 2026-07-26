"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataIntegrationFlowExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_execution


class GetDataIntegrationFlowExecutionResponse(TypedDict, closed=True):
    flow_execution: "capo_supplychain.types.data_integration_flow_execution.DataIntegrationFlowExecution"
    """<p>The flow execution details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataIntegrationFlowExecutionResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_flow_execution

    out["flowExecution"] = (
        capo_supplychain.types.data_integration_flow_execution.serialize_json(
            value["flow_execution"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetDataIntegrationFlowExecutionResponse:
    out: GetDataIntegrationFlowExecutionResponse = {}  # type: ignore[typeddict-item]
    if "flowExecution" in data:
        import capo_supplychain.types.data_integration_flow_execution

        out["flow_execution"] = (
            capo_supplychain.types.data_integration_flow_execution.deserialize_json(
                data["flowExecution"]
            )
        )
    else:
        raise DeserializationError(
            "GetDataIntegrationFlowExecutionResponse.flow_execution required"
        )
    return out
