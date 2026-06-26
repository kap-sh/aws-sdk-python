"""Generated from Smithy shape ``com.amazonaws.amp#AmazonPrometheusService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_amp._auth._signers
import aws_sdk_amp._auth._sigv4
from aws_sdk_amp._auth._identity import Credentials
from aws_sdk_amp._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_amp._auth._zapros_handler import AuthMiddleware
from aws_sdk_amp._resources.amazon_prometheus_service.scraper import Scraper
from aws_sdk_amp._resources.amazon_prometheus_service.workspace import Workspace
from aws_sdk_amp._services._aws_config import aws_config
from aws_sdk_amp._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_amp.types.get_default_scraper_configuration_request
    import aws_sdk_amp.types.get_default_scraper_configuration_response
    import aws_sdk_amp.types.list_tags_for_resource_request
    import aws_sdk_amp.types.list_tags_for_resource_response
    import aws_sdk_amp.types.tag_keys
    import aws_sdk_amp.types.tag_map
    import aws_sdk_amp.types.tag_resource_request
    import aws_sdk_amp.types.tag_resource_response
    import aws_sdk_amp.types.untag_resource_request
    import aws_sdk_amp.types.untag_resource_response


class ampClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ampClient:
    """A client for the ``amp`` service.

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
        self._config = ampClientConfig(
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
        self.scraper = Scraper(self)
        self.workspace = Workspace(self)

    def operation_options(
        self, config_overrides: Optional[ampClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ampClientConfig = config_overrides or {}
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

    def get_default_scraper_configuration(
        self, *, config_overrides: Optional[ampClientConfig] = None
    ) -> "aws_sdk_amp.types.get_default_scraper_configuration_response.GetDefaultScraperConfigurationResponse":
        """<p>The <code>GetDefaultScraperConfiguration</code> operation returns the default scraper configuration used when Amazon EKS creates a scraper for you.</p>

        Raises:
            aws_sdk_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            aws_sdk_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_amp.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetDefaultScraperConfiguration

            >>> client.get_default_scraper_configuration()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amp.types.get_default_scraper_configuration_request.GetDefaultScraperConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_amp.types.get_default_scraper_configuration_response.GetDefaultScraperConfigurationResponse"
        ]:
            import aws_sdk_amp._operations.amazon_prometheus_service.get_default_scraper_configuration

            output, http_response = (
                aws_sdk_amp._operations.amazon_prometheus_service.get_default_scraper_configuration.get_default_scraper_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amp.types.get_default_scraper_configuration_request.GetDefaultScraperConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self, resource_arn: str, *, config_overrides: Optional[ampClientConfig] = None
    ) -> (
        "aws_sdk_amp.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>The <code>ListTagsForResource</code> operation returns the tags that are associated with an Amazon Managed Service for Prometheus resource. Currently, the only resources that can be tagged are scrapers, workspaces, and rule groups namespaces. </p>

        Args:
            resource_arn: <p>The ARN of the resource to list tages for. Must be a workspace, scraper, or rule groups namespace resource.</p>

        Raises:
            aws_sdk_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            aws_sdk_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            aws_sdk_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amp.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_amp.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_amp._operations.amazon_prometheus_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_amp._operations.amazon_prometheus_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amp.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: str,
        tags: "aws_sdk_amp.types.tag_map.TagMap",
        *,
        config_overrides: Optional[ampClientConfig] = None,
    ) -> "aws_sdk_amp.types.tag_resource_response.TagResourceResponse":
        """<p>The <code>TagResource</code> operation associates tags with an Amazon Managed Service for Prometheus resource. The only resources that can be tagged are rule groups namespaces, scrapers, and workspaces.</p> <p>If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag. To remove a tag, use <code>UntagResource</code>.</p>

        Args:
            resource_arn: <p>The ARN of the resource to apply tags to.</p>
            tags: <p>The list of tag keys and values to associate with the resource.</p> <p>Keys must not begin with <code>aws:</code>.</p>

        Raises:
            aws_sdk_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            aws_sdk_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            aws_sdk_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amp.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_amp.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_amp._operations.amazon_prometheus_service.tag_resource

            output, http_response = (
                aws_sdk_amp._operations.amazon_prometheus_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amp.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: str,
        tag_keys: "aws_sdk_amp.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[ampClientConfig] = None,
    ) -> "aws_sdk_amp.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from an Amazon Managed Service for Prometheus resource. The only resources that can be tagged are rule groups namespaces, scrapers, and workspaces. </p>

        Args:
            resource_arn: <p>The ARN of the resource from which to remove a tag.</p>
            tag_keys: <p>The keys of the tags to remove.</p>

        Raises:
            aws_sdk_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            aws_sdk_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            aws_sdk_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amp.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_amp.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_amp._operations.amazon_prometheus_service.untag_resource

            output, http_response = (
                aws_sdk_amp._operations.amazon_prometheus_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amp.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
