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
    import aws_sdk_partnercentral_selling.types.aws_submission
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.client_token
    import aws_sdk_partnercentral_selling.types.engagement_identifiers
    import aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_task_summary
    import aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request
    import aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response
    import aws_sdk_partnercentral_selling.types.list_tasks_sort_base
    import aws_sdk_partnercentral_selling.types.opportunity_identifier
    import aws_sdk_partnercentral_selling.types.opportunity_identifiers
    import aws_sdk_partnercentral_selling.types.start_engagement_from_opportunity_task_request
    import aws_sdk_partnercentral_selling.types.start_engagement_from_opportunity_task_response
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


class EngagementFromOpportunityTask:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken",
        identifier: "aws_sdk_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        aws_submission: "aws_sdk_partnercentral_selling.types.aws_submission.AwsSubmission",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        tags: Optional["aws_sdk_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_selling.types.start_engagement_from_opportunity_task_response.StartEngagementFromOpportunityTaskResponse":
        """<p>Similar to <code>StartEngagementByAcceptingInvitationTask</code>, this action is asynchronous and performs multiple steps before completion. This action orchestrates a comprehensive workflow that combines multiple API operations into a single task to create and initiate an engagement from an existing opportunity. It automatically executes a sequence of operations including <code>GetOpportunity</code>, <code>CreateEngagement</code> (if it doesn't exist), <code>CreateResourceSnapshot</code>, <code>CreateResourceSnapshotJob</code>, <code>CreateEngagementInvitation</code> (if not already invited/accepted), and <code>SubmitOpportunity</code>. </p>

        Args:
            catalog: <p>Specifies the catalog in which the engagement is tracked. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
            client_token: <p>A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.</p>
            identifier: <p>The unique identifier of the opportunity from which the engagement task is to be initiated. This helps ensure that the task is applied to the correct opportunity.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.start_engagement_from_opportunity_task_request.StartEngagementFromOpportunityTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.start_engagement_from_opportunity_task_response.StartEngagementFromOpportunityTaskResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_from_opportunity_task

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_from_opportunity_task.start_engagement_from_opportunity_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.start_engagement_from_opportunity_task_request.StartEngagementFromOpportunityTaskRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["client_token"] = client_token
        input["identifier"] = identifier
        input["aws_submission"] = aws_submission
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
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
        task_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
        opportunity_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response.ListEngagementFromOpportunityTasksResponse":
        """<p> Lists all in-progress, completed, or failed <code>EngagementFromOpportunity</code> tasks that were initiated by the caller's account. </p>

        Args:
            max_results: <p> Specifies the maximum number of results to return in a single page of the response.Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets. </p>
            next_token: <p> The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages. </p>
            sort: <p> Specifies the sorting criteria for the returned results. This allows you to order the tasks based on specific attributes. </p>
            catalog: <p> Specifies the catalog related to the request. Valid values are: </p> <ul> <li> <p> AWS: Retrieves the request from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the request from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            task_status: <p> Filters the tasks based on their current status. This allows you to focus on tasks in specific states. </p>
            task_identifier: <p> Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. </p>
            opportunity_identifier: <p> The identifier of the original opportunity associated with this task. </p>
            engagement_identifier: <p> Filters tasks by the identifiers of the engagements they created or are associated with. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request.ListEngagementFromOpportunityTasksRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response.ListEngagementFromOpportunityTasksResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_from_opportunity_tasks

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_from_opportunity_tasks.list_engagement_from_opportunity_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request.ListEngagementFromOpportunityTasksRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort is not None:
            input["sort"] = sort
        input["catalog"] = catalog
        if task_status is not None:
            input["task_status"] = task_status
        if task_identifier is not None:
            input["task_identifier"] = task_identifier
        if opportunity_identifier is not None:
            input["opportunity_identifier"] = opportunity_identifier
        if engagement_identifier is not None:
            input["engagement_identifier"] = engagement_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEngagementFromOpportunityTask:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken",
        identifier: "aws_sdk_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier",
        aws_submission: "aws_sdk_partnercentral_selling.types.aws_submission.AwsSubmission",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        tags: Optional["aws_sdk_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_selling.types.start_engagement_from_opportunity_task_response.StartEngagementFromOpportunityTaskResponse":
        """<p>Similar to <code>StartEngagementByAcceptingInvitationTask</code>, this action is asynchronous and performs multiple steps before completion. This action orchestrates a comprehensive workflow that combines multiple API operations into a single task to create and initiate an engagement from an existing opportunity. It automatically executes a sequence of operations including <code>GetOpportunity</code>, <code>CreateEngagement</code> (if it doesn't exist), <code>CreateResourceSnapshot</code>, <code>CreateResourceSnapshotJob</code>, <code>CreateEngagementInvitation</code> (if not already invited/accepted), and <code>SubmitOpportunity</code>. </p>

        Args:
            catalog: <p>Specifies the catalog in which the engagement is tracked. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
            client_token: <p>A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.</p>
            identifier: <p>The unique identifier of the opportunity from which the engagement task is to be initiated. This helps ensure that the task is applied to the correct opportunity.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.start_engagement_from_opportunity_task_request.StartEngagementFromOpportunityTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.start_engagement_from_opportunity_task_response.StartEngagementFromOpportunityTaskResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_from_opportunity_task

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_engagement_from_opportunity_task.async_start_engagement_from_opportunity_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.start_engagement_from_opportunity_task_request.StartEngagementFromOpportunityTaskRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["client_token"] = client_token
        input["identifier"] = identifier
        input["aws_submission"] = aws_submission
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
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
        task_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
        ] = None,
        opportunity_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
        ] = None,
        engagement_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response.ListEngagementFromOpportunityTasksResponse":
        """<p> Lists all in-progress, completed, or failed <code>EngagementFromOpportunity</code> tasks that were initiated by the caller's account. </p>

        Args:
            max_results: <p> Specifies the maximum number of results to return in a single page of the response.Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets. </p>
            next_token: <p> The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages. </p>
            sort: <p> Specifies the sorting criteria for the returned results. This allows you to order the tasks based on specific attributes. </p>
            catalog: <p> Specifies the catalog related to the request. Valid values are: </p> <ul> <li> <p> AWS: Retrieves the request from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the request from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            task_status: <p> Filters the tasks based on their current status. This allows you to focus on tasks in specific states. </p>
            task_identifier: <p> Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. </p>
            opportunity_identifier: <p> The identifier of the original opportunity associated with this task. </p>
            engagement_identifier: <p> Filters tasks by the identifiers of the engagements they created or are associated with. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request.ListEngagementFromOpportunityTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_tasks_response.ListEngagementFromOpportunityTasksResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_from_opportunity_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_from_opportunity_tasks.async_list_engagement_from_opportunity_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.list_engagement_from_opportunity_tasks_request.ListEngagementFromOpportunityTasksRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort is not None:
            input["sort"] = sort
        input["catalog"] = catalog
        if task_status is not None:
            input["task_status"] = task_status
        if task_identifier is not None:
            input["task_identifier"] = task_identifier
        if opportunity_identifier is not None:
            input["opportunity_identifier"] = opportunity_identifier
        if engagement_identifier is not None:
            input["engagement_identifier"] = engagement_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
