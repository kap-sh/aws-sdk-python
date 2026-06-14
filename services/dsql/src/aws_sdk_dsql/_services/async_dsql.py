"""Generated from Smithy shape ``com.amazonaws.dsql#DSQL``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_dsql._auth._signers
import aws_sdk_dsql._auth._sigv4
from aws_sdk_dsql._auth._identity import Credentials
from aws_sdk_dsql._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_dsql._auth._zapros_handler import AuthMiddleware
from aws_sdk_dsql._resources.dsql.cluster import AsyncCluster
from aws_sdk_dsql._resources.dsql.stream import AsyncStream
from aws_sdk_dsql._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_dsql.types.arn
    import aws_sdk_dsql.types.list_tags_for_resource_input
    import aws_sdk_dsql.types.list_tags_for_resource_output
    import aws_sdk_dsql.types.tag_key_list
    import aws_sdk_dsql.types.tag_map
    import aws_sdk_dsql.types.tag_resource_input
    import aws_sdk_dsql.types.untag_resource_input


class AsyncDSQLClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncDSQLClient:
    """A client for the ``DSQL`` service.

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
        self.config = AsyncDSQLClientConfig(
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

        # resources
        self.cluster = AsyncCluster(self)
        self.stream = AsyncStream(self)

    def operation_options(
        self, config_overrides: Optional[AsyncDSQLClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDSQLClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_dsql.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
    ) -> "aws_sdk_dsql.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists all of the tags for a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which you want to list the tags.</p>

        Examples:
            List Tags For Resource

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:dsql:us-east-1:111111222222:cluster/kiqenqglxyl2snyvkvnj2c3s2e')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dsql.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_dsql._operations.dsql.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_dsql.types.arn.Arn",
        tags: "aws_sdk_dsql.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
    ) -> None:
        """<p>Tags a resource with a map of key and value pairs.</p>

        Args:
            resource_arn: <p>The ARN of the resource that you want to tag.</p>
            tags: <p>A map of key and value pairs to use to tag your resource.</p>

        Examples:
            Tag Resource

            >>> await client.tag_resource(resource_arn='arn:aws:dsql:us-east-1:111111222222:cluster/kiqenqglxyl2snyvkvnj2c3s2e', tags={'MyKey': 'MyValue'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_dsql._operations.dsql.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_dsql.types.arn.Arn",
        tag_keys: "aws_sdk_dsql.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
    ) -> None:
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource from which to remove tags.</p>
            tag_keys: <p>The array of keys of the tags that you want to remove.</p>

        Examples:
            Untag Resource

            >>> await client.untag_resource(resource_arn='arn:aws:dsql:us-east-1:111111222222:cluster/kiqenqglxyl2snyvkvnj2c3s2e', tag_keys=['MyKeyA', 'MyKeyB'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dsql.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_dsql._operations.dsql.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_dsql._operations.dsql.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dsql.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
