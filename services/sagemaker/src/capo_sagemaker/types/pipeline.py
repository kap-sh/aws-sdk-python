"""Generated from Smithy shape ``com.amazonaws.sagemaker#Pipeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.parallelism_configuration
    import capo_sagemaker.types.pipeline_arn
    import capo_sagemaker.types.pipeline_description
    import capo_sagemaker.types.pipeline_name
    import capo_sagemaker.types.pipeline_status
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class Pipeline(TypedDict, closed=True):
    pipeline_arn: NotRequired["capo_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_name: NotRequired["capo_sagemaker.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline.</p>"""
    pipeline_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_name.PipelineName"
    ]
    """<p>The display name of the pipeline.</p>"""
    pipeline_description: NotRequired[
        "capo_sagemaker.types.pipeline_description.PipelineDescription"
    ]
    """<p>The description of the pipeline.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role that created the pipeline.</p>"""
    pipeline_status: NotRequired["capo_sagemaker.types.pipeline_status.PipelineStatus"]
    """<p>The status of the pipeline.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of the pipeline.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the pipeline was last modified.</p>"""
    last_run_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the pipeline was last run.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    parallelism_configuration: NotRequired[
        "capo_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>The parallelism configuration applied to the pipeline.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags that apply to the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Pipeline) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "pipeline_display_name" in value:
        out["PipelineDisplayName"] = value["pipeline_display_name"]
    if "pipeline_description" in value:
        out["PipelineDescription"] = value["pipeline_description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "pipeline_status" in value:
        import capo_sagemaker.types.pipeline_status

        out["PipelineStatus"] = (
            capo_sagemaker.types.pipeline_status.serialize_aws_json_1_1(
                value["pipeline_status"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_run_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastRunTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_run_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "parallelism_configuration" in value:
        import capo_sagemaker.types.parallelism_configuration

        out["ParallelismConfiguration"] = (
            capo_sagemaker.types.parallelism_configuration.serialize_aws_json_1_1(
                value["parallelism_configuration"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Pipeline:
    out: Pipeline = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    if "PipelineName" in data:
        out["pipeline_name"] = data["PipelineName"]
    if "PipelineDisplayName" in data:
        out["pipeline_display_name"] = data["PipelineDisplayName"]
    if "PipelineDescription" in data:
        out["pipeline_description"] = data["PipelineDescription"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "PipelineStatus" in data:
        import capo_sagemaker.types.pipeline_status

        out["pipeline_status"] = (
            capo_sagemaker.types.pipeline_status.deserialize_aws_json_1_1(
                data["PipelineStatus"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastRunTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_run_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["LastRunTime"]
        )
    if "CreatedBy" in data:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if "LastModifiedBy" in data:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "ParallelismConfiguration" in data:
        import capo_sagemaker.types.parallelism_configuration

        out["parallelism_configuration"] = (
            capo_sagemaker.types.parallelism_configuration.deserialize_aws_json_1_1(
                data["ParallelismConfiguration"]
            )
        )
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
