"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#PartnerCentralChannel``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

from aws_sdk_partnercentral_channel._auth._identity import Credentials
from aws_sdk_partnercentral_channel._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_partnercentral_channel._auth._zapros_handler import AuthMiddleware
from aws_sdk_partnercentral_channel._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
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


class PartnerCentralChannelClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class PartnerCentralChannelClient:
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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = PartnerCentralChannelClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[PartnerCentralChannelClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PartnerCentralChannelClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_channel.types.taggable_arn.TaggableArn",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "aws_sdk_partnercentral_channel.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags associated with a specific resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>

        Examples:
            Example for ListTagsForResource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/program-management-account/pma-u8ic702rtzng8')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.list_tags_for_resource

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_partnercentral_channel.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_channel.types.taggable_arn.TaggableArn",
        tags: "aws_sdk_partnercentral_channel.types.tag_list.TagList",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> (
        "aws_sdk_partnercentral_channel.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Adds or updates tags for a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>Key-value pairs to associate with the resource.</p>

        Examples:
            Example for TagResource

            >>> client.tag_resource(resource_arn='arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/program-management-account/pma-u8ic702rtzng8/relationship/rs-l9o4fj3b5zb91', tags=[{'key': 'ExampleKey', 'value': 'ExampleValue'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.tag_resource

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_partnercentral_channel.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_channel.types.taggable_arn.TaggableArn",
        tag_keys: "aws_sdk_partnercentral_channel.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "aws_sdk_partnercentral_channel.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The keys of the tags to remove from the resource.</p>

        Examples:
            Example for UntagResource

            >>> client.untag_resource(resource_arn='arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/channel-handshake/ch-4fj3bd2o3vb91', tag_keys=['ExampleKey'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.untag_resource

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_partnercentral_channel.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
