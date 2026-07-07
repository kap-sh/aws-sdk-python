"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.artifact_revision_list
    import aws_sdk_codepipeline.types.execution_mode
    import aws_sdk_codepipeline.types.execution_trigger
    import aws_sdk_codepipeline.types.execution_type
    import aws_sdk_codepipeline.types.pipeline_execution_id
    import aws_sdk_codepipeline.types.pipeline_execution_status
    import aws_sdk_codepipeline.types.pipeline_execution_status_summary
    import aws_sdk_codepipeline.types.pipeline_name
    import aws_sdk_codepipeline.types.pipeline_rollback_metadata
    import aws_sdk_codepipeline.types.pipeline_version
    import aws_sdk_codepipeline.types.resolved_pipeline_variable_list


class PipelineExecution(TypedDict, closed=True):
    pipeline_name: NotRequired["aws_sdk_codepipeline.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline with the specified pipeline execution.</p>"""
    pipeline_version: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_version.PipelineVersion"
    ]
    """<p>The version number of the pipeline with the specified pipeline execution.</p>"""
    pipeline_execution_id: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The ID of the pipeline execution.</p>"""
    status: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_execution_status.PipelineExecutionStatus"
    ]
    r"""<p>The status of the pipeline execution.</p> <ul> <li> <p>Cancelled: The pipeline’s definition was updated before the pipeline execution could be completed.</p> </li> <li> <p>InProgress: The pipeline execution is currently running.</p> </li> <li> <p>Stopped: The pipeline execution was manually stopped. For more information, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped\">Stopped Executions</a>.</p> </li> <li> <p>Stopping: The pipeline execution received a request to be manually stopped. Depending on the selected stop mode, the execution is either completing or abandoning in-progress actions. For more information, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-executions-stopped\">Stopped Executions</a>.</p> </li> <li> <p>Succeeded: The pipeline execution was completed successfully. </p> </li> <li> <p>Superseded: While this pipeline execution was waiting for the next stage to be completed, a newer pipeline execution advanced and continued through the pipeline instead. For more information, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-superseded\">Superseded Executions</a>.</p> </li> <li> <p>Failed: The pipeline execution was not completed successfully.</p> </li> </ul>"""
    status_summary: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_execution_status_summary.PipelineExecutionStatusSummary"
    ]
    """<p>A summary that contains a description of the pipeline execution status.</p>"""
    artifact_revisions: NotRequired[
        "aws_sdk_codepipeline.types.artifact_revision_list.ArtifactRevisionList"
    ]
    """<p>A list of <code>ArtifactRevision</code> objects included in a pipeline execution.</p>"""
    variables: NotRequired[
        "aws_sdk_codepipeline.types.resolved_pipeline_variable_list.ResolvedPipelineVariableList"
    ]
    """<p>A list of pipeline variables used for the pipeline execution.</p>"""
    trigger: NotRequired[
        "aws_sdk_codepipeline.types.execution_trigger.ExecutionTrigger"
    ]
    execution_mode: NotRequired[
        "aws_sdk_codepipeline.types.execution_mode.ExecutionMode"
    ]
    """<p>The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.</p>"""
    execution_type: NotRequired[
        "aws_sdk_codepipeline.types.execution_type.ExecutionType"
    ]
    """<p>The type of the pipeline execution.</p>"""
    rollback_metadata: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_rollback_metadata.PipelineRollbackMetadata"
    ]
    """<p>The metadata about the execution pertaining to stage rollback.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecution) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["pipelineName"] = value["pipeline_name"]
    if "pipeline_version" in value:
        out["pipelineVersion"] = value["pipeline_version"]
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    if "status" in value:
        import aws_sdk_codepipeline.types.pipeline_execution_status

        out["status"] = (
            aws_sdk_codepipeline.types.pipeline_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_summary" in value:
        out["statusSummary"] = value["status_summary"]
    if "artifact_revisions" in value:
        import aws_sdk_codepipeline.types.artifact_revision_list

        out["artifactRevisions"] = (
            aws_sdk_codepipeline.types.artifact_revision_list.serialize_aws_json_1_1(
                value["artifact_revisions"]
            )
        )
    if "variables" in value:
        import aws_sdk_codepipeline.types.resolved_pipeline_variable_list

        out["variables"] = (
            aws_sdk_codepipeline.types.resolved_pipeline_variable_list.serialize_aws_json_1_1(
                value["variables"]
            )
        )
    if "trigger" in value:
        import aws_sdk_codepipeline.types.execution_trigger

        out["trigger"] = (
            aws_sdk_codepipeline.types.execution_trigger.serialize_aws_json_1_1(
                value["trigger"]
            )
        )
    if "execution_mode" in value:
        import aws_sdk_codepipeline.types.execution_mode

        out["executionMode"] = (
            aws_sdk_codepipeline.types.execution_mode.serialize_aws_json_1_1(
                value["execution_mode"]
            )
        )
    if "execution_type" in value:
        import aws_sdk_codepipeline.types.execution_type

        out["executionType"] = (
            aws_sdk_codepipeline.types.execution_type.serialize_aws_json_1_1(
                value["execution_type"]
            )
        )
    if "rollback_metadata" in value:
        import aws_sdk_codepipeline.types.pipeline_rollback_metadata

        out["rollbackMetadata"] = (
            aws_sdk_codepipeline.types.pipeline_rollback_metadata.serialize_aws_json_1_1(
                value["rollback_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecution:
    out: PipelineExecution = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    if "pipelineVersion" in data:
        out["pipeline_version"] = data["pipelineVersion"]
    if "pipelineExecutionId" in data:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    if "status" in data:
        import aws_sdk_codepipeline.types.pipeline_execution_status

        out["status"] = (
            aws_sdk_codepipeline.types.pipeline_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "statusSummary" in data:
        out["status_summary"] = data["statusSummary"]
    if "artifactRevisions" in data:
        import aws_sdk_codepipeline.types.artifact_revision_list

        out["artifact_revisions"] = (
            aws_sdk_codepipeline.types.artifact_revision_list.deserialize_aws_json_1_1(
                data["artifactRevisions"]
            )
        )
    if "variables" in data:
        import aws_sdk_codepipeline.types.resolved_pipeline_variable_list

        out["variables"] = (
            aws_sdk_codepipeline.types.resolved_pipeline_variable_list.deserialize_aws_json_1_1(
                data["variables"]
            )
        )
    if "trigger" in data:
        import aws_sdk_codepipeline.types.execution_trigger

        out["trigger"] = (
            aws_sdk_codepipeline.types.execution_trigger.deserialize_aws_json_1_1(
                data["trigger"]
            )
        )
    if "executionMode" in data:
        import aws_sdk_codepipeline.types.execution_mode

        out["execution_mode"] = (
            aws_sdk_codepipeline.types.execution_mode.deserialize_aws_json_1_1(
                data["executionMode"]
            )
        )
    if "executionType" in data:
        import aws_sdk_codepipeline.types.execution_type

        out["execution_type"] = (
            aws_sdk_codepipeline.types.execution_type.deserialize_aws_json_1_1(
                data["executionType"]
            )
        )
    if "rollbackMetadata" in data:
        import aws_sdk_codepipeline.types.pipeline_rollback_metadata

        out["rollback_metadata"] = (
            aws_sdk_codepipeline.types.pipeline_rollback_metadata.deserialize_aws_json_1_1(
                data["rollbackMetadata"]
            )
        )
    return out
