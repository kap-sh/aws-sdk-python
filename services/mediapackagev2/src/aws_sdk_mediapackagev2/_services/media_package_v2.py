"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#mediapackagev2``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_mediapackagev2._auth._signers
import aws_sdk_mediapackagev2._auth._sigv4
from aws_sdk_mediapackagev2._auth._identity import Credentials
from aws_sdk_mediapackagev2._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_mediapackagev2._auth._zapros_handler import AuthMiddleware
from aws_sdk_mediapackagev2._resources.mediapackagev2.channel_group_resource import (
    ChannelGroupResource,
)
from aws_sdk_mediapackagev2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.list_tags_for_resource_request
    import aws_sdk_mediapackagev2.types.list_tags_for_resource_response
    import aws_sdk_mediapackagev2.types.tag_arn
    import aws_sdk_mediapackagev2.types.tag_key_list
    import aws_sdk_mediapackagev2.types.tag_map
    import aws_sdk_mediapackagev2.types.tag_resource_request
    import aws_sdk_mediapackagev2.types.untag_resource_request


class MediaPackageV2ClientConfig(TypedDict, total=False):
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


class MediaPackageV2Client:
    """A client for the ``MediaPackageV2`` service.

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
        self.config = MediaPackageV2ClientConfig(
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
        self.channel_group_resource = ChannelGroupResource(self)

    def operation_options(
        self, config_overrides: Optional[MediaPackageV2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MediaPackageV2ClientConfig = config_overrides or {}
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
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_mediapackagev2.types.tag_arn.TagArn",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "aws_sdk_mediapackagev2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags assigned to a resource.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch resource that you want to view tags for.</p>

        Examples:
            List all tags for a resource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:mediapackagev2:us-west-2:123456789012:channelGroup/exampleChannelGroup/channel/exampleChannel')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediapackagev2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediapackagev2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_mediapackagev2._operations.mediapackagev2.list_tags_for_resource

            output, http_response = (
                aws_sdk_mediapackagev2._operations.mediapackagev2.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackagev2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_mediapackagev2.types.tag_arn.TagArn",
        tags: "aws_sdk_mediapackagev2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> None:
        """<p>Assigns one of more tags (key-value pairs) to the specified MediaPackage resource.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values. You can use the TagResource operation with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p>

        Args:
            resource_arn: <p>The ARN of the MediaPackage resource that you're adding tags to.</p>
            tags: <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.</p>

        Examples:
            Add tags to a resource

            >>> client.tag_resource(resource_arn='arn:aws:mediapackagev2:us-west-2:123456789012:channelGroup/exampleChannelGroup/channel/exampleChannel', tags={'key3': 'value3', 'key4': 'value4'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediapackagev2.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_mediapackagev2._operations.mediapackagev2.tag_resource

            output, http_response = (
                aws_sdk_mediapackagev2._operations.mediapackagev2.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackagev2.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_mediapackagev2.types.tag_arn.TagArn",
        tag_keys: "aws_sdk_mediapackagev2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> None:
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the MediaPackage resource that you're removing tags from.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Examples:
            Remove tags from a resource

            >>> client.untag_resource(resource_arn='arn:aws:mediapackagev2:us-west-2:123456789012:channelGroup/exampleChannelGroup/channel/exampleChannel', tag_keys=['key3', 'key4'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediapackagev2.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_mediapackagev2._operations.mediapackagev2.untag_resource

            output, http_response = (
                aws_sdk_mediapackagev2._operations.mediapackagev2.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackagev2.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
