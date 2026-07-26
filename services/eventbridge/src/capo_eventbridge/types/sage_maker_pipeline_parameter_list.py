"""Generated from Smithy shape ``com.amazonaws.eventbridge#SageMakerPipelineParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.sage_maker_pipeline_parameter

SageMakerPipelineParameterList: TypeAlias = list[
    "capo_eventbridge.types.sage_maker_pipeline_parameter.SageMakerPipelineParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SageMakerPipelineParameterList) -> list:
    import capo_eventbridge.types.sage_maker_pipeline_parameter

    out: list = []
    for item in value:
        out.append(
            capo_eventbridge.types.sage_maker_pipeline_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SageMakerPipelineParameterList:
    import capo_eventbridge.types.sage_maker_pipeline_parameter

    out: SageMakerPipelineParameterList = []
    for item in data:
        out.append(
            capo_eventbridge.types.sage_maker_pipeline_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
