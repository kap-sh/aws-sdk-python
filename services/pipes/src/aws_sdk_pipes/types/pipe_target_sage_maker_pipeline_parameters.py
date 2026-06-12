"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetSageMakerPipelineParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pipes.types.sage_maker_pipeline_parameter_list


class PipeTargetSageMakerPipelineParameters(TypedDict):
    pipeline_parameter_list: NotRequired[
        "aws_sdk_pipes.types.sage_maker_pipeline_parameter_list.SageMakerPipelineParameterList"
    ]
    """<p>List of Parameter names and values for SageMaker Model Building Pipeline execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetSageMakerPipelineParameters) -> dict:
    out: dict = {}
    if "pipeline_parameter_list" in value:
        import aws_sdk_pipes.types.sage_maker_pipeline_parameter_list

        out["PipelineParameterList"] = (
            aws_sdk_pipes.types.sage_maker_pipeline_parameter_list.serialize_json(
                value["pipeline_parameter_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipeTargetSageMakerPipelineParameters:
    out: PipeTargetSageMakerPipelineParameters = {}  # type: ignore[typeddict-item]
    if "PipelineParameterList" in data:
        import aws_sdk_pipes.types.sage_maker_pipeline_parameter_list

        out["pipeline_parameter_list"] = (
            aws_sdk_pipes.types.sage_maker_pipeline_parameter_list.deserialize_json(
                data["PipelineParameterList"]
            )
        )
    return out
