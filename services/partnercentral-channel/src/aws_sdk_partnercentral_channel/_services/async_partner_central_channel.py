"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#PartnerCentralChannel``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_partnercentral_channel._auth._signers
import aws_sdk_partnercentral_channel._auth._sigv4
from aws_sdk_partnercentral_channel._auth._identity import Credentials
from aws_sdk_partnercentral_channel._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_partnercentral_channel._auth._zapros_handler import AuthMiddleware
from aws_sdk_partnercentral_channel._resources.partner_central_channel.channel_handshake_resource import (
    AsyncChannelHandshakeResource,
)
from aws_sdk_partnercentral_channel._resources.partner_central_channel.program_management_account_resource import (
    AsyncProgramManagementAccountResource,
)
from aws_sdk_partnercentral_channel._resources.partner_central_channel.relationship_resource import (
    AsyncRelationshipResource,
)
from aws_sdk_partnercentral_channel._services._aws_config import aaws_config
from aws_sdk_partnercentral_channel._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.list_tags_for_resource_request
    import aws_sdk_partnercentral_channel.types.list_tags_for_resource_response
    import aws_sdk_partnercentral_channel.types.tag_key_list
    import aws_sdk_partnercentral_channel.types.tag_list
    import aws_sdk_partnercentral_channel.types.tag_resource_request
    import aws_sdk_partnercentral_channel.types.tag_resource_response
    import aws_sdk_partnercentral_channel.types.taggable_arn
    import aws_sdk_partnercentral_channel.types.untag_resource_request
    import aws_sdk_partnercentral_channel.types.untag_resource_response


class AsyncPartnerCentralChannelClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


class AsyncPartnerCentralChannelClient:
    """A client for the ``PartnerCentralChannel`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncPartnerCentralChannelClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

        # resources
        self.channel_handshake_resource = AsyncChannelHandshakeResource(self)
        self.program_management_account_resource = (
            AsyncProgramManagementAccountResource(self)
        )
        self.relationship_resource = AsyncRelationshipResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPartnerCentralChannelClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_channel.types.taggable_arn.TaggableArn",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
    ) -> "aws_sdk_partnercentral_channel.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags associated with a specific resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>

        Examples:
            Example for ListTagsForResource

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/program-management-account/pma-u8ic702rtzng8')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_channel.types.taggable_arn.TaggableArn",
        tags: "aws_sdk_partnercentral_channel.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
    ) -> (
        "aws_sdk_partnercentral_channel.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Adds or updates tags for a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>Key-value pairs to associate with the resource.</p>

        Examples:
            Example for TagResource

            >>> await client.tag_resource(resource_arn='arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/program-management-account/pma-u8ic702rtzng8/relationship/rs-l9o4fj3b5zb91', tags=[{'key': 'ExampleKey', 'value': 'ExampleValue'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_partnercentral_channel.types.taggable_arn.TaggableArn",
        tag_keys: "aws_sdk_partnercentral_channel.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
    ) -> "aws_sdk_partnercentral_channel.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The keys of the tags to remove from the resource.</p>

        Examples:
            Example for UntagResource

            >>> await client.untag_resource(resource_arn='arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/channel-handshake/ch-4fj3bd2o3vb91', tag_keys=['ExampleKey'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
