"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataIntegrationFlowExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_execution


class GetDataIntegrationFlowExecutionResponse(TypedDict):
    flow_execution: "aws_sdk_supplychain.types.data_integration_flow_execution.DataIntegrationFlowExecution"
    """<p>The flow execution details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataIntegrationFlowExecutionResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_flow_execution

    out["flowExecution"] = (
        aws_sdk_supplychain.types.data_integration_flow_execution.serialize_json(
            value["flow_execution"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetDataIntegrationFlowExecutionResponse:
    out: GetDataIntegrationFlowExecutionResponse = {}  # type: ignore[typeddict-item]
    if "flowExecution" in data:
        import aws_sdk_supplychain.types.data_integration_flow_execution

        out["flow_execution"] = (
            aws_sdk_supplychain.types.data_integration_flow_execution.deserialize_json(
                data["flowExecution"]
            )
        )
    else:
        raise DeserializationError(
            "GetDataIntegrationFlowExecutionResponse.flow_execution required"
        )
    return out
