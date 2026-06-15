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
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.client_token
    import aws_sdk_partnercentral_selling.types.engagement_invitation_arn_or_identifier
    import aws_sdk_partnercentral_selling.types.engagement_invitation_identifiers
    import aws_sdk_partnercentral_selling.types.list_engagement_by_accepting_invitation_task_summary
    import aws_sdk_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_request
    import aws_sdk_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_response
    import aws_sdk_partnercentral_selling.types.list_tasks_sort_base
    import aws_sdk_partnercentral_selling.types.opportunity_identifiers
    import aws_sdk_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_request
    import aws_sdk_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_response
    import aws_sdk_partnercentral_selling.types.tag_list
    import aws_sdk_partnercentral_selling.types.task_identifiers
    import aws_sdk_partnercentral_selling.types.task_statuses
    from aws_sdk_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from aws_sdk_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class EngagementByAcceptingInvitationTask:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken",
        identifier: "aws_sdk_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        tags: Optional["aws_sdk_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_response.StartEngagementByAcceptingInvitationTaskResponse":
        """<p>This action starts the engagement by accepting an <code>EngagementInvitation</code>. The task is asynchronous and involves the following steps: accepting the invitation, creating an opportunity in the partner’s account from the AWS opportunity, and copying details for tracking. When completed, an <code>Opportunity Created</code> event is generated, indicating that the opportunity has been successfully created in the partner's account.</p>

        Args:
            catalog: <p>Specifies the catalog related to the task. Use <code>AWS</code> for production engagements and <code>Sandbox</code> for testing scenarios.</p>
            client_token: <p>A unique, case-sensitive identifier provided by the client that helps to ensure the idempotency of the request. This can be a random or meaningful string but must be unique for each request.</p>
            identifier: <p>Specifies the unique identifier of the <code>EngagementInvitation</code> to be accepted. Providing the correct identifier helps ensure that the correct engagement is processed.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_request.StartEngagementByAcceptingInvitationTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_response.StartEngagementByAcceptingInvitationTaskResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_by_accepting_invitation_task

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_by_accepting_invitation_task.start_engagement_by_accepting_invitation_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_request.StartEngagementByAcceptingInvitationTaskRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["client_token"] = client_token
        input_["identifier"] = identifier
        if tags is not None:
            input_["tags"] = tags

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
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "aws_sdk_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
        ] = None,
        task_status: Optional[
            "aws_sdk_partnercentral_selling.types.task_statuses.TaskStatuses"
        ] = None,
        opportunity_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_invitation_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_invitation_identifiers.EngagementInvitationIdentifiers"
        ] = None,
        task_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_response.ListEngagementByAcceptingInvitationTasksResponse":
        """<p> Lists all in-progress, completed, or failed StartEngagementByAcceptingInvitationTask tasks that were initiated by the caller's account. </p>

        Args:
            max_results: <p> Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets. </p>
            next_token: <p> Use this parameter for pagination when the result set spans multiple pages. This value is obtained from the NextToken field in the response of a previous call to this API. </p>
            sort: <p> Specifies the sorting criteria for the returned results. This allows you to order the tasks based on specific attributes. </p>
            catalog: <p> Specifies the catalog related to the request. Valid values are: </p> <ul> <li> <p> AWS: Retrieves the request from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the request from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            task_status: <p> Filters the tasks based on their current status. This allows you to focus on tasks in specific states. </p>
            opportunity_identifier: <p> Filters tasks by the identifiers of the opportunities they created or are associated with. </p>
            engagement_invitation_identifier: <p> Filters tasks by the identifiers of the engagement invitations they are processing. </p>
            task_identifier: <p> Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_request.ListEngagementByAcceptingInvitationTasksRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_response.ListEngagementByAcceptingInvitationTasksResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_by_accepting_invitation_tasks

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_by_accepting_invitation_tasks.list_engagement_by_accepting_invitation_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_request.ListEngagementByAcceptingInvitationTasksRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        input_["catalog"] = catalog
        if task_status is not None:
            input_["task_status"] = task_status
        if opportunity_identifier is not None:
            input_["opportunity_identifier"] = opportunity_identifier
        if engagement_invitation_identifier is not None:
            input_["engagement_invitation_identifier"] = (
                engagement_invitation_identifier
            )
        if task_identifier is not None:
            input_["task_identifier"] = task_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEngagementByAcceptingInvitationTask:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken",
        identifier: "aws_sdk_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        tags: Optional["aws_sdk_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_response.StartEngagementByAcceptingInvitationTaskResponse":
        """<p>This action starts the engagement by accepting an <code>EngagementInvitation</code>. The task is asynchronous and involves the following steps: accepting the invitation, creating an opportunity in the partner’s account from the AWS opportunity, and copying details for tracking. When completed, an <code>Opportunity Created</code> event is generated, indicating that the opportunity has been successfully created in the partner's account.</p>

        Args:
            catalog: <p>Specifies the catalog related to the task. Use <code>AWS</code> for production engagements and <code>Sandbox</code> for testing scenarios.</p>
            client_token: <p>A unique, case-sensitive identifier provided by the client that helps to ensure the idempotency of the request. This can be a random or meaningful string but must be unique for each request.</p>
            identifier: <p>Specifies the unique identifier of the <code>EngagementInvitation</code> to be accepted. Providing the correct identifier helps ensure that the correct engagement is processed.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_request.StartEngagementByAcceptingInvitationTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_response.StartEngagementByAcceptingInvitationTaskResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_by_accepting_invitation_task

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_by_accepting_invitation_task.async_start_engagement_by_accepting_invitation_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.start_engagement_by_accepting_invitation_task_request.StartEngagementByAcceptingInvitationTaskRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["client_token"] = client_token
        input_["identifier"] = identifier
        if tags is not None:
            input_["tags"] = tags

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
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "aws_sdk_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
        ] = None,
        task_status: Optional[
            "aws_sdk_partnercentral_selling.types.task_statuses.TaskStatuses"
        ] = None,
        opportunity_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_invitation_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_invitation_identifiers.EngagementInvitationIdentifiers"
        ] = None,
        task_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_response.ListEngagementByAcceptingInvitationTasksResponse":
        """<p> Lists all in-progress, completed, or failed StartEngagementByAcceptingInvitationTask tasks that were initiated by the caller's account. </p>

        Args:
            max_results: <p> Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets. </p>
            next_token: <p> Use this parameter for pagination when the result set spans multiple pages. This value is obtained from the NextToken field in the response of a previous call to this API. </p>
            sort: <p> Specifies the sorting criteria for the returned results. This allows you to order the tasks based on specific attributes. </p>
            catalog: <p> Specifies the catalog related to the request. Valid values are: </p> <ul> <li> <p> AWS: Retrieves the request from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the request from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            task_status: <p> Filters the tasks based on their current status. This allows you to focus on tasks in specific states. </p>
            opportunity_identifier: <p> Filters tasks by the identifiers of the opportunities they created or are associated with. </p>
            engagement_invitation_identifier: <p> Filters tasks by the identifiers of the engagement invitations they are processing. </p>
            task_identifier: <p> Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_request.ListEngagementByAcceptingInvitationTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_response.ListEngagementByAcceptingInvitationTasksResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_by_accepting_invitation_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_by_accepting_invitation_tasks.async_list_engagement_by_accepting_invitation_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.list_engagement_by_accepting_invitation_tasks_request.ListEngagementByAcceptingInvitationTasksRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        input_["catalog"] = catalog
        if task_status is not None:
            input_["task_status"] = task_status
        if opportunity_identifier is not None:
            input_["opportunity_identifier"] = opportunity_identifier
        if engagement_invitation_identifier is not None:
            input_["engagement_invitation_identifier"] = (
                engagement_invitation_identifier
            )
        if task_identifier is not None:
            input_["task_identifier"] = task_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
