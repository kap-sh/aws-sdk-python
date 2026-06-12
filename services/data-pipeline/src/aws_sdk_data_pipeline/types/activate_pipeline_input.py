"""Generated from Smithy shape ``com.amazonaws.datapipeline#ActivatePipelineInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id
    import aws_sdk_data_pipeline.types.parameter_value_list
    import aws_sdk_data_pipeline.types.timestamp


class ActivatePipelineInput(TypedDict):
    pipeline_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    parameter_values: NotRequired[
        "aws_sdk_data_pipeline.types.parameter_value_list.ParameterValueList"
    ]
    """<p>A list of parameter values to pass to the pipeline at activation.</p>"""
    start_timestamp: NotRequired["aws_sdk_data_pipeline.types.timestamp.timestamp"]
    """<p>The date and time to resume the pipeline. By default, the pipeline resumes from the last completed execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivatePipelineInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    if "parameter_values" in value:
        import aws_sdk_data_pipeline.types.parameter_value_list

        out["parameterValues"] = (
            aws_sdk_data_pipeline.types.parameter_value_list.serialize_aws_json_1_1(
                value["parameter_values"]
            )
        )
    if "start_timestamp" in value:
        import aws_sdk_data_pipeline.types.timestamp

        out["startTimestamp"] = (
            aws_sdk_data_pipeline.types.timestamp.serialize_aws_json_1_1(
                value["start_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActivatePipelineInput:
    out: ActivatePipelineInput = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("ActivatePipelineInput.pipeline_id required")
    if "parameterValues" in data:
        import aws_sdk_data_pipeline.types.parameter_value_list

        out["parameter_values"] = (
            aws_sdk_data_pipeline.types.parameter_value_list.deserialize_aws_json_1_1(
                data["parameterValues"]
            )
        )
    if "startTimestamp" in data:
        import aws_sdk_data_pipeline.types.timestamp

        out["start_timestamp"] = (
            aws_sdk_data_pipeline.types.timestamp.deserialize_aws_json_1_1(
                data["startTimestamp"]
            )
        )
    return out
