"""Generated from Smithy shape ``com.amazonaws.datapipeline#GetPipelineDefinitionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.parameter_object_list
    import capo_data_pipeline.types.parameter_value_list
    import capo_data_pipeline.types.pipeline_object_list


class GetPipelineDefinitionOutput(TypedDict, closed=True):
    pipeline_objects: NotRequired[
        "capo_data_pipeline.types.pipeline_object_list.PipelineObjectList"
    ]
    """<p>The objects defined in the pipeline.</p>"""
    parameter_objects: NotRequired[
        "capo_data_pipeline.types.parameter_object_list.ParameterObjectList"
    ]
    """<p>The parameter objects used in the pipeline definition.</p>"""
    parameter_values: NotRequired[
        "capo_data_pipeline.types.parameter_value_list.ParameterValueList"
    ]
    """<p>The parameter values used in the pipeline definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPipelineDefinitionOutput) -> dict:
    out: dict = {}
    if "pipeline_objects" in value:
        import capo_data_pipeline.types.pipeline_object_list

        out["pipelineObjects"] = (
            capo_data_pipeline.types.pipeline_object_list.serialize_aws_json_1_1(
                value["pipeline_objects"]
            )
        )
    if "parameter_objects" in value:
        import capo_data_pipeline.types.parameter_object_list

        out["parameterObjects"] = (
            capo_data_pipeline.types.parameter_object_list.serialize_aws_json_1_1(
                value["parameter_objects"]
            )
        )
    if "parameter_values" in value:
        import capo_data_pipeline.types.parameter_value_list

        out["parameterValues"] = (
            capo_data_pipeline.types.parameter_value_list.serialize_aws_json_1_1(
                value["parameter_values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPipelineDefinitionOutput:
    out: GetPipelineDefinitionOutput = {}  # type: ignore[typeddict-item]
    if "pipelineObjects" in data:
        import capo_data_pipeline.types.pipeline_object_list

        out["pipeline_objects"] = (
            capo_data_pipeline.types.pipeline_object_list.deserialize_aws_json_1_1(
                data["pipelineObjects"]
            )
        )
    if "parameterObjects" in data:
        import capo_data_pipeline.types.parameter_object_list

        out["parameter_objects"] = (
            capo_data_pipeline.types.parameter_object_list.deserialize_aws_json_1_1(
                data["parameterObjects"]
            )
        )
    if "parameterValues" in data:
        import capo_data_pipeline.types.parameter_value_list

        out["parameter_values"] = (
            capo_data_pipeline.types.parameter_value_list.deserialize_aws_json_1_1(
                data["parameterValues"]
            )
        )
    return out
