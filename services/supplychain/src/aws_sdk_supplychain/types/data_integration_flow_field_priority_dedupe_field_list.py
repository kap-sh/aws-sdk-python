"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowFieldPriorityDedupeFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field

DataIntegrationFlowFieldPriorityDedupeFieldList: TypeAlias = list[
    "aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field.DataIntegrationFlowFieldPriorityDedupeField"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowFieldPriorityDedupeFieldList) -> list:
    import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataIntegrationFlowFieldPriorityDedupeFieldList:
    import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field

    out: DataIntegrationFlowFieldPriorityDedupeFieldList = []
    for item in data:
        out.append(
            aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field.deserialize_json(
                item
            )
        )
    return out
