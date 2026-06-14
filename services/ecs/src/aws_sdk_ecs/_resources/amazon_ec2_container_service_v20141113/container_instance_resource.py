from typing import TYPE_CHECKING, Optional

from aws_sdk_ecs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attributes
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.container_instance_field_list
    import aws_sdk_ecs.types.container_instance_status
    import aws_sdk_ecs.types.delete_attributes_request
    import aws_sdk_ecs.types.delete_attributes_response
    import aws_sdk_ecs.types.describe_container_instances_request
    import aws_sdk_ecs.types.describe_container_instances_response
    import aws_sdk_ecs.types.desired_status
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.list_tasks_request
    import aws_sdk_ecs.types.list_tasks_response
    import aws_sdk_ecs.types.platform_devices
    import aws_sdk_ecs.types.put_attributes_request
    import aws_sdk_ecs.types.put_attributes_response
    import aws_sdk_ecs.types.register_container_instance_request
    import aws_sdk_ecs.types.register_container_instance_response
    import aws_sdk_ecs.types.resources
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list
    import aws_sdk_ecs.types.tags
    import aws_sdk_ecs.types.update_container_agent_request
    import aws_sdk_ecs.types.update_container_agent_response
    import aws_sdk_ecs.types.update_container_instances_state_request
    import aws_sdk_ecs.types.update_container_instances_state_response
    import aws_sdk_ecs.types.version_info
    from aws_sdk_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from aws_sdk_ecs._services.ecs import ECSClient, ECSClientConfig


class ContainerInstanceResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def delete_attributes(
        self,
        attributes: "aws_sdk_ecs.types.attributes.Attributes",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.delete_attributes_response.DeleteAttributesResponse":
        """<p>Deletes one or more custom attributes from an Amazon ECS resource.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to delete attributes. If you do not specify a cluster, the default cluster is assumed.</p>
            attributes: <p>The attributes to delete from your resource. You can specify up to 10 attributes for each request. For custom attributes, specify the attribute name and target ID, but don't specify the value. If you specify the target ID using the short form, you must also specify the target type.</p>

        Examples:
            To delete a custom attribute from an Amazon ECS instance
            This example deletes an attribute named stack from a container instance.

            >>> client.delete_attributes(attributes=[{'name': 'stack', 'targetId': 'aws:ecs:us-west-2:130757420319:container-instance/1c3be8ed-df30-47b4-8f1e-6e68ebd01f34'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.delete_attributes_request.DeleteAttributesRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.delete_attributes_response.DeleteAttributesResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_attributes

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_attributes.delete_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.delete_attributes_request.DeleteAttributesRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        input_["attributes"] = attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_container_instances(
        self,
        container_instances: "aws_sdk_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        include: Optional[
            "aws_sdk_ecs.types.container_instance_field_list.ContainerInstanceFieldList"
        ] = None,
    ) -> "aws_sdk_ecs.types.describe_container_instances_response.DescribeContainerInstancesResponse":
        """<p>Describes one or more container instances. Returns metadata about each container instance requested.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the container instance or container instances you are describing were launched in any cluster other than the default cluster.</p>
            container_instances: <p>A list of up to 100 container instance IDs or full Amazon Resource Name (ARN) entries.</p>
            include: <p>Specifies whether you want to see the resource tags for the container instance. If <code>TAGS</code> is specified, the tags are included in the response. If <code>CONTAINER_INSTANCE_HEALTH</code> is specified, the container instance health is included in the response. If this field is omitted, tags and container instance health status aren't included in the response.</p>

        Examples:
            To describe container instance
            This example provides a description of the specified container instance in your default region, using the container instance UUID as an identifier.

            >>> client.describe_container_instances(cluster='default', container_instances=['f2756532-8f13-4d53-87c9-aed50dc94cd7'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.describe_container_instances_request.DescribeContainerInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.describe_container_instances_response.DescribeContainerInstancesResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_container_instances

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_container_instances.describe_container_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.describe_container_instances_request.DescribeContainerInstancesRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        input_["container_instances"] = container_instances
        if include is not None:
            input_["include"] = include

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tasks(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        container_instance: Optional["aws_sdk_ecs.types.string.String"] = None,
        family: Optional["aws_sdk_ecs.types.string.String"] = None,
        next_token: Optional["aws_sdk_ecs.types.string.String"] = None,
        max_results: Optional["aws_sdk_ecs.types.boxed_integer.BoxedInteger"] = None,
        started_by: Optional["aws_sdk_ecs.types.string.String"] = None,
        service_name: Optional["aws_sdk_ecs.types.string.String"] = None,
        desired_status: Optional[
            "aws_sdk_ecs.types.desired_status.DesiredStatus"
        ] = None,
        launch_type: Optional["aws_sdk_ecs.types.launch_type.LaunchType"] = None,
        daemon_name: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.list_tasks_response.ListTasksResponse":
        """<p>Returns a list of tasks. You can filter the results by cluster, task definition family, container instance, launch type, what IAM principal started the task, or by the desired status of the task.</p> <p>Recently stopped tasks might appear in the returned results. </p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the <code>ListTasks</code> results. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instance: <p>The container instance ID or full ARN of the container instance to use when filtering the <code>ListTasks</code> results. Specifying a <code>containerInstance</code> limits the results to tasks that belong to that container instance.</p>
            family: <p>The name of the task definition family to use when filtering the <code>ListTasks</code> results. Specifying a <code>family</code> limits the results to tasks that belong to that family.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListTasks</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of task results that <code>ListTasks</code> returned in paginated output. When this parameter is used, <code>ListTasks</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListTasks</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListTasks</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            started_by: <p>The <code>startedBy</code> value to filter the task results with. Specifying a <code>startedBy</code> value limits the results to tasks that were started with that value.</p> <p>When you specify <code>startedBy</code> as the filter, it must be the only filter that you use.</p>
            service_name: <p>The name of the service to use when filtering the <code>ListTasks</code> results. Specifying a <code>serviceName</code> limits the results to tasks that belong to that service.</p>
            desired_status: <p>The task desired status to use when filtering the <code>ListTasks</code> results. Specifying a <code>desiredStatus</code> of <code>STOPPED</code> limits the results to tasks that Amazon ECS has set the desired status to <code>STOPPED</code>. This can be useful for debugging tasks that aren't starting properly or have died or finished. The default status filter is <code>RUNNING</code>, which shows tasks that Amazon ECS has set the desired status to <code>RUNNING</code>.</p> <note> <p>Although you can filter results based on a desired status of <code>PENDING</code>, this doesn't return any results. Amazon ECS never sets the desired status of a task to that value (only a task's <code>lastStatus</code> may have a value of <code>PENDING</code>).</p> </note>
            launch_type: <p>The launch type to use when filtering the <code>ListTasks</code> results.</p>
            daemon_name: <p>The name of the daemon to use when filtering the <code>ListTasks</code> results. Specifying a <code>daemonName</code> limits the results to tasks that belong to that daemon.</p>

        Examples:
            To list the tasks in a cluster
            This example lists all of the tasks in a cluster.

            >>> client.list_tasks(cluster='default')
            To list the tasks on a particular container instance
            This example lists the tasks of a specified container instance. Specifying a ``containerInstance`` value limits  the  results  to  tasks  that belong to that container instance.

            >>> client.list_tasks(cluster='default', container_instance='f6bbb147-5370-4ace-8c73-c7181ded911f')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.list_tasks_request.ListTasksRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.list_tasks_response.ListTasksResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.list_tasks

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.list_tasks.list_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.list_tasks_request.ListTasksRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        if container_instance is not None:
            input_["container_instance"] = container_instance
        if family is not None:
            input_["family"] = family
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if started_by is not None:
            input_["started_by"] = started_by
        if service_name is not None:
            input_["service_name"] = service_name
        if desired_status is not None:
            input_["desired_status"] = desired_status
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if daemon_name is not None:
            input_["daemon_name"] = daemon_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_attributes(
        self,
        attributes: "aws_sdk_ecs.types.attributes.Attributes",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.put_attributes_response.PutAttributesResponse":
        """<p>Create or update an attribute on an Amazon ECS resource. If the attribute doesn't exist, it's created. If the attribute exists, its value is replaced with the specified value. To delete an attribute, use <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteAttributes.html\">DeleteAttributes</a>. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes\">Attributes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to apply attributes. If you do not specify a cluster, the default cluster is assumed.</p>
            attributes: <p>The attributes to apply to your resource. You can specify up to 10 custom attributes for each resource. You can specify up to 10 attributes in a single call.</p>

        Examples:
            To create or update an attribute on a resource
            This example adds an attribute "stack" with the value "production" to a container instance.

            >>> client.put_attributes(cluster='MyCluster', attributes=[{'targetId': 'arn:aws:ecs:us-west-2:123456789012:container-instance/1c3be8ed-df30-47b4-8f1e-6e68ebd01f34', 'name': 'stack', 'value': 'production'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.put_attributes_request.PutAttributesRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.put_attributes_response.PutAttributesResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.put_attributes

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.put_attributes.put_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.put_attributes_request.PutAttributesRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        input_["attributes"] = attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_container_instance(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        instance_identity_document: Optional["aws_sdk_ecs.types.string.String"] = None,
        instance_identity_document_signature: Optional[
            "aws_sdk_ecs.types.string.String"
        ] = None,
        total_resources: Optional["aws_sdk_ecs.types.resources.Resources"] = None,
        version_info: Optional["aws_sdk_ecs.types.version_info.VersionInfo"] = None,
        container_instance_arn: Optional["aws_sdk_ecs.types.string.String"] = None,
        attributes: Optional["aws_sdk_ecs.types.attributes.Attributes"] = None,
        platform_devices: Optional[
            "aws_sdk_ecs.types.platform_devices.PlatformDevices"
        ] = None,
        tags: Optional["aws_sdk_ecs.types.tags.Tags"] = None,
    ) -> "aws_sdk_ecs.types.register_container_instance_response.RegisterContainerInstanceResponse":
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to register your container instance with. If you do not specify a cluster, the default cluster is assumed.</p>
            instance_identity_document: <p>The instance identity document for the EC2 instance to register. This document can be found by running the following command from the instance: <code>curl http://169.254.169.254/latest/dynamic/instance-identity/document/</code> </p>
            instance_identity_document_signature: <p>The instance identity document signature for the EC2 instance to register. This signature can be found by running the following command from the instance: <code>curl http://169.254.169.254/latest/dynamic/instance-identity/signature/</code> </p>
            total_resources: <p>The resources available on the instance.</p>
            version_info: <p>The version information for the Amazon ECS container agent and Docker daemon that runs on the container instance.</p>
            container_instance_arn: <p>The ARN of the container instance (if it was previously registered).</p>
            attributes: <p>The container instance attributes that this container instance supports.</p>
            platform_devices: <p>The devices that are available on the container instance. The supported device types are GPUs and Neuron devices.</p>
            tags: <p>The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.register_container_instance_request.RegisterContainerInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.register_container_instance_response.RegisterContainerInstanceResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.register_container_instance

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.register_container_instance.register_container_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.register_container_instance_request.RegisterContainerInstanceRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        if instance_identity_document is not None:
            input_["instance_identity_document"] = instance_identity_document
        if instance_identity_document_signature is not None:
            input_["instance_identity_document_signature"] = (
                instance_identity_document_signature
            )
        if total_resources is not None:
            input_["total_resources"] = total_resources
        if version_info is not None:
            input_["version_info"] = version_info
        if container_instance_arn is not None:
            input_["container_instance_arn"] = container_instance_arn
        if attributes is not None:
            input_["attributes"] = attributes
        if platform_devices is not None:
            input_["platform_devices"] = platform_devices
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_container_agent(
        self,
        container_instance: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> (
        "aws_sdk_ecs.types.update_container_agent_response.UpdateContainerAgentResponse"
    ):
        """<p>Updates the Amazon ECS container agent on a specified container instance. Updating the Amazon ECS container agent doesn't interrupt running tasks or services on the container instance. The process for updating the agent differs depending on whether your container instance was launched with the Amazon ECS-optimized AMI or another operating system.</p> <note> <p>The <code>UpdateContainerAgent</code> API isn't supported for container instances using the Amazon ECS-optimized Amazon Linux 2 (arm64) AMI. To update the container agent, you can update the <code>ecs-init</code> package. This updates the agent. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/agent-update-ecs-ami.html\">Updating the Amazon ECS container agent</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note> <note> <p>Agent updates with the <code>UpdateContainerAgent</code> API operation do not apply to Windows container instances. We recommend that you launch new container instances to update the agent version in your Windows clusters.</p> </note> <p>The <code>UpdateContainerAgent</code> API requires an Amazon ECS-optimized AMI or Amazon Linux AMI with the <code>ecs-init</code> service installed and running. For help updating the Amazon ECS container agent on other operating systems, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html#manually_update_agent\">Manually updating the Amazon ECS container agent</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that your container instance is running on. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instance: <p>The container instance ID or full ARN entries for the container instance where you would like to update the Amazon ECS container agent.</p>

        Examples:
            To update the container agent version on a container instance
            This example updates the container agent version on the specified container instance in cluster MyCluster.

            >>> client.update_container_agent(cluster='MyCluster', container_instance='53ac7152-dcd1-4102-81f5-208962864132')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.update_container_agent_request.UpdateContainerAgentRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.update_container_agent_response.UpdateContainerAgentResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_container_agent

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_container_agent.update_container_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.update_container_agent_request.UpdateContainerAgentRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        input_["container_instance"] = container_instance

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_container_instances_state(
        self,
        container_instances: "aws_sdk_ecs.types.string_list.StringList",
        status: "aws_sdk_ecs.types.container_instance_status.ContainerInstanceStatus",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.update_container_instances_state_response.UpdateContainerInstancesStateResponse":
        """<p>Modifies the status of an Amazon ECS container instance.</p> <p>Once a container instance has reached an <code>ACTIVE</code> state, you can change the status of a container instance to <code>DRAINING</code> to manually remove an instance from a cluster, for example to perform system updates, update the Docker daemon, or scale down the cluster size.</p> <important> <p>A container instance can't be changed to <code>DRAINING</code> until it has reached an <code>ACTIVE</code> status. If the instance is in any other status, an error will be received.</p> </important> <p>When you set a container instance to <code>DRAINING</code>, Amazon ECS prevents new tasks from being scheduled for placement on the container instance and replacement service tasks are started on other container instances in the cluster if the resources are available. Service tasks on the container instance that are in the <code>PENDING</code> state are stopped immediately.</p> <p>Service tasks on the container instance that are in the <code>RUNNING</code> state are stopped and replaced according to the service's deployment configuration parameters, <code>minimumHealthyPercent</code> and <code>maximumPercent</code>. You can change the deployment configuration of your service using <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html\">UpdateService</a>.</p> <ul> <li> <p>If <code>minimumHealthyPercent</code> is below 100%, the scheduler can ignore <code>desiredCount</code> temporarily during task replacement. For example, <code>desiredCount</code> is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. If the minimum is 100%, the service scheduler can't remove existing tasks until the replacement tasks are considered healthy. Tasks for services that do not use a load balancer are considered healthy if they're in the <code>RUNNING</code> state. Tasks for services that use a load balancer are considered healthy if they're in the <code>RUNNING</code> state and are reported as healthy by the load balancer.</p> </li> <li> <p>The <code>maximumPercent</code> parameter represents an upper limit on the number of running tasks during task replacement. You can use this to define the replacement batch size. For example, if <code>desiredCount</code> is four tasks, a maximum of 200% starts four new tasks before stopping the four tasks to be drained, provided that the cluster resources required to do this are available. If the maximum is 100%, then replacement tasks can't start until the draining tasks have stopped.</p> </li> </ul> <p>Any <code>PENDING</code> or <code>RUNNING</code> tasks that do not belong to a service aren't affected. You must wait for them to finish or stop them manually.</p> <p>A container instance has completed draining when it has no more <code>RUNNING</code> tasks. You can verify this using <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html\">ListTasks</a>.</p> <p>When a container instance has been drained, you can set a container instance to <code>ACTIVE</code> status and once it has reached that status the Amazon ECS scheduler can begin scheduling tasks on the instance again.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to update. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instances: <p>A list of up to 10 container instance IDs or full ARN entries.</p>
            status: <p>The container instance state to update the container instance with. The only valid values for this action are <code>ACTIVE</code> and <code>DRAINING</code>. A container instance can only be updated to <code>DRAINING</code> status once it has reached an <code>ACTIVE</code> state. If a container instance is in <code>REGISTERING</code>, <code>DEREGISTERING</code>, or <code>REGISTRATION_FAILED</code> state you can describe the container instance but can't update the container instance state.</p>

        Examples:
            To update the state of a container instance
            This example updates the state of the specified container instance in the default cluster to DRAINING.

            >>> client.update_container_instances_state(cluster='default', container_instances=['1c3be8ed-df30-47b4-8f1e-6e68ebd01f34'], status='DRAINING')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.update_container_instances_state_request.UpdateContainerInstancesStateRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.update_container_instances_state_response.UpdateContainerInstancesStateResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_container_instances_state

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_container_instances_state.update_container_instances_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.update_container_instances_state_request.UpdateContainerInstancesStateRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        input_["container_instances"] = container_instances
        input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncContainerInstanceResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def delete_attributes(
        self,
        attributes: "aws_sdk_ecs.types.attributes.Attributes",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.delete_attributes_response.DeleteAttributesResponse":
        """<p>Deletes one or more custom attributes from an Amazon ECS resource.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to delete attributes. If you do not specify a cluster, the default cluster is assumed.</p>
            attributes: <p>The attributes to delete from your resource. You can specify up to 10 attributes for each request. For custom attributes, specify the attribute name and target ID, but don't specify the value. If you specify the target ID using the short form, you must also specify the target type.</p>

        Examples:
            To delete a custom attribute from an Amazon ECS instance
            This example deletes an attribute named stack from a container instance.

            >>> await client.delete_attributes(attributes=[{'name': 'stack', 'targetId': 'aws:ecs:us-west-2:130757420319:container-instance/1c3be8ed-df30-47b4-8f1e-6e68ebd01f34'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.delete_attributes_request.DeleteAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.delete_attributes_response.DeleteAttributesResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_attributes.async_delete_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.delete_attributes_request.DeleteAttributesRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_container_instances(
        self,
        container_instances: "aws_sdk_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        include: Optional[
            "aws_sdk_ecs.types.container_instance_field_list.ContainerInstanceFieldList"
        ] = None,
    ) -> "aws_sdk_ecs.types.describe_container_instances_response.DescribeContainerInstancesResponse":
        """<p>Describes one or more container instances. Returns metadata about each container instance requested.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the container instance or container instances you are describing were launched in any cluster other than the default cluster.</p>
            container_instances: <p>A list of up to 100 container instance IDs or full Amazon Resource Name (ARN) entries.</p>
            include: <p>Specifies whether you want to see the resource tags for the container instance. If <code>TAGS</code> is specified, the tags are included in the response. If <code>CONTAINER_INSTANCE_HEALTH</code> is specified, the container instance health is included in the response. If this field is omitted, tags and container instance health status aren't included in the response.</p>

        Examples:
            To describe container instance
            This example provides a description of the specified container instance in your default region, using the container instance UUID as an identifier.

            >>> await client.describe_container_instances(cluster='default', container_instances=['f2756532-8f13-4d53-87c9-aed50dc94cd7'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.describe_container_instances_request.DescribeContainerInstancesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.describe_container_instances_response.DescribeContainerInstancesResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_container_instances

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_container_instances.async_describe_container_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.describe_container_instances_request.DescribeContainerInstancesRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        input_["container_instances"] = container_instances
        if include is not None:
            input_["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tasks(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        container_instance: Optional["aws_sdk_ecs.types.string.String"] = None,
        family: Optional["aws_sdk_ecs.types.string.String"] = None,
        next_token: Optional["aws_sdk_ecs.types.string.String"] = None,
        max_results: Optional["aws_sdk_ecs.types.boxed_integer.BoxedInteger"] = None,
        started_by: Optional["aws_sdk_ecs.types.string.String"] = None,
        service_name: Optional["aws_sdk_ecs.types.string.String"] = None,
        desired_status: Optional[
            "aws_sdk_ecs.types.desired_status.DesiredStatus"
        ] = None,
        launch_type: Optional["aws_sdk_ecs.types.launch_type.LaunchType"] = None,
        daemon_name: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.list_tasks_response.ListTasksResponse":
        """<p>Returns a list of tasks. You can filter the results by cluster, task definition family, container instance, launch type, what IAM principal started the task, or by the desired status of the task.</p> <p>Recently stopped tasks might appear in the returned results. </p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the <code>ListTasks</code> results. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instance: <p>The container instance ID or full ARN of the container instance to use when filtering the <code>ListTasks</code> results. Specifying a <code>containerInstance</code> limits the results to tasks that belong to that container instance.</p>
            family: <p>The name of the task definition family to use when filtering the <code>ListTasks</code> results. Specifying a <code>family</code> limits the results to tasks that belong to that family.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListTasks</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of task results that <code>ListTasks</code> returned in paginated output. When this parameter is used, <code>ListTasks</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListTasks</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListTasks</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            started_by: <p>The <code>startedBy</code> value to filter the task results with. Specifying a <code>startedBy</code> value limits the results to tasks that were started with that value.</p> <p>When you specify <code>startedBy</code> as the filter, it must be the only filter that you use.</p>
            service_name: <p>The name of the service to use when filtering the <code>ListTasks</code> results. Specifying a <code>serviceName</code> limits the results to tasks that belong to that service.</p>
            desired_status: <p>The task desired status to use when filtering the <code>ListTasks</code> results. Specifying a <code>desiredStatus</code> of <code>STOPPED</code> limits the results to tasks that Amazon ECS has set the desired status to <code>STOPPED</code>. This can be useful for debugging tasks that aren't starting properly or have died or finished. The default status filter is <code>RUNNING</code>, which shows tasks that Amazon ECS has set the desired status to <code>RUNNING</code>.</p> <note> <p>Although you can filter results based on a desired status of <code>PENDING</code>, this doesn't return any results. Amazon ECS never sets the desired status of a task to that value (only a task's <code>lastStatus</code> may have a value of <code>PENDING</code>).</p> </note>
            launch_type: <p>The launch type to use when filtering the <code>ListTasks</code> results.</p>
            daemon_name: <p>The name of the daemon to use when filtering the <code>ListTasks</code> results. Specifying a <code>daemonName</code> limits the results to tasks that belong to that daemon.</p>

        Examples:
            To list the tasks in a cluster
            This example lists all of the tasks in a cluster.

            >>> await client.list_tasks(cluster='default')
            To list the tasks on a particular container instance
            This example lists the tasks of a specified container instance. Specifying a ``containerInstance`` value limits  the  results  to  tasks  that belong to that container instance.

            >>> await client.list_tasks(cluster='default', container_instance='f6bbb147-5370-4ace-8c73-c7181ded911f')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.list_tasks_request.ListTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.list_tasks_response.ListTasksResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.list_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.list_tasks.async_list_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.list_tasks_request.ListTasksRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        if container_instance is not None:
            input_["container_instance"] = container_instance
        if family is not None:
            input_["family"] = family
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if started_by is not None:
            input_["started_by"] = started_by
        if service_name is not None:
            input_["service_name"] = service_name
        if desired_status is not None:
            input_["desired_status"] = desired_status
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if daemon_name is not None:
            input_["daemon_name"] = daemon_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_attributes(
        self,
        attributes: "aws_sdk_ecs.types.attributes.Attributes",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.put_attributes_response.PutAttributesResponse":
        """<p>Create or update an attribute on an Amazon ECS resource. If the attribute doesn't exist, it's created. If the attribute exists, its value is replaced with the specified value. To delete an attribute, use <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteAttributes.html\">DeleteAttributes</a>. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes\">Attributes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to apply attributes. If you do not specify a cluster, the default cluster is assumed.</p>
            attributes: <p>The attributes to apply to your resource. You can specify up to 10 custom attributes for each resource. You can specify up to 10 attributes in a single call.</p>

        Examples:
            To create or update an attribute on a resource
            This example adds an attribute "stack" with the value "production" to a container instance.

            >>> await client.put_attributes(cluster='MyCluster', attributes=[{'targetId': 'arn:aws:ecs:us-west-2:123456789012:container-instance/1c3be8ed-df30-47b4-8f1e-6e68ebd01f34', 'name': 'stack', 'value': 'production'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.put_attributes_request.PutAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.put_attributes_response.PutAttributesResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.put_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.put_attributes.async_put_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.put_attributes_request.PutAttributesRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def register_container_instance(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        instance_identity_document: Optional["aws_sdk_ecs.types.string.String"] = None,
        instance_identity_document_signature: Optional[
            "aws_sdk_ecs.types.string.String"
        ] = None,
        total_resources: Optional["aws_sdk_ecs.types.resources.Resources"] = None,
        version_info: Optional["aws_sdk_ecs.types.version_info.VersionInfo"] = None,
        container_instance_arn: Optional["aws_sdk_ecs.types.string.String"] = None,
        attributes: Optional["aws_sdk_ecs.types.attributes.Attributes"] = None,
        platform_devices: Optional[
            "aws_sdk_ecs.types.platform_devices.PlatformDevices"
        ] = None,
        tags: Optional["aws_sdk_ecs.types.tags.Tags"] = None,
    ) -> "aws_sdk_ecs.types.register_container_instance_response.RegisterContainerInstanceResponse":
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to register your container instance with. If you do not specify a cluster, the default cluster is assumed.</p>
            instance_identity_document: <p>The instance identity document for the EC2 instance to register. This document can be found by running the following command from the instance: <code>curl http://169.254.169.254/latest/dynamic/instance-identity/document/</code> </p>
            instance_identity_document_signature: <p>The instance identity document signature for the EC2 instance to register. This signature can be found by running the following command from the instance: <code>curl http://169.254.169.254/latest/dynamic/instance-identity/signature/</code> </p>
            total_resources: <p>The resources available on the instance.</p>
            version_info: <p>The version information for the Amazon ECS container agent and Docker daemon that runs on the container instance.</p>
            container_instance_arn: <p>The ARN of the container instance (if it was previously registered).</p>
            attributes: <p>The container instance attributes that this container instance supports.</p>
            platform_devices: <p>The devices that are available on the container instance. The supported device types are GPUs and Neuron devices.</p>
            tags: <p>The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.register_container_instance_request.RegisterContainerInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.register_container_instance_response.RegisterContainerInstanceResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.register_container_instance

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.register_container_instance.async_register_container_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.register_container_instance_request.RegisterContainerInstanceRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        if instance_identity_document is not None:
            input_["instance_identity_document"] = instance_identity_document
        if instance_identity_document_signature is not None:
            input_["instance_identity_document_signature"] = (
                instance_identity_document_signature
            )
        if total_resources is not None:
            input_["total_resources"] = total_resources
        if version_info is not None:
            input_["version_info"] = version_info
        if container_instance_arn is not None:
            input_["container_instance_arn"] = container_instance_arn
        if attributes is not None:
            input_["attributes"] = attributes
        if platform_devices is not None:
            input_["platform_devices"] = platform_devices
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_container_agent(
        self,
        container_instance: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> (
        "aws_sdk_ecs.types.update_container_agent_response.UpdateContainerAgentResponse"
    ):
        """<p>Updates the Amazon ECS container agent on a specified container instance. Updating the Amazon ECS container agent doesn't interrupt running tasks or services on the container instance. The process for updating the agent differs depending on whether your container instance was launched with the Amazon ECS-optimized AMI or another operating system.</p> <note> <p>The <code>UpdateContainerAgent</code> API isn't supported for container instances using the Amazon ECS-optimized Amazon Linux 2 (arm64) AMI. To update the container agent, you can update the <code>ecs-init</code> package. This updates the agent. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/agent-update-ecs-ami.html\">Updating the Amazon ECS container agent</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note> <note> <p>Agent updates with the <code>UpdateContainerAgent</code> API operation do not apply to Windows container instances. We recommend that you launch new container instances to update the agent version in your Windows clusters.</p> </note> <p>The <code>UpdateContainerAgent</code> API requires an Amazon ECS-optimized AMI or Amazon Linux AMI with the <code>ecs-init</code> service installed and running. For help updating the Amazon ECS container agent on other operating systems, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html#manually_update_agent\">Manually updating the Amazon ECS container agent</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that your container instance is running on. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instance: <p>The container instance ID or full ARN entries for the container instance where you would like to update the Amazon ECS container agent.</p>

        Examples:
            To update the container agent version on a container instance
            This example updates the container agent version on the specified container instance in cluster MyCluster.

            >>> await client.update_container_agent(cluster='MyCluster', container_instance='53ac7152-dcd1-4102-81f5-208962864132')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.update_container_agent_request.UpdateContainerAgentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.update_container_agent_response.UpdateContainerAgentResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_container_agent

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_container_agent.async_update_container_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.update_container_agent_request.UpdateContainerAgentRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        input_["container_instance"] = container_instance

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_container_instances_state(
        self,
        container_instances: "aws_sdk_ecs.types.string_list.StringList",
        status: "aws_sdk_ecs.types.container_instance_status.ContainerInstanceStatus",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.update_container_instances_state_response.UpdateContainerInstancesStateResponse":
        """<p>Modifies the status of an Amazon ECS container instance.</p> <p>Once a container instance has reached an <code>ACTIVE</code> state, you can change the status of a container instance to <code>DRAINING</code> to manually remove an instance from a cluster, for example to perform system updates, update the Docker daemon, or scale down the cluster size.</p> <important> <p>A container instance can't be changed to <code>DRAINING</code> until it has reached an <code>ACTIVE</code> status. If the instance is in any other status, an error will be received.</p> </important> <p>When you set a container instance to <code>DRAINING</code>, Amazon ECS prevents new tasks from being scheduled for placement on the container instance and replacement service tasks are started on other container instances in the cluster if the resources are available. Service tasks on the container instance that are in the <code>PENDING</code> state are stopped immediately.</p> <p>Service tasks on the container instance that are in the <code>RUNNING</code> state are stopped and replaced according to the service's deployment configuration parameters, <code>minimumHealthyPercent</code> and <code>maximumPercent</code>. You can change the deployment configuration of your service using <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html\">UpdateService</a>.</p> <ul> <li> <p>If <code>minimumHealthyPercent</code> is below 100%, the scheduler can ignore <code>desiredCount</code> temporarily during task replacement. For example, <code>desiredCount</code> is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. If the minimum is 100%, the service scheduler can't remove existing tasks until the replacement tasks are considered healthy. Tasks for services that do not use a load balancer are considered healthy if they're in the <code>RUNNING</code> state. Tasks for services that use a load balancer are considered healthy if they're in the <code>RUNNING</code> state and are reported as healthy by the load balancer.</p> </li> <li> <p>The <code>maximumPercent</code> parameter represents an upper limit on the number of running tasks during task replacement. You can use this to define the replacement batch size. For example, if <code>desiredCount</code> is four tasks, a maximum of 200% starts four new tasks before stopping the four tasks to be drained, provided that the cluster resources required to do this are available. If the maximum is 100%, then replacement tasks can't start until the draining tasks have stopped.</p> </li> </ul> <p>Any <code>PENDING</code> or <code>RUNNING</code> tasks that do not belong to a service aren't affected. You must wait for them to finish or stop them manually.</p> <p>A container instance has completed draining when it has no more <code>RUNNING</code> tasks. You can verify this using <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html\">ListTasks</a>.</p> <p>When a container instance has been drained, you can set a container instance to <code>ACTIVE</code> status and once it has reached that status the Amazon ECS scheduler can begin scheduling tasks on the instance again.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to update. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instances: <p>A list of up to 10 container instance IDs or full ARN entries.</p>
            status: <p>The container instance state to update the container instance with. The only valid values for this action are <code>ACTIVE</code> and <code>DRAINING</code>. A container instance can only be updated to <code>DRAINING</code> status once it has reached an <code>ACTIVE</code> state. If a container instance is in <code>REGISTERING</code>, <code>DEREGISTERING</code>, or <code>REGISTRATION_FAILED</code> state you can describe the container instance but can't update the container instance state.</p>

        Examples:
            To update the state of a container instance
            This example updates the state of the specified container instance in the default cluster to DRAINING.

            >>> await client.update_container_instances_state(cluster='default', container_instances=['1c3be8ed-df30-47b4-8f1e-6e68ebd01f34'], status='DRAINING')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.update_container_instances_state_request.UpdateContainerInstancesStateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.update_container_instances_state_response.UpdateContainerInstancesStateResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_container_instances_state

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_container_instances_state.async_update_container_instances_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.update_container_instances_state_request.UpdateContainerInstancesStateRequest = {}  # type: ignore[typeddict-item]
        if cluster is not None:
            input_["cluster"] = cluster
        input_["container_instances"] = container_instances
        input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
