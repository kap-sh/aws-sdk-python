"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_execution

DataIntegrationFlowExecutionList: TypeAlias = list[
    "capo_supplychain.types.data_integration_flow_execution.DataIntegrationFlowExecution"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowExecutionList) -> list:
    import capo_supplychain.types.data_integration_flow_execution

    out: list = []
    for item in value:
        out.append(
            capo_supplychain.types.data_integration_flow_execution.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataIntegrationFlowExecutionList:
    import capo_supplychain.types.data_integration_flow_execution

    out: DataIntegrationFlowExecutionList = []
    for item in data:
        out.append(
            capo_supplychain.types.data_integration_flow_execution.deserialize_json(
                item
            )
        )
    return out
