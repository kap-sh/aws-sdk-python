"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdatePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.parallelism_configuration
    import aws_sdk_sagemaker.types.pipeline_definition
    import aws_sdk_sagemaker.types.pipeline_definition_s3_location
    import aws_sdk_sagemaker.types.pipeline_description
    import aws_sdk_sagemaker.types.pipeline_name
    import aws_sdk_sagemaker.types.role_arn


class UpdatePipelineRequest(TypedDict, closed=True):
    pipeline_name: NotRequired["aws_sdk_sagemaker.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline to update.</p>"""
    pipeline_display_name: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_name.PipelineName"
    ]
    """<p>The display name of the pipeline.</p>"""
    pipeline_definition: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_definition.PipelineDefinition"
    ]
    """<p>The JSON pipeline definition.</p>"""
    pipeline_definition_s3_location: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_definition_s3_location.PipelineDefinitionS3Location"
    ]
    """<p>The location of the pipeline definition stored in Amazon S3. If specified, SageMaker will retrieve the pipeline definition from this location.</p>"""
    pipeline_description: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_description.PipelineDescription"
    ]
    """<p>The description of the pipeline.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that the pipeline uses to execute.</p>"""
    parallelism_configuration: NotRequired[
        "aws_sdk_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>If specified, it applies to all executions of this pipeline by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePipelineRequest) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "pipeline_display_name" in value:
        out["PipelineDisplayName"] = value["pipeline_display_name"]
    if "pipeline_definition" in value:
        out["PipelineDefinition"] = value["pipeline_definition"]
    if "pipeline_definition_s3_location" in value:
        import aws_sdk_sagemaker.types.pipeline_definition_s3_location

        out["PipelineDefinitionS3Location"] = (
            aws_sdk_sagemaker.types.pipeline_definition_s3_location.serialize_aws_json_1_1(
                value["pipeline_definition_s3_location"]
            )
        )
    if "pipeline_description" in value:
        out["PipelineDescription"] = value["pipeline_description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "parallelism_configuration" in value:
        import aws_sdk_sagemaker.types.parallelism_configuration

        out["ParallelismConfiguration"] = (
            aws_sdk_sagemaker.types.parallelism_configuration.serialize_aws_json_1_1(
                value["parallelism_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePipelineRequest:
    out: UpdatePipelineRequest = {}  # type: ignore[typeddict-item]
    if "PipelineName" in data:
        out["pipeline_name"] = data["PipelineName"]
    if "PipelineDisplayName" in data:
        out["pipeline_display_name"] = data["PipelineDisplayName"]
    if "PipelineDefinition" in data:
        out["pipeline_definition"] = data["PipelineDefinition"]
    if "PipelineDefinitionS3Location" in data:
        import aws_sdk_sagemaker.types.pipeline_definition_s3_location

        out["pipeline_definition_s3_location"] = (
            aws_sdk_sagemaker.types.pipeline_definition_s3_location.deserialize_aws_json_1_1(
                data["PipelineDefinitionS3Location"]
            )
        )
    if "PipelineDescription" in data:
        out["pipeline_description"] = data["PipelineDescription"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ParallelismConfiguration" in data:
        import aws_sdk_sagemaker.types.parallelism_configuration

        out["parallelism_configuration"] = (
            aws_sdk_sagemaker.types.parallelism_configuration.deserialize_aws_json_1_1(
                data["ParallelismConfiguration"]
            )
        )
    return out
