"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowDedupeStrategy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy_type
    import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_strategy_configuration


class DataIntegrationFlowDedupeStrategy(TypedDict):
    type: "aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy_type.DataIntegrationFlowDedupeStrategyType"
    """<p>The type of the deduplication strategy.</p> <ul> <li> <p> <b>FIELD_PRIORITY</b> - Field priority configuration for the deduplication strategy specifies an ordered list of fields used to tie-break the data records sharing the same primary key values. Fields earlier in the list have higher priority for evaluation. For each field, the sort order determines whether to retain data record with larger or smaller field value.</p> </li> </ul>"""
    field_priority: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_strategy_configuration.DataIntegrationFlowFieldPriorityDedupeStrategyConfiguration"
    ]
    """<p>The field priority deduplication strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowDedupeStrategy) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy_type

    out["type"] = (
        aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy_type.serialize_json(
            value["type"]
        )
    )
    if "field_priority" in value:
        import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_strategy_configuration

        out["fieldPriority"] = (
            aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_strategy_configuration.serialize_json(
                value["field_priority"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowDedupeStrategy:
    out: DataIntegrationFlowDedupeStrategy = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy_type

        out["type"] = (
            aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlowDedupeStrategy.type required")
    if "fieldPriority" in data:
        import aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_strategy_configuration

        out["field_priority"] = (
            aws_sdk_supplychain.types.data_integration_flow_field_priority_dedupe_strategy_configuration.deserialize_json(
                data["fieldPriority"]
            )
        )
    return out
