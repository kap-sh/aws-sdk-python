from typing import TYPE_CHECKING, Optional

import aws_sdk_mediatailor._auth._signers
import aws_sdk_mediatailor._auth._sigv4
from aws_sdk_mediatailor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.custom_output_configuration
    import aws_sdk_mediatailor.types.delete_function_request
    import aws_sdk_mediatailor.types.delete_function_response
    import aws_sdk_mediatailor.types.function
    import aws_sdk_mediatailor.types.function_type
    import aws_sdk_mediatailor.types.get_function_request
    import aws_sdk_mediatailor.types.get_function_response
    import aws_sdk_mediatailor.types.http_request_configuration
    import aws_sdk_mediatailor.types.list_functions_request
    import aws_sdk_mediatailor.types.list_functions_response
    import aws_sdk_mediatailor.types.max_results
    import aws_sdk_mediatailor.types.put_function_request
    import aws_sdk_mediatailor.types.put_function_response
    import aws_sdk_mediatailor.types.sequential_executor_configuration
    from aws_sdk_mediatailor._services.async_media_tailor import (
        AsyncMediaTailorClient,
        AsyncMediaTailorClientConfig,
    )
    from aws_sdk_mediatailor._services.media_tailor import (
        MediaTailorClient,
        MediaTailorClientConfig,
    )


