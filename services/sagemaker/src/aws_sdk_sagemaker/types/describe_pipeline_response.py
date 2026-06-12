"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribePipelineResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.parallelism_configuration
    import aws_sdk_sagemaker.types.pipeline_arn
    import aws_sdk_sagemaker.types.pipeline_definition
    import aws_sdk_sagemaker.types.pipeline_description
    import aws_sdk_sagemaker.types.pipeline_name
    import aws_sdk_sagemaker.types.pipeline_status
    import aws_sdk_sagemaker.types.pipeline_version_description
    import aws_sdk_sagemaker.types.pipeline_version_name
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.user_context


class DescribePipelineResponse(TypedDict):
    pipeline_arn: NotRequired["aws_sdk_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_name: NotRequired["aws_sdk_sagemaker.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline.</p>"""
    pipeline_display_name: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_name.PipelineName"
    ]
    """<p>The display name of the pipeline.</p>"""
    pipeline_definition: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_definition.PipelineDefinition"
    ]
    """<p>The JSON pipeline definition.</p>"""
    pipeline_description: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_description.PipelineDescription"
    ]
    """<p>The description of the pipeline.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that the pipeline uses to execute.</p>"""
    pipeline_status: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_status.PipelineStatus"
    ]
    """<p>The status of the pipeline execution.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the pipeline was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the pipeline was last modified.</p>"""
    last_run_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the pipeline was last run.</p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    last_modified_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    parallelism_configuration: NotRequired[
        "aws_sdk_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>Lists the parallelism configuration applied to the pipeline.</p>"""
    pipeline_version_display_name: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_name.PipelineVersionName"
    ]
    """<p>The display name of the pipeline version.</p>"""
    pipeline_version_description: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_description.PipelineVersionDescription"
    ]
    """<p>The description of the pipeline version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePipelineResponse) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "pipeline_display_name" in value:
        out["PipelineDisplayName"] = value["pipeline_display_name"]
    if "pipeline_definition" in value:
        out["PipelineDefinition"] = value["pipeline_definition"]
    if "pipeline_description" in value:
        out["PipelineDescription"] = value["pipeline_description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "pipeline_status" in value:
        import aws_sdk_sagemaker.types.pipeline_status

        out["PipelineStatus"] = (
            aws_sdk_sagemaker.types.pipeline_status.serialize_aws_json_1_1(
                value["pipeline_status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_run_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastRunTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_run_time"]
        )
    if "created_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["CreatedBy"] = aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "parallelism_configuration" in value:
        import aws_sdk_sagemaker.types.parallelism_configuration

        out["ParallelismConfiguration"] = (
            aws_sdk_sagemaker.types.parallelism_configuration.serialize_aws_json_1_1(
                value["parallelism_configuration"]
            )
        )
    if "pipeline_version_display_name" in value:
        out["PipelineVersionDisplayName"] = value["pipeline_version_display_name"]
    if "pipeline_version_description" in value:
        out["PipelineVersionDescription"] = value["pipeline_version_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePipelineResponse:
    out: DescribePipelineResponse = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    if "PipelineName" in data:
        out["pipeline_name"] = data["PipelineName"]
    if "PipelineDisplayName" in data:
        out["pipeline_display_name"] = data["PipelineDisplayName"]
    if "PipelineDefinition" in data:
        out["pipeline_definition"] = data["PipelineDefinition"]
    if "PipelineDescription" in data:
        out["pipeline_description"] = data["PipelineDescription"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "PipelineStatus" in data:
        import aws_sdk_sagemaker.types.pipeline_status

        out["pipeline_status"] = (
            aws_sdk_sagemaker.types.pipeline_status.deserialize_aws_json_1_1(
                data["PipelineStatus"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastRunTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_run_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastRunTime"]
            )
        )
    if "CreatedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["created_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["CreatedBy"]
            )
        )
    if "LastModifiedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["last_modified_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "ParallelismConfiguration" in data:
        import aws_sdk_sagemaker.types.parallelism_configuration

        out["parallelism_configuration"] = (
            aws_sdk_sagemaker.types.parallelism_configuration.deserialize_aws_json_1_1(
                data["ParallelismConfiguration"]
            )
        )
    if "PipelineVersionDisplayName" in data:
        out["pipeline_version_display_name"] = data["PipelineVersionDisplayName"]
    if "PipelineVersionDescription" in data:
        out["pipeline_version_description"] = data["PipelineVersionDescription"]
    return out
