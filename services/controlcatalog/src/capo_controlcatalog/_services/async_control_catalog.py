"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlCatalog``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_controlcatalog._auth._signers
import capo_controlcatalog._auth._sigv4
from capo_controlcatalog._auth._identity import Credentials
from capo_controlcatalog._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_controlcatalog._auth._zapros_handler import AuthMiddleware
from capo_controlcatalog._pagination import resolve_path as _resolve_path
from capo_controlcatalog._resources.control_catalog.common_control_resource import (
    AsyncCommonControlResource,
)
from capo_controlcatalog._resources.control_catalog.control_resource import (
    AsyncControlResource,
)
from capo_controlcatalog._resources.control_catalog.domain_resource import (
    AsyncDomainResource,
)
from capo_controlcatalog._resources.control_catalog.objective_resource import (
    AsyncObjectiveResource,
)
from capo_controlcatalog._services._aws_config import aaws_config
from capo_controlcatalog._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_controlcatalog.types.control_mapping
    import capo_controlcatalog.types.control_mapping_filter
    import capo_controlcatalog.types.list_control_mappings_request
    import capo_controlcatalog.types.list_control_mappings_response
    import capo_controlcatalog.types.max_list_control_mappings_results
    import capo_controlcatalog.types.pagination_token


class AsyncControlCatalogClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncControlCatalogClient:
    """A client for the ``ControlCatalog`` service.

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
        self._config = AsyncControlCatalogClientConfig(
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
        self.common_control_resource = AsyncCommonControlResource(self)
        self.control_resource = AsyncControlResource(self)
        self.domain_resource = AsyncDomainResource(self)
        self.objective_resource = AsyncObjectiveResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncControlCatalogClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncControlCatalogClientConfig = config_overrides or {}
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

    async def list_control_mappings(
        self,
        *,
        config_overrides: Optional[AsyncControlCatalogClientConfig] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_control_mappings_results.MaxListControlMappingsResults"
        ] = None,
        filter: Optional[
            "capo_controlcatalog.types.control_mapping_filter.ControlMappingFilter"
        ] = None,
    ) -> "capo_controlcatalog.types.list_control_mappings_response.ListControlMappingsResponse":
        """<p>Returns a paginated list of control mappings from the Control Catalog. Control mappings show relationships between controls and other entities, such as common controls or compliance frameworks.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            filter: <p>An optional filter that narrows the results to specific control mappings based on control ARNs, common control ARNs, or mapping types.</p>

        Raises:
            capo_controlcatalog.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controlcatalog.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred during the processing of your request. Try again later.</p>
            capo_controlcatalog.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controlcatalog.errors.validation_exception.ValidationException: <p>The request has invalid or missing parameters.</p>
            capo_controlcatalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controlcatalog.types.list_control_mappings_request.ListControlMappingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_controlcatalog.types.list_control_mappings_response.ListControlMappingsResponse"
        ]:
            import capo_controlcatalog._operations.control_catalog.list_control_mappings

            (
                output,
                http_response,
            ) = await capo_controlcatalog._operations.control_catalog.list_control_mappings.async_list_control_mappings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controlcatalog.types.list_control_mappings_request.ListControlMappingsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_control_mappings(
        self,
        *,
        config_overrides: Optional[AsyncControlCatalogClientConfig] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_control_mappings_results.MaxListControlMappingsResults"
        ] = None,
        filter: Optional[
            "capo_controlcatalog.types.control_mapping_filter.ControlMappingFilter"
        ] = None,
    ) -> "AsyncIterator[capo_controlcatalog.types.control_mapping.ControlMapping]":
        _token = next_token
        while True:
            _response = await self.list_control_mappings(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("control_mappings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
