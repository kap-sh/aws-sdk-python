"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#SageMakerPipelineParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.sage_maker_pipeline_parameter_list


class SageMakerPipelineParameters(TypedDict, closed=True):
    pipeline_parameter_list: NotRequired[
        "aws_sdk_cloudwatch_events.types.sage_maker_pipeline_parameter_list.SageMakerPipelineParameterList"
    ]
    """<p>List of Parameter names and values for SageMaker AI Model Building Pipeline execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SageMakerPipelineParameters) -> dict:
    out: dict = {}
    if "pipeline_parameter_list" in value:
        import aws_sdk_cloudwatch_events.types.sage_maker_pipeline_parameter_list

        out["PipelineParameterList"] = (
            aws_sdk_cloudwatch_events.types.sage_maker_pipeline_parameter_list.serialize_aws_json_1_1(
                value["pipeline_parameter_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SageMakerPipelineParameters:
    out: SageMakerPipelineParameters = {}  # type: ignore[typeddict-item]
    if "PipelineParameterList" in data:
        import aws_sdk_cloudwatch_events.types.sage_maker_pipeline_parameter_list

        out["pipeline_parameter_list"] = (
            aws_sdk_cloudwatch_events.types.sage_maker_pipeline_parameter_list.deserialize_aws_json_1_1(
                data["PipelineParameterList"]
            )
        )
    return out
