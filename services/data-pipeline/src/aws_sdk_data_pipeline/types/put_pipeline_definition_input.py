"""Generated from Smithy shape ``com.amazonaws.datapipeline#PutPipelineDefinitionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id
    import aws_sdk_data_pipeline.types.parameter_object_list
    import aws_sdk_data_pipeline.types.parameter_value_list
    import aws_sdk_data_pipeline.types.pipeline_object_list


class PutPipelineDefinitionInput(TypedDict):
    pipeline_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    pipeline_objects: (
        "aws_sdk_data_pipeline.types.pipeline_object_list.PipelineObjectList"
    )
    """<p>The objects that define the pipeline. These objects overwrite the existing pipeline definition.</p>"""
    parameter_objects: NotRequired[
        "aws_sdk_data_pipeline.types.parameter_object_list.ParameterObjectList"
    ]
    """<p>The parameter objects used with the pipeline.</p>"""
    parameter_values: NotRequired[
        "aws_sdk_data_pipeline.types.parameter_value_list.ParameterValueList"
    ]
    """<p>The parameter values used with the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPipelineDefinitionInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    import aws_sdk_data_pipeline.types.pipeline_object_list

    out["pipelineObjects"] = (
        aws_sdk_data_pipeline.types.pipeline_object_list.serialize_aws_json_1_1(
            value["pipeline_objects"]
        )
    )
    if "parameter_objects" in value:
        import aws_sdk_data_pipeline.types.parameter_object_list

        out["parameterObjects"] = (
            aws_sdk_data_pipeline.types.parameter_object_list.serialize_aws_json_1_1(
                value["parameter_objects"]
            )
        )
    if "parameter_values" in value:
        import aws_sdk_data_pipeline.types.parameter_value_list

        out["parameterValues"] = (
            aws_sdk_data_pipeline.types.parameter_value_list.serialize_aws_json_1_1(
                value["parameter_values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPipelineDefinitionInput:
    out: PutPipelineDefinitionInput = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("PutPipelineDefinitionInput.pipeline_id required")
    if "pipelineObjects" in data:
        import aws_sdk_data_pipeline.types.pipeline_object_list

        out["pipeline_objects"] = (
            aws_sdk_data_pipeline.types.pipeline_object_list.deserialize_aws_json_1_1(
                data["pipelineObjects"]
            )
        )
    else:
        raise DeserializationError(
            "PutPipelineDefinitionInput.pipeline_objects required"
        )
    if "parameterObjects" in data:
        import aws_sdk_data_pipeline.types.parameter_object_list

        out["parameter_objects"] = (
            aws_sdk_data_pipeline.types.parameter_object_list.deserialize_aws_json_1_1(
                data["parameterObjects"]
            )
        )
    if "parameterValues" in data:
        import aws_sdk_data_pipeline.types.parameter_value_list

        out["parameter_values"] = (
            aws_sdk_data_pipeline.types.parameter_value_list.deserialize_aws_json_1_1(
                data["parameterValues"]
            )
        )
    return out
