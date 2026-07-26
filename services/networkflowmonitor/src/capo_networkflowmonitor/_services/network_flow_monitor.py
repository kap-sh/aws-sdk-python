"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#NetworkFlowMonitor``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_networkflowmonitor._auth._signers
import capo_networkflowmonitor._auth._sigv4
from capo_networkflowmonitor._auth._identity import Credentials
from capo_networkflowmonitor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_networkflowmonitor._auth._zapros_handler import AuthMiddleware
from capo_networkflowmonitor._resources.network_flow_monitor.monitor_resource import (
    MonitorResource,
)
from capo_networkflowmonitor._resources.network_flow_monitor.scope_resource import (
    ScopeResource,
)
from capo_networkflowmonitor._services._aws_config import aws_config
from capo_networkflowmonitor._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.arn
    import capo_networkflowmonitor.types.list_tags_for_resource_input
    import capo_networkflowmonitor.types.list_tags_for_resource_output
    import capo_networkflowmonitor.types.tag_key_list
    import capo_networkflowmonitor.types.tag_map
    import capo_networkflowmonitor.types.tag_resource_input
    import capo_networkflowmonitor.types.tag_resource_output
    import capo_networkflowmonitor.types.untag_resource_input
    import capo_networkflowmonitor.types.untag_resource_output


class NetworkFlowMonitorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class NetworkFlowMonitorClient:
    """A client for the ``NetworkFlowMonitor`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = NetworkFlowMonitorClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.monitor_resource = MonitorResource(self)
        self.scope_resource = ScopeResource(self)

    def operation_options(
        self, config_overrides: Optional[NetworkFlowMonitorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: NetworkFlowMonitorClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_networkflowmonitor.types.arn.Arn",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns all the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.list_tags_for_resource

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_networkflowmonitor.types.arn.Arn",
        tags: "capo_networkflowmonitor.types.tag_map.TagMap",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.tag_resource_output.TagResourceOutput":
        """<p>Adds a tag to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags for a resource.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.tag_resource

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_networkflowmonitor.types.arn.Arn",
        tag_keys: "capo_networkflowmonitor.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>Keys that you specified when you tagged a resource.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.untag_resource

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

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
