"""Generated from Smithy shape ``com.amazonaws.scheduler#SageMakerPipelineParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_scheduler.types.sage_maker_pipeline_parameter

SageMakerPipelineParameterList: TypeAlias = list[
    "capo_scheduler.types.sage_maker_pipeline_parameter.SageMakerPipelineParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerPipelineParameterList) -> list:
    import capo_scheduler.types.sage_maker_pipeline_parameter

    out: list = []
    for item in value:
        out.append(
            capo_scheduler.types.sage_maker_pipeline_parameter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SageMakerPipelineParameterList:
    import capo_scheduler.types.sage_maker_pipeline_parameter

    out: SageMakerPipelineParameterList = []
    for item in data:
        out.append(
            capo_scheduler.types.sage_maker_pipeline_parameter.deserialize_json(item)
        )
    return out
