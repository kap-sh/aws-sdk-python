"""Generated from Smithy shape ``com.amazonaws.omics#StartRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.cache_behavior
    import aws_sdk_omics.types.configuration_name
    import aws_sdk_omics.types.engine_settings
    import aws_sdk_omics.types.networking_mode
    import aws_sdk_omics.types.numeric_id_in_arn
    import aws_sdk_omics.types.run_group_id
    import aws_sdk_omics.types.run_id
    import aws_sdk_omics.types.run_log_level
    import aws_sdk_omics.types.run_name
    import aws_sdk_omics.types.run_output_uri
    import aws_sdk_omics.types.run_parameters
    import aws_sdk_omics.types.run_request_id
    import aws_sdk_omics.types.run_retention_mode
    import aws_sdk_omics.types.run_role_arn
    import aws_sdk_omics.types.storage_type
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.workflow_id
    import aws_sdk_omics.types.workflow_owner_id
    import aws_sdk_omics.types.workflow_type
    import aws_sdk_omics.types.workflow_version_name


class StartRunRequest(TypedDict):
    workflow_id: NotRequired["aws_sdk_omics.types.workflow_id.WorkflowId"]
    """<p>The run's workflow ID. The <code>workflowId</code> is not the UUID.</p>"""
    workflow_type: NotRequired["aws_sdk_omics.types.workflow_type.WorkflowType"]
    """<p>The run's workflow type. The <code>workflowType</code> must be specified if you are running a <code>READY2RUN</code> workflow. If you are running a <code>PRIVATE</code> workflow (default), you do not need to include the workflow type. </p>"""
    run_id: NotRequired["aws_sdk_omics.types.run_id.RunId"]
    """<p>The ID of a run to duplicate.</p>"""
    role_arn: "aws_sdk_omics.types.run_role_arn.RunRoleArn"
    """<p>A service role for the run. The <code>roleArn</code> requires access to Amazon Web Services HealthOmics, S3, Cloudwatch logs, and EC2. An example <code>roleArn</code> is <code>arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ</code>. In this example, the AWS account ID is <code>123456789012</code> and the role name is <code>omics-service-role-serviceRole-W8O1XMPL7QZ</code>.</p>"""
    name: NotRequired["aws_sdk_omics.types.run_name.RunName"]
    """<p>A name for the run. This is recommended to view and organize runs in the Amazon Web Services HealthOmics console and CloudWatch logs.</p>"""
    cache_id: NotRequired["aws_sdk_omics.types.numeric_id_in_arn.NumericIdInArn"]
    """<p>Identifier of the cache associated with this run. If you don't specify a cache ID, no task outputs are cached for this run.</p>"""
    cache_behavior: NotRequired["aws_sdk_omics.types.cache_behavior.CacheBehavior"]
    r"""<p>The cache behavior for the run. You specify this value if you want to override the default behavior for the cache. You had set the default value when you created the cache. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior\">Run cache behavior</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    run_group_id: NotRequired["aws_sdk_omics.types.run_group_id.RunGroupId"]
    """<p>The run's group ID. Use a run group to cap the compute resources (and number of concurrent runs) for the runs that you add to the run group.</p>"""
    priority: NotRequired["int"]
    r"""<p>Use the run priority (highest: 1) to establish the order of runs in a run group when you start a run. If multiple runs share the same priority, the run that was initiated first will have the higher priority. Runs that do not belong to a run group can be assigned a priority. The priorities of these runs are ranked among other runs that are not in a run group. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/creating-run-groups.html#run-priority\">Run priority</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    parameters: NotRequired["aws_sdk_omics.types.run_parameters.RunParameters"]
    """<p>Parameters for the run. The run needs all required parameters and can include optional parameters. The run cannot include any parameters that are not defined in the parameter template. To retrieve parameters from the run, use the GetRun API operation.</p>"""
    storage_capacity: NotRequired["int"]
    """<p>The <code>STATIC</code> storage capacity (in gibibytes, GiB) for this run. The default run storage capacity is 1200 GiB. If your requested storage capacity is unavailable, the system rounds up the value to the nearest 1200 GiB multiple. If the requested storage capacity is still unavailable, the system rounds up the value to the nearest 2400 GiB multiple. This field is not required if the storage type is <code>DYNAMIC</code> (the system ignores any value that you enter).</p>"""
    output_uri: "aws_sdk_omics.types.run_output_uri.RunOutputUri"
    """<p>An output S3 URI for the run. The S3 bucket must be in the same region as the workflow. The role ARN must have permission to write to this S3 bucket.</p>"""
    log_level: NotRequired["aws_sdk_omics.types.run_log_level.RunLogLevel"]
    """<p>A log level for the run.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    r"""<p>Tags for the run. You can add up to 50 tags per run. For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html\">Adding a tag</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    request_id: "aws_sdk_omics.types.run_request_id.RunRequestId"
    """<p>An idempotency token used to dedupe retry requests so that duplicate runs are not created.</p>"""
    retention_mode: NotRequired[
        "aws_sdk_omics.types.run_retention_mode.RunRetentionMode"
    ]
    r"""<p>The retention mode for the run. The default value is <code>RETAIN</code>. </p> <p>Amazon Web Services HealthOmics stores a fixed number of runs that are available to the console and API. In the default mode (<code>RETAIN</code>), you need to remove runs manually when the number of run exceeds the maximum. If you set the retention mode to <code>REMOVE</code>, Amazon Web Services HealthOmics automatically removes runs (that have mode set to <code>REMOVE</code>) when the number of run exceeds the maximum. All run logs are available in CloudWatch logs, if you need information about a run that is no longer available to the API.</p> <p>For more information about retention mode, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html\">Specifying run retention mode</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    storage_type: NotRequired["aws_sdk_omics.types.storage_type.StorageType"]
    r"""<p>The storage type for the run. If you set the storage type to <code>DYNAMIC</code>, Amazon Web Services HealthOmics dynamically scales the storage up or down, based on file system utilization. By default, the run uses <code>STATIC</code> storage type, which allocates a fixed amount of storage. For more information about <code>DYNAMIC</code> and <code>STATIC</code> storage, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html\">Run storage types</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    workflow_owner_id: NotRequired[
        "aws_sdk_omics.types.workflow_owner_id.WorkflowOwnerId"
    ]
    """<p>The 12-digit account ID of the workflow owner that is used for running a shared workflow. The workflow owner ID can be retrieved using the <code>GetShare</code> API operation. If you are the workflow owner, you do not need to include this ID.</p>"""
    workflow_version_name: NotRequired[
        "aws_sdk_omics.types.workflow_version_name.WorkflowVersionName"
    ]
    r"""<p>The name of the workflow version. Use workflow versions to track and organize changes to the workflow. If your workflow has multiple versions, the run uses the default version unless you specify a version name. To learn more, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html\">Workflow versioning</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    networking_mode: NotRequired["aws_sdk_omics.types.networking_mode.NetworkingMode"]
    """<p>Optional configuration for run networking behavior. If not specified, this will default to RESTRICTED.</p>"""
    configuration_name: NotRequired[
        "aws_sdk_omics.types.configuration_name.ConfigurationName"
    ]
    """<p>Optional configuration name to use for the workflow run.</p>"""
    engine_settings: NotRequired["aws_sdk_omics.types.engine_settings.EngineSettings"]
    """<p>Engine-specific settings for the workflow run. Use this field to specify configuration options that are specific to the workflow engine (for example, Nextflow profiles).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRunRequest) -> dict:
    out: dict = {}
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "workflow_type" in value:
        out["workflowType"] = value["workflow_type"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
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
    out["outputUri"] = value["output_uri"]
    if "log_level" in value:
        out["logLevel"] = value["log_level"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    out["requestId"] = value["request_id"]
    if "retention_mode" in value:
        out["retentionMode"] = value["retention_mode"]
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "workflow_owner_id" in value:
        out["workflowOwnerId"] = value["workflow_owner_id"]
    if "workflow_version_name" in value:
        out["workflowVersionName"] = value["workflow_version_name"]
    if "networking_mode" in value:
        out["networkingMode"] = value["networking_mode"]
    if "configuration_name" in value:
        out["configurationName"] = value["configuration_name"]
    if "engine_settings" in value:
        out["engineSettings"] = value["engine_settings"]
    return out


def deserialize_json(data: dict) -> StartRunRequest:
    out: StartRunRequest = {}  # type: ignore[typeddict-item]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    if "workflowType" in data:
        out["workflow_type"] = data["workflowType"]
    if "runId" in data:
        out["run_id"] = data["runId"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("StartRunRequest.role_arn required")
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
    else:
        raise DeserializationError("StartRunRequest.output_uri required")
    if "logLevel" in data:
        out["log_level"] = data["logLevel"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("StartRunRequest.request_id required")
    if "retentionMode" in data:
        out["retention_mode"] = data["retentionMode"]
    if "storageType" in data:
        out["storage_type"] = data["storageType"]
    if "workflowOwnerId" in data:
        out["workflow_owner_id"] = data["workflowOwnerId"]
    if "workflowVersionName" in data:
        out["workflow_version_name"] = data["workflowVersionName"]
    if "networkingMode" in data:
        out["networking_mode"] = data["networkingMode"]
    if "configurationName" in data:
        out["configuration_name"] = data["configurationName"]
    if "engineSettings" in data:
        out["engine_settings"] = data["engineSettings"]
    return out
