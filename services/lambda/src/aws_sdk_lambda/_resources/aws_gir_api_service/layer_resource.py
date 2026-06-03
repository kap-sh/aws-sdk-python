from typing import Optional, TYPE_CHECKING
from aws_sdk_lambda._services._pipeline import (
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
)
import aws_sdk_lambda._auth._signers
import aws_sdk_lambda._auth._sigv4

if TYPE_CHECKING:
    from aws_sdk_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from aws_sdk_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )
    import aws_sdk_lambda.types.architecture
    import aws_sdk_lambda.types.list_layers_request
    import aws_sdk_lambda.types.list_layers_response
    import aws_sdk_lambda.types.max_layer_list_items
    import aws_sdk_lambda.types.runtime
    import aws_sdk_lambda.types.string


class LayerResource:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def list(
        self,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        compatible_runtime: Optional["aws_sdk_lambda.types.runtime.Runtime"] = None,
        marker: Optional["aws_sdk_lambda.types.string.String"] = None,
        max_items: Optional[
            "aws_sdk_lambda.types.max_layer_list_items.MaxLayerListItems"
        ] = None,
        compatible_architecture: Optional[
            "aws_sdk_lambda.types.architecture.Architecture"
        ] = None,
    ) -> "aws_sdk_lambda.types.list_layers_response.ListLayersResponse":
        """<p>Lists <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-layers.html\">Lambda layers</a> and shows information about the latest version of each. Specify a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\">runtime identifier</a> to list only layers that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layers that are compatible with that <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html\">instruction set architecture</a>.</p>

        Args:
            compatible_runtime: <p>A runtime identifier.</p> <p>The following list includes deprecated runtimes. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>
            marker: <p>A pagination token returned by a previous call.</p>
            max_items: <p>The maximum number of layers to return.</p>
            compatible_architecture: <p>The compatible <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html\">instruction set architecture</a>.</p>

        Examples:
            To list the layers that are compatible with your function's runtime
            The following example returns information about layers that are compatible with the Python 3.7 runtime.

            >>> client.list(compatible_runtime='python3.7')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.list_layers_request.ListLayersRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.list_layers_response.ListLayersResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.list_layers

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.list_layers.list_layers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_lambda.types.list_layers_request.ListLayersRequest = {}  # type: ignore[typeddict-item]
        if compatible_runtime is not None:
            input["compatible_runtime"] = compatible_runtime
        if marker is not None:
            input["marker"] = marker
        if max_items is not None:
            input["max_items"] = max_items
        if compatible_architecture is not None:
            input["compatible_architecture"] = compatible_architecture

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncLayerResource:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        compatible_runtime: Optional["aws_sdk_lambda.types.runtime.Runtime"] = None,
        marker: Optional["aws_sdk_lambda.types.string.String"] = None,
        max_items: Optional[
            "aws_sdk_lambda.types.max_layer_list_items.MaxLayerListItems"
        ] = None,
        compatible_architecture: Optional[
            "aws_sdk_lambda.types.architecture.Architecture"
        ] = None,
    ) -> "aws_sdk_lambda.types.list_layers_response.ListLayersResponse":
        """<p>Lists <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-layers.html\">Lambda layers</a> and shows information about the latest version of each. Specify a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\">runtime identifier</a> to list only layers that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layers that are compatible with that <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html\">instruction set architecture</a>.</p>

        Args:
            compatible_runtime: <p>A runtime identifier.</p> <p>The following list includes deprecated runtimes. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>
            marker: <p>A pagination token returned by a previous call.</p>
            max_items: <p>The maximum number of layers to return.</p>
            compatible_architecture: <p>The compatible <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html\">instruction set architecture</a>.</p>

        Examples:
            To list the layers that are compatible with your function's runtime
            The following example returns information about layers that are compatible with the Python 3.7 runtime.

            >>> await client.list(compatible_runtime='python3.7')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lambda.types.list_layers_request.ListLayersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lambda.types.list_layers_response.ListLayersResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.list_layers

            (
                output,
                http_response,
            ) = await aws_sdk_lambda._operations.aws_gir_api_service.list_layers.async_list_layers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_lambda.types.list_layers_request.ListLayersRequest = {}  # type: ignore[typeddict-item]
        if compatible_runtime is not None:
            input["compatible_runtime"] = compatible_runtime
        if marker is not None:
            input["marker"] = marker
        if max_items is not None:
            input["max_items"] = max_items
        if compatible_architecture is not None:
            input["compatible_architecture"] = compatible_architecture

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
