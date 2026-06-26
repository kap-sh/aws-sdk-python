"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AWSErmineControlPlaneService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_workspaces_web._auth._signers
import aws_sdk_workspaces_web._auth._sigv4
from aws_sdk_workspaces_web._auth._identity import Credentials
from aws_sdk_workspaces_web._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_workspaces_web._auth._zapros_handler import AuthMiddleware
from aws_sdk_workspaces_web._pagination import resolve_path as _resolve_path
from aws_sdk_workspaces_web._resources.aws_ermine_control_plane_service.browser_settings_resource import (
    BrowserSettingsResource,
)
from aws_sdk_workspaces_web._resources.aws_ermine_control_plane_service.data_protection_settings_resource import (
    DataProtectionSettingsResource,
)
from aws_sdk_workspaces_web._resources.aws_ermine_control_plane_service.identity_provider_resource import (
    IdentityProviderResource,
)
from aws_sdk_workspaces_web._resources.aws_ermine_control_plane_service.ip_access_settings_resource import (
    IpAccessSettingsResource,
)
from aws_sdk_workspaces_web._resources.aws_ermine_control_plane_service.network_settings_resource import (
    NetworkSettingsResource,
)
from aws_sdk_workspaces_web._resources.aws_ermine_control_plane_service.portal_resource import (
    PortalResource,
)
from aws_sdk_workspaces_web._resources.aws_ermine_control_plane_service.session_logger_resource import (
    SessionLoggerResource,
)
from aws_sdk_workspaces_web._resources.aws_ermine_control_plane_service.trust_store_resource import (
    TrustStoreResource,
)
from aws_sdk_workspaces_web._resources.aws_ermine_control_plane_service.user_access_logging_settings_resource import (
    UserAccessLoggingSettingsResource,
)
from aws_sdk_workspaces_web._resources.aws_ermine_control_plane_service.user_settings_resource import (
    UserSettingsResource,
)
from aws_sdk_workspaces_web._services._aws_config import aws_config
from aws_sdk_workspaces_web._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

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


class WorkSpacesWebClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class WorkSpacesWebClient:
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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = WorkSpacesWebClientConfig(
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
        self.browser_settings_resource = BrowserSettingsResource(self)
        self.data_protection_settings_resource = DataProtectionSettingsResource(self)
        self.identity_provider_resource = IdentityProviderResource(self)
        self.ip_access_settings_resource = IpAccessSettingsResource(self)
        self.network_settings_resource = NetworkSettingsResource(self)
        self.portal_resource = PortalResource(self)
        self.session_logger_resource = SessionLoggerResource(self)
        self.trust_store_resource = TrustStoreResource(self)
        self.user_access_logging_settings_resource = UserAccessLoggingSettingsResource(
            self
        )
        self.user_settings_resource = UserSettingsResource(self)

    def operation_options(
        self, config_overrides: Optional[WorkSpacesWebClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: WorkSpacesWebClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def expire_session(
        self,
        portal_id: "aws_sdk_workspaces_web.types.portal_id.PortalId",
        session_id: "aws_sdk_workspaces_web.types.session_id.SessionId",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "aws_sdk_workspaces_web.types.expire_session_response.ExpireSessionResponse":
        """<p>Expires an active secure browser session.</p>

        Args:
            portal_id: <p>The ID of the web portal for the session.</p>
            session_id: <p>The ID of the session to expire.</p>

        Raises:
            aws_sdk_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            aws_sdk_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            aws_sdk_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            aws_sdk_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            aws_sdk_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            aws_sdk_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workspaces_web.types.expire_session_request.ExpireSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_workspaces_web.types.expire_session_response.ExpireSessionResponse"
        ]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.expire_session

            output, http_response = (
                aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.expire_session.expire_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_web.types.expire_session_request.ExpireSessionRequest = {}  # type: ignore[typeddict-item]
        input_["portal_id"] = portal_id
        input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_session(
        self,
        portal_id: "aws_sdk_workspaces_web.types.portal_id.PortalId",
        session_id: "aws_sdk_workspaces_web.types.session_id.SessionId",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "aws_sdk_workspaces_web.types.get_session_response.GetSessionResponse":
        """<p>Gets information for a secure browser session.</p>

        Args:
            portal_id: <p>The ID of the web portal for the session.</p>
            session_id: <p>The ID of the session.</p>

        Raises:
            aws_sdk_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            aws_sdk_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            aws_sdk_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            aws_sdk_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            aws_sdk_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            aws_sdk_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workspaces_web.types.get_session_request.GetSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_workspaces_web.types.get_session_response.GetSessionResponse"
        ]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_session

            output, http_response = (
                aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_session.get_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_web.types.get_session_request.GetSessionRequest = {}  # type: ignore[typeddict-item]
        input_["portal_id"] = portal_id
        input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_sessions(
        self,
        portal_id: "aws_sdk_workspaces_web.types.portal_id.PortalId",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        username: Optional["aws_sdk_workspaces_web.types.username.Username"] = None,
        session_id: Optional[
            "aws_sdk_workspaces_web.types.session_id.SessionId"
        ] = None,
        sort_by: Optional[
            "aws_sdk_workspaces_web.types.session_sort_by.SessionSortBy"
        ] = None,
        status: Optional[
            "aws_sdk_workspaces_web.types.session_status.SessionStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_workspaces_web.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_workspaces_web.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists information for multiple secure browser sessions from a specific portal.</p>

        Args:
            portal_id: <p>The ID of the web portal for the sessions.</p>
            username: <p>The username of the session.</p>
            session_id: <p>The ID of the session.</p>
            sort_by: <p>The method in which the returned sessions should be sorted.</p>
            status: <p>The status of the session.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>

        Raises:
            aws_sdk_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            aws_sdk_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            aws_sdk_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            aws_sdk_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            aws_sdk_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            aws_sdk_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workspaces_web.types.list_sessions_request.ListSessionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workspaces_web.types.list_sessions_response.ListSessionsResponse"
        ]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_sessions

            output, http_response = (
                aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_web.types.list_sessions_request.ListSessionsRequest = {}  # type: ignore[typeddict-item]
        input_["portal_id"] = portal_id
        if username is not None:
            input_["username"] = username
        if session_id is not None:
            input_["session_id"] = session_id
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_sessions(
        self,
        portal_id: "aws_sdk_workspaces_web.types.portal_id.PortalId",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        username: Optional["aws_sdk_workspaces_web.types.username.Username"] = None,
        session_id: Optional[
            "aws_sdk_workspaces_web.types.session_id.SessionId"
        ] = None,
        sort_by: Optional[
            "aws_sdk_workspaces_web.types.session_sort_by.SessionSortBy"
        ] = None,
        status: Optional[
            "aws_sdk_workspaces_web.types.session_status.SessionStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_workspaces_web.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_workspaces_web.types.session_summary.SessionSummary]":
        _token = next_token
        while True:
            _response = self.list_sessions(
                portal_id,
                config_overrides=config_overrides,
                username=username,
                session_id=session_id,
                sort_by=sort_by,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "aws_sdk_workspaces_web.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            aws_sdk_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            aws_sdk_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            aws_sdk_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            aws_sdk_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            aws_sdk_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            aws_sdk_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workspaces_web.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workspaces_web.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_web.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_workspaces_web.types.arn.ARN",
        tags: "aws_sdk_workspaces_web.types.tag_list.TagList",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        client_token: Optional[
            "aws_sdk_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_workspaces_web.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or overwrites one or more tags for the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>The tags of the resource.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            aws_sdk_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            aws_sdk_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            aws_sdk_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            aws_sdk_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            aws_sdk_workspaces_web.errors.too_many_tags_exception.TooManyTagsException: <p>There are too many tags.</p>
            aws_sdk_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            aws_sdk_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workspaces_web.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workspaces_web.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.tag_resource

            output, http_response = (
                aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_web.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_workspaces_web.types.arn.ARN",
        tag_keys: "aws_sdk_workspaces_web.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "aws_sdk_workspaces_web.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            aws_sdk_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            aws_sdk_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            aws_sdk_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            aws_sdk_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            aws_sdk_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            aws_sdk_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workspaces_web.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workspaces_web.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.untag_resource

            output, http_response = (
                aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workspaces_web.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
