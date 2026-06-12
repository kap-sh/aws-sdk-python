from typing import Optional, TYPE_CHECKING
from aws_sdk_connectcases._services.async_connect_cases import ensure_async_iterator
from aws_sdk_connectcases._services.connect_cases import ensure_sync_iterator
from aws_sdk_connectcases._services._pipeline import (
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
)
import aws_sdk_connectcases._auth._signers
import aws_sdk_connectcases._auth._sigv4

if TYPE_CHECKING:
    from aws_sdk_connectcases._services.connect_cases import (
        ConnectCasesClient,
        ConnectCasesClientConfig,
    )
    from aws_sdk_connectcases._services.async_connect_cases import (
        AsyncConnectCasesClient,
        AsyncConnectCasesClientConfig,
    )
    import aws_sdk_connectcases.types.case_filter
    import aws_sdk_connectcases.types.case_id
    import aws_sdk_connectcases.types.contact_arn
    import aws_sdk_connectcases.types.create_case_request
    import aws_sdk_connectcases.types.create_case_response
    import aws_sdk_connectcases.types.delete_case_request
    import aws_sdk_connectcases.types.delete_case_response
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.field_identifier_list
    import aws_sdk_connectcases.types.field_value_list
    import aws_sdk_connectcases.types.get_case_audit_events_request
    import aws_sdk_connectcases.types.get_case_audit_events_response
    import aws_sdk_connectcases.types.get_case_request
    import aws_sdk_connectcases.types.get_case_response
    import aws_sdk_connectcases.types.list_cases_for_contact_request
    import aws_sdk_connectcases.types.list_cases_for_contact_response
    import aws_sdk_connectcases.types.mutable_tags
    import aws_sdk_connectcases.types.next_token
    import aws_sdk_connectcases.types.search_cases_request
    import aws_sdk_connectcases.types.search_cases_response
    import aws_sdk_connectcases.types.search_cases_response_item
    import aws_sdk_connectcases.types.sort_list
    import aws_sdk_connectcases.types.template_id
    import aws_sdk_connectcases.types.update_case_request
    import aws_sdk_connectcases.types.update_case_response
    import aws_sdk_connectcases.types.user_union


