from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_runtime._auth._signers
import aws_sdk_bedrock_runtime._auth._sigv4
from aws_sdk_bedrock_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.async_invoke_idempotency_token
    import aws_sdk_bedrock_runtime.types.async_invoke_identifier
    import aws_sdk_bedrock_runtime.types.async_invoke_output_data_config
    import aws_sdk_bedrock_runtime.types.async_invoke_status
    import aws_sdk_bedrock_runtime.types.async_invoke_summary
    import aws_sdk_bedrock_runtime.types.get_async_invoke_request
    import aws_sdk_bedrock_runtime.types.get_async_invoke_response
    import aws_sdk_bedrock_runtime.types.invocation_arn
    import aws_sdk_bedrock_runtime.types.list_async_invokes_request
    import aws_sdk_bedrock_runtime.types.list_async_invokes_response
    import aws_sdk_bedrock_runtime.types.max_results
    import aws_sdk_bedrock_runtime.types.model_input_payload
    import aws_sdk_bedrock_runtime.types.pagination_token
    import aws_sdk_bedrock_runtime.types.sort_async_invocation_by
    import aws_sdk_bedrock_runtime.types.sort_order
    import aws_sdk_bedrock_runtime.types.start_async_invoke_request
    import aws_sdk_bedrock_runtime.types.start_async_invoke_response
    import aws_sdk_bedrock_runtime.types.tag_list
    import aws_sdk_bedrock_runtime.types.timestamp
    from aws_sdk_bedrock_runtime._services.async_bedrock_runtime import (
        AsyncBedrockRuntimeClient,
        AsyncBedrockRuntimeClientConfig,
    )
    from aws_sdk_bedrock_runtime._services.bedrock_runtime import (
        BedrockRuntimeClient,
        BedrockRuntimeClientConfig,
    )


