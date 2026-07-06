"""Generated from Smithy shape ``com.amazonaws.internetmonitor#InternetMonitor20210603``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import aws_sdk_internetmonitor._auth._signers
import aws_sdk_internetmonitor._auth._sigv4
from aws_sdk_internetmonitor._auth._identity import Credentials
from aws_sdk_internetmonitor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_internetmonitor._auth._zapros_handler import AuthMiddleware
from aws_sdk_internetmonitor._resources.internet_monitor20210603.internet_event_resource import (
    InternetEventResource,
)
from aws_sdk_internetmonitor._resources.internet_monitor20210603.monitor_resource import (
    MonitorResource,
)
from aws_sdk_internetmonitor._services._aws_config import aws_config
from aws_sdk_internetmonitor._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.list_tags_for_resource_input
    import aws_sdk_internetmonitor.types.list_tags_for_resource_output
    import aws_sdk_internetmonitor.types.monitor_arn
    import aws_sdk_internetmonitor.types.tag_keys
    import aws_sdk_internetmonitor.types.tag_map
    import aws_sdk_internetmonitor.types.tag_resource_input
    import aws_sdk_internetmonitor.types.tag_resource_output
    import aws_sdk_internetmonitor.types.untag_resource_input
    import aws_sdk_internetmonitor.types.untag_resource_output


class InternetMonitorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class InternetMonitorClient:
    """A client for the ``InternetMonitor`` service.

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
        self._config = InternetMonitorClientConfig(
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
        self.internet_event_resource = InternetEventResource(self)
        self.monitor_resource = MonitorResource(self)

    def operation_options(
        self, config_overrides: Optional[InternetMonitorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: InternetMonitorClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_internetmonitor.types.monitor_arn.MonitorArn",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
    ) -> "aws_sdk_internetmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags for a resource. Tags are supported only for monitors in Amazon CloudWatch Internet Monitor.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a resource.</p>

        Raises:
            aws_sdk_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_internetmonitor.errors.bad_request_exception.BadRequestException: <p>A bad request was received.</p>
            aws_sdk_internetmonitor.errors.internal_server_error_exception.InternalServerErrorException: <p>There was an internal server error.</p>
            aws_sdk_internetmonitor.errors.not_found_exception.NotFoundException: <p>The request specifies something that doesn't exist.</p>
            aws_sdk_internetmonitor.errors.too_many_requests_exception.TooManyRequestsException: <p>There were too many requests.</p>
            aws_sdk_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_internetmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_internetmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_internetmonitor._operations.internet_monitor20210603.list_tags_for_resource

            output, http_response = (
                aws_sdk_internetmonitor._operations.internet_monitor20210603.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_internetmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_internetmonitor.types.monitor_arn.MonitorArn",
        tags: "aws_sdk_internetmonitor.types.tag_map.TagMap",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
    ) -> "aws_sdk_internetmonitor.types.tag_resource_output.TagResourceOutput":
        """<p>Adds a tag to a resource. Tags are supported only for monitors in Amazon CloudWatch Internet Monitor. You can add a maximum of 50 tags in Internet Monitor.</p> <p>A minimum of one tag is required for this call. It returns an error if you use the <code>TagResource</code> request with 0 tags.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a tag that you add to a resource. Tags are supported only for monitors in Amazon CloudWatch Internet Monitor.</p>
            tags: <p>Tags that you add to a resource. You can add a maximum of 50 tags in Internet Monitor.</p>

        Raises:
            aws_sdk_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_internetmonitor.errors.bad_request_exception.BadRequestException: <p>A bad request was received.</p>
            aws_sdk_internetmonitor.errors.internal_server_error_exception.InternalServerErrorException: <p>There was an internal server error.</p>
            aws_sdk_internetmonitor.errors.not_found_exception.NotFoundException: <p>The request specifies something that doesn't exist.</p>
            aws_sdk_internetmonitor.errors.too_many_requests_exception.TooManyRequestsException: <p>There were too many requests.</p>
            aws_sdk_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_internetmonitor.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_internetmonitor.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_internetmonitor._operations.internet_monitor20210603.tag_resource

            output, http_response = (
                aws_sdk_internetmonitor._operations.internet_monitor20210603.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_internetmonitor.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_internetmonitor.types.monitor_arn.MonitorArn",
        tag_keys: "aws_sdk_internetmonitor.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
    ) -> "aws_sdk_internetmonitor.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a tag you remove a resource from.</p>
            tag_keys: <p>Tag keys that you remove from a resource.</p>

        Raises:
            aws_sdk_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_internetmonitor.errors.bad_request_exception.BadRequestException: <p>A bad request was received.</p>
            aws_sdk_internetmonitor.errors.internal_server_error_exception.InternalServerErrorException: <p>There was an internal server error.</p>
            aws_sdk_internetmonitor.errors.not_found_exception.NotFoundException: <p>The request specifies something that doesn't exist.</p>
            aws_sdk_internetmonitor.errors.too_many_requests_exception.TooManyRequestsException: <p>There were too many requests.</p>
            aws_sdk_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_internetmonitor.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_internetmonitor.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_internetmonitor._operations.internet_monitor20210603.untag_resource

            output, http_response = (
                aws_sdk_internetmonitor._operations.internet_monitor20210603.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_internetmonitor.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
