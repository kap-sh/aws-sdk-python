"""Generated from Smithy shape ``com.amazonaws.batch#JobDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.array_properties_detail
    import aws_sdk_batch.types.attempt_details
    import aws_sdk_batch.types.boolean
    import aws_sdk_batch.types.consumable_resource_properties
    import aws_sdk_batch.types.container_detail
    import aws_sdk_batch.types.ecs_properties_detail
    import aws_sdk_batch.types.eks_attempt_details
    import aws_sdk_batch.types.eks_properties_detail
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.job_dependency_list
    import aws_sdk_batch.types.job_status
    import aws_sdk_batch.types.job_timeout
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.node_details
    import aws_sdk_batch.types.node_properties
    import aws_sdk_batch.types.parameters_map
    import aws_sdk_batch.types.platform_capability_list
    import aws_sdk_batch.types.retry_strategy
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class JobDetail(TypedDict):
    job_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The job name.</p>"""
    job_id: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The job ID.</p>"""
    job_queue: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job queue that the job is associated with.</p>"""
    status: NotRequired["aws_sdk_batch.types.job_status.JobStatus"]
    r"""<p>The current status for the job.</p> <note> <p>If your jobs don't progress to <code>STARTING</code>, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#job_stuck_in_runnable\">Jobs stuck in RUNNABLE status</a> in the troubleshooting section of the <i>Batch User Guide</i>.</p> </note>"""
    share_identifier: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The share identifier for the job.</p>"""
    scheduling_priority: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The scheduling policy of the job definition. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.</p>"""
    attempts: NotRequired["aws_sdk_batch.types.attempt_details.AttemptDetails"]
    """<p>A list of job attempts that are associated with this job.</p>"""
    status_reason: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A short, human-readable string to provide more details for the current status of the job.</p> <ul> <li> <p> <code>CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY</code> - All compute environments have insufficient capacity to service the job.</p> </li> <li> <p> <code>MISCONFIGURATION:COMPUTE_ENVIRONMENT_MAX_RESOURCE</code> - All compute environments have a <code>maxVcpu</code> setting that is smaller than the job requirements.</p> </li> <li> <p> <code>MISCONFIGURATION:JOB_RESOURCE_REQUIREMENT</code> - All compute environments have no connected instances that meet the job requirements.</p> </li> <li> <p> <code>MISCONFIGURATION:SERVICE_ROLE_PERMISSIONS</code> - All compute environments have problems with the service role permissions.</p> </li> </ul>"""
    created_at: NotRequired["aws_sdk_batch.types.long.Long"]
    r"""<p>The Unix timestamp (in milliseconds) for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the <code>SUBMITTED</code> state. This is specifically at the time <a href=\"https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html\">SubmitJob</a> was called. For array child jobs, this is when the child job was spawned by its parent and entered the <code>PENDING</code> state.</p>"""
    retry_strategy: NotRequired["aws_sdk_batch.types.retry_strategy.RetryStrategy"]
    """<p>The retry strategy to use for this job if an attempt fails.</p>"""
    started_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the job was started. More specifically, it's when the job transitioned from the <code>STARTING</code> state to the <code>RUNNING</code> state. </p>"""
    stopped_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the job was stopped. More specifically, it's when the job transitioned from the <code>RUNNING</code> state to a terminal state, such as <code>SUCCEEDED</code> or <code>FAILED</code>.</p>"""
    depends_on: NotRequired["aws_sdk_batch.types.job_dependency_list.JobDependencyList"]
    """<p>A list of job IDs that this job depends on.</p>"""
    job_definition: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job definition that this job uses.</p>"""
    parameters: NotRequired["aws_sdk_batch.types.parameters_map.ParametersMap"]
    """<p>Additional parameters that are passed to the job that replace parameter substitution placeholders or override any corresponding parameter defaults from the job definition.</p>"""
    container: NotRequired["aws_sdk_batch.types.container_detail.ContainerDetail"]
    """<p>An object that represents the details for the container that's associated with the job. If the details are for a multiple-container job, this object will be empty. </p>"""
    node_details: NotRequired["aws_sdk_batch.types.node_details.NodeDetails"]
    """<p>An object that represents the details of a node that's associated with a multi-node parallel job.</p>"""
    node_properties: NotRequired["aws_sdk_batch.types.node_properties.NodeProperties"]
    """<p>An object that represents the node properties of a multi-node parallel job.</p> <note> <p>This isn't applicable to jobs that are running on Fargate resources.</p> </note>"""
    array_properties: NotRequired[
        "aws_sdk_batch.types.array_properties_detail.ArrayPropertiesDetail"
    ]
    """<p>The array properties of the job, if it's an array job.</p>"""
    timeout: NotRequired["aws_sdk_batch.types.job_timeout.JobTimeout"]
    """<p>The timeout configuration for the job.</p>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that are applied to the job.</p>"""
    propagate_tags: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks when the tasks are created. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the <code>FAILED</code> state.</p>"""
    platform_capabilities: NotRequired[
        "aws_sdk_batch.types.platform_capability_list.PlatformCapabilityList"
    ]
    """<p>The platform capabilities required by the job definition. If no value is specified, it defaults to <code>EC2</code>. Jobs run on Fargate resources specify <code>FARGATE</code>.</p>"""
    eks_properties: NotRequired[
        "aws_sdk_batch.types.eks_properties_detail.EksPropertiesDetail"
    ]
    """<p>An object with various properties that are specific to Amazon EKS based jobs. </p>"""
    eks_attempts: NotRequired[
        "aws_sdk_batch.types.eks_attempt_details.EksAttemptDetails"
    ]
    """<p>A list of job attempts that are associated with this job.</p>"""
    ecs_properties: NotRequired[
        "aws_sdk_batch.types.ecs_properties_detail.EcsPropertiesDetail"
    ]
    """<p>An object with properties that are specific to Amazon ECS-based jobs. </p>"""
    is_cancelled: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>Indicates whether the job is canceled.</p>"""
    is_terminated: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>Indicates whether the job is terminated.</p>"""
    consumable_resource_properties: NotRequired[
        "aws_sdk_batch.types.consumable_resource_properties.ConsumableResourceProperties"
    ]
    """<p>Contains a list of consumable resources required by the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDetail) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
    if "status" in value:
        import aws_sdk_batch.types.job_status

        out["status"] = aws_sdk_batch.types.job_status.serialize_json(value["status"])
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "scheduling_priority" in value:
        out["schedulingPriority"] = value["scheduling_priority"]
    if "attempts" in value:
        import aws_sdk_batch.types.attempt_details

        out["attempts"] = aws_sdk_batch.types.attempt_details.serialize_json(
            value["attempts"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "retry_strategy" in value:
        import aws_sdk_batch.types.retry_strategy

        out["retryStrategy"] = aws_sdk_batch.types.retry_strategy.serialize_json(
            value["retry_strategy"]
        )
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    if "stopped_at" in value:
        out["stoppedAt"] = value["stopped_at"]
    if "depends_on" in value:
        import aws_sdk_batch.types.job_dependency_list

        out["dependsOn"] = aws_sdk_batch.types.job_dependency_list.serialize_json(
            value["depends_on"]
        )
    if "job_definition" in value:
        out["jobDefinition"] = value["job_definition"]
    if "parameters" in value:
        import aws_sdk_batch.types.parameters_map

        out["parameters"] = aws_sdk_batch.types.parameters_map.serialize_json(
            value["parameters"]
        )
    if "container" in value:
        import aws_sdk_batch.types.container_detail

        out["container"] = aws_sdk_batch.types.container_detail.serialize_json(
            value["container"]
        )
    if "node_details" in value:
        import aws_sdk_batch.types.node_details

        out["nodeDetails"] = aws_sdk_batch.types.node_details.serialize_json(
            value["node_details"]
        )
    if "node_properties" in value:
        import aws_sdk_batch.types.node_properties

        out["nodeProperties"] = aws_sdk_batch.types.node_properties.serialize_json(
            value["node_properties"]
        )
    if "array_properties" in value:
        import aws_sdk_batch.types.array_properties_detail

        out["arrayProperties"] = (
            aws_sdk_batch.types.array_properties_detail.serialize_json(
                value["array_properties"]
            )
        )
    if "timeout" in value:
        import aws_sdk_batch.types.job_timeout

        out["timeout"] = aws_sdk_batch.types.job_timeout.serialize_json(
            value["timeout"]
        )
    if "tags" in value:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.serialize_json(value["tags"])
    if "propagate_tags" in value:
        out["propagateTags"] = value["propagate_tags"]
    if "platform_capabilities" in value:
        import aws_sdk_batch.types.platform_capability_list

        out["platformCapabilities"] = (
            aws_sdk_batch.types.platform_capability_list.serialize_json(
                value["platform_capabilities"]
            )
        )
    if "eks_properties" in value:
        import aws_sdk_batch.types.eks_properties_detail

        out["eksProperties"] = aws_sdk_batch.types.eks_properties_detail.serialize_json(
            value["eks_properties"]
        )
    if "eks_attempts" in value:
        import aws_sdk_batch.types.eks_attempt_details

        out["eksAttempts"] = aws_sdk_batch.types.eks_attempt_details.serialize_json(
            value["eks_attempts"]
        )
    if "ecs_properties" in value:
        import aws_sdk_batch.types.ecs_properties_detail

        out["ecsProperties"] = aws_sdk_batch.types.ecs_properties_detail.serialize_json(
            value["ecs_properties"]
        )
    if "is_cancelled" in value:
        out["isCancelled"] = value["is_cancelled"]
    if "is_terminated" in value:
        out["isTerminated"] = value["is_terminated"]
    if "consumable_resource_properties" in value:
        import aws_sdk_batch.types.consumable_resource_properties

        out["consumableResourceProperties"] = (
            aws_sdk_batch.types.consumable_resource_properties.serialize_json(
                value["consumable_resource_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobDetail:
    out: JobDetail = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobQueue" in data:
        out["job_queue"] = data["jobQueue"]
    if "status" in data:
        import aws_sdk_batch.types.job_status

        out["status"] = aws_sdk_batch.types.job_status.deserialize_json(data["status"])
    if "shareIdentifier" in data:
        out["share_identifier"] = data["shareIdentifier"]
    if "schedulingPriority" in data:
        out["scheduling_priority"] = data["schedulingPriority"]
    if "attempts" in data:
        import aws_sdk_batch.types.attempt_details

        out["attempts"] = aws_sdk_batch.types.attempt_details.deserialize_json(
            data["attempts"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "retryStrategy" in data:
        import aws_sdk_batch.types.retry_strategy

        out["retry_strategy"] = aws_sdk_batch.types.retry_strategy.deserialize_json(
            data["retryStrategy"]
        )
    if "startedAt" in data:
        out["started_at"] = data["startedAt"]
    if "stoppedAt" in data:
        out["stopped_at"] = data["stoppedAt"]
    if "dependsOn" in data:
        import aws_sdk_batch.types.job_dependency_list

        out["depends_on"] = aws_sdk_batch.types.job_dependency_list.deserialize_json(
            data["dependsOn"]
        )
    if "jobDefinition" in data:
        out["job_definition"] = data["jobDefinition"]
    if "parameters" in data:
        import aws_sdk_batch.types.parameters_map

        out["parameters"] = aws_sdk_batch.types.parameters_map.deserialize_json(
            data["parameters"]
        )
    if "container" in data:
        import aws_sdk_batch.types.container_detail

        out["container"] = aws_sdk_batch.types.container_detail.deserialize_json(
            data["container"]
        )
    if "nodeDetails" in data:
        import aws_sdk_batch.types.node_details

        out["node_details"] = aws_sdk_batch.types.node_details.deserialize_json(
            data["nodeDetails"]
        )
    if "nodeProperties" in data:
        import aws_sdk_batch.types.node_properties

        out["node_properties"] = aws_sdk_batch.types.node_properties.deserialize_json(
            data["nodeProperties"]
        )
    if "arrayProperties" in data:
        import aws_sdk_batch.types.array_properties_detail

        out["array_properties"] = (
            aws_sdk_batch.types.array_properties_detail.deserialize_json(
                data["arrayProperties"]
            )
        )
    if "timeout" in data:
        import aws_sdk_batch.types.job_timeout

        out["timeout"] = aws_sdk_batch.types.job_timeout.deserialize_json(
            data["timeout"]
        )
    if "tags" in data:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    if "propagateTags" in data:
        out["propagate_tags"] = data["propagateTags"]
    if "platformCapabilities" in data:
        import aws_sdk_batch.types.platform_capability_list

        out["platform_capabilities"] = (
            aws_sdk_batch.types.platform_capability_list.deserialize_json(
                data["platformCapabilities"]
            )
        )
    if "eksProperties" in data:
        import aws_sdk_batch.types.eks_properties_detail

        out["eks_properties"] = (
            aws_sdk_batch.types.eks_properties_detail.deserialize_json(
                data["eksProperties"]
            )
        )
    if "eksAttempts" in data:
        import aws_sdk_batch.types.eks_attempt_details

        out["eks_attempts"] = aws_sdk_batch.types.eks_attempt_details.deserialize_json(
            data["eksAttempts"]
        )
    if "ecsProperties" in data:
        import aws_sdk_batch.types.ecs_properties_detail

        out["ecs_properties"] = (
            aws_sdk_batch.types.ecs_properties_detail.deserialize_json(
                data["ecsProperties"]
            )
        )
    if "isCancelled" in data:
        out["is_cancelled"] = data["isCancelled"]
    if "isTerminated" in data:
        out["is_terminated"] = data["isTerminated"]
    if "consumableResourceProperties" in data:
        import aws_sdk_batch.types.consumable_resource_properties

        out["consumable_resource_properties"] = (
            aws_sdk_batch.types.consumable_resource_properties.deserialize_json(
                data["consumableResourceProperties"]
            )
        )
    return out