class FunctionResource:
    def __init__(self, service: MediaTailorClient) -> None:
        self._service = service

    def put(
        self,
        function_id: "aws_sdk_mediatailor.types.__string.__string",
        function_type: "aws_sdk_mediatailor.types.function_type.FunctionType",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        description: Optional["aws_sdk_mediatailor.types.__string.__string"] = None,
        http_request_configuration: Optional[
            "aws_sdk_mediatailor.types.http_request_configuration.HttpRequestConfiguration"
        ] = None,
        custom_output_configuration: Optional[
            "aws_sdk_mediatailor.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        sequential_executor_configuration: Optional[
            "aws_sdk_mediatailor.types.sequential_executor_configuration.SequentialExecutorConfiguration"
        ] = None,
        tags: Optional[
            "aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "aws_sdk_mediatailor.types.put_function_response.PutFunctionResponse":
        """<p>Creates or updates a function. A function defines reusable logic that MediaTailor executes at lifecycle hooks during ad insertion. For more information about functions, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html\">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function. The identifier must be unique within your account.</p>
            function_type: <p>The type of the function. The function type determines what the function can do at runtime. Valid values: <code>CUSTOM_OUTPUT</code> evaluates expressions and produces output bindings with no external calls. <code>HTTP_REQUEST</code> makes an HTTP call to an external service and evaluates output expressions that can reference the response. <code>SEQUENTIAL_EXECUTOR</code> runs a sequence of child functions in order, passing data between steps through temporary data. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types.html\">Function types and composition</a> in the <i>MediaTailor User Guide</i>.</p>
            description: <p>A description of the function.</p>
            http_request_configuration: <p>The configuration for an <code>HTTP_REQUEST</code> function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when <code>FunctionType</code> is <code>HTTP_REQUEST</code>.</p>
            custom_output_configuration: <p>The configuration for a <code>CUSTOM_OUTPUT</code> function. Specifies the runtime and output expressions. Required when <code>FunctionType</code> is <code>CUSTOM_OUTPUT</code>.</p>
            sequential_executor_configuration: <p>The configuration for a <code>SEQUENTIAL_EXECUTOR</code> function. Specifies the ordered list of child functions to execute, an optional output block, and a timeout. Required when <code>FunctionType</code> is <code>SEQUENTIAL_EXECUTOR</code>.</p>
            tags: <p>The tags to assign to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.put_function_request.PutFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.put_function_response.PutFunctionResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.put_function

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.put_function.put_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.put_function_request.PutFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["function_id"] = function_id
        input_["function_type"] = function_type
        if description is not None:
            input_["description"] = description
        if http_request_configuration is not None:
            input_["http_request_configuration"] = http_request_configuration
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if sequential_executor_configuration is not None:
            input_["sequential_executor_configuration"] = (
                sequential_executor_configuration
            )
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        function_id: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.get_function_response.GetFunctionResponse":
        """<p>Retrieves the configuration and metadata for a function. For more information about functions, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html\">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.get_function_request.GetFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.get_function_response.GetFunctionResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.get_function

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.get_function.get_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.get_function_request.GetFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["function_id"] = function_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        function_id: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.delete_function_response.DeleteFunctionResponse":
        """<p>Deletes a function. MediaTailor prevents deletion of a function that is still referenced by a playback configuration or by another function. Remove all references before deleting. For more information about functions, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html\">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.delete_function_request.DeleteFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.delete_function

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.delete_function.delete_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.delete_function_request.DeleteFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["function_id"] = function_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediatailor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediatailor.types.__string.__string"] = None,
    ) -> "aws_sdk_mediatailor.types.list_functions_response.ListFunctionsResponse":
        """<p>Retrieves all functions associated with your AWS account in the current Region. For more information about functions, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html\">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of functions that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> functions, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses token-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListFunctions</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.list_functions_request.ListFunctionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.list_functions_response.ListFunctionsResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.list_functions

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.list_functions.list_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.list_functions_request.ListFunctionsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncFunctionResource:
    def __init__(self, service: AsyncMediaTailorClient) -> None:
        self._service = service

    async def put(
        self,
        function_id: "aws_sdk_mediatailor.types.__string.__string",
        function_type: "aws_sdk_mediatailor.types.function_type.FunctionType",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        description: Optional["aws_sdk_mediatailor.types.__string.__string"] = None,
        http_request_configuration: Optional[
            "aws_sdk_mediatailor.types.http_request_configuration.HttpRequestConfiguration"
        ] = None,
        custom_output_configuration: Optional[
            "aws_sdk_mediatailor.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        sequential_executor_configuration: Optional[
            "aws_sdk_mediatailor.types.sequential_executor_configuration.SequentialExecutorConfiguration"
        ] = None,
        tags: Optional[
            "aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "aws_sdk_mediatailor.types.put_function_response.PutFunctionResponse":
        """<p>Creates or updates a function. A function defines reusable logic that MediaTailor executes at lifecycle hooks during ad insertion. For more information about functions, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html\">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function. The identifier must be unique within your account.</p>
            function_type: <p>The type of the function. The function type determines what the function can do at runtime. Valid values: <code>CUSTOM_OUTPUT</code> evaluates expressions and produces output bindings with no external calls. <code>HTTP_REQUEST</code> makes an HTTP call to an external service and evaluates output expressions that can reference the response. <code>SEQUENTIAL_EXECUTOR</code> runs a sequence of child functions in order, passing data between steps through temporary data. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types.html\">Function types and composition</a> in the <i>MediaTailor User Guide</i>.</p>
            description: <p>A description of the function.</p>
            http_request_configuration: <p>The configuration for an <code>HTTP_REQUEST</code> function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when <code>FunctionType</code> is <code>HTTP_REQUEST</code>.</p>
            custom_output_configuration: <p>The configuration for a <code>CUSTOM_OUTPUT</code> function. Specifies the runtime and output expressions. Required when <code>FunctionType</code> is <code>CUSTOM_OUTPUT</code>.</p>
            sequential_executor_configuration: <p>The configuration for a <code>SEQUENTIAL_EXECUTOR</code> function. Specifies the ordered list of child functions to execute, an optional output block, and a timeout. Required when <code>FunctionType</code> is <code>SEQUENTIAL_EXECUTOR</code>.</p>
            tags: <p>The tags to assign to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.put_function_request.PutFunctionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.put_function_response.PutFunctionResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.put_function

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.put_function.async_put_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.put_function_request.PutFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["function_id"] = function_id
        input_["function_type"] = function_type
        if description is not None:
            input_["description"] = description
        if http_request_configuration is not None:
            input_["http_request_configuration"] = http_request_configuration
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if sequential_executor_configuration is not None:
            input_["sequential_executor_configuration"] = (
                sequential_executor_configuration
            )
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        function_id: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.get_function_response.GetFunctionResponse":
        """<p>Retrieves the configuration and metadata for a function. For more information about functions, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html\">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.get_function_request.GetFunctionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.get_function_response.GetFunctionResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.get_function

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.get_function.async_get_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.get_function_request.GetFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["function_id"] = function_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        function_id: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.delete_function_response.DeleteFunctionResponse":
        """<p>Deletes a function. MediaTailor prevents deletion of a function that is still referenced by a playback configuration or by another function. Remove all references before deleting. For more information about functions, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html\">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.delete_function_request.DeleteFunctionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.delete_function

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.delete_function.async_delete_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.delete_function_request.DeleteFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["function_id"] = function_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediatailor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediatailor.types.__string.__string"] = None,
    ) -> "aws_sdk_mediatailor.types.list_functions_response.ListFunctionsResponse":
        """<p>Retrieves all functions associated with your AWS account in the current Region. For more information about functions, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html\">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of functions that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> functions, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses token-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListFunctions</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.list_functions_request.ListFunctionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.list_functions_response.ListFunctionsResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.list_functions

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.list_functions.async_list_functions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.list_functions_request.ListFunctionsRequest = {}  # type: ignore[typeddict-item]
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
