from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock._services.async_bedrock import ensure_async_iterator
from aws_sdk_bedrock._services.bedrock import ensure_sync_iterator
from aws_sdk_bedrock._services._pipeline import (
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
)
import aws_sdk_bedrock._auth._signers
import aws_sdk_bedrock._auth._sigv4

if TYPE_CHECKING:
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    import aws_sdk_bedrock.types.accept_eula
    import aws_sdk_bedrock.types.arn
    import aws_sdk_bedrock.types.create_marketplace_model_endpoint_request
    import aws_sdk_bedrock.types.create_marketplace_model_endpoint_response
    import aws_sdk_bedrock.types.delete_marketplace_model_endpoint_request
    import aws_sdk_bedrock.types.delete_marketplace_model_endpoint_response
    import aws_sdk_bedrock.types.deregister_marketplace_model_endpoint_request
    import aws_sdk_bedrock.types.deregister_marketplace_model_endpoint_response
    import aws_sdk_bedrock.types.endpoint_config
    import aws_sdk_bedrock.types.endpoint_name
    import aws_sdk_bedrock.types.get_marketplace_model_endpoint_request
    import aws_sdk_bedrock.types.get_marketplace_model_endpoint_response
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.list_marketplace_model_endpoints_request
    import aws_sdk_bedrock.types.list_marketplace_model_endpoints_response
    import aws_sdk_bedrock.types.marketplace_model_endpoint_summary
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.model_source_identifier
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.register_marketplace_model_endpoint_request
    import aws_sdk_bedrock.types.register_marketplace_model_endpoint_response
    import aws_sdk_bedrock.types.tag_list
    import aws_sdk_bedrock.types.update_marketplace_model_endpoint_request
    import aws_sdk_bedrock.types.update_marketplace_model_endpoint_response


class BedrockMarketplaceResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create_marketplace_model_endpoint(
        self,
        model_source_identifier: "aws_sdk_bedrock.types.model_source_identifier.ModelSourceIdentifier",
        endpoint_config: "aws_sdk_bedrock.types.endpoint_config.EndpointConfig",
        endpoint_name: "aws_sdk_bedrock.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        accept_eula: Optional["aws_sdk_bedrock.types.accept_eula.AcceptEula"] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock.types.create_marketplace_model_endpoint_response.CreateMarketplaceModelEndpointResponse":
        """<p>Creates an endpoint for a model from Amazon Bedrock Marketplace. The endpoint is hosted by Amazon SageMaker.</p>

        Args:
            model_source_identifier: <p>The ARN of the model from Amazon Bedrock Marketplace that you want to deploy to the endpoint.</p>
            endpoint_config: <p>The configuration for the endpoint, including the number and type of instances to use.</p>
            accept_eula: <p>Indicates whether you accept the end-user license agreement (EULA) for the model. Set to <code>true</code> to accept the EULA.</p>
            endpoint_name: <p>The name of the endpoint. This name must be unique within your Amazon Web Services account and region.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>
            tags: <p>An array of key-value pairs to apply to the underlying Amazon SageMaker endpoint. You can use these tags to organize and identify your Amazon Web Services resources.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.create_marketplace_model_endpoint_request.CreateMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.create_marketplace_model_endpoint_response.CreateMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_marketplace_model_endpoint

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_marketplace_model_endpoint.create_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_marketplace_model_endpoint_request.CreateMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["model_source_identifier"] = model_source_identifier
        input["endpoint_config"] = endpoint_config
        if accept_eula is not None:
            input["accept_eula"] = accept_eula
        input["endpoint_name"] = endpoint_name
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_marketplace_model_endpoint(
        self,
        endpoint_arn: "aws_sdk_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_marketplace_model_endpoint_response.DeleteMarketplaceModelEndpointResponse":
        """<p>Deletes an endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.delete_marketplace_model_endpoint_request.DeleteMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.delete_marketplace_model_endpoint_response.DeleteMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_marketplace_model_endpoint

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_marketplace_model_endpoint.delete_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_marketplace_model_endpoint_request.DeleteMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["endpoint_arn"] = endpoint_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deregister_marketplace_model_endpoint(
        self,
        endpoint_arn: "aws_sdk_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.deregister_marketplace_model_endpoint_response.DeregisterMarketplaceModelEndpointResponse":
        """<p>Deregisters an endpoint for a model from Amazon Bedrock Marketplace. This operation removes the endpoint's association with Amazon Bedrock but does not delete the underlying Amazon SageMaker endpoint.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to deregister.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.deregister_marketplace_model_endpoint_request.DeregisterMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.deregister_marketplace_model_endpoint_response.DeregisterMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.deregister_marketplace_model_endpoint

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.deregister_marketplace_model_endpoint.deregister_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.deregister_marketplace_model_endpoint_request.DeregisterMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["endpoint_arn"] = endpoint_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_marketplace_model_endpoint(
        self,
        endpoint_arn: "aws_sdk_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_marketplace_model_endpoint_response.GetMarketplaceModelEndpointResponse":
        """<p>Retrieves details about a specific endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to get information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_marketplace_model_endpoint_request.GetMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_marketplace_model_endpoint_response.GetMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_marketplace_model_endpoint

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_marketplace_model_endpoint.get_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_marketplace_model_endpoint_request.GetMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["endpoint_arn"] = endpoint_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_marketplace_model_endpoints(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        model_source_equals: Optional[
            "aws_sdk_bedrock.types.model_source_identifier.ModelSourceIdentifier"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_marketplace_model_endpoints_response.ListMarketplaceModelEndpointsResponse":
        """<p>Lists the endpoints for models from Amazon Bedrock Marketplace in your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. If more results are available, the operation returns a <code>NextToken</code> value.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous <code>ListMarketplaceModelEndpoints</code> call.</p>
            model_source_equals: <p>If specified, only endpoints for the given model source identifier are returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_marketplace_model_endpoints_request.ListMarketplaceModelEndpointsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_marketplace_model_endpoints_response.ListMarketplaceModelEndpointsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_marketplace_model_endpoints

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_marketplace_model_endpoints.list_marketplace_model_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_marketplace_model_endpoints_request.ListMarketplaceModelEndpointsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if model_source_equals is not None:
            input["model_source_equals"] = model_source_equals

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_marketplace_model_endpoint(
        self,
        endpoint_identifier: "aws_sdk_bedrock.types.arn.Arn",
        model_source_identifier: "aws_sdk_bedrock.types.model_source_identifier.ModelSourceIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.register_marketplace_model_endpoint_response.RegisterMarketplaceModelEndpointResponse":
        """<p>Registers an existing Amazon SageMaker endpoint with Amazon Bedrock Marketplace, allowing it to be used with Amazon Bedrock APIs.</p>

        Args:
            endpoint_identifier: <p>The ARN of the Amazon SageMaker endpoint you want to register with Amazon Bedrock Marketplace.</p>
            model_source_identifier: <p>The ARN of the model from Amazon Bedrock Marketplace that is deployed on the endpoint.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.register_marketplace_model_endpoint_request.RegisterMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.register_marketplace_model_endpoint_response.RegisterMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.register_marketplace_model_endpoint

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.register_marketplace_model_endpoint.register_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.register_marketplace_model_endpoint_request.RegisterMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["endpoint_identifier"] = endpoint_identifier
        input["model_source_identifier"] = model_source_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_marketplace_model_endpoint(
        self,
        endpoint_arn: "aws_sdk_bedrock.types.arn.Arn",
        endpoint_config: "aws_sdk_bedrock.types.endpoint_config.EndpointConfig",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "aws_sdk_bedrock.types.update_marketplace_model_endpoint_response.UpdateMarketplaceModelEndpointResponse":
        """<p>Updates the configuration of an existing endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to update.</p>
            endpoint_config: <p>The new configuration for the endpoint, including the number and type of instances to use.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.update_marketplace_model_endpoint_request.UpdateMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.update_marketplace_model_endpoint_response.UpdateMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.update_marketplace_model_endpoint

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.update_marketplace_model_endpoint.update_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.update_marketplace_model_endpoint_request.UpdateMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["endpoint_arn"] = endpoint_arn
        input["endpoint_config"] = endpoint_config
        if client_request_token is not None:
            input["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncBedrockMarketplaceResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create_marketplace_model_endpoint(
        self,
        model_source_identifier: "aws_sdk_bedrock.types.model_source_identifier.ModelSourceIdentifier",
        endpoint_config: "aws_sdk_bedrock.types.endpoint_config.EndpointConfig",
        endpoint_name: "aws_sdk_bedrock.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        accept_eula: Optional["aws_sdk_bedrock.types.accept_eula.AcceptEula"] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock.types.create_marketplace_model_endpoint_response.CreateMarketplaceModelEndpointResponse":
        """<p>Creates an endpoint for a model from Amazon Bedrock Marketplace. The endpoint is hosted by Amazon SageMaker.</p>

        Args:
            model_source_identifier: <p>The ARN of the model from Amazon Bedrock Marketplace that you want to deploy to the endpoint.</p>
            endpoint_config: <p>The configuration for the endpoint, including the number and type of instances to use.</p>
            accept_eula: <p>Indicates whether you accept the end-user license agreement (EULA) for the model. Set to <code>true</code> to accept the EULA.</p>
            endpoint_name: <p>The name of the endpoint. This name must be unique within your Amazon Web Services account and region.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>
            tags: <p>An array of key-value pairs to apply to the underlying Amazon SageMaker endpoint. You can use these tags to organize and identify your Amazon Web Services resources.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.create_marketplace_model_endpoint_request.CreateMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.create_marketplace_model_endpoint_response.CreateMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_marketplace_model_endpoint.async_create_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_marketplace_model_endpoint_request.CreateMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["model_source_identifier"] = model_source_identifier
        input["endpoint_config"] = endpoint_config
        if accept_eula is not None:
            input["accept_eula"] = accept_eula
        input["endpoint_name"] = endpoint_name
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_marketplace_model_endpoint(
        self,
        endpoint_arn: "aws_sdk_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_marketplace_model_endpoint_response.DeleteMarketplaceModelEndpointResponse":
        """<p>Deletes an endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.delete_marketplace_model_endpoint_request.DeleteMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.delete_marketplace_model_endpoint_response.DeleteMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_marketplace_model_endpoint.async_delete_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_marketplace_model_endpoint_request.DeleteMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["endpoint_arn"] = endpoint_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def deregister_marketplace_model_endpoint(
        self,
        endpoint_arn: "aws_sdk_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.deregister_marketplace_model_endpoint_response.DeregisterMarketplaceModelEndpointResponse":
        """<p>Deregisters an endpoint for a model from Amazon Bedrock Marketplace. This operation removes the endpoint's association with Amazon Bedrock but does not delete the underlying Amazon SageMaker endpoint.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to deregister.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.deregister_marketplace_model_endpoint_request.DeregisterMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.deregister_marketplace_model_endpoint_response.DeregisterMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.deregister_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.deregister_marketplace_model_endpoint.async_deregister_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.deregister_marketplace_model_endpoint_request.DeregisterMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["endpoint_arn"] = endpoint_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_marketplace_model_endpoint(
        self,
        endpoint_arn: "aws_sdk_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_marketplace_model_endpoint_response.GetMarketplaceModelEndpointResponse":
        """<p>Retrieves details about a specific endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to get information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_marketplace_model_endpoint_request.GetMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_marketplace_model_endpoint_response.GetMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_marketplace_model_endpoint.async_get_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_marketplace_model_endpoint_request.GetMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["endpoint_arn"] = endpoint_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_marketplace_model_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        model_source_equals: Optional[
            "aws_sdk_bedrock.types.model_source_identifier.ModelSourceIdentifier"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_marketplace_model_endpoints_response.ListMarketplaceModelEndpointsResponse":
        """<p>Lists the endpoints for models from Amazon Bedrock Marketplace in your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. If more results are available, the operation returns a <code>NextToken</code> value.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous <code>ListMarketplaceModelEndpoints</code> call.</p>
            model_source_equals: <p>If specified, only endpoints for the given model source identifier are returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_marketplace_model_endpoints_request.ListMarketplaceModelEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_marketplace_model_endpoints_response.ListMarketplaceModelEndpointsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_marketplace_model_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_marketplace_model_endpoints.async_list_marketplace_model_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_marketplace_model_endpoints_request.ListMarketplaceModelEndpointsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if model_source_equals is not None:
            input["model_source_equals"] = model_source_equals

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def register_marketplace_model_endpoint(
        self,
        endpoint_identifier: "aws_sdk_bedrock.types.arn.Arn",
        model_source_identifier: "aws_sdk_bedrock.types.model_source_identifier.ModelSourceIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.register_marketplace_model_endpoint_response.RegisterMarketplaceModelEndpointResponse":
        """<p>Registers an existing Amazon SageMaker endpoint with Amazon Bedrock Marketplace, allowing it to be used with Amazon Bedrock APIs.</p>

        Args:
            endpoint_identifier: <p>The ARN of the Amazon SageMaker endpoint you want to register with Amazon Bedrock Marketplace.</p>
            model_source_identifier: <p>The ARN of the model from Amazon Bedrock Marketplace that is deployed on the endpoint.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.register_marketplace_model_endpoint_request.RegisterMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.register_marketplace_model_endpoint_response.RegisterMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.register_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.register_marketplace_model_endpoint.async_register_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.register_marketplace_model_endpoint_request.RegisterMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["endpoint_identifier"] = endpoint_identifier
        input["model_source_identifier"] = model_source_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_marketplace_model_endpoint(
        self,
        endpoint_arn: "aws_sdk_bedrock.types.arn.Arn",
        endpoint_config: "aws_sdk_bedrock.types.endpoint_config.EndpointConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "aws_sdk_bedrock.types.update_marketplace_model_endpoint_response.UpdateMarketplaceModelEndpointResponse":
        """<p>Updates the configuration of an existing endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to update.</p>
            endpoint_config: <p>The new configuration for the endpoint, including the number and type of instances to use.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.update_marketplace_model_endpoint_request.UpdateMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.update_marketplace_model_endpoint_response.UpdateMarketplaceModelEndpointResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.update_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.update_marketplace_model_endpoint.async_update_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.update_marketplace_model_endpoint_request.UpdateMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
        input["endpoint_arn"] = endpoint_arn
        input["endpoint_config"] = endpoint_config
        if client_request_token is not None:
            input["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
