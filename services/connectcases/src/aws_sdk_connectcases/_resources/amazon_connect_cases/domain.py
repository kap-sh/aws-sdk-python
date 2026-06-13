from typing import TYPE_CHECKING, Optional

import aws_sdk_connectcases._auth._signers
import aws_sdk_connectcases._auth._sigv4
from aws_sdk_connectcases._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.create_domain_request
    import aws_sdk_connectcases.types.create_domain_response
    import aws_sdk_connectcases.types.delete_domain_request
    import aws_sdk_connectcases.types.delete_domain_response
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.domain_name
    import aws_sdk_connectcases.types.event_bridge_configuration
    import aws_sdk_connectcases.types.get_case_event_configuration_request
    import aws_sdk_connectcases.types.get_case_event_configuration_response
    import aws_sdk_connectcases.types.get_domain_request
    import aws_sdk_connectcases.types.get_domain_response
    import aws_sdk_connectcases.types.list_domains_request
    import aws_sdk_connectcases.types.list_domains_response
    import aws_sdk_connectcases.types.max_results
    import aws_sdk_connectcases.types.next_token
    import aws_sdk_connectcases.types.put_case_event_configuration_request
    import aws_sdk_connectcases.types.put_case_event_configuration_response
    import aws_sdk_connectcases.types.related_item_filter_list
    import aws_sdk_connectcases.types.search_all_related_items_request
    import aws_sdk_connectcases.types.search_all_related_items_response
    import aws_sdk_connectcases.types.search_all_related_items_response_item
    import aws_sdk_connectcases.types.search_all_related_items_sort_list
    from aws_sdk_connectcases._services.async_connect_cases import (
        AsyncConnectCasesClient,
        AsyncConnectCasesClientConfig,
    )
    from aws_sdk_connectcases._services.connect_cases import (
        ConnectCasesClient,
        ConnectCasesClientConfig,
    )


