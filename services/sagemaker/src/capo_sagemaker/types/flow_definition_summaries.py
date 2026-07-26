"""Generated from Smithy shape ``com.amazonaws.sagemaker#FlowDefinitionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.flow_definition_summary

FlowDefinitionSummaries: TypeAlias = list[
    "capo_sagemaker.types.flow_definition_summary.FlowDefinitionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowDefinitionSummaries) -> list:
    import capo_sagemaker.types.flow_definition_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.flow_definition_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FlowDefinitionSummaries:
    import capo_sagemaker.types.flow_definition_summary

    out: FlowDefinitionSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.flow_definition_summary.deserialize_aws_json_1_1(item)
        )
    return out
