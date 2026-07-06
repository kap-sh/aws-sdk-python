"""Generated from Smithy shape ``com.amazonaws.elementalinference#ElementalInference``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import aws_sdk_elementalinference._auth._signers
import aws_sdk_elementalinference._auth._sigv4
from aws_sdk_elementalinference._auth._identity import Credentials
from aws_sdk_elementalinference._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_elementalinference._auth._zapros_handler import AuthMiddleware
from aws_sdk_elementalinference._resources.elemental_inference.dictionary_resource import (
    DictionaryResource,
)
from aws_sdk_elementalinference._resources.elemental_inference.feed_resource import (
    FeedResource,
)
from aws_sdk_elementalinference._services._aws_config import aws_config
from aws_sdk_elementalinference._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.list_tags_for_resource_request
    import aws_sdk_elementalinference.types.list_tags_for_resource_response
    import aws_sdk_elementalinference.types.resource_arn
    import aws_sdk_elementalinference.types.tag_key_list
    import aws_sdk_elementalinference.types.tag_map
    import aws_sdk_elementalinference.types.tag_resource_request
    import aws_sdk_elementalinference.types.untag_resource_request


class ElementalInferenceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ElementalInferenceClient:
    """A client for the ``ElementalInference`` service.

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
        self._config = ElementalInferenceClientConfig(
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
        self.dictionary_resource = DictionaryResource(self)
        self.feed_resource = FeedResource(self)

    def operation_options(
        self, config_overrides: Optional[ElementalInferenceClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ElementalInferenceClientConfig = config_overrides or {}
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
        resource_arn: "aws_sdk_elementalinference.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "aws_sdk_elementalinference.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all tags that are on an Elemental Inference resource in the current region.</p>

        Args:
            resource_arn: <p>The ARN of the resource whose tags you want to query.</p>

        Raises:
            aws_sdk_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            aws_sdk_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            aws_sdk_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            aws_sdk_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            aws_sdk_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.list_tags_for_resource

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_elementalinference.types.resource_arn.ResourceArn",
        tags: "aws_sdk_elementalinference.types.tag_map.TagMap",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> None:
        """<p>Associates the specified tags to the resource identified by the specified resourceArn in the current region. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are also deleted. </p>

        Args:
            resource_arn: <p>The ARN of the resource where you want to add tags.</p>
            tags: <p>A list of tags to add to the resource.</p>

        Raises:
            aws_sdk_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            aws_sdk_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            aws_sdk_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            aws_sdk_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            aws_sdk_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            aws_sdk_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_elementalinference._operations.elemental_inference.tag_resource

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_elementalinference.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_elementalinference.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> None:
        """<p>Deletes specified tags from the specified resource in the current region.</p>

        Args:
            resource_arn: <p>The ARN of the resource where you want to delete one or more tags.</p>
            tag_keys: <p>The keys of the tags to delete.</p>

        Raises:
            aws_sdk_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            aws_sdk_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            aws_sdk_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            aws_sdk_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            aws_sdk_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            aws_sdk_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_elementalinference._operations.elemental_inference.untag_resource

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
