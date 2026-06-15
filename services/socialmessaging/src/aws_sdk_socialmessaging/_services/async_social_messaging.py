"""Generated from Smithy shape ``com.amazonaws.socialmessaging#SocialMessaging``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_socialmessaging._auth._signers
import aws_sdk_socialmessaging._auth._sigv4
from aws_sdk_socialmessaging._auth._identity import Credentials
from aws_sdk_socialmessaging._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_socialmessaging._auth._zapros_handler import AuthMiddleware
from aws_sdk_socialmessaging._resources.social_messaging.linked_whats_app_business_account_resource import (
    AsyncLinkedWhatsAppBusinessAccountResource,
)
from aws_sdk_socialmessaging._resources.social_messaging.linked_whats_app_phone_number_resource import (
    AsyncLinkedWhatsAppPhoneNumberResource,
)
from aws_sdk_socialmessaging._services._aws_config import aaws_config
from aws_sdk_socialmessaging._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.arn
    import aws_sdk_socialmessaging.types.list_tags_for_resource_input
    import aws_sdk_socialmessaging.types.list_tags_for_resource_output
    import aws_sdk_socialmessaging.types.string_list
    import aws_sdk_socialmessaging.types.tag_list
    import aws_sdk_socialmessaging.types.tag_resource_input
    import aws_sdk_socialmessaging.types.tag_resource_output
    import aws_sdk_socialmessaging.types.untag_resource_input
    import aws_sdk_socialmessaging.types.untag_resource_output


class AsyncSocialMessagingClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class AsyncSocialMessagingClient:
    """A client for the ``SocialMessaging`` service.

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
        self._config = AsyncSocialMessagingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

        # resources
        self.linked_whats_app_business_account_resource = (
            AsyncLinkedWhatsAppBusinessAccountResource(self)
        )
        self.linked_whats_app_phone_number_resource = (
            AsyncLinkedWhatsAppPhoneNumberResource(self)
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSocialMessagingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSocialMessagingClientConfig = config_overrides or {}
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
        resource_arn: "aws_sdk_socialmessaging.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>List all tags associated with a resource, such as a phone number or WABA.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to retrieve the tags from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_socialmessaging.types.arn.Arn",
        tags: "aws_sdk_socialmessaging.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.tag_resource_output.TagResourceOutput":
        """<p>Adds or overwrites only the specified tags for the specified resource. When you specify an existing tag key, the value is overwritten with the new value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>The tags to add to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_socialmessaging.types.arn.Arn",
        tag_keys: "aws_sdk_socialmessaging.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncSocialMessagingClientConfig] = None,
    ) -> "aws_sdk_socialmessaging.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes the specified tags from a resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The keys of the tags to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_socialmessaging.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_socialmessaging.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_socialmessaging._operations.social_messaging.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_socialmessaging._operations.social_messaging.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_socialmessaging.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
