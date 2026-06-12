"""Generated from Smithy shape ``com.amazonaws.batch#RegisterJobDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.boolean
    import aws_sdk_batch.types.consumable_resource_properties
    import aws_sdk_batch.types.container_properties
    import aws_sdk_batch.types.ecs_properties
    import aws_sdk_batch.types.eks_properties
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.job_definition_type
    import aws_sdk_batch.types.job_timeout
    import aws_sdk_batch.types.node_properties
    import aws_sdk_batch.types.parameters_map
    import aws_sdk_batch.types.platform_capability_list
    import aws_sdk_batch.types.retry_strategy
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class RegisterJobDefinitionRequest(TypedDict):
    job_definition_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the job definition to register. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>"""
    type: NotRequired["aws_sdk_batch.types.job_definition_type.JobDefinitionType"]
    """<p>The type of job definition. For more information about multi-node parallel jobs, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html\">Creating a multi-node parallel job definition</a> in the <i>Batch User Guide</i>.</p> <ul> <li> <p>If the value is <code>container</code>, then one of the following is required: <code>containerProperties</code>, <code>ecsProperties</code>, or <code>eksProperties</code>.</p> </li> <li> <p>If the value is <code>multinode</code>, then <code>nodeProperties</code> is required.</p> </li> </ul> <note> <p>If the job is run on Fargate resources, then <code>multinode</code> isn't supported.</p> </note>"""
    parameters: NotRequired["aws_sdk_batch.types.parameters_map.ParametersMap"]
    """<p>Default parameter substitution placeholders to set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a <code>SubmitJob</code> request override any corresponding parameter defaults from the job definition.</p>"""
    scheduling_priority: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The scheduling priority for jobs that are submitted with this job definition. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.</p> <p>The minimum supported value is 0 and the maximum supported value is 9999.</p>"""
    container_properties: NotRequired[
        "aws_sdk_batch.types.container_properties.ContainerProperties"
    ]
    """<p>An object with properties specific to Amazon ECS-based single-node container-based jobs. If the job definition's <code>type</code> parameter is <code>container</code>, then you must specify either <code>containerProperties</code> or <code>nodeProperties</code>. This must not be specified for Amazon EKS-based job definitions.</p> <note> <p>If the job runs on Fargate resources, then you must not specify <code>nodeProperties</code>; use only <code>containerProperties</code>.</p> </note>"""
    node_properties: NotRequired["aws_sdk_batch.types.node_properties.NodeProperties"]
    """<p>An object with properties specific to multi-node parallel jobs. If you specify node properties for a job, it becomes a multi-node parallel job. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/multi-node-parallel-jobs.html\">Multi-node Parallel Jobs</a> in the <i>Batch User Guide</i>.</p> <note> <p>If the job runs on Fargate resources, then you must not specify <code>nodeProperties</code>; use <code>containerProperties</code> instead.</p> </note> <note> <p>If the job runs on Amazon EKS resources, then you must not specify <code>nodeProperties</code>.</p> </note>"""
    retry_strategy: NotRequired["aws_sdk_batch.types.retry_strategy.RetryStrategy"]
    """<p>The retry strategy to use for failed jobs that are submitted with this job definition. Any retry strategy that's specified during a <a>SubmitJob</a> operation overrides the retry strategy defined here. If a job is terminated due to a timeout, it isn't retried.</p>"""
    propagate_tags: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags are not propagated. Tags can only be propagated to the tasks during task creation. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the <code>FAILED</code> state.</p> <note> <p>If the job runs on Amazon EKS resources, then you must not specify <code>propagateTags</code>.</p> </note>"""
    timeout: NotRequired["aws_sdk_batch.types.job_timeout.JobTimeout"]
    """<p>The timeout configuration for jobs that are submitted with this job definition, after which Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout, it isn't retried. The minimum value for the timeout is 60 seconds. Any timeout configuration that's specified during a <a>SubmitJob</a> operation overrides the timeout configuration defined here. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/job_timeouts.html\">Job Timeouts</a> in the <i>Batch User Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that you apply to the job definition to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html\">Tagging Amazon Web Services Resources</a> in <i>Batch User Guide</i>.</p>"""
    platform_capabilities: NotRequired[
        "aws_sdk_batch.types.platform_capability_list.PlatformCapabilityList"
    ]
    """<p>The platform capabilities required by the job definition. If no value is specified, it defaults to <code>EC2</code>. To run the job on Fargate resources, specify <code>FARGATE</code>.</p> <note> <p>If the job runs on Amazon EKS resources, then you must not specify <code>platformCapabilities</code>.</p> </note>"""
    eks_properties: NotRequired["aws_sdk_batch.types.eks_properties.EksProperties"]
    """<p>An object with properties that are specific to Amazon EKS-based jobs. This must not be specified for Amazon ECS based job definitions.</p>"""
    ecs_properties: NotRequired["aws_sdk_batch.types.ecs_properties.EcsProperties"]
    """<p>An object with properties that are specific to Amazon ECS-based jobs. This must not be specified for Amazon EKS-based job definitions.</p>"""
    consumable_resource_properties: NotRequired[
        "aws_sdk_batch.types.consumable_resource_properties.ConsumableResourceProperties"
    ]
    """<p>Contains a list of consumable resources required by the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterJobDefinitionRequest) -> dict:
    out: dict = {}
    if "job_definition_name" in value:
        out["jobDefinitionName"] = value["job_definition_name"]
    if "type" in value:
        import aws_sdk_batch.types.job_definition_type

        out["type"] = aws_sdk_batch.types.job_definition_type.serialize_json(
            value["type"]
        )
    if "parameters" in value:
        import aws_sdk_batch.types.parameters_map

        out["parameters"] = aws_sdk_batch.types.parameters_map.serialize_json(
            value["parameters"]
        )
    if "scheduling_priority" in value:
        out["schedulingPriority"] = value["scheduling_priority"]
    if "container_properties" in value:
        import aws_sdk_batch.types.container_properties

        out["containerProperties"] = (
            aws_sdk_batch.types.container_properties.serialize_json(
                value["container_properties"]
            )
        )
    if "node_properties" in value:
        import aws_sdk_batch.types.node_properties

        out["nodeProperties"] = aws_sdk_batch.types.node_properties.serialize_json(
            value["node_properties"]
        )
    if "retry_strategy" in value:
        import aws_sdk_batch.types.retry_strategy

        out["retryStrategy"] = aws_sdk_batch.types.retry_strategy.serialize_json(
            value["retry_strategy"]
        )
    if "propagate_tags" in value:
        out["propagateTags"] = value["propagate_tags"]
    if "timeout" in value:
        import aws_sdk_batch.types.job_timeout

        out["timeout"] = aws_sdk_batch.types.job_timeout.serialize_json(
            value["timeout"]
        )
    if "tags" in value:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.serialize_json(value["tags"])
    if "platform_capabilities" in value:
        import aws_sdk_batch.types.platform_capability_list

        out["platformCapabilities"] = (
            aws_sdk_batch.types.platform_capability_list.serialize_json(
                value["platform_capabilities"]
            )
        )
    if "eks_properties" in value:
        import aws_sdk_batch.types.eks_properties

        out["eksProperties"] = aws_sdk_batch.types.eks_properties.serialize_json(
            value["eks_properties"]
        )
    if "ecs_properties" in value:
        import aws_sdk_batch.types.ecs_properties

        out["ecsProperties"] = aws_sdk_batch.types.ecs_properties.serialize_json(
            value["ecs_properties"]
        )
    if "consumable_resource_properties" in value:
        import aws_sdk_batch.types.consumable_resource_properties

        out["consumableResourceProperties"] = (
            aws_sdk_batch.types.consumable_resource_properties.serialize_json(
                value["consumable_resource_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisterJobDefinitionRequest:
    out: RegisterJobDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "jobDefinitionName" in data:
        out["job_definition_name"] = data["jobDefinitionName"]
    if "type" in data:
        import aws_sdk_batch.types.job_definition_type

        out["type"] = aws_sdk_batch.types.job_definition_type.deserialize_json(
            data["type"]
        )
    if "parameters" in data:
        import aws_sdk_batch.types.parameters_map

        out["parameters"] = aws_sdk_batch.types.parameters_map.deserialize_json(
            data["parameters"]
        )
    if "schedulingPriority" in data:
        out["scheduling_priority"] = data["schedulingPriority"]
    if "containerProperties" in data:
        import aws_sdk_batch.types.container_properties

        out["container_properties"] = (
            aws_sdk_batch.types.container_properties.deserialize_json(
                data["containerProperties"]
            )
        )
    if "nodeProperties" in data:
        import aws_sdk_batch.types.node_properties

        out["node_properties"] = aws_sdk_batch.types.node_properties.deserialize_json(
            data["nodeProperties"]
        )
    if "retryStrategy" in data:
        import aws_sdk_batch.types.retry_strategy

        out["retry_strategy"] = aws_sdk_batch.types.retry_strategy.deserialize_json(
            data["retryStrategy"]
        )
    if "propagateTags" in data:
        out["propagate_tags"] = data["propagateTags"]
    if "timeout" in data:
        import aws_sdk_batch.types.job_timeout

        out["timeout"] = aws_sdk_batch.types.job_timeout.deserialize_json(
            data["timeout"]
        )
    if "tags" in data:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    if "platformCapabilities" in data:
        import aws_sdk_batch.types.platform_capability_list

        out["platform_capabilities"] = (
            aws_sdk_batch.types.platform_capability_list.deserialize_json(
                data["platformCapabilities"]
            )
        )
    if "eksProperties" in data:
        import aws_sdk_batch.types.eks_properties

        out["eks_properties"] = aws_sdk_batch.types.eks_properties.deserialize_json(
            data["eksProperties"]
        )
    if "ecsProperties" in data:
        import aws_sdk_batch.types.ecs_properties

        out["ecs_properties"] = aws_sdk_batch.types.ecs_properties.deserialize_json(
            data["ecsProperties"]
        )
    if "consumableResourceProperties" in data:
        import aws_sdk_batch.types.consumable_resource_properties

        out["consumable_resource_properties"] = (
            aws_sdk_batch.types.consumable_resource_properties.deserialize_json(
                data["consumableResourceProperties"]
            )
        )
    return out