class Case:
    def __init__(self, service: ConnectCasesClient) -> None:
        self._service = service

    def create(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        template_id: "aws_sdk_connectcases.types.template_id.TemplateId",
        fields: "aws_sdk_connectcases.types.field_value_list.FieldValueList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        client_token: Optional[str] = None,
        performed_by: Optional[
            "aws_sdk_connectcases.types.user_union.UserUnion"
        ] = None,
        tags: Optional["aws_sdk_connectcases.types.mutable_tags.MutableTags"] = None,
    ) -> "aws_sdk_connectcases.types.create_case_response.CreateCaseResponse":
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must also have <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html\">connect:DescribeUser</a> permission on the User ARN resource that you provide</p> </note> <p>Creates a case in the specified Cases domain. Case system and custom fields are taken as an array id/value pairs with a declared data types.</p> <p>When creating a case from a template that has tag propagation configurations, the specified tags are automatically applied to the case.</p> <p>The following fields are required when creating a case:</p> <ul> <li> <p> <code>customer_id</code> - You must provide the full customer profile ARN in this format: <code>arn:aws:profile:your_AWS_Region:your_AWS_account ID:domains/your_profiles_domain_name/profiles/profile_ID</code> </p> </li> <li> <p> <code>title</code> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier of a template.</p>
            fields: <p>An array of objects with field ID (matching ListFields/DescribeField) and value union data.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.create_case_request.CreateCaseRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.create_case_response.CreateCaseResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.create_case

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.create_case.create_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.create_case_request.CreateCaseRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        input["template_id"] = template_id
        input["fields"] = fields
        if client_token is not None:
            input["client_token"] = client_token
        if performed_by is not None:
            input["performed_by"] = performed_by
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        case_id: "aws_sdk_connectcases.types.case_id.CaseId",
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        fields: "aws_sdk_connectcases.types.field_identifier_list.FieldIdentifierList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.get_case_response.GetCaseResponse":
        """<p>Returns information about a specific case if it exists. </p>

        Args:
            case_id: <p>A unique identifier of the case.</p>
            domain_id: <p>The unique identifier of the Cases domain. </p>
            fields: <p>A list of unique field identifiers. </p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.get_case_request.GetCaseRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.get_case_response.GetCaseResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.get_case

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.get_case.get_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.get_case_request.GetCaseRequest = {}  # type: ignore[typeddict-item]
        input["case_id"] = case_id
        input["domain_id"] = domain_id
        input["fields"] = fields
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        case_id: "aws_sdk_connectcases.types.case_id.CaseId",
        fields: "aws_sdk_connectcases.types.field_value_list.FieldValueList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        performed_by: Optional[
            "aws_sdk_connectcases.types.user_union.UserUnion"
        ] = None,
    ) -> "aws_sdk_connectcases.types.update_case_response.UpdateCaseResponse":
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must also have <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html\">connect:DescribeUser</a> permission on the User ARN resource that you provide</p> </note> <p>Updates the values of fields on a case. Fields to be updated are received as an array of id/value pairs identical to the <code>CreateCase</code> input .</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>A unique identifier of the case.</p>
            fields: <p>An array of objects with <code>fieldId</code> (matching ListFields/DescribeField) and value union data, structured identical to <code>CreateCase</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.update_case_request.UpdateCaseRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.update_case_response.UpdateCaseResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.update_case

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.update_case.update_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.update_case_request.UpdateCaseRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        input["case_id"] = case_id
        input["fields"] = fields
        if performed_by is not None:
            input["performed_by"] = performed_by

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        case_id: "aws_sdk_connectcases.types.case_id.CaseId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.delete_case_response.DeleteCaseResponse":
        """<p> The DeleteCase API permanently deletes a case and all its associated resources from the cases data store. After a successful deletion, you cannot:</p> <ul> <li> <p>Retrieve related items</p> </li> <li> <p>Access audit history</p> </li> <li> <p>Perform any operations that require the CaseID</p> </li> </ul> <important> <p>This action is irreversible. After you delete a case, you cannot recover its data.</p> </important>

        Args:
            domain_id: <p>A unique identifier of the Cases domain.</p>
            case_id: <p>A unique identifier of the case.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.delete_case_request.DeleteCaseRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.delete_case_response.DeleteCaseResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.delete_case

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.delete_case.delete_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.delete_case_request.DeleteCaseRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        input["case_id"] = case_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_case_audit_events(
        self,
        case_id: "aws_sdk_connectcases.types.case_id.CaseId",
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse":
        """<p>Returns the audit history about a specific case if it exists.</p>

        Args:
            case_id: <p>A unique identifier of the case.</p>
            domain_id: <p>The unique identifier of the Cases domain.</p>
            max_results: <p>The maximum number of audit events to return. When no value is provided, 25 is the default.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.get_case_audit_events_request.GetCaseAuditEventsRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.get_case_audit_events

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.get_case_audit_events.get_case_audit_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.get_case_audit_events_request.GetCaseAuditEventsRequest = {}  # type: ignore[typeddict-item]
        input["case_id"] = case_id
        input["domain_id"] = domain_id
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

    def list_cases_for_contact(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        contact_arn: "aws_sdk_connectcases.types.contact_arn.ContactArn",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.list_cases_for_contact_response.ListCasesForContactResponse":
        """<p>Lists cases for a given contact.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            contact_arn: <p>A unique identifier of a contact in Amazon Connect.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.list_cases_for_contact_request.ListCasesForContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.list_cases_for_contact_response.ListCasesForContactResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.list_cases_for_contact

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.list_cases_for_contact.list_cases_for_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.list_cases_for_contact_request.ListCasesForContactRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        input["contact_arn"] = contact_arn
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

    def search_cases(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
        search_term: Optional[str] = None,
        filter: Optional["aws_sdk_connectcases.types.case_filter.CaseFilter"] = None,
        sorts: Optional["aws_sdk_connectcases.types.sort_list.SortList"] = None,
        fields: Optional[
            "aws_sdk_connectcases.types.field_identifier_list.FieldIdentifierList"
        ] = None,
    ) -> "aws_sdk_connectcases.types.search_cases_response.SearchCasesResponse":
        """<p>Searches for cases within their associated Cases domain. Search results are returned as a paginated list of abridged case documents.</p> <note> <p>For <code>customer_id</code> you must provide the full customer profile ARN in this format: <code> arn:aws:profile:your AWS Region:your AWS account ID:domains/profiles domain name/profiles/profile ID</code>. </p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of cases to return. When no value is provided, 25 is the default.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            search_term: <p>A word or phrase used to perform a quick search.</p>
            filter: <p>A list of filter objects.</p>
            sorts: <p>A list of sorts where each sort specifies a field and their sort order to be applied to the results. </p>
            fields: <p>The list of field identifiers to be returned as part of the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.search_cases_request.SearchCasesRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.search_cases_response.SearchCasesResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.search_cases

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.search_cases.search_cases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.search_cases_request.SearchCasesRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if search_term is not None:
            input["search_term"] = search_term
        if filter is not None:
            input["filter"] = filter
        if sorts is not None:
            input["sorts"] = sorts
        if fields is not None:
            input["fields"] = fields

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCase:
    def __init__(self, service: AsyncConnectCasesClient) -> None:
        self._service = service

    async def create(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        template_id: "aws_sdk_connectcases.types.template_id.TemplateId",
        fields: "aws_sdk_connectcases.types.field_value_list.FieldValueList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        client_token: Optional[str] = None,
        performed_by: Optional[
            "aws_sdk_connectcases.types.user_union.UserUnion"
        ] = None,
        tags: Optional["aws_sdk_connectcases.types.mutable_tags.MutableTags"] = None,
    ) -> "aws_sdk_connectcases.types.create_case_response.CreateCaseResponse":
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must also have <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html\">connect:DescribeUser</a> permission on the User ARN resource that you provide</p> </note> <p>Creates a case in the specified Cases domain. Case system and custom fields are taken as an array id/value pairs with a declared data types.</p> <p>When creating a case from a template that has tag propagation configurations, the specified tags are automatically applied to the case.</p> <p>The following fields are required when creating a case:</p> <ul> <li> <p> <code>customer_id</code> - You must provide the full customer profile ARN in this format: <code>arn:aws:profile:your_AWS_Region:your_AWS_account ID:domains/your_profiles_domain_name/profiles/profile_ID</code> </p> </li> <li> <p> <code>title</code> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier of a template.</p>
            fields: <p>An array of objects with field ID (matching ListFields/DescribeField) and value union data.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.create_case_request.CreateCaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.create_case_response.CreateCaseResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.create_case

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.create_case.async_create_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.create_case_request.CreateCaseRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        input["template_id"] = template_id
        input["fields"] = fields
        if client_token is not None:
            input["client_token"] = client_token
        if performed_by is not None:
            input["performed_by"] = performed_by
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        case_id: "aws_sdk_connectcases.types.case_id.CaseId",
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        fields: "aws_sdk_connectcases.types.field_identifier_list.FieldIdentifierList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.get_case_response.GetCaseResponse":
        """<p>Returns information about a specific case if it exists. </p>

        Args:
            case_id: <p>A unique identifier of the case.</p>
            domain_id: <p>The unique identifier of the Cases domain. </p>
            fields: <p>A list of unique field identifiers. </p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.get_case_request.GetCaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.get_case_response.GetCaseResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.get_case

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.get_case.async_get_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.get_case_request.GetCaseRequest = {}  # type: ignore[typeddict-item]
        input["case_id"] = case_id
        input["domain_id"] = domain_id
        input["fields"] = fields
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        case_id: "aws_sdk_connectcases.types.case_id.CaseId",
        fields: "aws_sdk_connectcases.types.field_value_list.FieldValueList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        performed_by: Optional[
            "aws_sdk_connectcases.types.user_union.UserUnion"
        ] = None,
    ) -> "aws_sdk_connectcases.types.update_case_response.UpdateCaseResponse":
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must also have <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html\">connect:DescribeUser</a> permission on the User ARN resource that you provide</p> </note> <p>Updates the values of fields on a case. Fields to be updated are received as an array of id/value pairs identical to the <code>CreateCase</code> input .</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>A unique identifier of the case.</p>
            fields: <p>An array of objects with <code>fieldId</code> (matching ListFields/DescribeField) and value union data, structured identical to <code>CreateCase</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.update_case_request.UpdateCaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.update_case_response.UpdateCaseResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.update_case

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.update_case.async_update_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.update_case_request.UpdateCaseRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        input["case_id"] = case_id
        input["fields"] = fields
        if performed_by is not None:
            input["performed_by"] = performed_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        case_id: "aws_sdk_connectcases.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.delete_case_response.DeleteCaseResponse":
        """<p> The DeleteCase API permanently deletes a case and all its associated resources from the cases data store. After a successful deletion, you cannot:</p> <ul> <li> <p>Retrieve related items</p> </li> <li> <p>Access audit history</p> </li> <li> <p>Perform any operations that require the CaseID</p> </li> </ul> <important> <p>This action is irreversible. After you delete a case, you cannot recover its data.</p> </important>

        Args:
            domain_id: <p>A unique identifier of the Cases domain.</p>
            case_id: <p>A unique identifier of the case.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.delete_case_request.DeleteCaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.delete_case_response.DeleteCaseResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.delete_case

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.delete_case.async_delete_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.delete_case_request.DeleteCaseRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        input["case_id"] = case_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_case_audit_events(
        self,
        case_id: "aws_sdk_connectcases.types.case_id.CaseId",
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse":
        """<p>Returns the audit history about a specific case if it exists.</p>

        Args:
            case_id: <p>A unique identifier of the case.</p>
            domain_id: <p>The unique identifier of the Cases domain.</p>
            max_results: <p>The maximum number of audit events to return. When no value is provided, 25 is the default.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.get_case_audit_events_request.GetCaseAuditEventsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.get_case_audit_events

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.get_case_audit_events.async_get_case_audit_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.get_case_audit_events_request.GetCaseAuditEventsRequest = {}  # type: ignore[typeddict-item]
        input["case_id"] = case_id
        input["domain_id"] = domain_id
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

    async def list_cases_for_contact(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        contact_arn: "aws_sdk_connectcases.types.contact_arn.ContactArn",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.list_cases_for_contact_response.ListCasesForContactResponse":
        """<p>Lists cases for a given contact.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            contact_arn: <p>A unique identifier of a contact in Amazon Connect.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.list_cases_for_contact_request.ListCasesForContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.list_cases_for_contact_response.ListCasesForContactResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.list_cases_for_contact

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.list_cases_for_contact.async_list_cases_for_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.list_cases_for_contact_request.ListCasesForContactRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        input["contact_arn"] = contact_arn
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

    async def search_cases(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
        search_term: Optional[str] = None,
        filter: Optional["aws_sdk_connectcases.types.case_filter.CaseFilter"] = None,
        sorts: Optional["aws_sdk_connectcases.types.sort_list.SortList"] = None,
        fields: Optional[
            "aws_sdk_connectcases.types.field_identifier_list.FieldIdentifierList"
        ] = None,
    ) -> "aws_sdk_connectcases.types.search_cases_response.SearchCasesResponse":
        """<p>Searches for cases within their associated Cases domain. Search results are returned as a paginated list of abridged case documents.</p> <note> <p>For <code>customer_id</code> you must provide the full customer profile ARN in this format: <code> arn:aws:profile:your AWS Region:your AWS account ID:domains/profiles domain name/profiles/profile ID</code>. </p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of cases to return. When no value is provided, 25 is the default.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            search_term: <p>A word or phrase used to perform a quick search.</p>
            filter: <p>A list of filter objects.</p>
            sorts: <p>A list of sorts where each sort specifies a field and their sort order to be applied to the results. </p>
            fields: <p>The list of field identifiers to be returned as part of the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.search_cases_request.SearchCasesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.search_cases_response.SearchCasesResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.search_cases

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.search_cases.async_search_cases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_connectcases.types.search_cases_request.SearchCasesRequest = {}  # type: ignore[typeddict-item]
        input["domain_id"] = domain_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if search_term is not None:
            input["search_term"] = search_term
        if filter is not None:
            input["filter"] = filter
        if sorts is not None:
            input["sorts"] = sorts
        if fields is not None:
            input["fields"] = fields

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
