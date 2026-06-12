"""Generated from Smithy shape ``com.amazonaws.batch#JobDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.boolean
    import aws_sdk_batch.types.consumable_resource_properties
    import aws_sdk_batch.types.container_properties
    import aws_sdk_batch.types.ecs_properties
    import aws_sdk_batch.types.eks_properties
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.job_timeout
    import aws_sdk_batch.types.node_properties
    import aws_sdk_batch.types.orchestration_type
    import aws_sdk_batch.types.parameters_map
    import aws_sdk_batch.types.platform_capability_list
    import aws_sdk_batch.types.retry_strategy
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class JobDefinition(TypedDict):
    job_definition_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the job definition.</p>"""
    job_definition_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the job definition.</p>"""
    revision: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The revision of the job definition.</p>"""
    status: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The status of the job definition.</p>"""
    type: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The type of job definition. It's either <code>container</code> or <code>multinode</code>. If the job is run on Fargate resources, then <code>multinode</code> isn't supported. For more information about multi-node parallel jobs, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html\">Creating a multi-node parallel job definition</a> in the <i>Batch User Guide</i>.</p>"""
    scheduling_priority: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The scheduling priority of the job definition. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.</p>"""
    parameters: NotRequired["aws_sdk_batch.types.parameters_map.ParametersMap"]
    """<p>Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a <code>SubmitJob</code> request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html\">Job definition parameters</a> in the <i>Batch User Guide</i>.</p>"""
    retry_strategy: NotRequired["aws_sdk_batch.types.retry_strategy.RetryStrategy"]
    """<p>The retry strategy to use for failed jobs that are submitted with this job definition.</p>"""
    container_properties: NotRequired[
        "aws_sdk_batch.types.container_properties.ContainerProperties"
    ]
    """<p>An object with properties specific to Amazon ECS-based jobs. When <code>containerProperties</code> is used in the job definition, it can't be used in addition to <code>eksProperties</code>, <code>ecsProperties</code>, or <code>nodeProperties</code>.</p>"""
    timeout: NotRequired["aws_sdk_batch.types.job_timeout.JobTimeout"]
    """<p>The timeout time for jobs that are submitted with this job definition. After the amount of time you specify passes, Batch terminates your jobs if they aren't finished.</p>"""
    node_properties: NotRequired["aws_sdk_batch.types.node_properties.NodeProperties"]
    """<p>An object with properties that are specific to multi-node parallel jobs. When <code>nodeProperties</code> is used in the job definition, it can't be used in addition to <code>containerProperties</code>, <code>ecsProperties</code>, or <code>eksProperties</code>.</p> <note> <p>If the job runs on Fargate resources, don't specify <code>nodeProperties</code>. Use <code>containerProperties</code> instead.</p> </note>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that are applied to the job definition.</p>"""
    propagate_tags: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks when the tasks are created. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the <code>FAILED</code> state.</p>"""
    platform_capabilities: NotRequired[
        "aws_sdk_batch.types.platform_capability_list.PlatformCapabilityList"
    ]
    """<p>The platform capabilities required by the job definition. If no value is specified, it defaults to <code>EC2</code>. Jobs run on Fargate resources specify <code>FARGATE</code>.</p>"""
    ecs_properties: NotRequired["aws_sdk_batch.types.ecs_properties.EcsProperties"]
    """<p>An object that contains the properties for the Amazon ECS resources of a job.When <code>ecsProperties</code> is used in the job definition, it can't be used in addition to <code>containerProperties</code>, <code>eksProperties</code>, or <code>nodeProperties</code>.</p>"""
    eks_properties: NotRequired["aws_sdk_batch.types.eks_properties.EksProperties"]
    """<p>An object with properties that are specific to Amazon EKS-based jobs. When <code>eksProperties</code> is used in the job definition, it can't be used in addition to <code>containerProperties</code>, <code>ecsProperties</code>, or <code>nodeProperties</code>.</p>"""
    container_orchestration_type: NotRequired[
        "aws_sdk_batch.types.orchestration_type.OrchestrationType"
    ]
    """<p>The orchestration type of the compute environment. The valid values are <code>ECS</code> (default) or <code>EKS</code>.</p>"""
    consumable_resource_properties: NotRequired[
        "aws_sdk_batch.types.consumable_resource_properties.ConsumableResourceProperties"
    ]
    """<p>Contains a list of consumable resources required by the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDefinition) -> dict:
    out: dict = {}
    if "job_definition_name" in value:
        out["jobDefinitionName"] = value["job_definition_name"]
    if "job_definition_arn" in value:
        out["jobDefinitionArn"] = value["job_definition_arn"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "status" in value:
        out["status"] = value["status"]
    if "type" in value:
        out["type"] = value["type"]
    if "scheduling_priority" in value:
        out["schedulingPriority"] = value["scheduling_priority"]
    if "parameters" in value:
        import aws_sdk_batch.types.parameters_map

        out["parameters"] = aws_sdk_batch.types.parameters_map.serialize_json(
            value["parameters"]
        )
    if "retry_strategy" in value:
        import aws_sdk_batch.types.retry_strategy

        out["retryStrategy"] = aws_sdk_batch.types.retry_strategy.serialize_json(
            value["retry_strategy"]
        )
    if "container_properties" in value:
        import aws_sdk_batch.types.container_properties

        out["containerProperties"] = (
            aws_sdk_batch.types.container_properties.serialize_json(
                value["container_properties"]
            )
        )
    if "timeout" in value:
        import aws_sdk_batch.types.job_timeout

        out["timeout"] = aws_sdk_batch.types.job_timeout.serialize_json(
            value["timeout"]
        )
    if "node_properties" in value:
        import aws_sdk_batch.types.node_properties

        out["nodeProperties"] = aws_sdk_batch.types.node_properties.serialize_json(
            value["node_properties"]
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
    if "ecs_properties" in value:
        import aws_sdk_batch.types.ecs_properties

        out["ecsProperties"] = aws_sdk_batch.types.ecs_properties.serialize_json(
            value["ecs_properties"]
        )
    if "eks_properties" in value:
        import aws_sdk_batch.types.eks_properties

        out["eksProperties"] = aws_sdk_batch.types.eks_properties.serialize_json(
            value["eks_properties"]
        )
    if "container_orchestration_type" in value:
        import aws_sdk_batch.types.orchestration_type

        out["containerOrchestrationType"] = (
            aws_sdk_batch.types.orchestration_type.serialize_json(
                value["container_orchestration_type"]
            )
        )
    if "consumable_resource_properties" in value:
        import aws_sdk_batch.types.consumable_resource_properties

        out["consumableResourceProperties"] = (
            aws_sdk_batch.types.consumable_resource_properties.serialize_json(
                value["consumable_resource_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobDefinition:
    out: JobDefinition = {}  # type: ignore[typeddict-item]
    if "jobDefinitionName" in data:
        out["job_definition_name"] = data["jobDefinitionName"]
    if "jobDefinitionArn" in data:
        out["job_definition_arn"] = data["jobDefinitionArn"]
    if "revision" in data:
        out["revision"] = data["revision"]
    if "status" in data:
        out["status"] = data["status"]
    if "type" in data:
        out["type"] = data["type"]
    if "schedulingPriority" in data:
        out["scheduling_priority"] = data["schedulingPriority"]
    if "parameters" in data:
        import aws_sdk_batch.types.parameters_map

        out["parameters"] = aws_sdk_batch.types.parameters_map.deserialize_json(
            data["parameters"]
        )
    if "retryStrategy" in data:
        import aws_sdk_batch.types.retry_strategy

        out["retry_strategy"] = aws_sdk_batch.types.retry_strategy.deserialize_json(
            data["retryStrategy"]
        )
    if "containerProperties" in data:
        import aws_sdk_batch.types.container_properties

        out["container_properties"] = (
            aws_sdk_batch.types.container_properties.deserialize_json(
                data["containerProperties"]
            )
        )
    if "timeout" in data:
        import aws_sdk_batch.types.job_timeout

        out["timeout"] = aws_sdk_batch.types.job_timeout.deserialize_json(
            data["timeout"]
        )
    if "nodeProperties" in data:
        import aws_sdk_batch.types.node_properties

        out["node_properties"] = aws_sdk_batch.types.node_properties.deserialize_json(
            data["nodeProperties"]
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
    if "ecsProperties" in data:
        import aws_sdk_batch.types.ecs_properties

        out["ecs_properties"] = aws_sdk_batch.types.ecs_properties.deserialize_json(
            data["ecsProperties"]
        )
    if "eksProperties" in data:
        import aws_sdk_batch.types.eks_properties

        out["eks_properties"] = aws_sdk_batch.types.eks_properties.deserialize_json(
            data["eksProperties"]
        )
    if "containerOrchestrationType" in data:
        import aws_sdk_batch.types.orchestration_type

        out["container_orchestration_type"] = (
            aws_sdk_batch.types.orchestration_type.deserialize_json(
                data["containerOrchestrationType"]
            )
        )
    if "consumableResourceProperties" in data:
        import aws_sdk_batch.types.consumable_resource_properties

        out["consumable_resource_properties"] = (
            aws_sdk_batch.types.consumable_resource_properties.deserialize_json(
                data["consumableResourceProperties"]
            )
        )
    return out
