"""Generated from Smithy shape ``com.amazonaws.appmesh#AppMesh``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_app_mesh._auth._signers
import aws_sdk_app_mesh._auth._sigv4
from aws_sdk_app_mesh._auth._identity import Credentials
from aws_sdk_app_mesh._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_app_mesh._auth._zapros_handler import AuthMiddleware
from aws_sdk_app_mesh._pagination import resolve_path as _resolve_path
from aws_sdk_app_mesh._resources.app_mesh.mesh import AsyncMesh
from aws_sdk_app_mesh._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.arn
    import aws_sdk_app_mesh.types.list_tags_for_resource_input
    import aws_sdk_app_mesh.types.list_tags_for_resource_output
    import aws_sdk_app_mesh.types.tag_key_list
    import aws_sdk_app_mesh.types.tag_list
    import aws_sdk_app_mesh.types.tag_ref
    import aws_sdk_app_mesh.types.tag_resource_input
    import aws_sdk_app_mesh.types.tag_resource_output
    import aws_sdk_app_mesh.types.tags_limit
    import aws_sdk_app_mesh.types.untag_resource_input
    import aws_sdk_app_mesh.types.untag_resource_output


class AsyncAppMeshClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
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


class AsyncAppMeshClient:
    """A client for the ``AppMesh`` service.

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
        self.config = AsyncAppMeshClientConfig(
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
        self.mesh = AsyncMesh(self)

    def operation_options(
        self, config_overrides: Optional[AsyncAppMeshClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAppMeshClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_app_mesh.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["aws_sdk_app_mesh.types.tags_limit.TagsLimit"] = None,
    ) -> (
        "aws_sdk_app_mesh.types.list_tags_for_resource_output.ListTagsForResourceOutput"
    ):
        """<p>List the tags for an App Mesh resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListTagsForResource</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>
            limit: <p>The maximum number of tag results returned by <code>ListTagsForResource</code> in paginated output. When this parameter is used, <code>ListTagsForResource</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListTagsForResource</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListTagsForResource</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_app_mesh.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_app_mesh.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_app_mesh._operations.app_mesh.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_app_mesh._operations.app_mesh.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_app_mesh.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_app_mesh.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["aws_sdk_app_mesh.types.tags_limit.TagsLimit"] = None,
    ) -> "AsyncIterator[aws_sdk_app_mesh.types.tag_ref.TagRef]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_app_mesh.types.arn.Arn",
        tags: "aws_sdk_app_mesh.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
    ) -> "aws_sdk_app_mesh.types.tag_resource_output.TagResourceOutput":
        """<p>Associates the specified tags to a resource with the specified <code>resourceArn</code>. If existing tags on a resource aren't specified in the request parameters, they aren't changed. When a resource is deleted, the tags associated with that resource are also deleted.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>
            tags: <p>The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_app_mesh.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_app_mesh.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_app_mesh._operations.app_mesh.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_app_mesh._operations.app_mesh.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_app_mesh.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_app_mesh.types.arn.Arn",
        tag_keys: "aws_sdk_app_mesh.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
    ) -> "aws_sdk_app_mesh.types.untag_resource_output.UntagResourceOutput":
        """<p>Deletes specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to delete tags from.</p>
            tag_keys: <p>The keys of the tags to be removed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_app_mesh.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_app_mesh.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_app_mesh._operations.app_mesh.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_app_mesh._operations.app_mesh.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_app_mesh.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