class AsyncInvokeResource:
    def __init__(self, service: BedrockRuntimeClient) -> None:
        self._service = service

    def get_async_invoke(
        self,
        invocation_arn: "aws_sdk_bedrock_runtime.types.invocation_arn.InvocationArn",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock_runtime.types.get_async_invoke_response.GetAsyncInvokeResponse"
    ):
        """<p>Retrieve information about an asynchronous invocation.</p>

        Args:
            invocation_arn: <p>The invocation's ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_runtime.types.get_async_invoke_request.GetAsyncInvokeRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_runtime.types.get_async_invoke_response.GetAsyncInvokeResponse"
        ]:
            import aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.get_async_invoke

            output, http_response = (
                aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.get_async_invoke.get_async_invoke(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_runtime.types.get_async_invoke_request.GetAsyncInvokeRequest = {}  # type: ignore[typeddict-item]
        input["invocation_arn"] = invocation_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_async_invokes(
        self,
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        submit_time_after: Optional[
            "aws_sdk_bedrock_runtime.types.timestamp.Timestamp"
        ] = None,
        submit_time_before: Optional[
            "aws_sdk_bedrock_runtime.types.timestamp.Timestamp"
        ] = None,
        status_equals: Optional[
            "aws_sdk_bedrock_runtime.types.async_invoke_status.AsyncInvokeStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_bedrock_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_runtime.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "aws_sdk_bedrock_runtime.types.sort_async_invocation_by.SortAsyncInvocationBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_bedrock_runtime.types.sort_order.SortOrder"
        ] = None,
    ) -> "aws_sdk_bedrock_runtime.types.list_async_invokes_response.ListAsyncInvokesResponse":
        """<p>Lists asynchronous invocations.</p>

        Args:
            submit_time_after: <p>Include invocations submitted after this time.</p>
            submit_time_before: <p>Include invocations submitted before this time.</p>
            status_equals: <p>Filter invocations by status.</p>
            max_results: <p>The maximum number of invocations to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            sort_by: <p>How to sort the response.</p>
            sort_order: <p>The sorting order for the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_runtime.types.list_async_invokes_request.ListAsyncInvokesRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_runtime.types.list_async_invokes_response.ListAsyncInvokesResponse"
        ]:
            import aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.list_async_invokes

            output, http_response = (
                aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.list_async_invokes.list_async_invokes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_runtime.types.list_async_invokes_request.ListAsyncInvokesRequest = {}  # type: ignore[typeddict-item]
        if submit_time_after is not None:
            input["submit_time_after"] = submit_time_after
        if submit_time_before is not None:
            input["submit_time_before"] = submit_time_before
        if status_equals is not None:
            input["status_equals"] = status_equals
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort_by is not None:
            input["sort_by"] = sort_by
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_async_invoke(
        self,
        model_id: "aws_sdk_bedrock_runtime.types.async_invoke_identifier.AsyncInvokeIdentifier",
        model_input: "aws_sdk_bedrock_runtime.types.model_input_payload.ModelInputPayload",
        output_data_config: "aws_sdk_bedrock_runtime.types.async_invoke_output_data_config.AsyncInvokeOutputDataConfig",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock_runtime.types.async_invoke_idempotency_token.AsyncInvokeIdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_bedrock_runtime.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_runtime.types.start_async_invoke_response.StartAsyncInvokeResponse":
        """<p>Starts an asynchronous invocation.</p> <p>This operation requires permission for the <code>bedrock:InvokeModel</code> action.</p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the Converse API actions (<a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html\">Converse</a> and <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html\">ConverseStream</a>). For more information see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference\">Deny access for inference on specific models</a>. </p> </important>

        Args:
            client_request_token: <p>Specify idempotency token to ensure that requests are not duplicated.</p>
            model_id: <p>The model to invoke.</p>
            model_input: <p>Input to send to the model.</p>
            output_data_config: <p>Where to store the output.</p>
            tags: <p>Tags to apply to the invocation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_runtime.types.start_async_invoke_request.StartAsyncInvokeRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_runtime.types.start_async_invoke_response.StartAsyncInvokeResponse"
        ]:
            import aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.start_async_invoke

            output, http_response = (
                aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.start_async_invoke.start_async_invoke(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_runtime.types.start_async_invoke_request.StartAsyncInvokeRequest = {}  # type: ignore[typeddict-item]
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        input["model_id"] = model_id
        input["model_input"] = model_input
        input["output_data_config"] = output_data_config
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAsyncInvokeResource:
    def __init__(self, service: AsyncBedrockRuntimeClient) -> None:
        self._service = service

    async def get_async_invoke(
        self,
        invocation_arn: "aws_sdk_bedrock_runtime.types.invocation_arn.InvocationArn",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock_runtime.types.get_async_invoke_response.GetAsyncInvokeResponse"
    ):
        """<p>Retrieve information about an asynchronous invocation.</p>

        Args:
            invocation_arn: <p>The invocation's ARN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_runtime.types.get_async_invoke_request.GetAsyncInvokeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_runtime.types.get_async_invoke_response.GetAsyncInvokeResponse"
        ]:
            import aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.get_async_invoke

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.get_async_invoke.async_get_async_invoke(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_runtime.types.get_async_invoke_request.GetAsyncInvokeRequest = {}  # type: ignore[typeddict-item]
        input["invocation_arn"] = invocation_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_async_invokes(
        self,
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
        submit_time_after: Optional[
            "aws_sdk_bedrock_runtime.types.timestamp.Timestamp"
        ] = None,
        submit_time_before: Optional[
            "aws_sdk_bedrock_runtime.types.timestamp.Timestamp"
        ] = None,
        status_equals: Optional[
            "aws_sdk_bedrock_runtime.types.async_invoke_status.AsyncInvokeStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_bedrock_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_runtime.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "aws_sdk_bedrock_runtime.types.sort_async_invocation_by.SortAsyncInvocationBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_bedrock_runtime.types.sort_order.SortOrder"
        ] = None,
    ) -> "aws_sdk_bedrock_runtime.types.list_async_invokes_response.ListAsyncInvokesResponse":
        """<p>Lists asynchronous invocations.</p>

        Args:
            submit_time_after: <p>Include invocations submitted after this time.</p>
            submit_time_before: <p>Include invocations submitted before this time.</p>
            status_equals: <p>Filter invocations by status.</p>
            max_results: <p>The maximum number of invocations to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            sort_by: <p>How to sort the response.</p>
            sort_order: <p>The sorting order for the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_runtime.types.list_async_invokes_request.ListAsyncInvokesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_runtime.types.list_async_invokes_response.ListAsyncInvokesResponse"
        ]:
            import aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.list_async_invokes

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.list_async_invokes.async_list_async_invokes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_runtime.types.list_async_invokes_request.ListAsyncInvokesRequest = {}  # type: ignore[typeddict-item]
        if submit_time_after is not None:
            input["submit_time_after"] = submit_time_after
        if submit_time_before is not None:
            input["submit_time_before"] = submit_time_before
        if status_equals is not None:
            input["status_equals"] = status_equals
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort_by is not None:
            input["sort_by"] = sort_by
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_async_invoke(
        self,
        model_id: "aws_sdk_bedrock_runtime.types.async_invoke_identifier.AsyncInvokeIdentifier",
        model_input: "aws_sdk_bedrock_runtime.types.model_input_payload.ModelInputPayload",
        output_data_config: "aws_sdk_bedrock_runtime.types.async_invoke_output_data_config.AsyncInvokeOutputDataConfig",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock_runtime.types.async_invoke_idempotency_token.AsyncInvokeIdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_bedrock_runtime.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_runtime.types.start_async_invoke_response.StartAsyncInvokeResponse":
        """<p>Starts an asynchronous invocation.</p> <p>This operation requires permission for the <code>bedrock:InvokeModel</code> action.</p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the Converse API actions (<a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html\">Converse</a> and <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html\">ConverseStream</a>). For more information see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference\">Deny access for inference on specific models</a>. </p> </important>

        Args:
            client_request_token: <p>Specify idempotency token to ensure that requests are not duplicated.</p>
            model_id: <p>The model to invoke.</p>
            model_input: <p>Input to send to the model.</p>
            output_data_config: <p>Where to store the output.</p>
            tags: <p>Tags to apply to the invocation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_runtime.types.start_async_invoke_request.StartAsyncInvokeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_runtime.types.start_async_invoke_response.StartAsyncInvokeResponse"
        ]:
            import aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.start_async_invoke

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.start_async_invoke.async_start_async_invoke(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_runtime.types.start_async_invoke_request.StartAsyncInvokeRequest = {}  # type: ignore[typeddict-item]
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        input["model_id"] = model_id
        input["model_input"] = model_input
        input["output_data_config"] = output_data_config
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
