"""Generated from Smithy shape ``com.amazonaws.grafana#AWSGrafanaControlPlane``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_grafana._auth._signers
import aws_sdk_grafana._auth._sigv4
from aws_sdk_grafana._auth._identity import Credentials
from aws_sdk_grafana._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_grafana._auth._zapros_handler import AuthMiddleware
from aws_sdk_grafana._pagination import resolve_path as _resolve_path
from aws_sdk_grafana._resources.aws_grafana_control_plane.api_key import AsyncApiKey
from aws_sdk_grafana._resources.aws_grafana_control_plane.authentication import (
    AsyncAuthentication,
)
from aws_sdk_grafana._resources.aws_grafana_control_plane.configuration import (
    AsyncConfiguration,
)
from aws_sdk_grafana._resources.aws_grafana_control_plane.license import AsyncLicense
from aws_sdk_grafana._resources.aws_grafana_control_plane.permission import (
    AsyncPermission,
)
from aws_sdk_grafana._resources.aws_grafana_control_plane.service_account import (
    AsyncServiceAccount,
)
from aws_sdk_grafana._resources.aws_grafana_control_plane.service_account_token import (
    AsyncServiceAccountToken,
)
from aws_sdk_grafana._resources.aws_grafana_control_plane.workspace import (
    AsyncWorkspace,
)
from aws_sdk_grafana._services._aws_config import aaws_config
from aws_sdk_grafana._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_grafana.types.grafana_version
    import aws_sdk_grafana.types.list_tags_for_resource_request
    import aws_sdk_grafana.types.list_tags_for_resource_response
    import aws_sdk_grafana.types.list_versions_request
    import aws_sdk_grafana.types.list_versions_response
    import aws_sdk_grafana.types.pagination_token
    import aws_sdk_grafana.types.tag_keys
    import aws_sdk_grafana.types.tag_map
    import aws_sdk_grafana.types.tag_resource_request
    import aws_sdk_grafana.types.tag_resource_response
    import aws_sdk_grafana.types.untag_resource_request
    import aws_sdk_grafana.types.untag_resource_response
    import aws_sdk_grafana.types.workspace_id


class AsyncgrafanaClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncgrafanaClient:
    """A client for the ``grafana`` service.

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
        self._config = AsyncgrafanaClientConfig(
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
        self.api_key = AsyncApiKey(self)
        self.authentication = AsyncAuthentication(self)
        self.configuration = AsyncConfiguration(self)
        self.license = AsyncLicense(self)
        self.permission = AsyncPermission(self)
        self.service_account = AsyncServiceAccount(self)
        self.service_account_token = AsyncServiceAccountToken(self)
        self.workspace = AsyncWorkspace(self)

    def operation_options(
        self, config_overrides: Optional[AsyncgrafanaClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncgrafanaClientConfig = config_overrides or {}
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
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>The <code>ListTagsForResource</code> operation returns the tags that are associated with the Amazon Managed Service for Grafana resource specified by the <code>resourceArn</code>. Currently, the only resource that can be tagged is a workspace. </p>

        Args:
            resource_arn: <p>The ARN of the resource the list of tags are associated with.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_versions(
        self,
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_grafana.types.pagination_token.PaginationToken"
        ] = None,
        workspace_id: Optional["aws_sdk_grafana.types.workspace_id.WorkspaceId"] = None,
    ) -> "aws_sdk_grafana.types.list_versions_response.ListVersionsResponse":
        """<p>Lists available versions of Grafana. These are available when calling <code>CreateWorkspace</code>. Optionally, include a workspace to list the versions to which it can be upgraded.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token to use when requesting the next set of results. You receive this token from a previous <code>ListVersions</code> operation.</p>
            workspace_id: <p>The ID of the workspace to list the available upgrade versions. If not included, lists all versions of Grafana that are supported for <code>CreateWorkspace</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.list_versions_request.ListVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.list_versions_response.ListVersionsResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_versions

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.list_versions.async_list_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.list_versions_request.ListVersionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if workspace_id is not None:
            input_["workspace_id"] = workspace_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_versions(
        self,
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_grafana.types.pagination_token.PaginationToken"
        ] = None,
        workspace_id: Optional["aws_sdk_grafana.types.workspace_id.WorkspaceId"] = None,
    ) -> "AsyncIterator[aws_sdk_grafana.types.grafana_version.GrafanaVersion]":
        _token = next_token
        while True:
            _response = await self.list_versions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                workspace_id=workspace_id,
            )
            _page = _resolve_path(_response, ("grafana_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def tag_resource(
        self,
        resource_arn: str,
        tags: "aws_sdk_grafana.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.tag_resource_response.TagResourceResponse":
        """<p>The <code>TagResource</code> operation associates tags with an Amazon Managed Grafana resource. Currently, the only resource that can be tagged is workspaces. </p> <p>If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p>

        Args:
            resource_arn: <p>The ARN of the resource the tag is associated with.</p>
            tags: <p>The list of tag keys and values to associate with the resource. You can associate tag keys only, tags (key and values) only or a combination of tag keys and tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: str,
        tag_keys: "aws_sdk_grafana.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.untag_resource_response.UntagResourceResponse":
        """<p>The <code>UntagResource</code> operation removes the association of the tag with the Amazon Managed Grafana resource. </p>

        Args:
            resource_arn: <p>The ARN of the resource the tag association is removed from. </p>
            tag_keys: <p>The key values of the tag to be removed from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
