"""Generated from Smithy shape ``com.amazonaws.scheduler#SageMakerPipelineParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.sage_maker_pipeline_parameter_list


class SageMakerPipelineParameters(TypedDict, closed=True):
    pipeline_parameter_list: NotRequired[
        "capo_scheduler.types.sage_maker_pipeline_parameter_list.SageMakerPipelineParameterList"
    ]
    """<p>List of parameter names and values to use when executing the SageMaker Model Building Pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerPipelineParameters) -> dict:
    out: dict = {}
    if "pipeline_parameter_list" in value:
        import capo_scheduler.types.sage_maker_pipeline_parameter_list

        out["PipelineParameterList"] = (
            capo_scheduler.types.sage_maker_pipeline_parameter_list.serialize_json(
                value["pipeline_parameter_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> SageMakerPipelineParameters:
    out: SageMakerPipelineParameters = {}  # type: ignore[typeddict-item]
    if data.get("PipelineParameterList") is not None:
        import capo_scheduler.types.sage_maker_pipeline_parameter_list

        out["pipeline_parameter_list"] = (
            capo_scheduler.types.sage_maker_pipeline_parameter_list.deserialize_json(
                data["PipelineParameterList"]
            )
        )
    return out
