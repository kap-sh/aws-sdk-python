"""Generated from Smithy shape ``com.amazonaws.lambda#AWSGirApiService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_lambda._auth._signers
import aws_sdk_lambda._auth._sigv4
from aws_sdk_lambda._auth._identity import Credentials
from aws_sdk_lambda._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_lambda._auth._zapros_handler import AuthMiddleware
from aws_sdk_lambda._pagination import resolve_path as _resolve_path
from aws_sdk_lambda._resources.aws_gir_api_service.capacity_provider_resource import (
    CapacityProviderResource,
)
from aws_sdk_lambda._resources.aws_gir_api_service.code_signing_config_resource import (
    CodeSigningConfigResource,
)
from aws_sdk_lambda._resources.aws_gir_api_service.event_source_mapping import (
    EventSourceMapping,
)
from aws_sdk_lambda._resources.aws_gir_api_service.function import Function
from aws_sdk_lambda._resources.aws_gir_api_service.function_alias import FunctionAlias
from aws_sdk_lambda._resources.aws_gir_api_service.function_version_resource import (
    FunctionVersionResource,
)
from aws_sdk_lambda._resources.aws_gir_api_service.layer_resource import LayerResource
from aws_sdk_lambda._resources.aws_gir_api_service.layer_version import LayerVersion
from aws_sdk_lambda._resources.aws_gir_api_service.permission import Permission
from aws_sdk_lambda._resources.aws_gir_api_service.provisioned_concurrency_config import (
    ProvisionedConcurrencyConfig,
)
from aws_sdk_lambda._resources.aws_gir_api_service.resource_policy import ResourcePolicy
from aws_sdk_lambda._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_lambda.types.binary_operation_payload
    import aws_sdk_lambda.types.callback_id
    import aws_sdk_lambda.types.checkpoint_durable_execution_request
    import aws_sdk_lambda.types.checkpoint_durable_execution_response
    import aws_sdk_lambda.types.checkpoint_token
    import aws_sdk_lambda.types.client_token
    import aws_sdk_lambda.types.delete_function_event_invoke_config_request
    import aws_sdk_lambda.types.delete_function_request
    import aws_sdk_lambda.types.delete_function_response
    import aws_sdk_lambda.types.destination_config
    import aws_sdk_lambda.types.durable_execution_arn
    import aws_sdk_lambda.types.durable_execution_name
    import aws_sdk_lambda.types.error_object
    import aws_sdk_lambda.types.event
    import aws_sdk_lambda.types.execution
    import aws_sdk_lambda.types.execution_status_list
    import aws_sdk_lambda.types.execution_timestamp
    import aws_sdk_lambda.types.function_event_invoke_config
    import aws_sdk_lambda.types.get_account_settings_request
    import aws_sdk_lambda.types.get_account_settings_response
    import aws_sdk_lambda.types.get_durable_execution_history_request
    import aws_sdk_lambda.types.get_durable_execution_history_response
    import aws_sdk_lambda.types.get_durable_execution_request
    import aws_sdk_lambda.types.get_durable_execution_response
    import aws_sdk_lambda.types.get_durable_execution_state_request
    import aws_sdk_lambda.types.get_durable_execution_state_response
    import aws_sdk_lambda.types.get_function_event_invoke_config_request
    import aws_sdk_lambda.types.include_execution_data
    import aws_sdk_lambda.types.item_count
    import aws_sdk_lambda.types.list_durable_executions_by_function_request
    import aws_sdk_lambda.types.list_durable_executions_by_function_response
    import aws_sdk_lambda.types.list_function_event_invoke_configs_request
    import aws_sdk_lambda.types.list_function_event_invoke_configs_response
    import aws_sdk_lambda.types.list_tags_request
    import aws_sdk_lambda.types.list_tags_response
    import aws_sdk_lambda.types.max_function_event_invoke_config_list_items
    import aws_sdk_lambda.types.maximum_event_age_in_seconds
    import aws_sdk_lambda.types.maximum_retry_attempts
    import aws_sdk_lambda.types.namespaced_function_name
    import aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier
    import aws_sdk_lambda.types.operation
    import aws_sdk_lambda.types.operation_updates
    import aws_sdk_lambda.types.put_function_event_invoke_config_request
    import aws_sdk_lambda.types.reverse_order
    import aws_sdk_lambda.types.send_durable_execution_callback_failure_request
    import aws_sdk_lambda.types.send_durable_execution_callback_failure_response
    import aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_request
    import aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_response
    import aws_sdk_lambda.types.send_durable_execution_callback_success_request
    import aws_sdk_lambda.types.send_durable_execution_callback_success_response
    import aws_sdk_lambda.types.stop_durable_execution_request
    import aws_sdk_lambda.types.stop_durable_execution_response
    import aws_sdk_lambda.types.string
    import aws_sdk_lambda.types.tag_key_list
    import aws_sdk_lambda.types.tag_resource_request
    import aws_sdk_lambda.types.taggable_resource
    import aws_sdk_lambda.types.tags
    import aws_sdk_lambda.types.untag_resource_request
    import aws_sdk_lambda.types.update_function_event_invoke_config_request


class LambdaClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class LambdaClient:
    """A client for the ``Lambda`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = LambdaClientConfig(
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

        # resources
        self.capacity_provider_resource = CapacityProviderResource(self)
        self.code_signing_config_resource = CodeSigningConfigResource(self)
        self.event_source_mapping = EventSourceMapping(self)
        self.function = Function(self)
        self.function_alias = FunctionAlias(self)
        self.function_version_resource = FunctionVersionResource(self)
        self.layer_resource = LayerResource(self)
        self.layer_version = LayerVersion(self)
        self.permission = Permission(self)
        self.provisioned_concurrency_config = ProvisionedConcurrencyConfig(self)
        self.resource_policy = ResourcePolicy(self)

    def operation_options(
        self, config_overrides: Optional[LambdaClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: LambdaClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def checkpoint_durable_execution(
        self,
        durable_execution_arn: "aws_sdk_lambda.types.durable_execution_arn.DurableExecutionArn",
        checkpoint_token: "aws_sdk_lambda.types.checkpoint_token.CheckpointToken",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        updates: Optional[
            "aws_sdk_lambda.types.operation_updates.OperationUpdates"
        ] = None,
        client_token: Optional["aws_sdk_lambda.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_lambda.types.checkpoint_durable_execution_response.CheckpointDurableExecutionResponse":
        r"""<p>Saves the progress of a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable function</a> execution during runtime. This API is used by the Lambda durable functions SDK to checkpoint completed steps and schedule asynchronous operations. You typically don't need to call this API directly as the SDK handles checkpointing automatically.</p> <p>Each checkpoint operation consumes the current checkpoint token and returns a new one for the next checkpoint. This ensures that checkpoints are applied in the correct order and prevents duplicate or out-of-order state updates.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            checkpoint_token: <p>A unique token that identifies the current checkpoint state. This token is provided by the Lambda runtime and must be used to ensure checkpoints are applied in the correct order. Each checkpoint operation consumes this token and returns a new one.</p>
            updates: <p>An array of state updates to apply during this checkpoint. Each update represents a change to the execution state, such as completing a step, starting a callback, or scheduling a timer. Updates are applied atomically as part of the checkpoint operation.</p>
            client_token: <p>An optional idempotency token to ensure that duplicate checkpoint requests are handled correctly. If provided, Lambda uses this token to detect and handle duplicate requests within a 15-minute window.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.checkpoint_durable_execution_request.CheckpointDurableExecutionRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.checkpoint_durable_execution_response.CheckpointDurableExecutionResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.checkpoint_durable_execution

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.checkpoint_durable_execution.checkpoint_durable_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.checkpoint_durable_execution_request.CheckpointDurableExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["durable_execution_arn"] = durable_execution_arn
        input_["checkpoint_token"] = checkpoint_token
        if updates is not None:
            input_["updates"] = updates
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_function(
        self,
        function_name: "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "aws_sdk_lambda.types.delete_function_response.DeleteFunctionResponse":
        r"""<p>Deletes a Lambda function. To delete a specific function version, use the <code>Qualifier</code> parameter. Otherwise, all versions and aliases are deleted. This doesn't require the user to have explicit permissions for <a>DeleteAlias</a>.</p> <note> <p>A deleted Lambda function cannot be recovered. Ensure that you specify the correct function name and version before deleting.</p> </note> <p>To delete Lambda event source mappings that invoke a function, use <a>DeleteEventSourceMapping</a>. For Amazon Web Services services and resources that invoke your function directly, delete the trigger in the service where you originally configured it.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function or version.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:1</code> (with version).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version to delete. You can't delete a version that an alias references.</p>

        Examples:
            To delete a version of a Lambda function
            The following example deletes version 1 of a Lambda function named my-function.

            >>> client.delete_function(function_name='my-function', qualifier='1')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.delete_function_request.DeleteFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.delete_function

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.delete_function.delete_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.delete_function_request.DeleteFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["function_name"] = function_name
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_function_event_invoke_config(
        self,
        function_name: "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> None:
        r"""<p>Deletes the configuration for asynchronous invocation for a function, version, or alias.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>

        Examples:
            To delete an asynchronous invocation configuration
            The following example deletes the asynchronous invocation configuration for the GREEN alias of a function named my-function.

            >>> client.delete_function_event_invoke_config(function_name='my-function', qualifier='GREEN')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.delete_function_event_invoke_config_request.DeleteFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_lambda._operations.aws_gir_api_service.delete_function_event_invoke_config

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.delete_function_event_invoke_config.delete_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.delete_function_event_invoke_config_request.DeleteFunctionEventInvokeConfigRequest = {}  # type: ignore[typeddict-item]
        input_["function_name"] = function_name
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_account_settings(
        self, *, config_overrides: Optional[LambdaClientConfig] = None
    ) -> (
        "aws_sdk_lambda.types.get_account_settings_response.GetAccountSettingsResponse"
    ):
        r"""<p>Retrieves details about your account's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/limits.html\">limits</a> and usage in an Amazon Web Services Region.</p>

        Examples:
            To get account settings
            This operation takes no parameters and returns details about storage and concurrency quotas in the current Region.

            >>> client.get_account_settings()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.get_account_settings_request.GetAccountSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.get_account_settings_response.GetAccountSettingsResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.get_account_settings

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.get_account_settings.get_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.get_account_settings_request.GetAccountSettingsRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_durable_execution(
        self,
        durable_execution_arn: "aws_sdk_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "aws_sdk_lambda.types.get_durable_execution_response.GetDurableExecutionResponse":
        r"""<p>Retrieves detailed information about a specific <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable execution</a>, including its current status, input payload, result or error information, and execution metadata such as start time and usage statistics.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.get_durable_execution_request.GetDurableExecutionRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.get_durable_execution_response.GetDurableExecutionResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.get_durable_execution

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.get_durable_execution.get_durable_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.get_durable_execution_request.GetDurableExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["durable_execution_arn"] = durable_execution_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_durable_execution_history(
        self,
        durable_execution_arn: "aws_sdk_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        include_execution_data: Optional[
            "aws_sdk_lambda.types.include_execution_data.IncludeExecutionData"
        ] = None,
        max_items: Optional["aws_sdk_lambda.types.item_count.ItemCount"] = None,
        marker: Optional["aws_sdk_lambda.types.string.String"] = None,
        reverse_order: Optional[
            "aws_sdk_lambda.types.reverse_order.ReverseOrder"
        ] = None,
    ) -> "aws_sdk_lambda.types.get_durable_execution_history_response.GetDurableExecutionHistoryResponse":
        r"""<p>Retrieves the execution history for a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable execution</a>, showing all the steps, callbacks, and events that occurred during the execution. This provides a detailed audit trail of the execution's progress over time.</p> <p>The history is available while the execution is running and for a retention period after it completes (1-90 days, default 30 days). You can control whether to include execution data such as step results and callback payloads.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            include_execution_data: <p>Specifies whether to include execution data such as step results and callback payloads in the history events. Set to <code>true</code> to include data, or <code>false</code> to exclude it for a more compact response. The default is <code>true</code>.</p>
            max_items: <p>The maximum number of history events to return per call. You can use <code>Marker</code> to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.</p>
            marker: <p>If <code>NextMarker</code> was returned from a previous request, use this value to retrieve the next page of results. Each pagination token expires after 24 hours.</p>
            reverse_order: <p>When set to <code>true</code>, returns the history events in reverse chronological order (newest first). By default, events are returned in chronological order (oldest first).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.get_durable_execution_history_request.GetDurableExecutionHistoryRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.get_durable_execution_history_response.GetDurableExecutionHistoryResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.get_durable_execution_history

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.get_durable_execution_history.get_durable_execution_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.get_durable_execution_history_request.GetDurableExecutionHistoryRequest = {}  # type: ignore[typeddict-item]
        input_["durable_execution_arn"] = durable_execution_arn
        if include_execution_data is not None:
            input_["include_execution_data"] = include_execution_data
        if max_items is not None:
            input_["max_items"] = max_items
        if marker is not None:
            input_["marker"] = marker
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_durable_execution_history(
        self,
        durable_execution_arn: "aws_sdk_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        include_execution_data: Optional[
            "aws_sdk_lambda.types.include_execution_data.IncludeExecutionData"
        ] = None,
        max_items: Optional["aws_sdk_lambda.types.item_count.ItemCount"] = None,
        marker: Optional["aws_sdk_lambda.types.string.String"] = None,
        reverse_order: Optional[
            "aws_sdk_lambda.types.reverse_order.ReverseOrder"
        ] = None,
    ) -> "Iterator[aws_sdk_lambda.types.event.Event]":
        _token = marker
        while True:
            _response = self.get_durable_execution_history(
                durable_execution_arn,
                config_overrides=config_overrides,
                include_execution_data=include_execution_data,
                max_items=max_items,
                marker=_token,
                reverse_order=reverse_order,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def get_durable_execution_state(
        self,
        durable_execution_arn: "aws_sdk_lambda.types.durable_execution_arn.DurableExecutionArn",
        checkpoint_token: "aws_sdk_lambda.types.checkpoint_token.CheckpointToken",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["aws_sdk_lambda.types.string.String"] = None,
        max_items: Optional["aws_sdk_lambda.types.item_count.ItemCount"] = None,
    ) -> "aws_sdk_lambda.types.get_durable_execution_state_response.GetDurableExecutionStateResponse":
        r"""<p>Retrieves the current execution state required for the replay process during <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable function</a> execution. This API is used by the Lambda durable functions SDK to get state information needed for replay. You typically don't need to call this API directly as the SDK handles state management automatically.</p> <p>The response contains operations ordered by start sequence number in ascending order. Completed operations with children don't include child operation details since they don't need to be replayed.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            checkpoint_token: <p>A checkpoint token that identifies the current state of the execution. This token is provided by the Lambda runtime and ensures that state retrieval is consistent with the current execution context.</p>
            marker: <p>If <code>NextMarker</code> was returned from a previous request, use this value to retrieve the next page of operations. Each pagination token expires after 24 hours.</p>
            max_items: <p>The maximum number of operations to return per call. You can use <code>Marker</code> to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.get_durable_execution_state_request.GetDurableExecutionStateRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.get_durable_execution_state_response.GetDurableExecutionStateResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.get_durable_execution_state

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.get_durable_execution_state.get_durable_execution_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.get_durable_execution_state_request.GetDurableExecutionStateRequest = {}  # type: ignore[typeddict-item]
        input_["durable_execution_arn"] = durable_execution_arn
        input_["checkpoint_token"] = checkpoint_token
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_durable_execution_state(
        self,
        durable_execution_arn: "aws_sdk_lambda.types.durable_execution_arn.DurableExecutionArn",
        checkpoint_token: "aws_sdk_lambda.types.checkpoint_token.CheckpointToken",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["aws_sdk_lambda.types.string.String"] = None,
        max_items: Optional["aws_sdk_lambda.types.item_count.ItemCount"] = None,
    ) -> "Iterator[aws_sdk_lambda.types.operation.Operation]":
        _token = marker
        while True:
            _response = self.get_durable_execution_state(
                durable_execution_arn,
                checkpoint_token,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def get_function_event_invoke_config(
        self,
        function_name: "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "aws_sdk_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig":
        r"""<p>Retrieves the configuration for asynchronous invocation for a function, version, or alias.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>

        Examples:
            To get an asynchronous invocation configuration
            The following example returns the asynchronous invocation configuration for the BLUE alias of a function named my-function.

            >>> client.get_function_event_invoke_config(function_name='my-function', qualifier='BLUE')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.get_function_event_invoke_config_request.GetFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.get_function_event_invoke_config

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.get_function_event_invoke_config.get_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.get_function_event_invoke_config_request.GetFunctionEventInvokeConfigRequest = {}  # type: ignore[typeddict-item]
        input_["function_name"] = function_name
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_durable_executions_by_function(
        self,
        function_name: "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        durable_execution_name: Optional[
            "aws_sdk_lambda.types.durable_execution_name.DurableExecutionName"
        ] = None,
        statuses: Optional[
            "aws_sdk_lambda.types.execution_status_list.ExecutionStatusList"
        ] = None,
        started_after: Optional[
            "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        started_before: Optional[
            "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        reverse_order: Optional[
            "aws_sdk_lambda.types.reverse_order.ReverseOrder"
        ] = None,
        marker: Optional["aws_sdk_lambda.types.string.String"] = None,
        max_items: Optional["aws_sdk_lambda.types.item_count.ItemCount"] = None,
    ) -> "aws_sdk_lambda.types.list_durable_executions_by_function_response.ListDurableExecutionsByFunctionResponse":
        r"""<p>Returns a list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable executions</a> for a specified Lambda function. You can filter the results by execution name, status, and start time range. This API supports pagination for large result sets.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function. You can specify a function name, a partial ARN, or a full ARN.</p>
            qualifier: <p>The function version or alias. If not specified, lists executions for the $LATEST version.</p>
            durable_execution_name: <p>Filter executions by name. Only executions with names that matches this string are returned.</p>
            statuses: <p>Filter executions by status. Valid values: RUNNING, SUCCEEDED, FAILED, TIMED_OUT, STOPPED.</p>
            started_after: <p>Filter executions that started after this timestamp (ISO 8601 format).</p>
            started_before: <p>Filter executions that started before this timestamp (ISO 8601 format).</p>
            reverse_order: <p>Set to true to return results in reverse chronological order (newest first). Default is false.</p>
            marker: <p>Pagination token from a previous request to continue retrieving results.</p>
            max_items: <p>Maximum number of executions to return (1-1000). Default is 100.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.list_durable_executions_by_function_request.ListDurableExecutionsByFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.list_durable_executions_by_function_response.ListDurableExecutionsByFunctionResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.list_durable_executions_by_function

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.list_durable_executions_by_function.list_durable_executions_by_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.list_durable_executions_by_function_request.ListDurableExecutionsByFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["function_name"] = function_name
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if durable_execution_name is not None:
            input_["durable_execution_name"] = durable_execution_name
        if statuses is not None:
            input_["statuses"] = statuses
        if started_after is not None:
            input_["started_after"] = started_after
        if started_before is not None:
            input_["started_before"] = started_before
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_durable_executions_by_function(
        self,
        function_name: "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        durable_execution_name: Optional[
            "aws_sdk_lambda.types.durable_execution_name.DurableExecutionName"
        ] = None,
        statuses: Optional[
            "aws_sdk_lambda.types.execution_status_list.ExecutionStatusList"
        ] = None,
        started_after: Optional[
            "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        started_before: Optional[
            "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        reverse_order: Optional[
            "aws_sdk_lambda.types.reverse_order.ReverseOrder"
        ] = None,
        marker: Optional["aws_sdk_lambda.types.string.String"] = None,
        max_items: Optional["aws_sdk_lambda.types.item_count.ItemCount"] = None,
    ) -> "Iterator[aws_sdk_lambda.types.execution.Execution]":
        _token = marker
        while True:
            _response = self.list_durable_executions_by_function(
                function_name,
                config_overrides=config_overrides,
                qualifier=qualifier,
                durable_execution_name=durable_execution_name,
                statuses=statuses,
                started_after=started_after,
                started_before=started_before,
                reverse_order=reverse_order,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("durable_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_function_event_invoke_configs(
        self,
        function_name: "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["aws_sdk_lambda.types.string.String"] = None,
        max_items: Optional[
            "aws_sdk_lambda.types.max_function_event_invoke_config_list_items.MaxFunctionEventInvokeConfigListItems"
        ] = None,
    ) -> "aws_sdk_lambda.types.list_function_event_invoke_configs_response.ListFunctionEventInvokeConfigsResponse":
        r"""<p>Retrieves a list of configurations for asynchronous invocation for a function.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of configurations to return.</p>

        Examples:
            To view a list of asynchronous invocation configurations
            The following example returns a list of asynchronous invocation configurations for a function named my-function.

            >>> client.list_function_event_invoke_configs(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.list_function_event_invoke_configs_request.ListFunctionEventInvokeConfigsRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.list_function_event_invoke_configs_response.ListFunctionEventInvokeConfigsResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.list_function_event_invoke_configs

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.list_function_event_invoke_configs.list_function_event_invoke_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.list_function_event_invoke_configs_request.ListFunctionEventInvokeConfigsRequest = {}  # type: ignore[typeddict-item]
        input_["function_name"] = function_name
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags(
        self,
        resource: "aws_sdk_lambda.types.taggable_resource.TaggableResource",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "aws_sdk_lambda.types.list_tags_response.ListTagsResponse":
        r"""<p>Returns a function, event source mapping, or code signing configuration's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a>. You can also view function tags with <a>GetFunction</a>.</p>

        Args:
            resource: <p>The resource's Amazon Resource Name (ARN). Note: Lambda does not support adding tags to function aliases or versions.</p>

        Examples:
            To retrieve the list of tags for a Lambda function
            The following example displays the tags attached to the my-function Lambda function.

            >>> client.list_tags(resource='arn:aws:lambda:us-west-2:123456789012:function:my-function')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.list_tags_request.ListTagsRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.list_tags_response.ListTagsResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.list_tags

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.list_tags.list_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.list_tags_request.ListTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_function_event_invoke_config(
        self,
        function_name: "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        maximum_retry_attempts: Optional[
            "aws_sdk_lambda.types.maximum_retry_attempts.MaximumRetryAttempts"
        ] = None,
        maximum_event_age_in_seconds: Optional[
            "aws_sdk_lambda.types.maximum_event_age_in_seconds.MaximumEventAgeInSeconds"
        ] = None,
        destination_config: Optional[
            "aws_sdk_lambda.types.destination_config.DestinationConfig"
        ] = None,
    ) -> "aws_sdk_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig":
        r"""<p>Configures options for <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html\">asynchronous invocation</a> on a function, version, or alias. If a configuration already exists for a function, version, or alias, this operation overwrites it. If you exclude any settings, they are removed. To set one option without affecting existing settings for other options, use <a>UpdateFunctionEventInvokeConfig</a>.</p> <p>By default, Lambda retries an asynchronous invocation twice if the function returns an error. It retains events in a queue for up to six hours. When an event fails all processing attempts or stays in the asynchronous invocation queue for too long, Lambda discards it. To retain discarded events, configure a dead-letter queue with <a>UpdateFunctionConfiguration</a>.</p> <p>To send an invocation record to a queue, topic, S3 bucket, function, or event bus, specify a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations\">destination</a>. You can configure separate destinations for successful invocations (on-success) and events that fail all processing attempts (on-failure). You can configure destinations in addition to or instead of a dead-letter queue.</p> <note> <p>S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.</p> </note>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>
            maximum_retry_attempts: <p>The maximum number of times to retry when the function returns an error.</p>
            maximum_event_age_in_seconds: <p>The maximum age of a request that Lambda sends to a function for processing.</p>
            destination_config: <p>A destination for events after they have been sent to a function for processing.</p> <p class=\"title\"> <b>Destinations</b> </p> <ul> <li> <p> <b>Function</b> - The Amazon Resource Name (ARN) of a Lambda function.</p> </li> <li> <p> <b>Queue</b> - The ARN of a standard SQS queue.</p> </li> <li> <p> <b>Bucket</b> - The ARN of an Amazon S3 bucket.</p> </li> <li> <p> <b>Topic</b> - The ARN of a standard SNS topic.</p> </li> <li> <p> <b>Event Bus</b> - The ARN of an Amazon EventBridge event bus.</p> </li> </ul> <note> <p>S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.</p> </note>

        Examples:
            To configure error handling for asynchronous invocation
            The following example sets a maximum event age of one hour and disables retries for the specified function.

            >>> client.put_function_event_invoke_config(function_name='my-function', maximum_retry_attempts=0, maximum_event_age_in_seconds=3600)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.put_function_event_invoke_config_request.PutFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.put_function_event_invoke_config

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.put_function_event_invoke_config.put_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.put_function_event_invoke_config_request.PutFunctionEventInvokeConfigRequest = {}  # type: ignore[typeddict-item]
        input_["function_name"] = function_name
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if maximum_retry_attempts is not None:
            input_["maximum_retry_attempts"] = maximum_retry_attempts
        if maximum_event_age_in_seconds is not None:
            input_["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
        if destination_config is not None:
            input_["destination_config"] = destination_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_durable_execution_callback_failure(
        self,
        callback_id: "aws_sdk_lambda.types.callback_id.CallbackId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        error: Optional["aws_sdk_lambda.types.error_object.ErrorObject"] = None,
    ) -> "aws_sdk_lambda.types.send_durable_execution_callback_failure_response.SendDurableExecutionCallbackFailureResponse":
        """<p>Sends a failure response for a callback operation in a durable execution. Use this API when an external system cannot complete a callback operation successfully.</p>

        Args:
            callback_id: <p>The unique identifier for the callback operation.</p>
            error: <p>Error details describing why the callback operation failed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.send_durable_execution_callback_failure_request.SendDurableExecutionCallbackFailureRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.send_durable_execution_callback_failure_response.SendDurableExecutionCallbackFailureResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.send_durable_execution_callback_failure

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.send_durable_execution_callback_failure.send_durable_execution_callback_failure(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.send_durable_execution_callback_failure_request.SendDurableExecutionCallbackFailureRequest = {}  # type: ignore[typeddict-item]
        input_["callback_id"] = callback_id
        if error is not None:
            input_["error"] = error

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_durable_execution_callback_heartbeat(
        self,
        callback_id: "aws_sdk_lambda.types.callback_id.CallbackId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_response.SendDurableExecutionCallbackHeartbeatResponse":
        """<p>Sends a heartbeat signal for a long-running callback operation to prevent timeout. Use this API to extend the callback timeout period while the external operation is still in progress.</p>

        Args:
            callback_id: <p>The unique identifier for the callback operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_request.SendDurableExecutionCallbackHeartbeatRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_response.SendDurableExecutionCallbackHeartbeatResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.send_durable_execution_callback_heartbeat

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.send_durable_execution_callback_heartbeat.send_durable_execution_callback_heartbeat(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.send_durable_execution_callback_heartbeat_request.SendDurableExecutionCallbackHeartbeatRequest = {}  # type: ignore[typeddict-item]
        input_["callback_id"] = callback_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_durable_execution_callback_success(
        self,
        callback_id: "aws_sdk_lambda.types.callback_id.CallbackId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        result: Optional[
            "aws_sdk_lambda.types.binary_operation_payload.BinaryOperationPayload"
        ] = None,
    ) -> "aws_sdk_lambda.types.send_durable_execution_callback_success_response.SendDurableExecutionCallbackSuccessResponse":
        """<p>Sends a successful completion response for a callback operation in a durable execution. Use this API when an external system has successfully completed a callback operation.</p>

        Args:
            callback_id: <p>The unique identifier for the callback operation.</p>
            result: <p>The result data from the successful callback operation. Maximum size is 256 KB.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.send_durable_execution_callback_success_request.SendDurableExecutionCallbackSuccessRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.send_durable_execution_callback_success_response.SendDurableExecutionCallbackSuccessResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.send_durable_execution_callback_success

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.send_durable_execution_callback_success.send_durable_execution_callback_success(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.send_durable_execution_callback_success_request.SendDurableExecutionCallbackSuccessRequest = {}  # type: ignore[typeddict-item]
        input_["callback_id"] = callback_id
        if result is not None:
            input_["result"] = result

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_durable_execution(
        self,
        durable_execution_arn: "aws_sdk_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        error: Optional["aws_sdk_lambda.types.error_object.ErrorObject"] = None,
    ) -> "aws_sdk_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse":
        r"""<p>Stops a running <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable execution</a>. The execution transitions to STOPPED status and cannot be resumed. Any in-progress operations are terminated.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            error: <p>Optional error details explaining why the execution is being stopped.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.stop_durable_execution_request.StopDurableExecutionRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.stop_durable_execution

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.stop_durable_execution.stop_durable_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.stop_durable_execution_request.StopDurableExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["durable_execution_arn"] = durable_execution_arn
        if error is not None:
            input_["error"] = error

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource: "aws_sdk_lambda.types.taggable_resource.TaggableResource",
        tags: "aws_sdk_lambda.types.tags.Tags",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Adds <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a> to a function, event source mapping, or code signing configuration.</p>

        Args:
            resource: <p>The resource's Amazon Resource Name (ARN).</p>
            tags: <p>A list of tags to apply to the resource.</p>

        Examples:
            To add tags to an existing Lambda function
            The following example adds a tag with the key name DEPARTMENT and a value of 'Department A' to the specified Lambda function.

            >>> client.tag_resource(resource='arn:aws:lambda:us-west-2:123456789012:function:my-function', tags={'DEPARTMENT': 'Department A'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_lambda._operations.aws_gir_api_service.tag_resource

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource: "aws_sdk_lambda.types.taggable_resource.TaggableResource",
        tag_keys: "aws_sdk_lambda.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Removes <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a> from a function, event source mapping, or code signing configuration.</p>

        Args:
            resource: <p>The resource's Amazon Resource Name (ARN).</p>
            tag_keys: <p>A list of tag keys to remove from the resource.</p>

        Examples:
            To remove tags from an existing Lambda function
            The following example removes the tag with the key name DEPARTMENT tag from the my-function Lambda function.

            >>> client.untag_resource(resource='arn:aws:lambda:us-west-2:123456789012:function:my-function', tag_keys=['DEPARTMENT'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_lambda._operations.aws_gir_api_service.untag_resource

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_function_event_invoke_config(
        self,
        function_name: "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        maximum_retry_attempts: Optional[
            "aws_sdk_lambda.types.maximum_retry_attempts.MaximumRetryAttempts"
        ] = None,
        maximum_event_age_in_seconds: Optional[
            "aws_sdk_lambda.types.maximum_event_age_in_seconds.MaximumEventAgeInSeconds"
        ] = None,
        destination_config: Optional[
            "aws_sdk_lambda.types.destination_config.DestinationConfig"
        ] = None,
    ) -> "aws_sdk_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig":
        r"""<p>Updates the configuration for asynchronous invocation for a function, version, or alias.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>
            maximum_retry_attempts: <p>The maximum number of times to retry when the function returns an error.</p>
            maximum_event_age_in_seconds: <p>The maximum age of a request that Lambda sends to a function for processing.</p>
            destination_config: <p>A destination for events after they have been sent to a function for processing.</p> <p class=\"title\"> <b>Destinations</b> </p> <ul> <li> <p> <b>Function</b> - The Amazon Resource Name (ARN) of a Lambda function.</p> </li> <li> <p> <b>Queue</b> - The ARN of a standard SQS queue.</p> </li> <li> <p> <b>Bucket</b> - The ARN of an Amazon S3 bucket.</p> </li> <li> <p> <b>Topic</b> - The ARN of a standard SNS topic.</p> </li> <li> <p> <b>Event Bus</b> - The ARN of an Amazon EventBridge event bus.</p> </li> </ul> <note> <p>S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.</p> </note>

        Examples:
            To update an asynchronous invocation configuration
            The following example adds an on-failure destination to the existing asynchronous invocation configuration for a function named my-function.

            >>> client.update_function_event_invoke_config(function_name='my-function', destination_config={'OnFailure': {'Destination': 'arn:aws:sqs:us-east-2:123456789012:destination'}})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.update_function_event_invoke_config_request.UpdateFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.update_function_event_invoke_config

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.update_function_event_invoke_config.update_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lambda.types.update_function_event_invoke_config_request.UpdateFunctionEventInvokeConfigRequest = {}  # type: ignore[typeddict-item]
        input_["function_name"] = function_name
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if maximum_retry_attempts is not None:
            input_["maximum_retry_attempts"] = maximum_retry_attempts
        if maximum_event_age_in_seconds is not None:
            input_["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
        if destination_config is not None:
            input_["destination_config"] = destination_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
