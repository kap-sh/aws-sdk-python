"""Generated from Smithy shape ``com.amazonaws.pipes#SageMakerPipelineParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.sage_maker_pipeline_parameter

SageMakerPipelineParameterList: TypeAlias = list[
    "aws_sdk_pipes.types.sage_maker_pipeline_parameter.SageMakerPipelineParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerPipelineParameterList) -> list:
    import aws_sdk_pipes.types.sage_maker_pipeline_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pipes.types.sage_maker_pipeline_parameter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SageMakerPipelineParameterList:
    import aws_sdk_pipes.types.sage_maker_pipeline_parameter

    out: SageMakerPipelineParameterList = []
    for item in data:
        out.append(
            aws_sdk_pipes.types.sage_maker_pipeline_parameter.deserialize_json(item)
        )
    return out
