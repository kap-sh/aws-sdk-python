"""Generated from Smithy shape ``com.amazonaws.omics#DefaultRunSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.aws_account_id
    import aws_sdk_omics.types.cache_behavior
    import aws_sdk_omics.types.configuration_name
    import aws_sdk_omics.types.engine_settings
    import aws_sdk_omics.types.networking_mode
    import aws_sdk_omics.types.numeric_id_in_arn
    import aws_sdk_omics.types.run_group_id
    import aws_sdk_omics.types.run_log_level
    import aws_sdk_omics.types.run_name
    import aws_sdk_omics.types.run_output_uri
    import aws_sdk_omics.types.run_parameters
    import aws_sdk_omics.types.run_retention_mode
    import aws_sdk_omics.types.run_role_arn
    import aws_sdk_omics.types.storage_type
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.workflow_id
    import aws_sdk_omics.types.workflow_owner_id
    import aws_sdk_omics.types.workflow_type
    import aws_sdk_omics.types.workflow_version_name


class DefaultRunSetting(TypedDict, closed=True):
    workflow_id: "aws_sdk_omics.types.workflow_id.WorkflowId"
    """<p>The identifier of the workflow to run.</p>"""
    workflow_type: NotRequired["aws_sdk_omics.types.workflow_type.WorkflowType"]
    """<p>The type of the originating workflow. Batch runs are not supported with <code>READY2RUN</code> workflows.</p>"""
    role_arn: "aws_sdk_omics.types.run_role_arn.RunRoleArn"
    """<p>The IAM role ARN that grants HealthOmics permissions to access required AWS resources such as Amazon S3 and CloudWatch. The role must have the same permissions required for individual <code>StartRun</code> calls.</p>"""
    name: NotRequired["aws_sdk_omics.types.run_name.RunName"]
    """<p>An optional user-friendly name applied to each workflow run. Can be overridden per run.</p>"""
    cache_id: NotRequired["aws_sdk_omics.types.numeric_id_in_arn.NumericIdInArn"]
    """<p>The identifier of the run cache to associate with the runs.</p>"""
    cache_behavior: NotRequired["aws_sdk_omics.types.cache_behavior.CacheBehavior"]
    """<p>The cache behavior for the runs. Requires <code>cacheId</code> to be set.</p>"""
    run_group_id: NotRequired["aws_sdk_omics.types.run_group_id.RunGroupId"]
    """<p>The ID of the run group to contain all workflow runs in the batch.</p>"""
    priority: NotRequired["int"]
    """<p>An integer priority for the workflow runs. Higher values correspond to higher priority. A value of 0 corresponds to the lowest priority. Can be overridden per run.</p>"""
    parameters: NotRequired["aws_sdk_omics.types.run_parameters.RunParameters"]
    """<p>Workflow parameter names and values shared across all runs. Merged with per-run parameters; run-specific values take precedence when keys overlap. Can be overridden per run.</p>"""
    storage_capacity: NotRequired["int"]
    """<p>The filesystem size in gibibytes (GiB) provisioned for each workflow run and shared by all tasks in that run. Defaults to 1200 GiB if not specified.</p>"""
    output_uri: NotRequired["aws_sdk_omics.types.run_output_uri.RunOutputUri"]
    """<p>The destination S3 URI for workflow outputs. Must begin with <code>s3://</code>. The <code>roleArn</code> must grant write permissions to this bucket. Can be overridden per run.</p>"""
    log_level: NotRequired["aws_sdk_omics.types.run_log_level.RunLogLevel"]
    """<p>The verbosity level for CloudWatch Logs emitted during each run.</p>"""
    run_tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>AWS tags to associate with each workflow run. Merged with per-run <code>runTags</code>; run-specific values take precedence when keys overlap.</p>"""
    retention_mode: NotRequired[
        "aws_sdk_omics.types.run_retention_mode.RunRetentionMode"
    ]
    """<p>The retention behavior for runs after completion.</p>"""
    storage_type: NotRequired["aws_sdk_omics.types.storage_type.StorageType"]
    """<p>The storage type for the workflow runs.</p>"""
    workflow_owner_id: NotRequired[
        "aws_sdk_omics.types.workflow_owner_id.WorkflowOwnerId"
    ]
    """<p>The AWS account ID of the workflow owner, used for cross-account workflow sharing.</p>"""
    output_bucket_owner_id: NotRequired[
        "aws_sdk_omics.types.aws_account_id.AwsAccountId"
    ]
    """<p>The expected AWS account ID of the owner of the output S3 bucket. Can be overridden per run.</p>"""
    workflow_version_name: NotRequired[
        "aws_sdk_omics.types.workflow_version_name.WorkflowVersionName"
    ]
    """<p>The version name of the specified workflow.</p>"""
    networking_mode: NotRequired["aws_sdk_omics.types.networking_mode.NetworkingMode"]
    """<p>Optional configuration for run networking behavior. If not specified, this will default to RESTRICTED.</p>"""
    configuration_name: NotRequired[
        "aws_sdk_omics.types.configuration_name.ConfigurationName"
    ]
    """<p>Optional configuration name to use for the workflow run.</p>"""
    engine_settings: NotRequired["aws_sdk_omics.types.engine_settings.EngineSettings"]
    """<p>Engine-specific settings for the workflow run. Use this field to specify configuration options that are specific to the workflow engine (for example, Nextflow profiles).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultRunSetting) -> dict:
    out: dict = {}
    out["workflowId"] = value["workflow_id"]
    if "workflow_type" in value:
        out["workflowType"] = value["workflow_type"]
    out["roleArn"] = value["role_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "cache_id" in value:
        out["cacheId"] = value["cache_id"]
    if "cache_behavior" in value:
        out["cacheBehavior"] = value["cache_behavior"]
    if "run_group_id" in value:
        out["runGroupId"] = value["run_group_id"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    if "storage_capacity" in value:
        out["storageCapacity"] = value["storage_capacity"]
    if "output_uri" in value:
        out["outputUri"] = value["output_uri"]
    if "log_level" in value:
        out["logLevel"] = value["log_level"]
    if "run_tags" in value:
        import aws_sdk_omics.types.tag_map

        out["runTags"] = aws_sdk_omics.types.tag_map.serialize_json(value["run_tags"])
    if "retention_mode" in value:
        out["retentionMode"] = value["retention_mode"]
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "workflow_owner_id" in value:
        out["workflowOwnerId"] = value["workflow_owner_id"]
    if "output_bucket_owner_id" in value:
        out["outputBucketOwnerId"] = value["output_bucket_owner_id"]
    if "workflow_version_name" in value:
        out["workflowVersionName"] = value["workflow_version_name"]
    if "networking_mode" in value:
        out["networkingMode"] = value["networking_mode"]
    if "configuration_name" in value:
        out["configurationName"] = value["configuration_name"]
    if "engine_settings" in value:
        out["engineSettings"] = value["engine_settings"]
    return out


def deserialize_json(data: dict) -> DefaultRunSetting:
    out: DefaultRunSetting = {}  # type: ignore[typeddict-item]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError("DefaultRunSetting.workflow_id required")
    if "workflowType" in data:
        out["workflow_type"] = data["workflowType"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("DefaultRunSetting.role_arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "cacheId" in data:
        out["cache_id"] = data["cacheId"]
    if "cacheBehavior" in data:
        out["cache_behavior"] = data["cacheBehavior"]
    if "runGroupId" in data:
        out["run_group_id"] = data["runGroupId"]
    if "priority" in data:
        out["priority"] = data["priority"]
    if "parameters" in data:
        out["parameters"] = data["parameters"]
    if "storageCapacity" in data:
        out["storage_capacity"] = data["storageCapacity"]
    if "outputUri" in data:
        out["output_uri"] = data["outputUri"]
    if "logLevel" in data:
        out["log_level"] = data["logLevel"]
    if "runTags" in data:
        import aws_sdk_omics.types.tag_map

        out["run_tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["runTags"])
    if "retentionMode" in data:
        out["retention_mode"] = data["retentionMode"]
    if "storageType" in data:
        out["storage_type"] = data["storageType"]
    if "workflowOwnerId" in data:
        out["workflow_owner_id"] = data["workflowOwnerId"]
    if "outputBucketOwnerId" in data:
        out["output_bucket_owner_id"] = data["outputBucketOwnerId"]
    if "workflowVersionName" in data:
        out["workflow_version_name"] = data["workflowVersionName"]
    if "networkingMode" in data:
        out["networking_mode"] = data["networkingMode"]
    if "configurationName" in data:
        out["configuration_name"] = data["configurationName"]
    if "engineSettings" in data:
        out["engine_settings"] = data["engineSettings"]
    return out
