"""Generated from Smithy shape ``com.amazonaws.lambda#AWSGirApiService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
from capo_lambda._auth._identity import Credentials
from capo_lambda._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lambda._auth._zapros_handler import AuthMiddleware
from capo_lambda._resources.aws_gir_api_service.capacity_provider_resource import (
    CapacityProviderResource,
)
from capo_lambda._resources.aws_gir_api_service.code_signing_config_resource import (
    CodeSigningConfigResource,
)
from capo_lambda._resources.aws_gir_api_service.durable_execution import (
    DurableExecution,
)
from capo_lambda._resources.aws_gir_api_service.event_source_mapping import (
    EventSourceMapping,
)
from capo_lambda._resources.aws_gir_api_service.function import Function
from capo_lambda._resources.aws_gir_api_service.function_alias import FunctionAlias
from capo_lambda._resources.aws_gir_api_service.function_version_resource import (
    FunctionVersionResource,
)
from capo_lambda._resources.aws_gir_api_service.layer_resource import LayerResource
from capo_lambda._resources.aws_gir_api_service.layer_version import LayerVersion
from capo_lambda._resources.aws_gir_api_service.permission import Permission
from capo_lambda._resources.aws_gir_api_service.provisioned_concurrency_config import (
    ProvisionedConcurrencyConfig,
)
from capo_lambda._services._aws_config import aws_config
from capo_lambda._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_lambda.types.binary_operation_payload
    import capo_lambda.types.callback_id
    import capo_lambda.types.delete_function_event_invoke_config_request
    import capo_lambda.types.delete_function_request
    import capo_lambda.types.delete_function_response
    import capo_lambda.types.destination_config
    import capo_lambda.types.error_object
    import capo_lambda.types.function_event_invoke_config
    import capo_lambda.types.get_account_settings_request
    import capo_lambda.types.get_account_settings_response
    import capo_lambda.types.get_function_event_invoke_config_request
    import capo_lambda.types.list_function_event_invoke_configs_request
    import capo_lambda.types.list_function_event_invoke_configs_response
    import capo_lambda.types.list_tags_request
    import capo_lambda.types.list_tags_response
    import capo_lambda.types.max_function_event_invoke_config_list_items
    import capo_lambda.types.maximum_event_age_in_seconds
    import capo_lambda.types.maximum_retry_attempts
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.numeric_latest_published_or_alias_qualifier
    import capo_lambda.types.put_function_event_invoke_config_request
    import capo_lambda.types.send_durable_execution_callback_failure_request
    import capo_lambda.types.send_durable_execution_callback_failure_response
    import capo_lambda.types.send_durable_execution_callback_heartbeat_request
    import capo_lambda.types.send_durable_execution_callback_heartbeat_response
    import capo_lambda.types.send_durable_execution_callback_success_request
    import capo_lambda.types.send_durable_execution_callback_success_response
    import capo_lambda.types.string
    import capo_lambda.types.tag_key_list
    import capo_lambda.types.tag_resource_request
    import capo_lambda.types.taggable_resource
    import capo_lambda.types.tags
    import capo_lambda.types.untag_resource_request
    import capo_lambda.types.update_function_event_invoke_config_request


class LambdaClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = LambdaClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.capacity_provider_resource = CapacityProviderResource(self)
        self.code_signing_config_resource = CodeSigningConfigResource(self)
        self.durable_execution = DurableExecution(self)
        self.event_source_mapping = EventSourceMapping(self)
        self.function = Function(self)
        self.function_alias = FunctionAlias(self)
        self.function_version_resource = FunctionVersionResource(self)
        self.layer_resource = LayerResource(self)
        self.layer_version = LayerVersion(self)
        self.permission = Permission(self)
        self.provisioned_concurrency_config = ProvisionedConcurrencyConfig(self)

    def operation_options(
        self, config_overrides: Optional[LambdaClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: LambdaClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
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

    def delete_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.delete_function_response.DeleteFunctionResponse":
        r"""<p>Deletes a Lambda function. To delete a specific function version, use the <code>Qualifier</code> parameter. Otherwise, all versions and aliases are deleted. This doesn't require the user to have explicit permissions for <a>DeleteAlias</a>.</p> <note> <p>A deleted Lambda function cannot be recovered. Ensure that you specify the correct function name and version before deleting.</p> </note> <p>To delete Lambda event source mappings that invoke a function, use <a>DeleteEventSourceMapping</a>. For Amazon Web Services services and resources that invoke your function directly, delete the trigger in the service where you originally configured it.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function or version.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:1</code> (with version).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version to delete. You can't delete a version that an alias references.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a version of a Lambda function
            The following example deletes version 1 of a Lambda function named my-function.

            >>> client.delete_function(function_name='my-function', qualifier='1')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_function_request.DeleteFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.delete_function

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_function.delete_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_request.DeleteFunctionRequest = {}  # type: ignore[typeddict-item]
        input_["function_name"] = function_name
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function_event_invoke_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> None:
        r"""<p>Deletes the configuration for asynchronous invocation for a function, version, or alias.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an asynchronous invocation configuration
            The following example deletes the asynchronous invocation configuration for the GREEN alias of a function named my-function.

            >>> client.delete_function_event_invoke_config(function_name='my-function', qualifier='GREEN')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_function_event_invoke_config_request.DeleteFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_function_event_invoke_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_function_event_invoke_config.delete_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_event_invoke_config_request.DeleteFunctionEventInvokeConfigRequest = {}  # type: ignore[typeddict-item]
        input_["function_name"] = function_name
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_account_settings(
        self, *, config_overrides: Optional[LambdaClientConfig] = None
    ) -> "capo_lambda.types.get_account_settings_response.GetAccountSettingsResponse":
        r"""<p>Retrieves details about your account's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/limits.html\">limits</a> and usage in an Amazon Web Services Region.</p>

        Raises:
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get account settings
            This operation takes no parameters and returns details about storage and concurrency quotas in the current Region.

            >>> client.get_account_settings()
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_account_settings_request.GetAccountSettingsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_account_settings_response.GetAccountSettingsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_account_settings

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_account_settings.get_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_account_settings_request.GetAccountSettingsRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_event_invoke_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig":
        r"""<p>Retrieves the configuration for asynchronous invocation for a function, version, or alias.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get an asynchronous invocation configuration
            The following example returns the asynchronous invocation configuration for the BLUE alias of a function named my-function.

            >>> client.get_function_event_invoke_config(function_name='my-function', qualifier='BLUE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_event_invoke_config_request.GetFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_event_invoke_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_event_invoke_config.get_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_event_invoke_config_request.GetFunctionEventInvokeConfigRequest = {}  # type: ignore[typeddict-item]
        input_["function_name"] = function_name
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_function_event_invoke_configs(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_function_event_invoke_config_list_items.MaxFunctionEventInvokeConfigListItems"
        ] = None,
    ) -> "capo_lambda.types.list_function_event_invoke_configs_response.ListFunctionEventInvokeConfigsResponse":
        r"""<p>Retrieves a list of configurations for asynchronous invocation for a function.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of configurations to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view a list of asynchronous invocation configurations
            The following example returns a list of asynchronous invocation configurations for a function named my-function.

            >>> client.list_function_event_invoke_configs(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_function_event_invoke_configs_request.ListFunctionEventInvokeConfigsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_function_event_invoke_configs_response.ListFunctionEventInvokeConfigsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_function_event_invoke_configs

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_function_event_invoke_configs.list_function_event_invoke_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_function_event_invoke_configs_request.ListFunctionEventInvokeConfigsRequest = {}  # type: ignore[typeddict-item]
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
        response.response.close()
        return response.output

    def list_tags(
        self,
        resource: "capo_lambda.types.taggable_resource.TaggableResource",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.list_tags_response.ListTagsResponse":
        r"""<p>Returns a function, event source mapping, or code signing configuration's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a>. You can also view function tags with <a>GetFunction</a>.</p>

        Args:
            resource: <p>The resource's Amazon Resource Name (ARN). Note: Lambda does not support adding tags to function aliases or versions.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve the list of tags for a Lambda function
            The following example displays the tags attached to the my-function Lambda function.

            >>> client.list_tags(resource='arn:aws:lambda:us-west-2:123456789012:function:my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_tags_request.ListTagsRequest]",
        ) -> OperationResponse["capo_lambda.types.list_tags_response.ListTagsResponse"]:
            import capo_lambda._operations.aws_gir_api_service.list_tags

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_tags.list_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_tags_request.ListTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_function_event_invoke_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        maximum_retry_attempts: Optional[
            "capo_lambda.types.maximum_retry_attempts.MaximumRetryAttempts"
        ] = None,
        maximum_event_age_in_seconds: Optional[
            "capo_lambda.types.maximum_event_age_in_seconds.MaximumEventAgeInSeconds"
        ] = None,
        destination_config: Optional[
            "capo_lambda.types.destination_config.DestinationConfig"
        ] = None,
    ) -> "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig":
        r"""<p>Configures options for <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html\">asynchronous invocation</a> on a function, version, or alias. If a configuration already exists for a function, version, or alias, this operation overwrites it. If you exclude any settings, they are removed. To set one option without affecting existing settings for other options, use <a>UpdateFunctionEventInvokeConfig</a>.</p> <p>By default, Lambda retries an asynchronous invocation twice if the function returns an error. It retains events in a queue for up to six hours. When an event fails all processing attempts or stays in the asynchronous invocation queue for too long, Lambda discards it. To retain discarded events, configure a dead-letter queue with <a>UpdateFunctionConfiguration</a>.</p> <p>To send an invocation record to a queue, topic, S3 bucket, function, or event bus, specify a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations\">destination</a>. You can configure separate destinations for successful invocations (on-success) and events that fail all processing attempts (on-failure). You can configure destinations in addition to or instead of a dead-letter queue.</p> <note> <p>S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.</p> </note>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>
            maximum_retry_attempts: <p>The maximum number of times to retry when the function returns an error.</p>
            maximum_event_age_in_seconds: <p>The maximum age of a request that Lambda sends to a function for processing.</p>
            destination_config: <p>A destination for events after they have been sent to a function for processing.</p> <p class=\"title\"> <b>Destinations</b> </p> <ul> <li> <p> <b>Function</b> - The Amazon Resource Name (ARN) of a Lambda function.</p> </li> <li> <p> <b>Queue</b> - The ARN of a standard SQS queue.</p> </li> <li> <p> <b>Bucket</b> - The ARN of an Amazon S3 bucket.</p> </li> <li> <p> <b>Topic</b> - The ARN of a standard SNS topic.</p> </li> <li> <p> <b>Event Bus</b> - The ARN of an Amazon EventBridge event bus.</p> </li> </ul> <note> <p>S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.</p> </note>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To configure error handling for asynchronous invocation
            The following example sets a maximum event age of one hour and disables retries for the specified function.

            >>> client.put_function_event_invoke_config(function_name='my-function', maximum_event_age_in_seconds=3600, maximum_retry_attempts=0)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_function_event_invoke_config_request.PutFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_function_event_invoke_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_function_event_invoke_config.put_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_event_invoke_config_request.PutFunctionEventInvokeConfigRequest = {}  # type: ignore[typeddict-item]
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
        response.response.close()
        return response.output

    def send_durable_execution_callback_failure(
        self,
        callback_id: "capo_lambda.types.callback_id.CallbackId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        error: Optional["capo_lambda.types.error_object.ErrorObject"] = None,
    ) -> "capo_lambda.types.send_durable_execution_callback_failure_response.SendDurableExecutionCallbackFailureResponse":
        """<p>Sends a failure response for a callback operation in a durable execution. Use this API when an external system cannot complete a callback operation successfully.</p>

        Args:
            callback_id: <p>The unique identifier for the callback operation.</p>
            error: <p>Error details describing why the callback operation failed.</p>

        Raises:
            capo_lambda.errors.callback_timeout_exception.CallbackTimeoutException: <p>The callback ID token has either expired or the callback associated with the token has already been closed.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.send_durable_execution_callback_failure_request.SendDurableExecutionCallbackFailureRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.send_durable_execution_callback_failure_response.SendDurableExecutionCallbackFailureResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_failure

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_failure.send_durable_execution_callback_failure(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.send_durable_execution_callback_failure_request.SendDurableExecutionCallbackFailureRequest = {}  # type: ignore[typeddict-item]
        input_["callback_id"] = callback_id
        if error is not None:
            input_["error"] = error

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_durable_execution_callback_heartbeat(
        self,
        callback_id: "capo_lambda.types.callback_id.CallbackId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.send_durable_execution_callback_heartbeat_response.SendDurableExecutionCallbackHeartbeatResponse":
        """<p>Sends a heartbeat signal for a long-running callback operation to prevent timeout. Use this API to extend the callback timeout period while the external operation is still in progress.</p>

        Args:
            callback_id: <p>The unique identifier for the callback operation.</p>

        Raises:
            capo_lambda.errors.callback_timeout_exception.CallbackTimeoutException: <p>The callback ID token has either expired or the callback associated with the token has already been closed.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.send_durable_execution_callback_heartbeat_request.SendDurableExecutionCallbackHeartbeatRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.send_durable_execution_callback_heartbeat_response.SendDurableExecutionCallbackHeartbeatResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_heartbeat

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_heartbeat.send_durable_execution_callback_heartbeat(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.send_durable_execution_callback_heartbeat_request.SendDurableExecutionCallbackHeartbeatRequest = {}  # type: ignore[typeddict-item]
        input_["callback_id"] = callback_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_durable_execution_callback_success(
        self,
        callback_id: "capo_lambda.types.callback_id.CallbackId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        result: Optional[
            "capo_lambda.types.binary_operation_payload.BinaryOperationPayload"
        ] = None,
    ) -> "capo_lambda.types.send_durable_execution_callback_success_response.SendDurableExecutionCallbackSuccessResponse":
        """<p>Sends a successful completion response for a callback operation in a durable execution. Use this API when an external system has successfully completed a callback operation.</p>

        Args:
            callback_id: <p>The unique identifier for the callback operation.</p>
            result: <p>The result data from the successful callback operation. Maximum size is 256 KB.</p>

        Raises:
            capo_lambda.errors.callback_timeout_exception.CallbackTimeoutException: <p>The callback ID token has either expired or the callback associated with the token has already been closed.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.send_durable_execution_callback_success_request.SendDurableExecutionCallbackSuccessRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.send_durable_execution_callback_success_response.SendDurableExecutionCallbackSuccessResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_success

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_success.send_durable_execution_callback_success(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.send_durable_execution_callback_success_request.SendDurableExecutionCallbackSuccessRequest = {}  # type: ignore[typeddict-item]
        input_["callback_id"] = callback_id
        if result is not None:
            input_["result"] = result

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource: "capo_lambda.types.taggable_resource.TaggableResource",
        tags: "capo_lambda.types.tags.Tags",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Adds <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a> to a function, event source mapping, or code signing configuration.</p>

        Args:
            resource: <p>The resource's Amazon Resource Name (ARN).</p>
            tags: <p>A list of tags to apply to the resource.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add tags to an existing Lambda function
            The following example adds a tag with the key name DEPARTMENT and a value of 'Department A' to the specified Lambda function.

            >>> client.tag_resource(resource='arn:aws:lambda:us-west-2:123456789012:function:my-function', tags={'DEPARTMENT': 'Department A'})
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.tag_resource

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource: "capo_lambda.types.taggable_resource.TaggableResource",
        tag_keys: "capo_lambda.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Removes <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a> from a function, event source mapping, or code signing configuration.</p>

        Args:
            resource: <p>The resource's Amazon Resource Name (ARN).</p>
            tag_keys: <p>A list of tag keys to remove from the resource.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove tags from an existing Lambda function
            The following example removes the tag with the key name DEPARTMENT tag from the my-function Lambda function.

            >>> client.untag_resource(resource='arn:aws:lambda:us-west-2:123456789012:function:my-function', tag_keys=['DEPARTMENT'])
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.untag_resource

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_function_event_invoke_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        maximum_retry_attempts: Optional[
            "capo_lambda.types.maximum_retry_attempts.MaximumRetryAttempts"
        ] = None,
        maximum_event_age_in_seconds: Optional[
            "capo_lambda.types.maximum_event_age_in_seconds.MaximumEventAgeInSeconds"
        ] = None,
        destination_config: Optional[
            "capo_lambda.types.destination_config.DestinationConfig"
        ] = None,
    ) -> "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig":
        r"""<p>Updates the configuration for asynchronous invocation for a function, version, or alias.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>
            maximum_retry_attempts: <p>The maximum number of times to retry when the function returns an error.</p>
            maximum_event_age_in_seconds: <p>The maximum age of a request that Lambda sends to a function for processing.</p>
            destination_config: <p>A destination for events after they have been sent to a function for processing.</p> <p class=\"title\"> <b>Destinations</b> </p> <ul> <li> <p> <b>Function</b> - The Amazon Resource Name (ARN) of a Lambda function.</p> </li> <li> <p> <b>Queue</b> - The ARN of a standard SQS queue.</p> </li> <li> <p> <b>Bucket</b> - The ARN of an Amazon S3 bucket.</p> </li> <li> <p> <b>Topic</b> - The ARN of a standard SNS topic.</p> </li> <li> <p> <b>Event Bus</b> - The ARN of an Amazon EventBridge event bus.</p> </li> </ul> <note> <p>S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.</p> </note>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an asynchronous invocation configuration
            The following example adds an on-failure destination to the existing asynchronous invocation configuration for a function named my-function.

            >>> client.update_function_event_invoke_config(destination_config={'OnFailure': {'Destination': 'arn:aws:sqs:us-east-2:123456789012:destination'}}, function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_function_event_invoke_config_request.UpdateFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_function_event_invoke_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_function_event_invoke_config.update_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.update_function_event_invoke_config_request.UpdateFunctionEventInvokeConfigRequest = {}  # type: ignore[typeddict-item]
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
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
