from typing import TYPE_CHECKING, Optional

import aws_sdk_controlcatalog._auth._signers
import aws_sdk_controlcatalog._auth._sigv4
from aws_sdk_controlcatalog._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.domain_summary
    import aws_sdk_controlcatalog.types.list_domains_request
    import aws_sdk_controlcatalog.types.list_domains_response
    import aws_sdk_controlcatalog.types.max_list_domains_results
    import aws_sdk_controlcatalog.types.pagination_token
    from aws_sdk_controlcatalog._services.async_control_catalog import (
        AsyncControlCatalogClient,
        AsyncControlCatalogClientConfig,
    )
    from aws_sdk_controlcatalog._services.control_catalog import (
        ControlCatalogClient,
        ControlCatalogClientConfig,
    )


class DomainResource:
    def __init__(self, service: ControlCatalogClient) -> None:
        self._service = service

    def list(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        max_results: Optional[
            "aws_sdk_controlcatalog.types.max_list_domains_results.MaxListDomainsResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_controlcatalog.types.list_domains_response.ListDomainsResponse":
        """<p>Returns a paginated list of domains from the Control Catalog.</p>

        Args:
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controlcatalog.types.list_domains_request.ListDomainsRequest]",
        ) -> OperationResponse[
            "aws_sdk_controlcatalog.types.list_domains_response.ListDomainsResponse"
        ]:
            import aws_sdk_controlcatalog._operations.control_catalog.list_domains

            output, http_response = (
                aws_sdk_controlcatalog._operations.control_catalog.list_domains.list_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controlcatalog.types.list_domains_request.ListDomainsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncDomainResource:
    def __init__(self, service: AsyncControlCatalogClient) -> None:
        self._service = service

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncControlCatalogClientConfig] = None,
        max_results: Optional[
            "aws_sdk_controlcatalog.types.max_list_domains_results.MaxListDomainsResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_controlcatalog.types.list_domains_response.ListDomainsResponse":
        """<p>Returns a paginated list of domains from the Control Catalog.</p>

        Args:
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controlcatalog.types.list_domains_request.ListDomainsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controlcatalog.types.list_domains_response.ListDomainsResponse"
        ]:
            import aws_sdk_controlcatalog._operations.control_catalog.list_domains

            (
                output,
                http_response,
            ) = await aws_sdk_controlcatalog._operations.control_catalog.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controlcatalog.types.list_domains_request.ListDomainsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
