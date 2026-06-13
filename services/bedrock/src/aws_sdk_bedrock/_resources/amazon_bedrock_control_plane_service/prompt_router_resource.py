from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock._auth._signers
import aws_sdk_bedrock._auth._sigv4
from aws_sdk_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.create_prompt_router_request
    import aws_sdk_bedrock.types.create_prompt_router_response
    import aws_sdk_bedrock.types.delete_prompt_router_request
    import aws_sdk_bedrock.types.delete_prompt_router_response
    import aws_sdk_bedrock.types.get_prompt_router_request
    import aws_sdk_bedrock.types.get_prompt_router_response
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.list_prompt_routers_request
    import aws_sdk_bedrock.types.list_prompt_routers_response
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.prompt_router_arn
    import aws_sdk_bedrock.types.prompt_router_description
    import aws_sdk_bedrock.types.prompt_router_name
    import aws_sdk_bedrock.types.prompt_router_summary
    import aws_sdk_bedrock.types.prompt_router_target_model
    import aws_sdk_bedrock.types.prompt_router_target_models
    import aws_sdk_bedrock.types.prompt_router_type
    import aws_sdk_bedrock.types.routing_criteria
    import aws_sdk_bedrock.types.tag_list
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class PromptRouterResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create(
        self,
        prompt_router_name: "aws_sdk_bedrock.types.prompt_router_name.PromptRouterName",
        models: "aws_sdk_bedrock.types.prompt_router_target_models.PromptRouterTargetModels",
        routing_criteria: "aws_sdk_bedrock.types.routing_criteria.RoutingCriteria",
        fallback_model: "aws_sdk_bedrock.types.prompt_router_target_model.PromptRouterTargetModel",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock.types.prompt_router_description.PromptRouterDescription"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
    ) -> (
        "aws_sdk_bedrock.types.create_prompt_router_response.CreatePromptRouterResponse"
    ):
        """<p>Creates a prompt router that manages the routing of requests between multiple foundation models based on the routing criteria.</p>

        Args:
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of your requests. If not specified, the Amazon Web Services SDK automatically generates one for you.</p>
            prompt_router_name: <p>The name of the prompt router. The name must be unique within your Amazon Web Services account in the current region.</p>
            models: <p>A list of foundation models that the prompt router can route requests to. At least one model must be specified.</p>
            description: <p>An optional description of the prompt router to help identify its purpose.</p>
            routing_criteria: <p>The criteria, which is the response quality difference, used to determine how incoming requests are routed to different models.</p>
            fallback_model: <p>The default model to use when the routing criteria is not met.</p>
            tags: <p>An array of key-value pairs to apply to this resource as tags. You can use tags to categorize and manage your Amazon Web Services resources.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.create_prompt_router_response.CreatePromptRouterResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_prompt_router

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_prompt_router.create_prompt_router(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest = {}  # type: ignore[typeddict-item]
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        input["prompt_router_name"] = prompt_router_name
        input["models"] = models
        if description is not None:
            input["description"] = description
        input["routing_criteria"] = routing_criteria
        input["fallback_model"] = fallback_model
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
        prompt_router_arn: "aws_sdk_bedrock.types.prompt_router_arn.PromptRouterArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_prompt_router_response.GetPromptRouterResponse":
        """<p>Retrieves details about a prompt router.</p>

        Args:
            prompt_router_arn: <p>The prompt router's ARN</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_prompt_router_request.GetPromptRouterRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_prompt_router_response.GetPromptRouterResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_prompt_router

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_prompt_router.get_prompt_router(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_prompt_router_request.GetPromptRouterRequest = {}  # type: ignore[typeddict-item]
        input["prompt_router_arn"] = prompt_router_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        prompt_router_arn: "aws_sdk_bedrock.types.prompt_router_arn.PromptRouterArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock.types.delete_prompt_router_response.DeletePromptRouterResponse"
    ):
        """<p>Deletes a specified prompt router. This action cannot be undone.</p>

        Args:
            prompt_router_arn: <p>The Amazon Resource Name (ARN) of the prompt router to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.delete_prompt_router_request.DeletePromptRouterRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.delete_prompt_router_response.DeletePromptRouterResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_prompt_router

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_prompt_router.delete_prompt_router(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_prompt_router_request.DeletePromptRouterRequest = {}  # type: ignore[typeddict-item]
        input["prompt_router_arn"] = prompt_router_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        type: Optional[
            "aws_sdk_bedrock.types.prompt_router_type.PromptRouterType"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse":
        """<p>Retrieves a list of prompt routers.</p>

        Args:
            max_results: <p>The maximum number of prompt routers to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            type: <p>The type of the prompt routers, such as whether it's default or custom.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_prompt_routers_request.ListPromptRoutersRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_prompt_routers

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_prompt_routers.list_prompt_routers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_prompt_routers_request.ListPromptRoutersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if type is not None:
            input["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncPromptRouterResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create(
        self,
        prompt_router_name: "aws_sdk_bedrock.types.prompt_router_name.PromptRouterName",
        models: "aws_sdk_bedrock.types.prompt_router_target_models.PromptRouterTargetModels",
        routing_criteria: "aws_sdk_bedrock.types.routing_criteria.RoutingCriteria",
        fallback_model: "aws_sdk_bedrock.types.prompt_router_target_model.PromptRouterTargetModel",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock.types.prompt_router_description.PromptRouterDescription"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
    ) -> (
        "aws_sdk_bedrock.types.create_prompt_router_response.CreatePromptRouterResponse"
    ):
        """<p>Creates a prompt router that manages the routing of requests between multiple foundation models based on the routing criteria.</p>

        Args:
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of your requests. If not specified, the Amazon Web Services SDK automatically generates one for you.</p>
            prompt_router_name: <p>The name of the prompt router. The name must be unique within your Amazon Web Services account in the current region.</p>
            models: <p>A list of foundation models that the prompt router can route requests to. At least one model must be specified.</p>
            description: <p>An optional description of the prompt router to help identify its purpose.</p>
            routing_criteria: <p>The criteria, which is the response quality difference, used to determine how incoming requests are routed to different models.</p>
            fallback_model: <p>The default model to use when the routing criteria is not met.</p>
            tags: <p>An array of key-value pairs to apply to this resource as tags. You can use tags to categorize and manage your Amazon Web Services resources.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.create_prompt_router_response.CreatePromptRouterResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_prompt_router

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_prompt_router.async_create_prompt_router(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest = {}  # type: ignore[typeddict-item]
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        input["prompt_router_name"] = prompt_router_name
        input["models"] = models
        if description is not None:
            input["description"] = description
        input["routing_criteria"] = routing_criteria
        input["fallback_model"] = fallback_model
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
        prompt_router_arn: "aws_sdk_bedrock.types.prompt_router_arn.PromptRouterArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_prompt_router_response.GetPromptRouterResponse":
        """<p>Retrieves details about a prompt router.</p>

        Args:
            prompt_router_arn: <p>The prompt router's ARN</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_prompt_router_request.GetPromptRouterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_prompt_router_response.GetPromptRouterResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_prompt_router

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_prompt_router.async_get_prompt_router(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_prompt_router_request.GetPromptRouterRequest = {}  # type: ignore[typeddict-item]
        input["prompt_router_arn"] = prompt_router_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        prompt_router_arn: "aws_sdk_bedrock.types.prompt_router_arn.PromptRouterArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock.types.delete_prompt_router_response.DeletePromptRouterResponse"
    ):
        """<p>Deletes a specified prompt router. This action cannot be undone.</p>

        Args:
            prompt_router_arn: <p>The Amazon Resource Name (ARN) of the prompt router to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.delete_prompt_router_request.DeletePromptRouterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.delete_prompt_router_response.DeletePromptRouterResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_prompt_router

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_prompt_router.async_delete_prompt_router(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_prompt_router_request.DeletePromptRouterRequest = {}  # type: ignore[typeddict-item]
        input["prompt_router_arn"] = prompt_router_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        type: Optional[
            "aws_sdk_bedrock.types.prompt_router_type.PromptRouterType"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse":
        """<p>Retrieves a list of prompt routers.</p>

        Args:
            max_results: <p>The maximum number of prompt routers to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            type: <p>The type of the prompt routers, such as whether it's default or custom.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_prompt_routers_request.ListPromptRoutersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_prompt_routers

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_prompt_routers.async_list_prompt_routers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_prompt_routers_request.ListPromptRoutersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if type is not None:
            input["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
