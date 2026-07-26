"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowExecutionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.flow_execution_summary

FlowExecutionSummaries: TypeAlias = list[
    "capo_iotthingsgraph.types.flow_execution_summary.FlowExecutionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowExecutionSummaries) -> list:
    import capo_iotthingsgraph.types.flow_execution_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotthingsgraph.types.flow_execution_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FlowExecutionSummaries:
    import capo_iotthingsgraph.types.flow_execution_summary

    out: FlowExecutionSummaries = []
    for item in data:
        out.append(
            capo_iotthingsgraph.types.flow_execution_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
