"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#AmazonSageMakerA2IRuntime``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_sagemaker_a2i_runtime._auth._signers
import aws_sdk_sagemaker_a2i_runtime._auth._sigv4
from aws_sdk_sagemaker_a2i_runtime._auth._identity import Credentials
from aws_sdk_sagemaker_a2i_runtime._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_sagemaker_a2i_runtime._auth._zapros_handler import AuthMiddleware
from aws_sdk_sagemaker_a2i_runtime._pagination import resolve_path as _resolve_path
from aws_sdk_sagemaker_a2i_runtime._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_sagemaker_a2i_runtime.types.delete_human_loop_request
    import aws_sdk_sagemaker_a2i_runtime.types.delete_human_loop_response
    import aws_sdk_sagemaker_a2i_runtime.types.describe_human_loop_request
    import aws_sdk_sagemaker_a2i_runtime.types.describe_human_loop_response
    import aws_sdk_sagemaker_a2i_runtime.types.flow_definition_arn
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_data_attributes
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_input
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_name
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_summary
    import aws_sdk_sagemaker_a2i_runtime.types.list_human_loops_request
    import aws_sdk_sagemaker_a2i_runtime.types.list_human_loops_response
    import aws_sdk_sagemaker_a2i_runtime.types.max_results
    import aws_sdk_sagemaker_a2i_runtime.types.next_token
    import aws_sdk_sagemaker_a2i_runtime.types.sort_order
    import aws_sdk_sagemaker_a2i_runtime.types.start_human_loop_request
    import aws_sdk_sagemaker_a2i_runtime.types.start_human_loop_response
    import aws_sdk_sagemaker_a2i_runtime.types.stop_human_loop_request
    import aws_sdk_sagemaker_a2i_runtime.types.stop_human_loop_response
    import aws_sdk_sagemaker_a2i_runtime.types.timestamp


