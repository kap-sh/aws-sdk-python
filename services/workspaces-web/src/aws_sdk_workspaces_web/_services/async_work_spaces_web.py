"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AWSErmineControlPlaneService``."""

from aws_sdk_workspaces_web._auth._signers import SigV4Signer
from aws_sdk_workspaces_web._auth._sigv4 import presign_sigv4
import datetime
from collections.abc import AsyncIterator
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from aws_sdk_workspaces_web._pagination import resolve_path as _resolve_path
from typing import Any, Iterable, TypedDict, Unpack, TYPE_CHECKING
from typing_extensions import Self
from typing import Optional
from zapros import URL, AsyncBaseHandler, AsyncClient
from aws_sdk_workspaces_web._auth._zapros_handler import AuthMiddleware
from aws_sdk_workspaces_web._services._pipeline import AsyncInterceptor, AsyncOperationOptions, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline, aretry
from aws_sdk_workspaces_web._async import anysleep
import time
from aws_sdk_workspaces_web.errors import ServiceError, WaiterFailedError, WaiterTimeoutError
import warnings
import aws_sdk_workspaces_web._auth._signers
import aws_sdk_workspaces_web._auth._sigv4
from aws_sdk_workspaces_web._auth._identity import Credentials
from aws_sdk_workspaces_web._auth._providers import CredentialsProvider, StaticAwsCredentialsProvider
from aws_sdk_workspaces_web._auth._providers import BearerTokenProvider, StaticBearerTokenProvider
from aws_sdk_workspaces_web._auth._providers import BasicCredentialsProvider, StaticBasicCredentialsProvider
from aws_sdk_workspaces_web._auth._providers import ApiKeyProvider, StaticApiKeyProvider
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.client_token
    import aws_sdk_workspaces_web.types.expire_session_request
    import aws_sdk_workspaces_web.types.expire_session_response
    import aws_sdk_workspaces_web.types.get_session_request
    import aws_sdk_workspaces_web.types.get_session_response
    import aws_sdk_workspaces_web.types.list_sessions_request
    import aws_sdk_workspaces_web.types.list_sessions_response
    import aws_sdk_workspaces_web.types.list_tags_for_resource_request
    import aws_sdk_workspaces_web.types.list_tags_for_resource_response
    import aws_sdk_workspaces_web.types.max_results
    import aws_sdk_workspaces_web.types.pagination_token
    import aws_sdk_workspaces_web.types.portal_id
    import aws_sdk_workspaces_web.types.session_id
    import aws_sdk_workspaces_web.types.session_sort_by
    import aws_sdk_workspaces_web.types.session_status
    import aws_sdk_workspaces_web.types.session_summary
    import aws_sdk_workspaces_web.types.tag_key_list
    import aws_sdk_workspaces_web.types.tag_list
    import aws_sdk_workspaces_web.types.tag_resource_request
    import aws_sdk_workspaces_web.types.tag_resource_response
    import aws_sdk_workspaces_web.types.untag_resource_request
    import aws_sdk_workspaces_web.types.untag_resource_response
    import aws_sdk_workspaces_web.types.username

class AsyncWorkSpacesWebClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None

DEFAULT_RETRY_MAX_ATTEMPTS = 3

async def ensure_async_iterator(it: AsyncIterator[bytes] | bytes) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk

