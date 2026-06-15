from __future__ import annotations

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
    import aws_sdk_partnercentral_selling.types.aws_account_list
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.client_token
    import aws_sdk_partnercentral_selling.types.create_engagement_request
    import aws_sdk_partnercentral_selling.types.create_engagement_response
    import aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier
    import aws_sdk_partnercentral_selling.types.engagement_context_type_list
    import aws_sdk_partnercentral_selling.types.engagement_contexts
    import aws_sdk_partnercentral_selling.types.engagement_description
    import aws_sdk_partnercentral_selling.types.engagement_identifiers
    import aws_sdk_partnercentral_selling.types.engagement_member
    import aws_sdk_partnercentral_selling.types.engagement_page_size
    import aws_sdk_partnercentral_selling.types.engagement_sort
    import aws_sdk_partnercentral_selling.types.engagement_summary
    import aws_sdk_partnercentral_selling.types.engagement_title
    import aws_sdk_partnercentral_selling.types.get_engagement_request
    import aws_sdk_partnercentral_selling.types.get_engagement_response
    import aws_sdk_partnercentral_selling.types.list_engagement_members_request
    import aws_sdk_partnercentral_selling.types.list_engagement_members_response
    import aws_sdk_partnercentral_selling.types.list_engagements_request
    import aws_sdk_partnercentral_selling.types.list_engagements_response
    import aws_sdk_partnercentral_selling.types.member_page_size
    from aws_sdk_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from aws_sdk_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class Engagement:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken",
        title: "aws_sdk_partnercentral_selling.types.engagement_title.EngagementTitle",
        description: "aws_sdk_partnercentral_selling.types.engagement_description.EngagementDescription",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        contexts: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_contexts.EngagementContexts"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.create_engagement_response.CreateEngagementResponse":
        """<p>The <code>CreateEngagement</code> action allows you to create an <code>Engagement</code>, which serves as a collaborative space between different parties such as AWS Partners and AWS Sellers. This action automatically adds the caller's AWS account as an active member of the newly created <code>Engagement</code>.</p>

        Args:
            catalog: <p>The <code>CreateEngagementRequest$Catalog</code> parameter specifies the catalog related to the engagement. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement is managed.</p>
            client_token: <p>The <code>CreateEngagementRequest$ClientToken</code> parameter specifies a unique, case-sensitive identifier to ensure that the request is handled exactly once. The value must not exceed sixty-four alphanumeric characters.</p>
            title: <p>Specifies the title of the <code>Engagement</code>.</p>
            description: <p>Provides a description of the <code>Engagement</code>.</p>
            contexts: <p>The <code>Contexts</code> field is a required array of objects, with a maximum of 5 contexts allowed, specifying detailed information about customer projects associated with the Engagement. Each context object contains a <code>Type</code> field indicating the context type, which must be <code>CustomerProject</code> in this version, and a <code>Payload</code> field containing the <code>CustomerProject</code> details. The <code>CustomerProject</code> object is composed of two main components: <code>Customer</code> and <code>Project</code>. The <code>Customer</code> object includes information such as <code>CompanyName</code>, <code>WebsiteUrl</code>, <code>Industry</code>, and <code>CountryCode</code>, providing essential details about the customer. The <code>Project</code> object contains <code>Title</code>, <code>BusinessProblem</code>, and <code>TargetCompletionDate</code>, offering insights into the specific project associated with the customer. This structure allows comprehensive context to be included within the Engagement, facilitating effective collaboration between parties by providing relevant customer and project information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.create_engagement_request.CreateEngagementRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.create_engagement_response.CreateEngagementResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_engagement

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_engagement.create_engagement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.create_engagement_request.CreateEngagementRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["client_token"] = client_token
        input_["title"] = title
        input_["description"] = description
        if contexts is not None:
            input_["contexts"] = contexts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "aws_sdk_partnercentral_selling.types.get_engagement_response.GetEngagementResponse":
        """<p>Use this action to retrieve the engagement record for a given <code>EngagementIdentifier</code>.</p>

        Args:
            catalog: <p>Specifies the catalog related to the engagement request. Valid values are <code>AWS</code> and <code>Sandbox</code>.</p>
            identifier: <p>Specifies the identifier of the Engagement record to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.get_engagement_request.GetEngagementRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.get_engagement_response.GetEngagementResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_engagement

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_engagement.get_engagement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.get_engagement_request.GetEngagementRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        created_by: Optional[
            "aws_sdk_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        exclude_created_by: Optional[
            "aws_sdk_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        context_types: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        exclude_context_types: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        sort: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_sort.EngagementSort"
        ] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_page_size.EngagementPageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_engagements_response.ListEngagementsResponse":
        r"""<p>This action allows users to retrieve a list of Engagement records from Partner Central. This action can be used to manage and track various engagements across different stages of the partner selling process. </p>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            created_by: <p> A list of AWS account IDs. When specified, the response includes engagements created by these accounts. This filter is useful for finding engagements created by specific team members. </p>
            exclude_created_by: <p>An array of strings representing AWS Account IDs. Use this to exclude engagements created by specific users. </p>
            context_types: <p>Filters engagements to include only those containing the specified context types, such as \"CustomerProject\" or \"Lead\". Use this to find engagements that have specific types of contextual information associated with them.</p>
            exclude_context_types: <p>Filters engagements to exclude those containing the specified context types. Use this to find engagements that do not have certain types of contextual information, helping to narrow results based on context exclusion criteria.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results. This value is returned from a previous call.</p>
            engagement_identifier: <p>An array of strings representing engagement identifiers to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.list_engagements_request.ListEngagementsRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.list_engagements_response.ListEngagementsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagements

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagements.list_engagements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.list_engagements_request.ListEngagementsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if created_by is not None:
            input_["created_by"] = created_by
        if exclude_created_by is not None:
            input_["exclude_created_by"] = exclude_created_by
        if context_types is not None:
            input_["context_types"] = context_types
        if exclude_context_types is not None:
            input_["exclude_context_types"] = exclude_context_types
        if sort is not None:
            input_["sort"] = sort
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_engagement_members(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.member_page_size.MemberPageSize"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_engagement_members_response.ListEngagementMembersResponse":
        """<p>Retrieves the details of member partners in an Engagement. This operation can only be invoked by members of the Engagement. The <code>ListEngagementMembers</code> operation allows you to fetch information about the members of a specific Engagement. This action is restricted to members of the Engagement being queried. </p>

        Args:
            catalog: <p>The catalog related to the request.</p>
            identifier: <p>Identifier of the Engagement record to retrieve members from.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.list_engagement_members_request.ListEngagementMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.list_engagement_members_response.ListEngagementMembersResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_members

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_members.list_engagement_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.list_engagement_members_request.ListEngagementMembersRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
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


