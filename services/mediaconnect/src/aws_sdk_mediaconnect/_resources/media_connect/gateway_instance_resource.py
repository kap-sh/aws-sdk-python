from typing import TYPE_CHECKING, Optional

import aws_sdk_mediaconnect._auth._signers
import aws_sdk_mediaconnect._auth._sigv4
from aws_sdk_mediaconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge_placement
    import aws_sdk_mediaconnect.types.deregister_gateway_instance_request
    import aws_sdk_mediaconnect.types.deregister_gateway_instance_response
    import aws_sdk_mediaconnect.types.describe_gateway_instance_request
    import aws_sdk_mediaconnect.types.describe_gateway_instance_response
    import aws_sdk_mediaconnect.types.gateway_instance_arn
    import aws_sdk_mediaconnect.types.list_gateway_instances_request
    import aws_sdk_mediaconnect.types.list_gateway_instances_response
    import aws_sdk_mediaconnect.types.listed_gateway_instance
    import aws_sdk_mediaconnect.types.max_results
    import aws_sdk_mediaconnect.types.update_gateway_instance_request
    import aws_sdk_mediaconnect.types.update_gateway_instance_response
    from aws_sdk_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from aws_sdk_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class GatewayInstanceResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def read(
        self,
        gateway_instance_arn: "aws_sdk_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.describe_gateway_instance_response.DescribeGatewayInstanceResponse":
        """<p> Displays the details of an instance. </p>

        Args:
            gateway_instance_arn: <p> The Amazon Resource Name (ARN) of the gateway instance that you want to describe.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.describe_gateway_instance_request.DescribeGatewayInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.describe_gateway_instance_response.DescribeGatewayInstanceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_gateway_instance

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.describe_gateway_instance.describe_gateway_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.describe_gateway_instance_request.DescribeGatewayInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_instance_arn"] = gateway_instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        gateway_instance_arn: "aws_sdk_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        bridge_placement: Optional[
            "aws_sdk_mediaconnect.types.bridge_placement.BridgePlacement"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_gateway_instance_response.UpdateGatewayInstanceResponse":
        """<p>Updates an existing gateway instance. </p>

        Args:
            bridge_placement: <p>The state of the instance. <code>ACTIVE</code> or <code>INACTIVE</code>. </p>
            gateway_instance_arn: <p>The Amazon Resource Name (ARN) of the gateway instance that you want to update. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.update_gateway_instance_request.UpdateGatewayInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.update_gateway_instance_response.UpdateGatewayInstanceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_gateway_instance

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.update_gateway_instance.update_gateway_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.update_gateway_instance_request.UpdateGatewayInstanceRequest = {}  # type: ignore[typeddict-item]
        if bridge_placement is not None:
            input_["bridge_placement"] = bridge_placement
        input_["gateway_instance_arn"] = gateway_instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        gateway_instance_arn: "aws_sdk_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "aws_sdk_mediaconnect.types.deregister_gateway_instance_response.DeregisterGatewayInstanceResponse":
        """<p> Deregisters an instance. Before you deregister an instance, all bridges running on the instance must be stopped. If you want to deregister an instance without stopping the bridges, you must use the --force option.</p>

        Args:
            force: <p> Force the deregistration of an instance. Force will deregister an instance, even if there are bridges running on it.</p>
            gateway_instance_arn: <p> The Amazon Resource Name (ARN) of the gateway that contains the instance that you want to deregister.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.deregister_gateway_instance_request.DeregisterGatewayInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.deregister_gateway_instance_response.DeregisterGatewayInstanceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.deregister_gateway_instance

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.deregister_gateway_instance.deregister_gateway_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.deregister_gateway_instance_request.DeregisterGatewayInstanceRequest = {}  # type: ignore[typeddict-item]
        if force is not None:
            input_["force"] = force
        input_["gateway_instance_arn"] = gateway_instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        filter_arn: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_mediaconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.list_gateway_instances_response.ListGatewayInstancesResponse":
        """<p> Displays a list of instances associated with the Amazon Web Services account. This request returns a paginated result. You can use the filterArn property to display only the instances associated with the selected Gateway Amazon Resource Name (ARN).</p>

        Args:
            filter_arn: <p> Filter the list results to display only the instances associated with the selected Gateway ARN.</p>
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a ListInstances request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListInstances</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListInstances</code> request a second time and specify the <code>NextToken</code> value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.list_gateway_instances_request.ListGatewayInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.list_gateway_instances_response.ListGatewayInstancesResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_gateway_instances

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.list_gateway_instances.list_gateway_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.list_gateway_instances_request.ListGatewayInstancesRequest = {}  # type: ignore[typeddict-item]
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
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


class AsyncGatewayInstanceResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def read(
        self,
        gateway_instance_arn: "aws_sdk_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.describe_gateway_instance_response.DescribeGatewayInstanceResponse":
        """<p> Displays the details of an instance. </p>

        Args:
            gateway_instance_arn: <p> The Amazon Resource Name (ARN) of the gateway instance that you want to describe.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.describe_gateway_instance_request.DescribeGatewayInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.describe_gateway_instance_response.DescribeGatewayInstanceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_gateway_instance

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.describe_gateway_instance.async_describe_gateway_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.describe_gateway_instance_request.DescribeGatewayInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_instance_arn"] = gateway_instance_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        gateway_instance_arn: "aws_sdk_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        bridge_placement: Optional[
            "aws_sdk_mediaconnect.types.bridge_placement.BridgePlacement"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_gateway_instance_response.UpdateGatewayInstanceResponse":
        """<p>Updates an existing gateway instance. </p>

        Args:
            bridge_placement: <p>The state of the instance. <code>ACTIVE</code> or <code>INACTIVE</code>. </p>
            gateway_instance_arn: <p>The Amazon Resource Name (ARN) of the gateway instance that you want to update. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.update_gateway_instance_request.UpdateGatewayInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.update_gateway_instance_response.UpdateGatewayInstanceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_gateway_instance

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.update_gateway_instance.async_update_gateway_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.update_gateway_instance_request.UpdateGatewayInstanceRequest = {}  # type: ignore[typeddict-item]
        if bridge_placement is not None:
            input_["bridge_placement"] = bridge_placement
        input_["gateway_instance_arn"] = gateway_instance_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        gateway_instance_arn: "aws_sdk_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "aws_sdk_mediaconnect.types.deregister_gateway_instance_response.DeregisterGatewayInstanceResponse":
        """<p> Deregisters an instance. Before you deregister an instance, all bridges running on the instance must be stopped. If you want to deregister an instance without stopping the bridges, you must use the --force option.</p>

        Args:
            force: <p> Force the deregistration of an instance. Force will deregister an instance, even if there are bridges running on it.</p>
            gateway_instance_arn: <p> The Amazon Resource Name (ARN) of the gateway that contains the instance that you want to deregister.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.deregister_gateway_instance_request.DeregisterGatewayInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.deregister_gateway_instance_response.DeregisterGatewayInstanceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.deregister_gateway_instance

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.deregister_gateway_instance.async_deregister_gateway_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.deregister_gateway_instance_request.DeregisterGatewayInstanceRequest = {}  # type: ignore[typeddict-item]
        if force is not None:
            input_["force"] = force
        input_["gateway_instance_arn"] = gateway_instance_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        filter_arn: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_mediaconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.list_gateway_instances_response.ListGatewayInstancesResponse":
        """<p> Displays a list of instances associated with the Amazon Web Services account. This request returns a paginated result. You can use the filterArn property to display only the instances associated with the selected Gateway Amazon Resource Name (ARN).</p>

        Args:
            filter_arn: <p> Filter the list results to display only the instances associated with the selected Gateway ARN.</p>
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a ListInstances request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListInstances</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListInstances</code> request a second time and specify the <code>NextToken</code> value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.list_gateway_instances_request.ListGatewayInstancesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.list_gateway_instances_response.ListGatewayInstancesResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_gateway_instances

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.list_gateway_instances.async_list_gateway_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.list_gateway_instances_request.ListGatewayInstancesRequest = {}  # type: ignore[typeddict-item]
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
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
