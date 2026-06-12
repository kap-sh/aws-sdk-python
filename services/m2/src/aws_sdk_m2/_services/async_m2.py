"""Generated from Smithy shape ``com.amazonaws.m2#AwsSupernovaControlPlaneService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_m2._auth._signers
import aws_sdk_m2._auth._sigv4
from aws_sdk_m2._auth._identity import Credentials
from aws_sdk_m2._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_m2._auth._zapros_handler import AuthMiddleware
from aws_sdk_m2._pagination import resolve_path as _resolve_path
from aws_sdk_m2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_m2.types.arn
    import aws_sdk_m2.types.engine_type
    import aws_sdk_m2.types.engine_versions_summary
    import aws_sdk_m2.types.get_signed_bluinsights_url_response
    import aws_sdk_m2.types.list_engine_versions_request
    import aws_sdk_m2.types.list_engine_versions_response
    import aws_sdk_m2.types.list_tags_for_resource_request
    import aws_sdk_m2.types.list_tags_for_resource_response
    import aws_sdk_m2.types.max_results
    import aws_sdk_m2.types.next_token
    import aws_sdk_m2.types.tag_key_list
    import aws_sdk_m2.types.tag_map
    import aws_sdk_m2.types.tag_resource_request
    import aws_sdk_m2.types.tag_resource_response
    import aws_sdk_m2.types.untag_resource_request
    import aws_sdk_m2.types.untag_resource_response


class Asyncm2ClientConfig(TypedDict, total=False):
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


class Asyncm2Client:
    """A client for the ``m2`` service.

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
        self.config = Asyncm2ClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[Asyncm2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: Asyncm2ClientConfig = config_overrides or {}
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

    async def get_signed_bluinsights_url(
        self, *, config_overrides: Optional[Asyncm2ClientConfig] = None
    ) -> "aws_sdk_m2.types.get_signed_bluinsights_url_response.GetSignedBluinsightsUrlResponse":
        """<p>Gets a single sign-on URL that can be used to connect to AWS Blu Insights.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_m2.types.get_signed_bluinsights_url_response.GetSignedBluinsightsUrlResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.get_signed_bluinsights_url

            (
                output,
                http_response,
            ) = await aws_sdk_m2._operations.aws_supernova_control_plane_service.get_signed_bluinsights_url.async_get_signed_bluinsights_url(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_engine_versions(
        self,
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        engine_type: Optional["aws_sdk_m2.types.engine_type.EngineType"] = None,
        next_token: Optional["aws_sdk_m2.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_m2.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_m2.types.list_engine_versions_response.ListEngineVersionsResponse":
        """<p>Lists the available engine versions.</p>

        Args:
            engine_type: <p>The type of target platform.</p>
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_m2.types.list_engine_versions_request.ListEngineVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_m2.types.list_engine_versions_response.ListEngineVersionsResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.list_engine_versions

            (
                output,
                http_response,
            ) = await aws_sdk_m2._operations.aws_supernova_control_plane_service.list_engine_versions.async_list_engine_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_m2.types.list_engine_versions_request.ListEngineVersionsRequest = {}  # type: ignore[typeddict-item]
        if engine_type is not None:
            input["engine_type"] = engine_type
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_engine_versions(
        self,
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        engine_type: Optional["aws_sdk_m2.types.engine_type.EngineType"] = None,
        next_token: Optional["aws_sdk_m2.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_m2.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[aws_sdk_m2.types.engine_versions_summary.EngineVersionsSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_engine_versions(
                config_overrides=config_overrides,
                engine_type=engine_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("engine_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_m2.types.arn.Arn",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "aws_sdk_m2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_m2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_m2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_m2._operations.aws_supernova_control_plane_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_m2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_m2.types.arn.Arn",
        tags: "aws_sdk_m2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "aws_sdk_m2.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags to add to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_m2.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_m2.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_m2._operations.aws_supernova_control_plane_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_m2.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_m2.types.arn.Arn",
        tag_keys: "aws_sdk_m2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "aws_sdk_m2.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The keys of the tags to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_m2.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_m2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_m2._operations.aws_supernova_control_plane_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_m2.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
