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
    import aws_sdk_ecs.types.auto_scaling_group_provider
    import aws_sdk_ecs.types.auto_scaling_group_provider_update
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.capacity_provider_field_list
    import aws_sdk_ecs.types.create_capacity_provider_request
    import aws_sdk_ecs.types.create_capacity_provider_response
    import aws_sdk_ecs.types.create_managed_instances_provider_configuration
    import aws_sdk_ecs.types.delete_capacity_provider_request
    import aws_sdk_ecs.types.delete_capacity_provider_response
    import aws_sdk_ecs.types.describe_capacity_providers_request
    import aws_sdk_ecs.types.describe_capacity_providers_response
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list
    import aws_sdk_ecs.types.tags
    import aws_sdk_ecs.types.update_capacity_provider_request
    import aws_sdk_ecs.types.update_capacity_provider_response
    import aws_sdk_ecs.types.update_managed_instances_provider_configuration
    from aws_sdk_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from aws_sdk_ecs._services.ecs import ECSClient, ECSClientConfig


class CapacityProviderResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def put(
        self,
        name: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        auto_scaling_group_provider: Optional[
            "aws_sdk_ecs.types.auto_scaling_group_provider.AutoScalingGroupProvider"
        ] = None,
        managed_instances_provider: Optional[
            "aws_sdk_ecs.types.create_managed_instances_provider_configuration.CreateManagedInstancesProviderConfiguration"
        ] = None,
        tags: Optional["aws_sdk_ecs.types.tags.Tags"] = None,
    ) -> "aws_sdk_ecs.types.create_capacity_provider_response.CreateCapacityProviderResponse":
        """<p>Creates a capacity provider. Capacity providers are associated with a cluster and are used in capacity provider strategies to facilitate cluster auto scaling. You can create capacity providers for Amazon ECS Managed Instances and EC2 instances. Fargate has the predefined <code>FARGATE</code> and <code>FARGATE_SPOT</code> capacity providers.</p>

        Args:
            name: <p>The name of the capacity provider. Up to 255 characters are allowed. They include letters (both upper and lowercase letters), numbers, underscores (_), and hyphens (-). The name can't be prefixed with \"<code>aws</code>\", \"<code>ecs</code>\", or \"<code>fargate</code>\".</p>
            cluster: <p>The name of the cluster to associate with the capacity provider. When you create a capacity provider with Amazon ECS Managed Instances, it becomes available only within the specified cluster.</p>
            auto_scaling_group_provider: <p>The details of the Auto Scaling group for the capacity provider.</p>
            managed_instances_provider: <p>The configuration for the Amazon ECS Managed Instances provider. This configuration specifies how Amazon ECS manages Amazon EC2 instances on your behalf, including the infrastructure role, instance launch template, and tag propagation settings.</p>
            tags: <p>The metadata that you apply to the capacity provider to categorize and organize them more conveniently. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>

        Examples:
            To create a capacity provider
            This example creates a capacity provider that uses the specified Auto Scaling group MyASG and has managed scaling and manager termination protection enabled.

            >>> client.put(name='MyCapacityProvider', auto_scaling_group_provider={'autoScalingGroupArn': 'arn:aws:autoscaling:us-east-1:123456789012:autoScalingGroup:57ffcb94-11f0-4d6d-bf60-3bac5EXAMPLE:autoScalingGroupName/MyASG', 'managedScaling': {'status': 'ENABLED', 'targetCapacity': 100}, 'managedTerminationProtection': 'ENABLED'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.create_capacity_provider_request.CreateCapacityProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.create_capacity_provider_response.CreateCapacityProviderResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.create_capacity_provider

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.create_capacity_provider.create_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.create_capacity_provider_request.CreateCapacityProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if cluster is not None:
            input_["cluster"] = cluster
        if auto_scaling_group_provider is not None:
            input_["auto_scaling_group_provider"] = auto_scaling_group_provider
        if managed_instances_provider is not None:
            input_["managed_instances_provider"] = managed_instances_provider
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        name: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        auto_scaling_group_provider: Optional[
            "aws_sdk_ecs.types.auto_scaling_group_provider_update.AutoScalingGroupProviderUpdate"
        ] = None,
        managed_instances_provider: Optional[
            "aws_sdk_ecs.types.update_managed_instances_provider_configuration.UpdateManagedInstancesProviderConfiguration"
        ] = None,
    ) -> "aws_sdk_ecs.types.update_capacity_provider_response.UpdateCapacityProviderResponse":
        """<p>Modifies the parameters for a capacity provider.</p> <p>These changes only apply to new Amazon ECS Managed Instances, or EC2 instances, not existing ones.</p>

        Args:
            name: <p>The name of the capacity provider to update.</p>
            cluster: <p>The name of the cluster that contains the capacity provider to update. Managed instances capacity providers are cluster-scoped and can only be updated within their associated cluster.</p>
            auto_scaling_group_provider: <p>An object that represent the parameters to update for the Auto Scaling group capacity provider.</p>
            managed_instances_provider: <p>The updated configuration for the Amazon ECS Managed Instances provider. You can modify the infrastructure role, instance launch template, and tag propagation settings. Changes take effect for new instances launched after the update.</p>

        Examples:
            To update a capacity provider's parameters
            This example updates the targetCapacity and instanceWarmupPeriod parameters for the capacity provider MyCapacityProvider to 90 and 150 respectively.

            >>> client.update(name='MyCapacityProvider', auto_scaling_group_provider={'managedScaling': {'status': 'ENABLED', 'targetCapacity': 90, 'instanceWarmupPeriod': 150}})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.update_capacity_provider_request.UpdateCapacityProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.update_capacity_provider_response.UpdateCapacityProviderResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_capacity_provider

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_capacity_provider.update_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.update_capacity_provider_request.UpdateCapacityProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if cluster is not None:
            input_["cluster"] = cluster
        if auto_scaling_group_provider is not None:
            input_["auto_scaling_group_provider"] = auto_scaling_group_provider
        if managed_instances_provider is not None:
            input_["managed_instances_provider"] = managed_instances_provider

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        capacity_provider: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.delete_capacity_provider_response.DeleteCapacityProviderResponse":
        """<p>Deletes the specified capacity provider.</p> <note> <p>The <code>FARGATE</code> and <code>FARGATE_SPOT</code> capacity providers are reserved and can't be deleted. You can disassociate them from a cluster using either <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html\">PutClusterCapacityProviders</a> or by deleting the cluster.</p> </note> <p>Prior to a capacity provider being deleted, the capacity provider must be removed from the capacity provider strategy from all services. The <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html\">UpdateService</a> API can be used to remove a capacity provider from a service's capacity provider strategy. When updating a service, the <code>forceNewDeployment</code> option can be used to ensure that any tasks using the Amazon EC2 instance capacity provided by the capacity provider are transitioned to use the capacity from the remaining capacity providers. Only capacity providers that aren't associated with a cluster can be deleted. To remove a capacity provider from a cluster, you can either use <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html\">PutClusterCapacityProviders</a> or delete the cluster.</p>

        Args:
            capacity_provider: <p>The short name or full Amazon Resource Name (ARN) of the capacity provider to delete.</p>
            cluster: <p>The name of the cluster that contains the capacity provider to delete. Managed instances capacity providers are cluster-scoped and can only be deleted from their associated cluster.</p>

        Examples:
            To delete a specified capacity provider
            This example deletes a specified capacity provider.

            >>> client.delete(capacity_provider='arn:aws:ecs:us-west-2:123456789012:capacity-provider/ExampleCapacityProvider')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.delete_capacity_provider_request.DeleteCapacityProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.delete_capacity_provider_response.DeleteCapacityProviderResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_capacity_provider

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_capacity_provider.delete_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.delete_capacity_provider_request.DeleteCapacityProviderRequest = {}  # type: ignore[typeddict-item]
        input_["capacity_provider"] = capacity_provider
        if cluster is not None:
            input_["cluster"] = cluster

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_capacity_providers(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        capacity_providers: Optional["aws_sdk_ecs.types.string_list.StringList"] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        include: Optional[
            "aws_sdk_ecs.types.capacity_provider_field_list.CapacityProviderFieldList"
        ] = None,
        max_results: Optional["aws_sdk_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.describe_capacity_providers_response.DescribeCapacityProvidersResponse":
        """<p>Describes one or more of your capacity providers.</p>

        Args:
            capacity_providers: <p>The short name or full Amazon Resource Name (ARN) of one or more capacity providers. Up to <code>100</code> capacity providers can be described in an action.</p>
            cluster: <p>The name of the cluster to describe capacity providers for. When specified, only capacity providers associated with this cluster are returned, including Amazon ECS Managed Instances capacity providers.</p>
            include: <p>Specifies whether or not you want to see the resource tags for the capacity provider. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>
            max_results: <p>The maximum number of account setting results returned by <code>DescribeCapacityProviders</code> in paginated output. When this parameter is used, <code>DescribeCapacityProviders</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeCapacityProviders</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 10. If this parameter is not used, then <code>DescribeCapacityProviders</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeCapacityProviders</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Examples:
            To describe all capacity providers
            This example retrieves details about all capacity providers.

            >>> client.describe_capacity_providers()
            To describe a specific capacity provider
            This example retrieves details about the capacity provider MyCapacityProvider

            >>> client.describe_capacity_providers(capacity_providers=['MyCapacityProvider'], include=['TAGS'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ecs.types.describe_capacity_providers_request.DescribeCapacityProvidersRequest]",
        ) -> OperationResponse[
            "aws_sdk_ecs.types.describe_capacity_providers_response.DescribeCapacityProvidersResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_capacity_providers

            output, http_response = (
                aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_capacity_providers.describe_capacity_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.describe_capacity_providers_request.DescribeCapacityProvidersRequest = {}  # type: ignore[typeddict-item]
        if capacity_providers is not None:
            input_["capacity_providers"] = capacity_providers
        if cluster is not None:
            input_["cluster"] = cluster
        if include is not None:
            input_["include"] = include
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCapacityProviderResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def put(
        self,
        name: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        auto_scaling_group_provider: Optional[
            "aws_sdk_ecs.types.auto_scaling_group_provider.AutoScalingGroupProvider"
        ] = None,
        managed_instances_provider: Optional[
            "aws_sdk_ecs.types.create_managed_instances_provider_configuration.CreateManagedInstancesProviderConfiguration"
        ] = None,
        tags: Optional["aws_sdk_ecs.types.tags.Tags"] = None,
    ) -> "aws_sdk_ecs.types.create_capacity_provider_response.CreateCapacityProviderResponse":
        """<p>Creates a capacity provider. Capacity providers are associated with a cluster and are used in capacity provider strategies to facilitate cluster auto scaling. You can create capacity providers for Amazon ECS Managed Instances and EC2 instances. Fargate has the predefined <code>FARGATE</code> and <code>FARGATE_SPOT</code> capacity providers.</p>

        Args:
            name: <p>The name of the capacity provider. Up to 255 characters are allowed. They include letters (both upper and lowercase letters), numbers, underscores (_), and hyphens (-). The name can't be prefixed with \"<code>aws</code>\", \"<code>ecs</code>\", or \"<code>fargate</code>\".</p>
            cluster: <p>The name of the cluster to associate with the capacity provider. When you create a capacity provider with Amazon ECS Managed Instances, it becomes available only within the specified cluster.</p>
            auto_scaling_group_provider: <p>The details of the Auto Scaling group for the capacity provider.</p>
            managed_instances_provider: <p>The configuration for the Amazon ECS Managed Instances provider. This configuration specifies how Amazon ECS manages Amazon EC2 instances on your behalf, including the infrastructure role, instance launch template, and tag propagation settings.</p>
            tags: <p>The metadata that you apply to the capacity provider to categorize and organize them more conveniently. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>

        Examples:
            To create a capacity provider
            This example creates a capacity provider that uses the specified Auto Scaling group MyASG and has managed scaling and manager termination protection enabled.

            >>> await client.put(name='MyCapacityProvider', auto_scaling_group_provider={'autoScalingGroupArn': 'arn:aws:autoscaling:us-east-1:123456789012:autoScalingGroup:57ffcb94-11f0-4d6d-bf60-3bac5EXAMPLE:autoScalingGroupName/MyASG', 'managedScaling': {'status': 'ENABLED', 'targetCapacity': 100}, 'managedTerminationProtection': 'ENABLED'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.create_capacity_provider_request.CreateCapacityProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.create_capacity_provider_response.CreateCapacityProviderResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.create_capacity_provider

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.create_capacity_provider.async_create_capacity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.create_capacity_provider_request.CreateCapacityProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if cluster is not None:
            input_["cluster"] = cluster
        if auto_scaling_group_provider is not None:
            input_["auto_scaling_group_provider"] = auto_scaling_group_provider
        if managed_instances_provider is not None:
            input_["managed_instances_provider"] = managed_instances_provider
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        name: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        auto_scaling_group_provider: Optional[
            "aws_sdk_ecs.types.auto_scaling_group_provider_update.AutoScalingGroupProviderUpdate"
        ] = None,
        managed_instances_provider: Optional[
            "aws_sdk_ecs.types.update_managed_instances_provider_configuration.UpdateManagedInstancesProviderConfiguration"
        ] = None,
    ) -> "aws_sdk_ecs.types.update_capacity_provider_response.UpdateCapacityProviderResponse":
        """<p>Modifies the parameters for a capacity provider.</p> <p>These changes only apply to new Amazon ECS Managed Instances, or EC2 instances, not existing ones.</p>

        Args:
            name: <p>The name of the capacity provider to update.</p>
            cluster: <p>The name of the cluster that contains the capacity provider to update. Managed instances capacity providers are cluster-scoped and can only be updated within their associated cluster.</p>
            auto_scaling_group_provider: <p>An object that represent the parameters to update for the Auto Scaling group capacity provider.</p>
            managed_instances_provider: <p>The updated configuration for the Amazon ECS Managed Instances provider. You can modify the infrastructure role, instance launch template, and tag propagation settings. Changes take effect for new instances launched after the update.</p>

        Examples:
            To update a capacity provider's parameters
            This example updates the targetCapacity and instanceWarmupPeriod parameters for the capacity provider MyCapacityProvider to 90 and 150 respectively.

            >>> await client.update(name='MyCapacityProvider', auto_scaling_group_provider={'managedScaling': {'status': 'ENABLED', 'targetCapacity': 90, 'instanceWarmupPeriod': 150}})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.update_capacity_provider_request.UpdateCapacityProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.update_capacity_provider_response.UpdateCapacityProviderResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_capacity_provider

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.update_capacity_provider.async_update_capacity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.update_capacity_provider_request.UpdateCapacityProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if cluster is not None:
            input_["cluster"] = cluster
        if auto_scaling_group_provider is not None:
            input_["auto_scaling_group_provider"] = auto_scaling_group_provider
        if managed_instances_provider is not None:
            input_["managed_instances_provider"] = managed_instances_provider

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        capacity_provider: "aws_sdk_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.delete_capacity_provider_response.DeleteCapacityProviderResponse":
        """<p>Deletes the specified capacity provider.</p> <note> <p>The <code>FARGATE</code> and <code>FARGATE_SPOT</code> capacity providers are reserved and can't be deleted. You can disassociate them from a cluster using either <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html\">PutClusterCapacityProviders</a> or by deleting the cluster.</p> </note> <p>Prior to a capacity provider being deleted, the capacity provider must be removed from the capacity provider strategy from all services. The <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html\">UpdateService</a> API can be used to remove a capacity provider from a service's capacity provider strategy. When updating a service, the <code>forceNewDeployment</code> option can be used to ensure that any tasks using the Amazon EC2 instance capacity provided by the capacity provider are transitioned to use the capacity from the remaining capacity providers. Only capacity providers that aren't associated with a cluster can be deleted. To remove a capacity provider from a cluster, you can either use <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html\">PutClusterCapacityProviders</a> or delete the cluster.</p>

        Args:
            capacity_provider: <p>The short name or full Amazon Resource Name (ARN) of the capacity provider to delete.</p>
            cluster: <p>The name of the cluster that contains the capacity provider to delete. Managed instances capacity providers are cluster-scoped and can only be deleted from their associated cluster.</p>

        Examples:
            To delete a specified capacity provider
            This example deletes a specified capacity provider.

            >>> await client.delete(capacity_provider='arn:aws:ecs:us-west-2:123456789012:capacity-provider/ExampleCapacityProvider')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.delete_capacity_provider_request.DeleteCapacityProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.delete_capacity_provider_response.DeleteCapacityProviderResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_capacity_provider

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.delete_capacity_provider.async_delete_capacity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.delete_capacity_provider_request.DeleteCapacityProviderRequest = {}  # type: ignore[typeddict-item]
        input_["capacity_provider"] = capacity_provider
        if cluster is not None:
            input_["cluster"] = cluster

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_capacity_providers(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        capacity_providers: Optional["aws_sdk_ecs.types.string_list.StringList"] = None,
        cluster: Optional["aws_sdk_ecs.types.string.String"] = None,
        include: Optional[
            "aws_sdk_ecs.types.capacity_provider_field_list.CapacityProviderFieldList"
        ] = None,
        max_results: Optional["aws_sdk_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["aws_sdk_ecs.types.string.String"] = None,
    ) -> "aws_sdk_ecs.types.describe_capacity_providers_response.DescribeCapacityProvidersResponse":
        """<p>Describes one or more of your capacity providers.</p>

        Args:
            capacity_providers: <p>The short name or full Amazon Resource Name (ARN) of one or more capacity providers. Up to <code>100</code> capacity providers can be described in an action.</p>
            cluster: <p>The name of the cluster to describe capacity providers for. When specified, only capacity providers associated with this cluster are returned, including Amazon ECS Managed Instances capacity providers.</p>
            include: <p>Specifies whether or not you want to see the resource tags for the capacity provider. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>
            max_results: <p>The maximum number of account setting results returned by <code>DescribeCapacityProviders</code> in paginated output. When this parameter is used, <code>DescribeCapacityProviders</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeCapacityProviders</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 10. If this parameter is not used, then <code>DescribeCapacityProviders</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeCapacityProviders</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Examples:
            To describe all capacity providers
            This example retrieves details about all capacity providers.

            >>> await client.describe_capacity_providers()
            To describe a specific capacity provider
            This example retrieves details about the capacity provider MyCapacityProvider

            >>> await client.describe_capacity_providers(capacity_providers=['MyCapacityProvider'], include=['TAGS'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ecs.types.describe_capacity_providers_request.DescribeCapacityProvidersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ecs.types.describe_capacity_providers_response.DescribeCapacityProvidersResponse"
        ]:
            import aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_capacity_providers

            (
                output,
                http_response,
            ) = await aws_sdk_ecs._operations.amazon_ec2_container_service_v20141113.describe_capacity_providers.async_describe_capacity_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ecs.types.describe_capacity_providers_request.DescribeCapacityProvidersRequest = {}  # type: ignore[typeddict-item]
        if capacity_providers is not None:
            input_["capacity_providers"] = capacity_providers
        if cluster is not None:
            input_["cluster"] = cluster
        if include is not None:
            input_["include"] = include
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
