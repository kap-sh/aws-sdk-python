"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.parallelism_configuration
    import aws_sdk_sagemaker.types.parameter_list
    import aws_sdk_sagemaker.types.pipeline_arn
    import aws_sdk_sagemaker.types.pipeline_execution_arn
    import aws_sdk_sagemaker.types.pipeline_execution_description
    import aws_sdk_sagemaker.types.pipeline_execution_failure_reason
    import aws_sdk_sagemaker.types.pipeline_execution_name
    import aws_sdk_sagemaker.types.pipeline_execution_status
    import aws_sdk_sagemaker.types.pipeline_experiment_config
    import aws_sdk_sagemaker.types.pipeline_version_id
    import aws_sdk_sagemaker.types.pipeline_version_name
    import aws_sdk_sagemaker.types.selective_execution_config
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.user_context


class PipelineExecution(TypedDict, closed=True):
    pipeline_arn: NotRequired["aws_sdk_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline that was executed.</p>"""
    pipeline_execution_arn: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the pipeline execution.</p>"""
    pipeline_execution_display_name: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_name.PipelineExecutionName"
    ]
    """<p>The display name of the pipeline execution.</p>"""
    pipeline_execution_status: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_status.PipelineExecutionStatus"
    ]
    """<p>The status of the pipeline status.</p>"""
    pipeline_execution_description: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_description.PipelineExecutionDescription"
    ]
    """<p>The description of the pipeline execution.</p>"""
    pipeline_experiment_config: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_experiment_config.PipelineExperimentConfig"
    ]
    failure_reason: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_failure_reason.PipelineExecutionFailureReason"
    ]
    """<p>If the execution failed, a message describing why.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of the pipeline execution.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the pipeline execution was last modified.</p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    last_modified_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    parallelism_configuration: NotRequired[
        "aws_sdk_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>The parallelism configuration applied to the pipeline execution.</p>"""
    selective_execution_config: NotRequired[
        "aws_sdk_sagemaker.types.selective_execution_config.SelectiveExecutionConfig"
    ]
    """<p>The selective execution configuration applied to the pipeline run.</p>"""
    pipeline_parameters: NotRequired[
        "aws_sdk_sagemaker.types.parameter_list.ParameterList"
    ]
    """<p>Contains a list of pipeline parameters. This list can be empty. </p>"""
    pipeline_version_id: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_id.PipelineVersionId"
    ]
    """<p>The ID of the pipeline version that started this execution.</p>"""
    pipeline_version_display_name: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_name.PipelineVersionName"
    ]
    """<p>The display name of the pipeline version that started this execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecution) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "pipeline_execution_arn" in value:
        out["PipelineExecutionArn"] = value["pipeline_execution_arn"]
    if "pipeline_execution_display_name" in value:
        out["PipelineExecutionDisplayName"] = value["pipeline_execution_display_name"]
    if "pipeline_execution_status" in value:
        import aws_sdk_sagemaker.types.pipeline_execution_status

        out["PipelineExecutionStatus"] = (
            aws_sdk_sagemaker.types.pipeline_execution_status.serialize_aws_json_1_1(
                value["pipeline_execution_status"]
            )
        )
    if "pipeline_execution_description" in value:
        out["PipelineExecutionDescription"] = value["pipeline_execution_description"]
    if "pipeline_experiment_config" in value:
        import aws_sdk_sagemaker.types.pipeline_experiment_config

        out["PipelineExperimentConfig"] = (
            aws_sdk_sagemaker.types.pipeline_experiment_config.serialize_aws_json_1_1(
                value["pipeline_experiment_config"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
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
    if "selective_execution_config" in value:
        import aws_sdk_sagemaker.types.selective_execution_config

        out["SelectiveExecutionConfig"] = (
            aws_sdk_sagemaker.types.selective_execution_config.serialize_aws_json_1_1(
                value["selective_execution_config"]
            )
        )
    if "pipeline_parameters" in value:
        import aws_sdk_sagemaker.types.parameter_list

        out["PipelineParameters"] = (
            aws_sdk_sagemaker.types.parameter_list.serialize_aws_json_1_1(
                value["pipeline_parameters"]
            )
        )
    if "pipeline_version_id" in value:
        out["PipelineVersionId"] = value["pipeline_version_id"]
    if "pipeline_version_display_name" in value:
        out["PipelineVersionDisplayName"] = value["pipeline_version_display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecution:
    out: PipelineExecution = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    if "PipelineExecutionArn" in data:
        out["pipeline_execution_arn"] = data["PipelineExecutionArn"]
    if "PipelineExecutionDisplayName" in data:
        out["pipeline_execution_display_name"] = data["PipelineExecutionDisplayName"]
    if "PipelineExecutionStatus" in data:
        import aws_sdk_sagemaker.types.pipeline_execution_status

        out["pipeline_execution_status"] = (
            aws_sdk_sagemaker.types.pipeline_execution_status.deserialize_aws_json_1_1(
                data["PipelineExecutionStatus"]
            )
        )
    if "PipelineExecutionDescription" in data:
        out["pipeline_execution_description"] = data["PipelineExecutionDescription"]
    if "PipelineExperimentConfig" in data:
        import aws_sdk_sagemaker.types.pipeline_experiment_config

        out["pipeline_experiment_config"] = (
            aws_sdk_sagemaker.types.pipeline_experiment_config.deserialize_aws_json_1_1(
                data["PipelineExperimentConfig"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
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
    if "SelectiveExecutionConfig" in data:
        import aws_sdk_sagemaker.types.selective_execution_config

        out["selective_execution_config"] = (
            aws_sdk_sagemaker.types.selective_execution_config.deserialize_aws_json_1_1(
                data["SelectiveExecutionConfig"]
            )
        )
    if "PipelineParameters" in data:
        import aws_sdk_sagemaker.types.parameter_list

        out["pipeline_parameters"] = (
            aws_sdk_sagemaker.types.parameter_list.deserialize_aws_json_1_1(
                data["PipelineParameters"]
            )
        )
    if "PipelineVersionId" in data:
        out["pipeline_version_id"] = data["PipelineVersionId"]
    if "PipelineVersionDisplayName" in data:
        out["pipeline_version_display_name"] = data["PipelineVersionDisplayName"]
    return out
