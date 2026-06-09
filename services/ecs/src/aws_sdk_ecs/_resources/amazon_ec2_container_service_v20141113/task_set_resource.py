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
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.capacity_provider_strategy
    import aws_sdk_ecs.types.create_task_set_request
    import aws_sdk_ecs.types.create_task_set_response
    import aws_sdk_ecs.types.delete_task_set_request
    import aws_sdk_ecs.types.delete_task_set_response
    import aws_sdk_ecs.types.describe_task_sets_request
    import aws_sdk_ecs.types.describe_task_sets_response
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.load_balancers
    import aws_sdk_ecs.types.network_configuration
    import aws_sdk_ecs.types.scale
    import aws_sdk_ecs.types.service_registries
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list
    import aws_sdk_ecs.types.tags
    import aws_sdk_ecs.types.task_set_field_list
    import aws_sdk_ecs.types.update_task_set_request
    import aws_sdk_ecs.types.update_task_set_response
    from aws_sdk_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from aws_sdk_ecs._services.ecs import ECSClient, ECSClientConfig


class TaskSetResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def update(
        self,
        cluster: "aws_sdk_ecs.types.string.String",
        service: "aws_sdk_ecs.types.string.String",
        task_set: "aws_sdk_ecs.types.string.String",
        scale: "aws_sdk_ecs.types.scale.Scale",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "aws_sdk_ecs.types.update_task_set_response.UpdateTaskSetResponse":
        """<p>Modifies a task set. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\">Amazon ECS Deployment Types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set is found in.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that the task set is found in.</p>
            task_set: <p>The short name or full Amazon Resource Name (ARN) of the task set to update.</p>
            scale: <p>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</p>

        Examples:
            To update a task set
            This example updates the task set to adjust the scale.

            >>> client.update(cluster='MyCluster', service='MyService', task_set='arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789', scale={'value': 50, 'unit': 'PERCENT'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.update_task_set_request.UpdateTaskSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.update_task_set_response.UpdateTaskSetResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_task_set

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_task_set.update_task_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.update_task_set_request.UpdateTaskSetRequest = {}  # type: ignore[typeddict-item]
        input["cluster"] = cluster
        input["service"] = service
        input["task_set"] = task_set
        input["scale"] = scale

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        cluster: "aws_sdk_ecs.types.string.String",
        service: "aws_sdk_ecs.types.string.String",
        task_set: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        force: Optional["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "aws_sdk_ecs.types.delete_task_set_response.DeleteTaskSetResponse":
        """<p>Deletes a specified task set within a service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\">Amazon ECS deployment types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set found in to delete.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that hosts the task set to delete.</p>
            task_set: <p>The task set ID or full Amazon Resource Name (ARN) of the task set to delete.</p>
            force: <p>If <code>true</code>, you can delete a task set even if it hasn't been scaled down to zero.</p>

        Examples:
            To delete a task set within a service that uses the EXTERNAL deployment controller type
            This example deletes a task set and uses the force flag to force deletion if it hasn't scaled to zero.

            >>> client.delete(cluster='MyCluster', service='MyService', task_set='arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789', force=True)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.delete_task_set_request.DeleteTaskSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.delete_task_set_response.DeleteTaskSetResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_set

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_set.delete_task_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.delete_task_set_request.DeleteTaskSetRequest = {}  # type: ignore[typeddict-item]
        input["cluster"] = cluster
        input["service"] = service
        input["task_set"] = task_set
        if force is not None:
            input["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_task_set(
        self,
        service: "aws_sdk_ecs.types.string.String",
        cluster: "aws_sdk_ecs.types.string.String",
        task_definition: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        external_id: Optional["aws_sdk_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "aws_sdk_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        load_balancers: Optional[
            "aws_sdk_ecs.types.load_balancers.LoadBalancers"
        ] = None,
        service_registries: Optional[
            "aws_sdk_ecs.types.service_registries.ServiceRegistries"
        ] = None,
        launch_type: Optional["aws_sdk_ecs.types.launch_type.LaunchType"] = None,
        capacity_provider_strategy: Optional[
            "aws_sdk_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        platform_version: Optional["aws_sdk_ecs.types.string.String"] = None,
        scale: Optional["aws_sdk_ecs.types.scale.Scale"] = None,
        client_token: Optional["aws_sdk_ecs.types.string.String"] = None,
        tags: Optional["aws_sdk_ecs.types.tags.Tags"] = None,
    ) -> "aws_sdk_ecs.types.create_task_set_response.CreateTaskSetResponse":
        """<p>Create a task set in the specified cluster and service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\">Amazon ECS deployment types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <p>For information about the maximum number of task sets and other quotas, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html\">Amazon ECS service quotas</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            service: <p>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</p>
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</p>
            external_id: <p>An optional non-unique tag that identifies this task set in external systems. If the task set is associated with a service discovery registry, the tasks in this task set will have the <code>ECS_TASK_SET_EXTERNAL_ID</code> Cloud Map attribute set to the provided value.</p>
            task_definition: <p>The task definition for the tasks in the task set to use. If a revision isn't specified, the latest <code>ACTIVE</code> revision is used.</p>
            network_configuration: <p>An object representing the network configuration for a task set.</p>
            load_balancers: <p>A load balancer object representing the load balancer to use with the task set. The supported load balancer types are either an Application Load Balancer or a Network Load Balancer.</p>
            service_registries: <p>The details of the service discovery registries to assign to this task set. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html\">Service discovery</a>.</p>
            launch_type: <p>The launch type that new tasks in the task set uses. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html\">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p>
            capacity_provider_strategy: <p>The capacity provider strategy to use for the task set.</p> <p>A capacity provider strategy consists of one or more capacity providers along with the <code>base</code> and <code>weight</code> to assign to them. A capacity provider must be associated with the cluster to be used in a capacity provider strategy. The <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html\">PutClusterCapacityProviders</a> API is used to associate a capacity provider with a cluster. Only capacity providers with an <code>ACTIVE</code> or <code>UPDATING</code> status can be used.</p> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProviderProvider.html\">CreateCapacityProviderProvider</a>API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p> <p>The <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html\">PutClusterCapacityProviders</a> API operation is used to update the list of available capacity providers for a cluster after the cluster is created.</p>
            platform_version: <p>The platform version that the tasks in the task set uses. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the <code>LATEST</code> platform version is used.</p>
            scale: <p>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>
            tags: <p>The metadata that you apply to the task set to help you categorize and organize them. Each tag consists of a key and an optional value. You define both. When a service is deleted, the tags are deleted.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>

        Examples:
            To create a task set
            This example creates a task set in a service that uses the EXTERNAL deployment controller.

            >>> client.create_task_set(service='MyService', cluster='MyCluster', task_definition='MyTaskDefinition:2', network_configuration={'awsvpcConfiguration': {'subnets': ['subnet-12344321'], 'securityGroups': ['sg-12344321']}})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.create_task_set_request.CreateTaskSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.create_task_set_response.CreateTaskSetResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.create_task_set

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.create_task_set.create_task_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.create_task_set_request.CreateTaskSetRequest = {}  # type: ignore[typeddict-item]
        input["service"] = service
        input["cluster"] = cluster
        if external_id is not None:
            input["external_id"] = external_id
        input["task_definition"] = task_definition
        if network_configuration is not None:
            input["network_configuration"] = network_configuration
        if load_balancers is not None:
            input["load_balancers"] = load_balancers
        if service_registries is not None:
            input["service_registries"] = service_registries
        if launch_type is not None:
            input["launch_type"] = launch_type
        if capacity_provider_strategy is not None:
            input["capacity_provider_strategy"] = capacity_provider_strategy
        if platform_version is not None:
            input["platform_version"] = platform_version
        if scale is not None:
            input["scale"] = scale
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_task_sets(
        self,
        cluster: "aws_sdk_ecs.types.string.String",
        service: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        task_sets: Optional["aws_sdk_ecs.types.string_list.StringList"] = None,
        include: Optional[
            "aws_sdk_ecs.types.task_set_field_list.TaskSetFieldList"
        ] = None,
    ) -> "aws_sdk_ecs.types.describe_task_sets_response.DescribeTaskSetsResponse":
        """<p>Describes the task sets in the specified cluster and service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\">Amazon ECS Deployment Types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that the task sets exist in.</p>
            task_sets: <p>The ID or full Amazon Resource Name (ARN) of task sets to describe.</p>
            include: <p>Specifies whether to see the resource tags for the task set. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>

        Examples:
            To describe a task set
            This example describes a task set in service MyService that uses an EXTERNAL deployment controller.

            >>> client.describe_task_sets(cluster='MyCluster', service='MyService', task_sets=['arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.describe_task_sets_request.DescribeTaskSetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.describe_task_sets_response.DescribeTaskSetsResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_task_sets

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_task_sets.describe_task_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.describe_task_sets_request.DescribeTaskSetsRequest = {}  # type: ignore[typeddict-item]
        input["cluster"] = cluster
        input["service"] = service
        if task_sets is not None:
            input["task_sets"] = task_sets
        if include is not None:
            input["include"] = include

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTaskSetResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def update(
        self,
        cluster: "aws_sdk_ecs.types.string.String",
        service: "aws_sdk_ecs.types.string.String",
        task_set: "aws_sdk_ecs.types.string.String",
        scale: "aws_sdk_ecs.types.scale.Scale",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "aws_sdk_ecs.types.update_task_set_response.UpdateTaskSetResponse":
        """<p>Modifies a task set. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\">Amazon ECS Deployment Types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set is found in.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that the task set is found in.</p>
            task_set: <p>The short name or full Amazon Resource Name (ARN) of the task set to update.</p>
            scale: <p>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</p>

        Examples:
            To update a task set
            This example updates the task set to adjust the scale.

            >>> await client.update(cluster='MyCluster', service='MyService', task_set='arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789', scale={'value': 50, 'unit': 'PERCENT'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.update_task_set_request.UpdateTaskSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.update_task_set_response.UpdateTaskSetResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_task_set

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_task_set.async_update_task_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.update_task_set_request.UpdateTaskSetRequest = {}  # type: ignore[typeddict-item]
        input["cluster"] = cluster
        input["service"] = service
        input["task_set"] = task_set
        input["scale"] = scale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        cluster: "aws_sdk_ecs.types.string.String",
        service: "aws_sdk_ecs.types.string.String",
        task_set: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        force: Optional["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "aws_sdk_ecs.types.delete_task_set_response.DeleteTaskSetResponse":
        """<p>Deletes a specified task set within a service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\">Amazon ECS deployment types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set found in to delete.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that hosts the task set to delete.</p>
            task_set: <p>The task set ID or full Amazon Resource Name (ARN) of the task set to delete.</p>
            force: <p>If <code>true</code>, you can delete a task set even if it hasn't been scaled down to zero.</p>

        Examples:
            To delete a task set within a service that uses the EXTERNAL deployment controller type
            This example deletes a task set and uses the force flag to force deletion if it hasn't scaled to zero.

            >>> await client.delete(cluster='MyCluster', service='MyService', task_set='arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789', force=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.delete_task_set_request.DeleteTaskSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.delete_task_set_response.DeleteTaskSetResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_set

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_set.async_delete_task_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.delete_task_set_request.DeleteTaskSetRequest = {}  # type: ignore[typeddict-item]
        input["cluster"] = cluster
        input["service"] = service
        input["task_set"] = task_set
        if force is not None:
            input["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_task_set(
        self,
        service: "aws_sdk_ecs.types.string.String",
        cluster: "aws_sdk_ecs.types.string.String",
        task_definition: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        external_id: Optional["aws_sdk_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "aws_sdk_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        load_balancers: Optional[
            "aws_sdk_ecs.types.load_balancers.LoadBalancers"
        ] = None,
        service_registries: Optional[
            "aws_sdk_ecs.types.service_registries.ServiceRegistries"
        ] = None,
        launch_type: Optional["aws_sdk_ecs.types.launch_type.LaunchType"] = None,
        capacity_provider_strategy: Optional[
            "aws_sdk_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        platform_version: Optional["aws_sdk_ecs.types.string.String"] = None,
        scale: Optional["aws_sdk_ecs.types.scale.Scale"] = None,
        client_token: Optional["aws_sdk_ecs.types.string.String"] = None,
        tags: Optional["aws_sdk_ecs.types.tags.Tags"] = None,
    ) -> "aws_sdk_ecs.types.create_task_set_response.CreateTaskSetResponse":
        """<p>Create a task set in the specified cluster and service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\">Amazon ECS deployment types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <p>For information about the maximum number of task sets and other quotas, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html\">Amazon ECS service quotas</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            service: <p>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</p>
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</p>
            external_id: <p>An optional non-unique tag that identifies this task set in external systems. If the task set is associated with a service discovery registry, the tasks in this task set will have the <code>ECS_TASK_SET_EXTERNAL_ID</code> Cloud Map attribute set to the provided value.</p>
            task_definition: <p>The task definition for the tasks in the task set to use. If a revision isn't specified, the latest <code>ACTIVE</code> revision is used.</p>
            network_configuration: <p>An object representing the network configuration for a task set.</p>
            load_balancers: <p>A load balancer object representing the load balancer to use with the task set. The supported load balancer types are either an Application Load Balancer or a Network Load Balancer.</p>
            service_registries: <p>The details of the service discovery registries to assign to this task set. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html\">Service discovery</a>.</p>
            launch_type: <p>The launch type that new tasks in the task set uses. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html\">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p>
            capacity_provider_strategy: <p>The capacity provider strategy to use for the task set.</p> <p>A capacity provider strategy consists of one or more capacity providers along with the <code>base</code> and <code>weight</code> to assign to them. A capacity provider must be associated with the cluster to be used in a capacity provider strategy. The <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html\">PutClusterCapacityProviders</a> API is used to associate a capacity provider with a cluster. Only capacity providers with an <code>ACTIVE</code> or <code>UPDATING</code> status can be used.</p> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProviderProvider.html\">CreateCapacityProviderProvider</a>API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p> <p>The <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html\">PutClusterCapacityProviders</a> API operation is used to update the list of available capacity providers for a cluster after the cluster is created.</p>
            platform_version: <p>The platform version that the tasks in the task set uses. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the <code>LATEST</code> platform version is used.</p>
            scale: <p>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>
            tags: <p>The metadata that you apply to the task set to help you categorize and organize them. Each tag consists of a key and an optional value. You define both. When a service is deleted, the tags are deleted.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>

        Examples:
            To create a task set
            This example creates a task set in a service that uses the EXTERNAL deployment controller.

            >>> await client.create_task_set(service='MyService', cluster='MyCluster', task_definition='MyTaskDefinition:2', network_configuration={'awsvpcConfiguration': {'subnets': ['subnet-12344321'], 'securityGroups': ['sg-12344321']}})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.create_task_set_request.CreateTaskSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.create_task_set_response.CreateTaskSetResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.create_task_set

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.create_task_set.async_create_task_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.create_task_set_request.CreateTaskSetRequest = {}  # type: ignore[typeddict-item]
        input["service"] = service
        input["cluster"] = cluster
        if external_id is not None:
            input["external_id"] = external_id
        input["task_definition"] = task_definition
        if network_configuration is not None:
            input["network_configuration"] = network_configuration
        if load_balancers is not None:
            input["load_balancers"] = load_balancers
        if service_registries is not None:
            input["service_registries"] = service_registries
        if launch_type is not None:
            input["launch_type"] = launch_type
        if capacity_provider_strategy is not None:
            input["capacity_provider_strategy"] = capacity_provider_strategy
        if platform_version is not None:
            input["platform_version"] = platform_version
        if scale is not None:
            input["scale"] = scale
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_task_sets(
        self,
        cluster: "aws_sdk_ecs.types.string.String",
        service: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        task_sets: Optional["aws_sdk_ecs.types.string_list.StringList"] = None,
        include: Optional[
            "aws_sdk_ecs.types.task_set_field_list.TaskSetFieldList"
        ] = None,
    ) -> "aws_sdk_ecs.types.describe_task_sets_response.DescribeTaskSetsResponse":
        """<p>Describes the task sets in the specified cluster and service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\">Amazon ECS Deployment Types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that the task sets exist in.</p>
            task_sets: <p>The ID or full Amazon Resource Name (ARN) of task sets to describe.</p>
            include: <p>Specifies whether to see the resource tags for the task set. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>

        Examples:
            To describe a task set
            This example describes a task set in service MyService that uses an EXTERNAL deployment controller.

            >>> await client.describe_task_sets(cluster='MyCluster', service='MyService', task_sets=['arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.describe_task_sets_request.DescribeTaskSetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.describe_task_sets_response.DescribeTaskSetsResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_task_sets

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_task_sets.async_describe_task_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_ecs.types.describe_task_sets_request.DescribeTaskSetsRequest = {}  # type: ignore[typeddict-item]
        input["cluster"] = cluster
        input["service"] = service
        if task_sets is not None:
            input["task_sets"] = task_sets
        if include is not None:
            input["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
