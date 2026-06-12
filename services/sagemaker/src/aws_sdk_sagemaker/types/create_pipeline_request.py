"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.idempotency_token
    import aws_sdk_sagemaker.types.parallelism_configuration
    import aws_sdk_sagemaker.types.pipeline_definition
    import aws_sdk_sagemaker.types.pipeline_definition_s3_location
    import aws_sdk_sagemaker.types.pipeline_description
    import aws_sdk_sagemaker.types.pipeline_name
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.tag_list


class CreatePipelineRequest(TypedDict):
    pipeline_name: NotRequired["aws_sdk_sagemaker.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline.</p>"""
    pipeline_display_name: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_name.PipelineName"
    ]
    """<p>The display name of the pipeline.</p>"""
    pipeline_definition: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_definition.PipelineDefinition"
    ]
    """<p>The <a href=\"https://aws-sagemaker-mlops.github.io/sagemaker-model-building-pipeline-definition-JSON-schema/\">JSON pipeline definition</a> of the pipeline.</p>"""
    pipeline_definition_s3_location: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_definition_s3_location.PipelineDefinitionS3Location"
    ]
    """<p>The location of the pipeline definition stored in Amazon S3. If specified, SageMaker will retrieve the pipeline definition from this location.</p>"""
    pipeline_description: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_description.PipelineDescription"
    ]
    """<p>A description of the pipeline.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_sagemaker.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role used by the pipeline to access and create resources.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags to apply to the created pipeline.</p>"""
    parallelism_configuration: NotRequired[
        "aws_sdk_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>This is the configuration that controls the parallelism of the pipeline. If specified, it applies to all runs of this pipeline by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePipelineRequest) -> dict:
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
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "parallelism_configuration" in value:
        import aws_sdk_sagemaker.types.parallelism_configuration

        out["ParallelismConfiguration"] = (
            aws_sdk_sagemaker.types.parallelism_configuration.serialize_aws_json_1_1(
                value["parallelism_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePipelineRequest:
    out: CreatePipelineRequest = {}  # type: ignore[typeddict-item]
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
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ParallelismConfiguration" in data:
        import aws_sdk_sagemaker.types.parallelism_configuration

        out["parallelism_configuration"] = (
            aws_sdk_sagemaker.types.parallelism_configuration.deserialize_aws_json_1_1(
                data["ParallelismConfiguration"]
            )
        )
    return out