class AsyncEngagement:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken",
        title: "aws_sdk_partnercentral_selling.types.engagement_title.EngagementTitle",
        description: "aws_sdk_partnercentral_selling.types.engagement_description.EngagementDescription",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        contexts: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_contexts.EngagementContexts"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.create_engagement_response.CreateEngagementResponse":
        """<p>The <code>CreateEngagement</code> action allows you to create an <code>Engagement</code>, which serves as a collaborative space between different parties such as AWS Partners and AWS Sellers. This action automatically adds the caller's AWS account as an active member of the newly created <code>Engagement</code>.</p>

        Args:
            catalog: <p>The <code>CreateEngagementRequest$Catalog</code> parameter specifies the catalog related to the engagement. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement is managed.</p>
            client_token: <p>The <code>CreateEngagementRequest$ClientToken</code> parameter specifies a unique, case-sensitive identifier to ensure that the request is handled exactly once. The value must not exceed sixty-four alphanumeric characters.</p>
            title: <p>Specifies the title of the <code>Engagement</code>.</p>
            description: <p>Provides a description of the <code>Engagement</code>.</p>
            contexts: <p>The <code>Contexts</code> field is a required array of objects, with a maximum of 5 contexts allowed, specifying detailed information about customer projects associated with the Engagement. Each context object contains a <code>Type</code> field indicating the context type, which must be <code>CustomerProject</code> in this version, and a <code>Payload</code> field containing the <code>CustomerProject</code> details. The <code>CustomerProject</code> object is composed of two main components: <code>Customer</code> and <code>Project</code>. The <code>Customer</code> object includes information such as <code>CompanyName</code>, <code>WebsiteUrl</code>, <code>Industry</code>, and <code>CountryCode</code>, providing essential details about the customer. The <code>Project</code> object contains <code>Title</code>, <code>BusinessProblem</code>, and <code>TargetCompletionDate</code>, offering insights into the specific project associated with the customer. This structure allows comprehensive context to be included within the Engagement, facilitating effective collaboration between parties by providing relevant customer and project information.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.create_engagement_request.CreateEngagementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.create_engagement_response.CreateEngagementResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_engagement

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_engagement.async_create_engagement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.create_engagement_request.CreateEngagementRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["client_token"] = client_token
        input_["title"] = title
        input_["description"] = description
        if contexts is not None:
            input_["contexts"] = contexts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "aws_sdk_partnercentral_selling.types.get_engagement_response.GetEngagementResponse":
        """<p>Use this action to retrieve the engagement record for a given <code>EngagementIdentifier</code>.</p>

        Args:
            catalog: <p>Specifies the catalog related to the engagement request. Valid values are <code>AWS</code> and <code>Sandbox</code>.</p>
            identifier: <p>Specifies the identifier of the Engagement record to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.get_engagement_request.GetEngagementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.get_engagement_response.GetEngagementResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_engagement

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_engagement.async_get_engagement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.get_engagement_request.GetEngagementRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        created_by: Optional[
            "aws_sdk_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        exclude_created_by: Optional[
            "aws_sdk_partnercentral_selling.types.aws_account_list.AwsAccountList"
        ] = None,
        context_types: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        exclude_context_types: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
        ] = None,
        sort: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_sort.EngagementSort"
        ] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_page_size.EngagementPageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_engagements_response.ListEngagementsResponse":
        r"""<p>This action allows users to retrieve a list of Engagement records from Partner Central. This action can be used to manage and track various engagements across different stages of the partner selling process. </p>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            created_by: <p> A list of AWS account IDs. When specified, the response includes engagements created by these accounts. This filter is useful for finding engagements created by specific team members. </p>
            exclude_created_by: <p>An array of strings representing AWS Account IDs. Use this to exclude engagements created by specific users. </p>
            context_types: <p>Filters engagements to include only those containing the specified context types, such as \"CustomerProject\" or \"Lead\". Use this to find engagements that have specific types of contextual information associated with them.</p>
            exclude_context_types: <p>Filters engagements to exclude those containing the specified context types. Use this to find engagements that do not have certain types of contextual information, helping to narrow results based on context exclusion criteria.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results. This value is returned from a previous call.</p>
            engagement_identifier: <p>An array of strings representing engagement identifiers to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.list_engagements_request.ListEngagementsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.list_engagements_response.ListEngagementsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagements

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagements.async_list_engagements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.list_engagements_request.ListEngagementsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if created_by is not None:
            input_["created_by"] = created_by
        if exclude_created_by is not None:
            input_["exclude_created_by"] = exclude_created_by
        if context_types is not None:
            input_["context_types"] = context_types
        if exclude_context_types is not None:
            input_["exclude_context_types"] = exclude_context_types
        if sort is not None:
            input_["sort"] = sort
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_engagement_members(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.member_page_size.MemberPageSize"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_engagement_members_response.ListEngagementMembersResponse":
        """<p>Retrieves the details of member partners in an Engagement. This operation can only be invoked by members of the Engagement. The <code>ListEngagementMembers</code> operation allows you to fetch information about the members of a specific Engagement. This action is restricted to members of the Engagement being queried. </p>

        Args:
            catalog: <p>The catalog related to the request.</p>
            identifier: <p>Identifier of the Engagement record to retrieve members from.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.list_engagement_members_request.ListEngagementMembersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.list_engagement_members_response.ListEngagementMembersResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_members

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_members.async_list_engagement_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.list_engagement_members_request.ListEngagementMembersRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
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