class AsyncWorkSpacesWebClient:
    """A client for the ``WorkSpacesWeb`` service.

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
    def __init__(self, http_handler: AsyncBaseHandler | None = None, operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None, retry_max_attempts: int | None = None, region: str | None = None, use_dual_stack: bool | None = None, use_fips: bool | None = None, endpoint: str | None = None, credentials: Credentials | None = None, credentials_provider: CredentialsProvider | None = None):
        self._client = AsyncClient(http_handler).wrap_with_middleware(lambda next: AuthMiddleware(next))
        if credentials is not None and credentials_provider is not None:
            warnings.warn("Both credentials and credentials_provider given; provider takes precedence")
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncWorkSpacesWebClientConfig({"operation_interceptors": operation_interceptors or [], "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS if retry_max_attempts is None else retry_max_attempts, "region": region, "use_dual_stack": use_dual_stack, "use_fips": use_fips, "endpoint": endpoint, "credentials_provider": credentials_provider})
    def operation_options(self, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncWorkSpacesWebClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [*overrides.get("operation_interceptors", self.config.get("operation_interceptors", [])), aretry()]
        options_: AsyncOperationOptions = AsyncOperationOptions(client=self._client, retry_max_attempts=overrides.get("retry_max_attempts", self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS)), region=overrides.get("region", self.config.get("region")), use_dual_stack=overrides.get("use_dual_stack", self.config.get("use_dual_stack")), use_fips=overrides.get("use_fips", self.config.get("use_fips")), endpoint=overrides.get("endpoint", self.config.get("endpoint")), credentials_provider=overrides.get("credentials_provider", self.config.get("credentials_provider")))
        return interceptors_, options_
    async def expire_session(self, portal_id: "aws_sdk_workspaces_web.types.portal_id.PortalId", session_id: "aws_sdk_workspaces_web.types.session_id.SessionId", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.expire_session_response.ExpireSessionResponse":
        """<p>Expires an active secure browser session.</p>

        Args:
            portal_id: <p>The ID of the web portal for the session.</p>
            session_id: <p>The ID of the session to expire.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.expire_session_request.ExpireSessionRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.expire_session_response.ExpireSessionResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.expire_session
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.expire_session.async_expire_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.expire_session_request.ExpireSessionRequest = {}  # type: ignore[typeddict-item]
        input["portal_id"] = portal_id
        input["session_id"] = session_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_session(self, portal_id: "aws_sdk_workspaces_web.types.portal_id.PortalId", session_id: "aws_sdk_workspaces_web.types.session_id.SessionId", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.get_session_response.GetSessionResponse":
        """<p>Gets information for a secure browser session.</p>

        Args:
            portal_id: <p>The ID of the web portal for the session.</p>
            session_id: <p>The ID of the session.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.get_session_request.GetSessionRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.get_session_response.GetSessionResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_session
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_session.async_get_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.get_session_request.GetSessionRequest = {}  # type: ignore[typeddict-item]
        input["portal_id"] = portal_id
        input["session_id"] = session_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_sessions(self, portal_id: "aws_sdk_workspaces_web.types.portal_id.PortalId", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None, username: Optional["aws_sdk_workspaces_web.types.username.Username"] = None, session_id: Optional["aws_sdk_workspaces_web.types.session_id.SessionId"] = None, sort_by: Optional["aws_sdk_workspaces_web.types.session_sort_by.SessionSortBy"] = None, status: Optional["aws_sdk_workspaces_web.types.session_status.SessionStatus"] = None, max_results: Optional["aws_sdk_workspaces_web.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_workspaces_web.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_workspaces_web.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists information for multiple secure browser sessions from a specific portal.</p>

        Args:
            portal_id: <p>The ID of the web portal for the sessions.</p>
            username: <p>The username of the session.</p>
            session_id: <p>The ID of the session.</p>
            sort_by: <p>The method in which the returned sessions should be sorted.</p>
            status: <p>The status of the session.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.list_sessions_request.ListSessionsRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.list_sessions_response.ListSessionsResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_sessions
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_sessions.async_list_sessions(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.list_sessions_request.ListSessionsRequest = {}  # type: ignore[typeddict-item]
        input["portal_id"] = portal_id
        if username is not None:
            input["username"] = username
        if session_id is not None:
            input["session_id"] = session_id
        if sort_by is not None:
            input["sort_by"] = sort_by
        if status is not None:
            input["status"] = status
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def iter_list_sessions(self, portal_id: "aws_sdk_workspaces_web.types.portal_id.PortalId", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None, username: Optional["aws_sdk_workspaces_web.types.username.Username"] = None, session_id: Optional["aws_sdk_workspaces_web.types.session_id.SessionId"] = None, sort_by: Optional["aws_sdk_workspaces_web.types.session_sort_by.SessionSortBy"] = None, status: Optional["aws_sdk_workspaces_web.types.session_status.SessionStatus"] = None, max_results: Optional["aws_sdk_workspaces_web.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_workspaces_web.types.pagination_token.PaginationToken"] = None) -> "AsyncIterator[aws_sdk_workspaces_web.types.session_summary.SessionSummary]":
        _token = next_token
        while True:
            _response = await self.list_sessions(
                portal_id,
                config_overrides=config_overrides,
                username=username,
                session_id=session_id,
                sort_by=sort_by,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ('sessions',))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ('next_token',))
            if not _token:
                break
    async def list_tags_for_resource(self, resource_arn: "aws_sdk_workspaces_web.types.arn.ARN", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.list_tags_for_resource_request.ListTagsForResourceRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.list_tags_for_resource_response.ListTagsForResourceResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_tags_for_resource
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_tags_for_resource.async_list_tags_for_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def tag_resource(self, resource_arn: "aws_sdk_workspaces_web.types.arn.ARN", tags: "aws_sdk_workspaces_web.types.tag_list.TagList", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None, client_token: Optional["aws_sdk_workspaces_web.types.client_token.ClientToken"] = None) -> "aws_sdk_workspaces_web.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or overwrites one or more tags for the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>The tags of the resource.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.tag_resource_request.TagResourceRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.tag_resource_response.TagResourceResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.tag_resource
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.tag_resource.async_tag_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def untag_resource(self, resource_arn: "aws_sdk_workspaces_web.types.arn.ARN", tag_keys: "aws_sdk_workspaces_web.types.tag_key_list.TagKeyList", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.untag_resource_request.UntagResourceRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.untag_resource_response.UntagResourceResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.untag_resource
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.untag_resource.async_untag_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def __aenter__(self) -> Self:
        return self
    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()