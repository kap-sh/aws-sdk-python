"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field_list


class DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration(
    TypedDict, closed=True
):
    fields: "aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field_list.DataIntegrationFlowFieldPriorityDedupeFieldList"
    """<p>The list of field names and their sort order for deduplication, arranged in descending priority from highest to lowest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration,
) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field_list

    out["fields"] = (
        aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field_list.serialize_json(
            value["fields"]
        )
    )
    return out


def deserialize_json(
    data: dict,
) -> DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration:
    out: DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field_list

        out["fields"] = (
            aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_field_list.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError(
            "DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration.fields required"
        )
    return out
