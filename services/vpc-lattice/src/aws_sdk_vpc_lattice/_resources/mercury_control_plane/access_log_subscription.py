from typing import TYPE_CHECKING, Optional

import aws_sdk_vpc_lattice._auth._signers
import aws_sdk_vpc_lattice._auth._sigv4
from aws_sdk_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.access_log_destination_arn
    import aws_sdk_vpc_lattice.types.access_log_subscription_identifier
    import aws_sdk_vpc_lattice.types.access_log_subscription_summary
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.create_access_log_subscription_request
    import aws_sdk_vpc_lattice.types.create_access_log_subscription_response
    import aws_sdk_vpc_lattice.types.delete_access_log_subscription_request
    import aws_sdk_vpc_lattice.types.delete_access_log_subscription_response
    import aws_sdk_vpc_lattice.types.get_access_log_subscription_request
    import aws_sdk_vpc_lattice.types.get_access_log_subscription_response
    import aws_sdk_vpc_lattice.types.list_access_log_subscriptions_request
    import aws_sdk_vpc_lattice.types.list_access_log_subscriptions_response
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.resource_identifier
    import aws_sdk_vpc_lattice.types.service_network_log_type
    import aws_sdk_vpc_lattice.types.tag_map
    import aws_sdk_vpc_lattice.types.update_access_log_subscription_request
    import aws_sdk_vpc_lattice.types.update_access_log_subscription_response
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class AccessLogSubscription:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        resource_identifier: "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        destination_arn: "aws_sdk_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        service_network_log_type: Optional[
            "aws_sdk_vpc_lattice.types.service_network_log_type.ServiceNetworkLogType"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_access_log_subscription_response.CreateAccessLogSubscriptionResponse":
        """<p>Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner can only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html\">Access logs</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
            destination_arn: <p>The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.</p>
            service_network_log_type: <p>The type of log that monitors your Amazon VPC Lattice service networks.</p>
            tags: <p>The tags for the access log subscription.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.create_access_log_subscription_request.CreateAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.create_access_log_subscription_response.CreateAccessLogSubscriptionResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_access_log_subscription

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.create_access_log_subscription.create_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.create_access_log_subscription_request.CreateAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["resource_identifier"] = resource_identifier
        input["destination_arn"] = destination_arn
        if service_network_log_type is not None:
            input["service_network_log_type"] = service_network_log_type
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        access_log_subscription_identifier: "aws_sdk_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_access_log_subscription_response.GetAccessLogSubscriptionResponse":
        """<p>Retrieves information about the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_access_log_subscription_request.GetAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_access_log_subscription_response.GetAccessLogSubscriptionResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_access_log_subscription

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_access_log_subscription.get_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.get_access_log_subscription_request.GetAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input["access_log_subscription_identifier"] = access_log_subscription_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        access_log_subscription_identifier: "aws_sdk_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        destination_arn: "aws_sdk_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_access_log_subscription_response.UpdateAccessLogSubscriptionResponse":
        """<p>Updates the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>
            destination_arn: <p>The Amazon Resource Name (ARN) of the access log destination.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.update_access_log_subscription_request.UpdateAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.update_access_log_subscription_response.UpdateAccessLogSubscriptionResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_access_log_subscription

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.update_access_log_subscription.update_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.update_access_log_subscription_request.UpdateAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input["access_log_subscription_identifier"] = access_log_subscription_identifier
        input["destination_arn"] = destination_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        access_log_subscription_identifier: "aws_sdk_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_access_log_subscription_response.DeleteAccessLogSubscriptionResponse":
        """<p>Deletes the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_access_log_subscription_request.DeleteAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_access_log_subscription_response.DeleteAccessLogSubscriptionResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_access_log_subscription

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_access_log_subscription.delete_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.delete_access_log_subscription_request.DeleteAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input["access_log_subscription_identifier"] = access_log_subscription_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        resource_identifier: "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_access_log_subscriptions_response.ListAccessLogSubscriptionsResponse":
        """<p>Lists the access log subscriptions for the specified service network or service.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_access_log_subscriptions_request.ListAccessLogSubscriptionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_access_log_subscriptions_response.ListAccessLogSubscriptionsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_access_log_subscriptions

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_access_log_subscriptions.list_access_log_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.list_access_log_subscriptions_request.ListAccessLogSubscriptionsRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAccessLogSubscription:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        resource_identifier: "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        destination_arn: "aws_sdk_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        service_network_log_type: Optional[
            "aws_sdk_vpc_lattice.types.service_network_log_type.ServiceNetworkLogType"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_access_log_subscription_response.CreateAccessLogSubscriptionResponse":
        """<p>Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner can only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html\">Access logs</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
            destination_arn: <p>The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.</p>
            service_network_log_type: <p>The type of log that monitors your Amazon VPC Lattice service networks.</p>
            tags: <p>The tags for the access log subscription.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.create_access_log_subscription_request.CreateAccessLogSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.create_access_log_subscription_response.CreateAccessLogSubscriptionResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_access_log_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.create_access_log_subscription.async_create_access_log_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.create_access_log_subscription_request.CreateAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["resource_identifier"] = resource_identifier
        input["destination_arn"] = destination_arn
        if service_network_log_type is not None:
            input["service_network_log_type"] = service_network_log_type
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        access_log_subscription_identifier: "aws_sdk_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_access_log_subscription_response.GetAccessLogSubscriptionResponse":
        """<p>Retrieves information about the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_access_log_subscription_request.GetAccessLogSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_access_log_subscription_response.GetAccessLogSubscriptionResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_access_log_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_access_log_subscription.async_get_access_log_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.get_access_log_subscription_request.GetAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input["access_log_subscription_identifier"] = access_log_subscription_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        access_log_subscription_identifier: "aws_sdk_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        destination_arn: "aws_sdk_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_access_log_subscription_response.UpdateAccessLogSubscriptionResponse":
        """<p>Updates the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>
            destination_arn: <p>The Amazon Resource Name (ARN) of the access log destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.update_access_log_subscription_request.UpdateAccessLogSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.update_access_log_subscription_response.UpdateAccessLogSubscriptionResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_access_log_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.update_access_log_subscription.async_update_access_log_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.update_access_log_subscription_request.UpdateAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input["access_log_subscription_identifier"] = access_log_subscription_identifier
        input["destination_arn"] = destination_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        access_log_subscription_identifier: "aws_sdk_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_access_log_subscription_response.DeleteAccessLogSubscriptionResponse":
        """<p>Deletes the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_access_log_subscription_request.DeleteAccessLogSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_access_log_subscription_response.DeleteAccessLogSubscriptionResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_access_log_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_access_log_subscription.async_delete_access_log_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.delete_access_log_subscription_request.DeleteAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input["access_log_subscription_identifier"] = access_log_subscription_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        resource_identifier: "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_access_log_subscriptions_response.ListAccessLogSubscriptionsResponse":
        """<p>Lists the access log subscriptions for the specified service network or service.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_access_log_subscriptions_request.ListAccessLogSubscriptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_access_log_subscriptions_response.ListAccessLogSubscriptionsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_access_log_subscriptions

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_access_log_subscriptions.async_list_access_log_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.list_access_log_subscriptions_request.ListAccessLogSubscriptionsRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
