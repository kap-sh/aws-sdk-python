"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowFieldPriorityDedupeField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field_name
    import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_sort_order


class DataIntegrationFlowFieldPriorityDedupeField(TypedDict):
    name: "aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field_name.DataIntegrationFlowFieldPriorityDedupeFieldName"
    """<p>The name of the deduplication field. Must exist in the dataset and not be a primary key.</p>"""
    sort_order: "aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_sort_order.DataIntegrationFlowFieldPriorityDedupeSortOrder"
    """<p>The sort order for the deduplication field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowFieldPriorityDedupeField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_sort_order

    out["sortOrder"] = (
        aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_sort_order.serialize_json(
            value["sort_order"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowFieldPriorityDedupeField:
    out: DataIntegrationFlowFieldPriorityDedupeField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "DataIntegrationFlowFieldPriorityDedupeField.name required"
        )
    if "sortOrder" in data:
        import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_sort_order

        out["sort_order"] = (
            aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_sort_order.deserialize_json(
                data["sortOrder"]
            )
        )
    else:
        raise DeserializationError(
            "DataIntegrationFlowFieldPriorityDedupeField.sort_order required"
        )
    return out
