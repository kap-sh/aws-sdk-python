"""Generated from Smithy shape ``com.amazonaws.pipes#Pipes``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_pipes._auth._signers
import aws_sdk_pipes._auth._sigv4
from aws_sdk_pipes._auth._identity import Credentials
from aws_sdk_pipes._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_pipes._auth._zapros_handler import AuthMiddleware
from aws_sdk_pipes._resources.pipes.pipe_resource import AsyncPipeResource
from aws_sdk_pipes._services._aws_config import aaws_config
from aws_sdk_pipes._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_pipes.types.list_tags_for_resource_request
    import aws_sdk_pipes.types.list_tags_for_resource_response
    import aws_sdk_pipes.types.pipe_arn
    import aws_sdk_pipes.types.tag_key_list
    import aws_sdk_pipes.types.tag_map
    import aws_sdk_pipes.types.tag_resource_request
    import aws_sdk_pipes.types.tag_resource_response
    import aws_sdk_pipes.types.untag_resource_request
    import aws_sdk_pipes.types.untag_resource_response


class AsyncPipesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncPipesClient:
    """A client for the ``Pipes`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncPipesClientConfig(
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
        self.pipe_resource = AsyncPipeResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncPipesClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPipesClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_pipes.types.pipe_arn.PipeArn",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
    ) -> "aws_sdk_pipes.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Displays the tags associated with a pipe.</p>

        Args:
            resource_arn: <p>The ARN of the pipe for which you want to view tags.</p>

        Raises:
            aws_sdk_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            aws_sdk_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            aws_sdk_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            aws_sdk_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pipes.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pipes.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_pipes._operations.pipes.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_pipes.types.pipe_arn.PipeArn",
        tags: "aws_sdk_pipes.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
    ) -> "aws_sdk_pipes.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified pipe. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with a pipe that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the pipe. If you specify a tag key that is already associated with the pipe, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a pipe.</p>

        Args:
            resource_arn: <p>The ARN of the pipe.</p>
            tags: <p>The list of key-value pairs associated with the pipe.</p>

        Raises:
            aws_sdk_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            aws_sdk_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            aws_sdk_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            aws_sdk_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pipes.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pipes.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_pipes._operations.pipes.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_pipes.types.pipe_arn.PipeArn",
        tag_keys: "aws_sdk_pipes.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
    ) -> "aws_sdk_pipes.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified pipes.</p>

        Args:
            resource_arn: <p>The ARN of the pipe.</p>
            tag_keys: <p>The list of tag keys to remove from the pipe.</p>

        Raises:
            aws_sdk_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            aws_sdk_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            aws_sdk_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            aws_sdk_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pipes.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pipes.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_pipes._operations.pipes.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

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
