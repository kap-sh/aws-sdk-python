"""Generated from Smithy shape ``com.amazonaws.eventbridge#SageMakerPipelineParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.sage_maker_pipeline_parameter

SageMakerPipelineParameterList: TypeAlias = list[
    "aws_sdk_eventbridge.types.sage_maker_pipeline_parameter.SageMakerPipelineParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SageMakerPipelineParameterList) -> list:
    import aws_sdk_eventbridge.types.sage_maker_pipeline_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_eventbridge.types.sage_maker_pipeline_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SageMakerPipelineParameterList:
    import aws_sdk_eventbridge.types.sage_maker_pipeline_parameter

    out: SageMakerPipelineParameterList = []
    for item in data:
        out.append(
            aws_sdk_eventbridge.types.sage_maker_pipeline_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