class AsyncSageMakerA2IRuntimeClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncSageMakerA2IRuntimeClient:
    """A client for the ``SageMakerA2IRuntime`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncSageMakerA2IRuntimeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSageMakerA2IRuntimeClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def delete_human_loop(
        self,
        human_loop_name: "aws_sdk_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName",
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
    ) -> "aws_sdk_sagemaker_a2i_runtime.types.delete_human_loop_response.DeleteHumanLoopResponse":
        """<p>Deletes the specified human loop for a flow definition.</p> <p>If the human loop was deleted, this operation will return a <code>ResourceNotFoundException</code>. </p>

        Args:
            human_loop_name: <p>The name of the human loop that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_a2i_runtime.types.delete_human_loop_request.DeleteHumanLoopRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_a2i_runtime.types.delete_human_loop_response.DeleteHumanLoopResponse"
        ]:
            import aws_sdk_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.delete_human_loop

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.delete_human_loop.async_delete_human_loop(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_a2i_runtime.types.delete_human_loop_request.DeleteHumanLoopRequest = {}  # type: ignore[typeddict-item]
        input_["human_loop_name"] = human_loop_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_human_loop(
        self,
        human_loop_name: "aws_sdk_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName",
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
    ) -> "aws_sdk_sagemaker_a2i_runtime.types.describe_human_loop_response.DescribeHumanLoopResponse":
        """<p>Returns information about the specified human loop. If the human loop was deleted, this operation will return a <code>ResourceNotFoundException</code> error. </p>

        Args:
            human_loop_name: <p>The name of the human loop that you want information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_a2i_runtime.types.describe_human_loop_request.DescribeHumanLoopRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_a2i_runtime.types.describe_human_loop_response.DescribeHumanLoopResponse"
        ]:
            import aws_sdk_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.describe_human_loop

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.describe_human_loop.async_describe_human_loop(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_a2i_runtime.types.describe_human_loop_request.DescribeHumanLoopRequest = {}  # type: ignore[typeddict-item]
        input_["human_loop_name"] = human_loop_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_human_loops(
        self,
        flow_definition_arn: "aws_sdk_sagemaker_a2i_runtime.types.flow_definition_arn.FlowDefinitionArn",
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
        creation_time_after: Optional[
            "aws_sdk_sagemaker_a2i_runtime.types.timestamp.Timestamp"
        ] = None,
        creation_time_before: Optional[
            "aws_sdk_sagemaker_a2i_runtime.types.timestamp.Timestamp"
        ] = None,
        sort_order: Optional[
            "aws_sdk_sagemaker_a2i_runtime.types.sort_order.SortOrder"
        ] = None,
        next_token: Optional[
            "aws_sdk_sagemaker_a2i_runtime.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_sagemaker_a2i_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_sagemaker_a2i_runtime.types.list_human_loops_response.ListHumanLoopsResponse":
        """<p>Returns information about human loops, given the specified parameters. If a human loop was deleted, it will not be included.</p>

        Args:
            creation_time_after: <p>(Optional) The timestamp of the date when you want the human loops to begin in ISO 8601 format. For example, <code>2020-02-24</code>.</p>
            creation_time_before: <p>(Optional) The timestamp of the date before which you want the human loops to begin in ISO 8601 format. For example, <code>2020-02-24</code>.</p>
            flow_definition_arn: <p>The Amazon Resource Name (ARN) of a flow definition.</p>
            sort_order: <p>Optional. The order for displaying results. Valid values: <code>Ascending</code> and <code>Descending</code>.</p>
            next_token: <p>A token to display the next page of results.</p>
            max_results: <p>The total number of items to return. If the total number of available items is more than the value specified in <code>MaxResults</code>, then a <code>NextToken</code> is returned in the output. You can use this token to display the next page of results. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_a2i_runtime.types.list_human_loops_request.ListHumanLoopsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_a2i_runtime.types.list_human_loops_response.ListHumanLoopsResponse"
        ]:
            import aws_sdk_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.list_human_loops

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.list_human_loops.async_list_human_loops(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_a2i_runtime.types.list_human_loops_request.ListHumanLoopsRequest = {}  # type: ignore[typeddict-item]
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        input_["flow_definition_arn"] = flow_definition_arn
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_human_loops(
        self,
        flow_definition_arn: "aws_sdk_sagemaker_a2i_runtime.types.flow_definition_arn.FlowDefinitionArn",
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
        creation_time_after: Optional[
            "aws_sdk_sagemaker_a2i_runtime.types.timestamp.Timestamp"
        ] = None,
        creation_time_before: Optional[
            "aws_sdk_sagemaker_a2i_runtime.types.timestamp.Timestamp"
        ] = None,
        sort_order: Optional[
            "aws_sdk_sagemaker_a2i_runtime.types.sort_order.SortOrder"
        ] = None,
        next_token: Optional[
            "aws_sdk_sagemaker_a2i_runtime.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_sagemaker_a2i_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_sagemaker_a2i_runtime.types.human_loop_summary.HumanLoopSummary]":
        _token = next_token
        while True:
            _response = await self.list_human_loops(
                flow_definition_arn,
                config_overrides=config_overrides,
                creation_time_after=creation_time_after,
                creation_time_before=creation_time_before,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("human_loop_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_human_loop(
        self,
        human_loop_name: "aws_sdk_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName",
        flow_definition_arn: "aws_sdk_sagemaker_a2i_runtime.types.flow_definition_arn.FlowDefinitionArn",
        human_loop_input: "aws_sdk_sagemaker_a2i_runtime.types.human_loop_input.HumanLoopInput",
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
        data_attributes: Optional[
            "aws_sdk_sagemaker_a2i_runtime.types.human_loop_data_attributes.HumanLoopDataAttributes"
        ] = None,
    ) -> "aws_sdk_sagemaker_a2i_runtime.types.start_human_loop_response.StartHumanLoopResponse":
        """<p>Starts a human loop, provided that at least one activation condition is met.</p>

        Args:
            human_loop_name: <p>The name of the human loop.</p>
            flow_definition_arn: <p>The Amazon Resource Name (ARN) of the flow definition associated with this human loop.</p>
            human_loop_input: <p>An object that contains information about the human loop.</p>
            data_attributes: <p>Attributes of the specified data. Use <code>DataAttributes</code> to specify if your data is free of personally identifiable information and/or free of adult content.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_a2i_runtime.types.start_human_loop_request.StartHumanLoopRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_a2i_runtime.types.start_human_loop_response.StartHumanLoopResponse"
        ]:
            import aws_sdk_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.start_human_loop

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.start_human_loop.async_start_human_loop(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_a2i_runtime.types.start_human_loop_request.StartHumanLoopRequest = {}  # type: ignore[typeddict-item]
        input_["human_loop_name"] = human_loop_name
        input_["flow_definition_arn"] = flow_definition_arn
        input_["human_loop_input"] = human_loop_input
        if data_attributes is not None:
            input_["data_attributes"] = data_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_human_loop(
        self,
        human_loop_name: "aws_sdk_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName",
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
    ) -> "aws_sdk_sagemaker_a2i_runtime.types.stop_human_loop_response.StopHumanLoopResponse":
        """<p>Stops the specified human loop.</p>

        Args:
            human_loop_name: <p>The name of the human loop that you want to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_a2i_runtime.types.stop_human_loop_request.StopHumanLoopRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_a2i_runtime.types.stop_human_loop_response.StopHumanLoopResponse"
        ]:
            import aws_sdk_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.stop_human_loop

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.stop_human_loop.async_stop_human_loop(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_a2i_runtime.types.stop_human_loop_request.StopHumanLoopRequest = {}  # type: ignore[typeddict-item]
        input_["human_loop_name"] = human_loop_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
