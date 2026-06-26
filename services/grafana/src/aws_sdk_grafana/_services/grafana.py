"""Generated from Smithy shape ``com.amazonaws.grafana#AWSGrafanaControlPlane``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

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
from aws_sdk_grafana._resources.aws_grafana_control_plane.api_key import ApiKey
from aws_sdk_grafana._resources.aws_grafana_control_plane.authentication import (
    Authentication,
)
from aws_sdk_grafana._resources.aws_grafana_control_plane.configuration import (
    Configuration,
)
from aws_sdk_grafana._resources.aws_grafana_control_plane.license import License
from aws_sdk_grafana._resources.aws_grafana_control_plane.permission import Permission
from aws_sdk_grafana._resources.aws_grafana_control_plane.service_account import (
    ServiceAccount,
)
from aws_sdk_grafana._resources.aws_grafana_control_plane.service_account_token import (
    ServiceAccountToken,
)
from aws_sdk_grafana._resources.aws_grafana_control_plane.workspace import Workspace
from aws_sdk_grafana._services._aws_config import aws_config
from aws_sdk_grafana._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
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


class grafanaClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class grafanaClient:
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
        self._config = grafanaClientConfig(
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
        self.api_key = ApiKey(self)
        self.authentication = Authentication(self)
        self.configuration = Configuration(self)
        self.license = License(self)
        self.permission = Permission(self)
        self.service_account = ServiceAccount(self)
        self.service_account_token = ServiceAccountToken(self)
        self.workspace = Workspace(self)

    def operation_options(
        self, config_overrides: Optional[grafanaClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: grafanaClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>The <code>ListTagsForResource</code> operation returns the tags that are associated with the Amazon Managed Service for Grafana resource specified by the <code>resourceArn</code>. Currently, the only resource that can be tagged is a workspace. </p>

        Args:
            resource_arn: <p>The ARN of the resource the list of tags are associated with.</p>

        Raises:
            aws_sdk_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            aws_sdk_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            aws_sdk_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            aws_sdk_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            aws_sdk_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_tags_for_resource

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_versions(
        self,
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
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

        Raises:
            aws_sdk_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            aws_sdk_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            aws_sdk_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            aws_sdk_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            aws_sdk_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.list_versions_request.ListVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.list_versions_response.ListVersionsResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_versions

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.list_versions.list_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.list_versions_request.ListVersionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if workspace_id is not None:
            input_["workspace_id"] = workspace_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_versions(
        self,
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_grafana.types.pagination_token.PaginationToken"
        ] = None,
        workspace_id: Optional["aws_sdk_grafana.types.workspace_id.WorkspaceId"] = None,
    ) -> "Iterator[aws_sdk_grafana.types.grafana_version.GrafanaVersion]":
        _token = next_token
        while True:
            _response = self.list_versions(
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

    def tag_resource(
        self,
        resource_arn: str,
        tags: "aws_sdk_grafana.types.tag_map.TagMap",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.tag_resource_response.TagResourceResponse":
        """<p>The <code>TagResource</code> operation associates tags with an Amazon Managed Grafana resource. Currently, the only resource that can be tagged is workspaces. </p> <p>If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p>

        Args:
            resource_arn: <p>The ARN of the resource the tag is associated with.</p>
            tags: <p>The list of tag keys and values to associate with the resource. You can associate tag keys only, tags (key and values) only or a combination of tag keys and tags.</p>

        Raises:
            aws_sdk_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            aws_sdk_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            aws_sdk_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            aws_sdk_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            aws_sdk_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.tag_resource

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: str,
        tag_keys: "aws_sdk_grafana.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.untag_resource_response.UntagResourceResponse":
        """<p>The <code>UntagResource</code> operation removes the association of the tag with the Amazon Managed Grafana resource. </p>

        Args:
            resource_arn: <p>The ARN of the resource the tag association is removed from. </p>
            tag_keys: <p>The key values of the tag to be removed from the resource.</p>

        Raises:
            aws_sdk_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            aws_sdk_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            aws_sdk_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            aws_sdk_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            aws_sdk_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.untag_resource

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
