"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowFieldPriorityDedupeFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_field_priority_dedupe_field

DataIntegrationFlowFieldPriorityDedupeFieldList: TypeAlias = list[
    "capo_supplychain.types.data_integration_flow_field_priority_dedupe_field.DataIntegrationFlowFieldPriorityDedupeField"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowFieldPriorityDedupeFieldList) -> list:
    import capo_supplychain.types.data_integration_flow_field_priority_dedupe_field

    out: list = []
    for item in value:
        out.append(
            capo_supplychain.types.data_integration_flow_field_priority_dedupe_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataIntegrationFlowFieldPriorityDedupeFieldList:
    import capo_supplychain.types.data_integration_flow_field_priority_dedupe_field

    out: DataIntegrationFlowFieldPriorityDedupeFieldList = []
    for item in data:
        out.append(
            capo_supplychain.types.data_integration_flow_field_priority_dedupe_field.deserialize_json(
                item
            )
        )
    return out
