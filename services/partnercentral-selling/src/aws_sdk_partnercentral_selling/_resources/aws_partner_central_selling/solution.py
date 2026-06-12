from typing import TYPE_CHECKING, Optional

from aws_sdk_partnercentral_selling._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.filter_status
    import aws_sdk_partnercentral_selling.types.list_solutions_request
    import aws_sdk_partnercentral_selling.types.list_solutions_response
    import aws_sdk_partnercentral_selling.types.page_size
    import aws_sdk_partnercentral_selling.types.solution_base
    import aws_sdk_partnercentral_selling.types.solution_identifiers
    import aws_sdk_partnercentral_selling.types.solution_sort
    import aws_sdk_partnercentral_selling.types.string_list
    from aws_sdk_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from aws_sdk_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class Solution:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def list(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "aws_sdk_partnercentral_selling.types.solution_sort.SolutionSort"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_selling.types.filter_status.FilterStatus"
        ] = None,
        identifier: Optional[
            "aws_sdk_partnercentral_selling.types.solution_identifiers.SolutionIdentifiers"
        ] = None,
        category: Optional[
            "aws_sdk_partnercentral_selling.types.string_list.StringList"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_solutions_response.ListSolutionsResponse":
        """<p>Retrieves a list of Partner Solutions that the partner registered on Partner Central. This API is used to generate a list of solutions that an end user selects from for association with an opportunity.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the solutions are listed in. Use <code>AWS</code> to list solutions in the Amazon Web Services catalog, and <code>Sandbox</code> to list solutions in a secure and isolated testing environment.</p>
            max_results: <p>The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results.</p> <p>Default: 20</p>
            next_token: <p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>
            sort: <p>Object that configures sorting done on the response. Default <code>Sort.SortBy</code> is <code>Identifier</code>.</p>
            status: <p>Filters solutions based on their status. This filter helps partners manage their solution portfolios effectively.</p>
            identifier: <p>Filters the solutions based on their unique identifier. Use this filter to retrieve specific solutions by providing the solution's identifier for accurate results.</p>
            category: <p>Filters the solutions based on the category to which they belong. This allows partners to search for solutions within specific categories, such as <code>Software</code>, <code>Consulting</code>, or <code>Managed Services</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.list_solutions_request.ListSolutionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.list_solutions_response.ListSolutionsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_solutions

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_solutions.list_solutions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.list_solutions_request.ListSolutionsRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort is not None:
            input["sort"] = sort
        if status is not None:
            input["status"] = status
        if identifier is not None:
            input["identifier"] = identifier
        if category is not None:
            input["category"] = category

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncSolution:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def list(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "aws_sdk_partnercentral_selling.types.solution_sort.SolutionSort"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_selling.types.filter_status.FilterStatus"
        ] = None,
        identifier: Optional[
            "aws_sdk_partnercentral_selling.types.solution_identifiers.SolutionIdentifiers"
        ] = None,
        category: Optional[
            "aws_sdk_partnercentral_selling.types.string_list.StringList"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_solutions_response.ListSolutionsResponse":
        """<p>Retrieves a list of Partner Solutions that the partner registered on Partner Central. This API is used to generate a list of solutions that an end user selects from for association with an opportunity.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the solutions are listed in. Use <code>AWS</code> to list solutions in the Amazon Web Services catalog, and <code>Sandbox</code> to list solutions in a secure and isolated testing environment.</p>
            max_results: <p>The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results.</p> <p>Default: 20</p>
            next_token: <p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>
            sort: <p>Object that configures sorting done on the response. Default <code>Sort.SortBy</code> is <code>Identifier</code>.</p>
            status: <p>Filters solutions based on their status. This filter helps partners manage their solution portfolios effectively.</p>
            identifier: <p>Filters the solutions based on their unique identifier. Use this filter to retrieve specific solutions by providing the solution's identifier for accurate results.</p>
            category: <p>Filters the solutions based on the category to which they belong. This allows partners to search for solutions within specific categories, such as <code>Software</code>, <code>Consulting</code>, or <code>Managed Services</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.list_solutions_request.ListSolutionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.list_solutions_response.ListSolutionsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_solutions

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_solutions.async_list_solutions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.list_solutions_request.ListSolutionsRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort is not None:
            input["sort"] = sort
        if status is not None:
            input["status"] = status
        if identifier is not None:
            input["identifier"] = identifier
        if category is not None:
            input["category"] = category

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