class Domain:
    def __init__(self, service: ConnectCasesClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_connectcases.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.create_domain_response.CreateDomainResponse":
        """<p>Creates a domain, which is a container for all case data, such as cases, fields, templates and layouts. Each Amazon Connect instance can be associated with only one Cases domain.</p> <important> <p>This will not associate your connect instance to Cases domain. Instead, use the Amazon Connect <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html\">CreateIntegrationAssociation</a> API. You need specific IAM permissions to successfully associate the Cases domain. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/required-permissions-iam-cases.html#onboard-cases-iam\">Onboard to Cases</a>.</p> </important>

        Args:
            name: <p>The name for your Cases domain. It must be unique for your Amazon Web Services account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.create_domain_request.CreateDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.create_domain_response.CreateDomainResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.create_domain

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.create_domain.create_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.create_domain_request.CreateDomainRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.get_domain_response.GetDomainResponse":
        """<p>Returns information about a specific domain if it exists. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.get_domain_request.GetDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.get_domain_response.GetDomainResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.get_domain

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.get_domain.get_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.get_domain_request.GetDomainRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.delete_domain_response.DeleteDomainResponse":
        """<p>Deletes a Cases domain.</p> <note> <p>After deleting your domain you must disassociate the deleted domain from your Amazon Connect instance with another API call before being able to use Cases again with this Amazon Connect instance. See <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteIntegrationAssociation.html\">DeleteIntegrationAssociation</a>.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.delete_domain_request.DeleteDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.delete_domain_response.DeleteDomainResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.delete_domain

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.delete_domain.delete_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.delete_domain_request.DeleteDomainRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcases.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.list_domains_response.ListDomainsResponse":
        """<p>Lists all cases domains in the Amazon Web Services account. Each list item is a condensed summary object of the domain.</p>

        Args:
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.list_domains_request.ListDomainsRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.list_domains_response.ListDomainsResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.list_domains

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.list_domains.list_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.list_domains_request.ListDomainsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_case_event_configuration(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.get_case_event_configuration_response.GetCaseEventConfigurationResponse":
        """<p>Returns the case event publishing configuration.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.get_case_event_configuration_request.GetCaseEventConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.get_case_event_configuration_response.GetCaseEventConfigurationResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.get_case_event_configuration

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.get_case_event_configuration.get_case_event_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.get_case_event_configuration_request.GetCaseEventConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_case_event_configuration(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        event_bridge: "aws_sdk_connectcases.types.event_bridge_configuration.EventBridgeConfiguration",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.put_case_event_configuration_response.PutCaseEventConfigurationResponse":
        """<p>Adds case event publishing configuration. For a complete list of fields you can add to the event message, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html\">Create case fields</a> in the <i>Amazon Connect Administrator Guide</i> </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            event_bridge: <p>Configuration to enable EventBridge case event delivery and determine what data is delivered.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.put_case_event_configuration_request.PutCaseEventConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.put_case_event_configuration_response.PutCaseEventConfigurationResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.put_case_event_configuration

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.put_case_event_configuration.put_case_event_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.put_case_event_configuration_request.PutCaseEventConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        input["event_bridge"] = event_bridge

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_all_related_items(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
        filters: Optional[
            "aws_sdk_connectcases.types.related_item_filter_list.RelatedItemFilterList"
        ] = None,
        sorts: Optional[
            "aws_sdk_connectcases.types.search_all_related_items_sort_list.SearchAllRelatedItemsSortList"
        ] = None,
    ) -> "aws_sdk_connectcases.types.search_all_related_items_response.SearchAllRelatedItemsResponse":
        """<p>Searches for related items across all cases within a domain. This is a global search operation that returns related items from multiple cases, unlike the case-specific <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchRelatedItems.html\">SearchRelatedItems</a> API.</p> <p> <b>Use cases</b> </p> <p>Following are common uses cases for this API:</p> <ul> <li> <p>Find cases with similar issues across the domain. For example, search for all cases containing comments about \"product defect\" to identify patterns and existing solutions.</p> </li> <li> <p>Locate all cases associated with specific contacts or orders. For example, find all cases linked to a contactArn to understand the complete customer journey. </p> </li> <li> <p>Monitor SLA compliance across cases. For example, search for all cases with \"Active\" SLA status to prioritize remediation efforts.</p> </li> </ul> <p> <b>Important things to know</b> </p> <ul> <li> <p>This API returns case identifiers, not complete case objects. To retrieve full case details, you must make additional calls to the <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCase.html\">GetCase</a> API for each returned case ID. </p> </li> <li> <p>This API searches across related items content, not case fields. Use the <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchCases.html\">SearchCases</a> API to search within case field values.</p> </li> </ul> <p> <b>Endpoints</b>: See <a href=\"https://docs.aws.amazon.com/general/latest/gr/connect_region.html\">Amazon Connect endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            filters: <p>The list of types of related items and their parameters to use for filtering. The filters work as an OR condition: caller gets back related items that match any of the specified filter types.</p>
            sorts: <p>A structured set of sort terms to specify the order in which related items should be returned. Supports sorting by association time or case ID. The sorts work in the order specified: first sort term takes precedence over subsequent terms.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.search_all_related_items_request.SearchAllRelatedItemsRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.search_all_related_items_response.SearchAllRelatedItemsResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.search_all_related_items

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.search_all_related_items.search_all_related_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.search_all_related_items_request.SearchAllRelatedItemsRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters
        if sorts is not None:
            input["sorts"] = sorts

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDomain:
    def __init__(self, service: AsyncConnectCasesClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_connectcases.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.create_domain_response.CreateDomainResponse":
        """<p>Creates a domain, which is a container for all case data, such as cases, fields, templates and layouts. Each Amazon Connect instance can be associated with only one Cases domain.</p> <important> <p>This will not associate your connect instance to Cases domain. Instead, use the Amazon Connect <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html\">CreateIntegrationAssociation</a> API. You need specific IAM permissions to successfully associate the Cases domain. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/required-permissions-iam-cases.html#onboard-cases-iam\">Onboard to Cases</a>.</p> </important>

        Args:
            name: <p>The name for your Cases domain. It must be unique for your Amazon Web Services account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.create_domain_request.CreateDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.create_domain_response.CreateDomainResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.create_domain

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.create_domain_request.CreateDomainRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.get_domain_response.GetDomainResponse":
        """<p>Returns information about a specific domain if it exists. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.get_domain_request.GetDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.get_domain_response.GetDomainResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.get_domain

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.get_domain.async_get_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.get_domain_request.GetDomainRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.delete_domain_response.DeleteDomainResponse":
        """<p>Deletes a Cases domain.</p> <note> <p>After deleting your domain you must disassociate the deleted domain from your Amazon Connect instance with another API call before being able to use Cases again with this Amazon Connect instance. See <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteIntegrationAssociation.html\">DeleteIntegrationAssociation</a>.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.delete_domain_request.DeleteDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.delete_domain_response.DeleteDomainResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.delete_domain

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.delete_domain_request.DeleteDomainRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcases.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.list_domains_response.ListDomainsResponse":
        """<p>Lists all cases domains in the Amazon Web Services account. Each list item is a condensed summary object of the domain.</p>

        Args:
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.list_domains_request.ListDomainsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.list_domains_response.ListDomainsResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.list_domains

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.list_domains_request.ListDomainsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_case_event_configuration(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.get_case_event_configuration_response.GetCaseEventConfigurationResponse":
        """<p>Returns the case event publishing configuration.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.get_case_event_configuration_request.GetCaseEventConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.get_case_event_configuration_response.GetCaseEventConfigurationResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.get_case_event_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.get_case_event_configuration.async_get_case_event_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.get_case_event_configuration_request.GetCaseEventConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_case_event_configuration(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        event_bridge: "aws_sdk_connectcases.types.event_bridge_configuration.EventBridgeConfiguration",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.put_case_event_configuration_response.PutCaseEventConfigurationResponse":
        """<p>Adds case event publishing configuration. For a complete list of fields you can add to the event message, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html\">Create case fields</a> in the <i>Amazon Connect Administrator Guide</i> </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            event_bridge: <p>Configuration to enable EventBridge case event delivery and determine what data is delivered.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.put_case_event_configuration_request.PutCaseEventConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.put_case_event_configuration_response.PutCaseEventConfigurationResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.put_case_event_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.put_case_event_configuration.async_put_case_event_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.put_case_event_configuration_request.PutCaseEventConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        input["event_bridge"] = event_bridge

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def search_all_related_items(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
        filters: Optional[
            "aws_sdk_connectcases.types.related_item_filter_list.RelatedItemFilterList"
        ] = None,
        sorts: Optional[
            "aws_sdk_connectcases.types.search_all_related_items_sort_list.SearchAllRelatedItemsSortList"
        ] = None,
    ) -> "aws_sdk_connectcases.types.search_all_related_items_response.SearchAllRelatedItemsResponse":
        """<p>Searches for related items across all cases within a domain. This is a global search operation that returns related items from multiple cases, unlike the case-specific <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchRelatedItems.html\">SearchRelatedItems</a> API.</p> <p> <b>Use cases</b> </p> <p>Following are common uses cases for this API:</p> <ul> <li> <p>Find cases with similar issues across the domain. For example, search for all cases containing comments about \"product defect\" to identify patterns and existing solutions.</p> </li> <li> <p>Locate all cases associated with specific contacts or orders. For example, find all cases linked to a contactArn to understand the complete customer journey. </p> </li> <li> <p>Monitor SLA compliance across cases. For example, search for all cases with \"Active\" SLA status to prioritize remediation efforts.</p> </li> </ul> <p> <b>Important things to know</b> </p> <ul> <li> <p>This API returns case identifiers, not complete case objects. To retrieve full case details, you must make additional calls to the <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCase.html\">GetCase</a> API for each returned case ID. </p> </li> <li> <p>This API searches across related items content, not case fields. Use the <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchCases.html\">SearchCases</a> API to search within case field values.</p> </li> </ul> <p> <b>Endpoints</b>: See <a href=\"https://docs.aws.amazon.com/general/latest/gr/connect_region.html\">Amazon Connect endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            filters: <p>The list of types of related items and their parameters to use for filtering. The filters work as an OR condition: caller gets back related items that match any of the specified filter types.</p>
            sorts: <p>A structured set of sort terms to specify the order in which related items should be returned. Supports sorting by association time or case ID. The sorts work in the order specified: first sort term takes precedence over subsequent terms.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.search_all_related_items_request.SearchAllRelatedItemsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.search_all_related_items_response.SearchAllRelatedItemsResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.search_all_related_items

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.search_all_related_items.async_search_all_related_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.search_all_related_items_request.SearchAllRelatedItemsRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters
        if sorts is not None:
            input["sorts"] = sorts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
