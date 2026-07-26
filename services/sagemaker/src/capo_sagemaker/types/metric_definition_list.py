"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.metric_definition

MetricDefinitionList: TypeAlias = list[
    "capo_sagemaker.types.metric_definition.MetricDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDefinitionList) -> list:
    import capo_sagemaker.types.metric_definition

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.metric_definition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricDefinitionList:
    import capo_sagemaker.types.metric_definition

    out: MetricDefinitionList = []
    for item in data:
        out.append(
            capo_sagemaker.types.metric_definition.deserialize_aws_json_1_1(item)
        )
    return out
