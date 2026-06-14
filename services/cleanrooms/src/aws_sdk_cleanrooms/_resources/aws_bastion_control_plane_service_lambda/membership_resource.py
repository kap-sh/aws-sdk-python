from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_cleanrooms._auth._signers
import aws_sdk_cleanrooms._auth._sigv4
from aws_sdk_cleanrooms._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.budgeted_resource_arn
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.compute_configuration
    import aws_sdk_cleanrooms.types.create_membership_input
    import aws_sdk_cleanrooms.types.create_membership_output
    import aws_sdk_cleanrooms.types.delete_membership_input
    import aws_sdk_cleanrooms.types.delete_membership_output
    import aws_sdk_cleanrooms.types.get_membership_input
    import aws_sdk_cleanrooms.types.get_membership_output
    import aws_sdk_cleanrooms.types.get_protected_job_input
    import aws_sdk_cleanrooms.types.get_protected_job_output
    import aws_sdk_cleanrooms.types.get_protected_query_input
    import aws_sdk_cleanrooms.types.get_protected_query_output
    import aws_sdk_cleanrooms.types.list_memberships_input
    import aws_sdk_cleanrooms.types.list_memberships_output
    import aws_sdk_cleanrooms.types.list_privacy_budgets_input
    import aws_sdk_cleanrooms.types.list_privacy_budgets_output
    import aws_sdk_cleanrooms.types.list_protected_jobs_input
    import aws_sdk_cleanrooms.types.list_protected_jobs_output
    import aws_sdk_cleanrooms.types.list_protected_queries_input
    import aws_sdk_cleanrooms.types.list_protected_queries_output
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.membership_job_log_status
    import aws_sdk_cleanrooms.types.membership_payment_configuration
    import aws_sdk_cleanrooms.types.membership_protected_job_result_configuration
    import aws_sdk_cleanrooms.types.membership_protected_query_result_configuration
    import aws_sdk_cleanrooms.types.membership_query_log_status
    import aws_sdk_cleanrooms.types.membership_status
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.preview_privacy_impact_input
    import aws_sdk_cleanrooms.types.preview_privacy_impact_output
    import aws_sdk_cleanrooms.types.preview_privacy_impact_parameters_input
    import aws_sdk_cleanrooms.types.privacy_budget_summary
    import aws_sdk_cleanrooms.types.privacy_budget_type
    import aws_sdk_cleanrooms.types.protected_job_compute_configuration
    import aws_sdk_cleanrooms.types.protected_job_identifier
    import aws_sdk_cleanrooms.types.protected_job_parameters
    import aws_sdk_cleanrooms.types.protected_job_result_configuration_input
    import aws_sdk_cleanrooms.types.protected_job_status
    import aws_sdk_cleanrooms.types.protected_job_summary
    import aws_sdk_cleanrooms.types.protected_job_type
    import aws_sdk_cleanrooms.types.protected_query_identifier
    import aws_sdk_cleanrooms.types.protected_query_result_configuration
    import aws_sdk_cleanrooms.types.protected_query_sql_parameters
    import aws_sdk_cleanrooms.types.protected_query_status
    import aws_sdk_cleanrooms.types.protected_query_summary
    import aws_sdk_cleanrooms.types.protected_query_type
    import aws_sdk_cleanrooms.types.start_protected_job_input
    import aws_sdk_cleanrooms.types.start_protected_job_output
    import aws_sdk_cleanrooms.types.start_protected_query_input
    import aws_sdk_cleanrooms.types.start_protected_query_output
    import aws_sdk_cleanrooms.types.tag_map
    import aws_sdk_cleanrooms.types.target_protected_job_status
    import aws_sdk_cleanrooms.types.target_protected_query_status
    import aws_sdk_cleanrooms.types.update_membership_input
    import aws_sdk_cleanrooms.types.update_membership_output
    import aws_sdk_cleanrooms.types.update_membership_payment_configuration
    import aws_sdk_cleanrooms.types.update_protected_job_input
    import aws_sdk_cleanrooms.types.update_protected_job_output
    import aws_sdk_cleanrooms.types.update_protected_query_input
    import aws_sdk_cleanrooms.types.update_protected_query_output
    from aws_sdk_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from aws_sdk_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class MembershipResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        query_log_status: "aws_sdk_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        job_log_status: Optional[
            "aws_sdk_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
        ] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
        default_result_configuration: Optional[
            "aws_sdk_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
        ] = None,
        default_job_result_configuration: Optional[
            "aws_sdk_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
        ] = None,
        payment_configuration: Optional[
            "aws_sdk_cleanrooms.types.membership_payment_configuration.MembershipPaymentConfiguration"
        ] = None,
        is_metrics_enabled: Optional[bool] = None,
    ) -> "aws_sdk_cleanrooms.types.create_membership_output.CreateMembershipOutput":
        """<p>Creates a membership for a specific collaboration identifier and joins the collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique ID for the associated collaboration.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            default_result_configuration: <p>The default protected query result configuration as specified by the member who can receive results.</p>
            default_job_result_configuration: <p>The default job result configuration that determines how job results are protected and managed within this membership. This configuration applies to all jobs.</p>
            payment_configuration: <p>The payment responsibilities accepted by the collaboration member.</p> <p>Not required if the collaboration member has the member ability to run queries. </p> <p>Required if the collaboration member doesn't have the member ability to run queries but is configured as a payer by the collaboration creator. </p>
            is_metrics_enabled: <p>An indicator as to whether Amazon CloudWatch metrics have been enabled or disabled for the membership.</p> <p>Amazon CloudWatch metrics are only available when the collaboration has metrics enabled. This option can be set by collaboration members who have the ability to run queries (analysis runners) or by members who are configured as payers.</p> <p>When <code>true</code>, metrics about query execution are collected in Amazon CloudWatch. The default value is <code>false</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.create_membership_input.CreateMembershipInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.create_membership_output.CreateMembershipOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_membership

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_membership.create_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_membership_input.CreateMembershipInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["query_log_status"] = query_log_status
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if tags is not None:
            input_["tags"] = tags
        if default_result_configuration is not None:
            input_["default_result_configuration"] = default_result_configuration
        if default_job_result_configuration is not None:
            input_["default_job_result_configuration"] = (
                default_job_result_configuration
            )
        if payment_configuration is not None:
            input_["payment_configuration"] = payment_configuration
        if is_metrics_enabled is not None:
            input_["is_metrics_enabled"] = is_metrics_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_membership_output.GetMembershipOutput":
        """<p>Retrieves a specified membership for an identifier.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_membership_input.GetMembershipInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_membership_output.GetMembershipOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_membership

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_membership.get_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_membership_input.GetMembershipInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        query_log_status: Optional[
            "aws_sdk_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus"
        ] = None,
        job_log_status: Optional[
            "aws_sdk_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
        ] = None,
        default_result_configuration: Optional[
            "aws_sdk_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
        ] = None,
        default_job_result_configuration: Optional[
            "aws_sdk_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
        ] = None,
        membership_payment_configuration: Optional[
            "aws_sdk_cleanrooms.types.update_membership_payment_configuration.UpdateMembershipPaymentConfiguration"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.update_membership_output.UpdateMembershipOutput":
        """<p>Updates a membership.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            default_result_configuration: <p>The default protected query result configuration as specified by the member who can receive results.</p>
            default_job_result_configuration: <p> The default job result configuration.</p>
            membership_payment_configuration: <p>The payment configuration to update for the membership.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.update_membership_input.UpdateMembershipInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.update_membership_output.UpdateMembershipOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_membership

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_membership.update_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_membership_input.UpdateMembershipInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        if query_log_status is not None:
            input_["query_log_status"] = query_log_status
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if default_result_configuration is not None:
            input_["default_result_configuration"] = default_result_configuration
        if default_job_result_configuration is not None:
            input_["default_job_result_configuration"] = (
                default_job_result_configuration
            )
        if membership_payment_configuration is not None:
            input_["membership_payment_configuration"] = (
                membership_payment_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_membership_output.DeleteMembershipOutput":
        """<p>Deletes a specified membership. All resources under a membership must be deleted.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.delete_membership_input.DeleteMembershipInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.delete_membership_output.DeleteMembershipOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_membership

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_membership.delete_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_membership_input.DeleteMembershipInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
        status: Optional[
            "aws_sdk_cleanrooms.types.membership_status.MembershipStatus"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.list_memberships_output.ListMembershipsOutput":
        """<p>Lists all memberships resources within the caller's account.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            status: <p>A filter which will return only memberships in the specified status.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_memberships_input.ListMembershipsInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_memberships_output.ListMembershipsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_memberships

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_memberships.list_memberships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_memberships_input.ListMembershipsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_protected_job(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_job_identifier: "aws_sdk_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_protected_job_output.GetProtectedJobOutput":
        """<p>Returns job processing metadata.</p>

        Args:
            membership_identifier: <p> The identifier for a membership in a protected job instance.</p>
            protected_job_identifier: <p> The identifier for the protected job instance.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_protected_job_input.GetProtectedJobInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_protected_job_output.GetProtectedJobOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_job

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_job.get_protected_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_protected_job_input.GetProtectedJobInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["protected_job_identifier"] = protected_job_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_protected_query(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_query_identifier: "aws_sdk_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_protected_query_output.GetProtectedQueryOutput":
        """<p>Returns query processing metadata.</p>

        Args:
            membership_identifier: <p>The identifier for a membership in a protected query instance.</p>
            protected_query_identifier: <p>The identifier for a protected query instance.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_protected_query_input.GetProtectedQueryInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_protected_query_output.GetProtectedQueryOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_query

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_query.get_protected_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_protected_query_input.GetProtectedQueryInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["protected_query_identifier"] = protected_query_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_privacy_budgets(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_type: "aws_sdk_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
        access_budget_resource_arn: Optional[
            "aws_sdk_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.list_privacy_budgets_output.ListPrivacyBudgetsOutput"
    ):
        """<p>Returns detailed information about the privacy budgets in a specified membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget is retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_type: <p>The privacy budget type.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            access_budget_resource_arn: <p>The Amazon Resource Name (ARN) of the access budget resource to filter privacy budgets by.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_privacy_budgets_input.ListPrivacyBudgetsInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_privacy_budgets_output.ListPrivacyBudgetsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budgets

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budgets.list_privacy_budgets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_privacy_budgets_input.ListPrivacyBudgetsInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["privacy_budget_type"] = privacy_budget_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if access_budget_resource_arn is not None:
            input_["access_budget_resource_arn"] = access_budget_resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_protected_jobs(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        status: Optional[
            "aws_sdk_cleanrooms.types.protected_job_status.ProtectedJobStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_protected_jobs_output.ListProtectedJobsOutput":
        """<p>Lists protected jobs, sorted by most recent job.</p>

        Args:
            membership_identifier: <p>The identifier for the membership in the collaboration.</p>
            status: <p>A filter on the status of the protected job.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_protected_jobs_input.ListProtectedJobsInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_protected_jobs_output.ListProtectedJobsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_jobs

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_jobs.list_protected_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_protected_jobs_input.ListProtectedJobsInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        if status is not None:
            input_["status"] = status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_protected_queries(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        status: Optional[
            "aws_sdk_cleanrooms.types.protected_query_status.ProtectedQueryStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_protected_queries_output.ListProtectedQueriesOutput":
        """<p>Lists protected queries, sorted by the most recent query.</p>

        Args:
            membership_identifier: <p>The identifier for the membership in the collaboration.</p>
            status: <p>A filter on the status of the protected query.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_protected_queries_input.ListProtectedQueriesInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_protected_queries_output.ListProtectedQueriesOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_queries

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_queries.list_protected_queries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_protected_queries_input.ListProtectedQueriesInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        if status is not None:
            input_["status"] = status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def preview_privacy_impact(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        parameters: "aws_sdk_cleanrooms.types.preview_privacy_impact_parameters_input.PreviewPrivacyImpactParametersInput",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.preview_privacy_impact_output.PreviewPrivacyImpactOutput":
        """<p>An estimate of the number of aggregation functions that the member who can query can run given epsilon and noise parameters.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. Accepts a membership ID.</p>
            parameters: <p>Specifies the desired epsilon and noise parameters to preview.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.preview_privacy_impact_input.PreviewPrivacyImpactInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.preview_privacy_impact_output.PreviewPrivacyImpactOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.preview_privacy_impact

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.preview_privacy_impact.preview_privacy_impact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.preview_privacy_impact_input.PreviewPrivacyImpactInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_protected_job(
        self,
        type: "aws_sdk_cleanrooms.types.protected_job_type.ProtectedJobType",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        job_parameters: "aws_sdk_cleanrooms.types.protected_job_parameters.ProtectedJobParameters",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        result_configuration: Optional[
            "aws_sdk_cleanrooms.types.protected_job_result_configuration_input.ProtectedJobResultConfigurationInput"
        ] = None,
        compute_configuration: Optional[
            "aws_sdk_cleanrooms.types.protected_job_compute_configuration.ProtectedJobComputeConfiguration"
        ] = None,
        job_compute_payer_account_id: Optional[
            "aws_sdk_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.start_protected_job_output.StartProtectedJobOutput":
        """<p>Creates a protected job that is started by Clean Rooms.</p>

        Args:
            type: <p> The type of protected job to start.</p>
            membership_identifier: <p>A unique identifier for the membership to run this job against. Currently accepts a membership ID.</p>
            job_parameters: <p> The job parameters.</p>
            result_configuration: <p>The details needed to write the job results.</p>
            compute_configuration: <p>The compute configuration for the protected job.</p>
            job_compute_payer_account_id: <p>The account ID of the member that pays for the job compute costs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.start_protected_job_input.StartProtectedJobInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.start_protected_job_output.StartProtectedJobOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_job

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_job.start_protected_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.start_protected_job_input.StartProtectedJobInput = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["membership_identifier"] = membership_identifier
        input_["job_parameters"] = job_parameters
        if result_configuration is not None:
            input_["result_configuration"] = result_configuration
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if job_compute_payer_account_id is not None:
            input_["job_compute_payer_account_id"] = job_compute_payer_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_protected_query(
        self,
        type: "aws_sdk_cleanrooms.types.protected_query_type.ProtectedQueryType",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        sql_parameters: "aws_sdk_cleanrooms.types.protected_query_sql_parameters.ProtectedQuerySQLParameters",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        result_configuration: Optional[
            "aws_sdk_cleanrooms.types.protected_query_result_configuration.ProtectedQueryResultConfiguration"
        ] = None,
        compute_configuration: Optional[
            "aws_sdk_cleanrooms.types.compute_configuration.ComputeConfiguration"
        ] = None,
        query_compute_payer_account_id: Optional[
            "aws_sdk_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.start_protected_query_output.StartProtectedQueryOutput":
        """<p>Creates a protected query that is started by Clean Rooms.</p>

        Args:
            type: <p>The type of the protected query to be started.</p>
            membership_identifier: <p>A unique identifier for the membership to run this query against. Currently accepts a membership ID.</p>
            sql_parameters: <p>The protected SQL query parameters.</p>
            result_configuration: <p>The details needed to write the query results.</p>
            compute_configuration: <p> The compute configuration for the protected query.</p>
            query_compute_payer_account_id: <p>The account ID of the member that pays for the query compute costs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.start_protected_query_input.StartProtectedQueryInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.start_protected_query_output.StartProtectedQueryOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_query

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_query.start_protected_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.start_protected_query_input.StartProtectedQueryInput = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["membership_identifier"] = membership_identifier
        input_["sql_parameters"] = sql_parameters
        if result_configuration is not None:
            input_["result_configuration"] = result_configuration
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if query_compute_payer_account_id is not None:
            input_["query_compute_payer_account_id"] = query_compute_payer_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_protected_job(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_job_identifier: "aws_sdk_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier",
        target_status: "aws_sdk_cleanrooms.types.target_protected_job_status.TargetProtectedJobStatus",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.update_protected_job_output.UpdateProtectedJobOutput"
    ):
        """<p>Updates the processing of a currently running job.</p>

        Args:
            membership_identifier: <p>The identifier for a member of a protected job instance.</p>
            protected_job_identifier: <p> The identifier of the protected job to update.</p>
            target_status: <p>The target status of a protected job. Used to update the execution status of a currently running job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.update_protected_job_input.UpdateProtectedJobInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.update_protected_job_output.UpdateProtectedJobOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_job

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_job.update_protected_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_protected_job_input.UpdateProtectedJobInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["protected_job_identifier"] = protected_job_identifier
        input_["target_status"] = target_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_protected_query(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_query_identifier: "aws_sdk_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier",
        target_status: "aws_sdk_cleanrooms.types.target_protected_query_status.TargetProtectedQueryStatus",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.update_protected_query_output.UpdateProtectedQueryOutput":
        """<p>Updates the processing of a currently running query.</p>

        Args:
            membership_identifier: <p>The identifier for a member of a protected query instance.</p>
            protected_query_identifier: <p>The identifier for a protected query instance.</p>
            target_status: <p>The target status of a query. Used to update the execution status of a currently running query.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.update_protected_query_input.UpdateProtectedQueryInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.update_protected_query_output.UpdateProtectedQueryOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_query

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_query.update_protected_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_protected_query_input.UpdateProtectedQueryInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["protected_query_identifier"] = protected_query_identifier
        input_["target_status"] = target_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncMembershipResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        query_log_status: "aws_sdk_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        job_log_status: Optional[
            "aws_sdk_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
        ] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
        default_result_configuration: Optional[
            "aws_sdk_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
        ] = None,
        default_job_result_configuration: Optional[
            "aws_sdk_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
        ] = None,
        payment_configuration: Optional[
            "aws_sdk_cleanrooms.types.membership_payment_configuration.MembershipPaymentConfiguration"
        ] = None,
        is_metrics_enabled: Optional[bool] = None,
    ) -> "aws_sdk_cleanrooms.types.create_membership_output.CreateMembershipOutput":
        """<p>Creates a membership for a specific collaboration identifier and joins the collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique ID for the associated collaboration.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            default_result_configuration: <p>The default protected query result configuration as specified by the member who can receive results.</p>
            default_job_result_configuration: <p>The default job result configuration that determines how job results are protected and managed within this membership. This configuration applies to all jobs.</p>
            payment_configuration: <p>The payment responsibilities accepted by the collaboration member.</p> <p>Not required if the collaboration member has the member ability to run queries. </p> <p>Required if the collaboration member doesn't have the member ability to run queries but is configured as a payer by the collaboration creator. </p>
            is_metrics_enabled: <p>An indicator as to whether Amazon CloudWatch metrics have been enabled or disabled for the membership.</p> <p>Amazon CloudWatch metrics are only available when the collaboration has metrics enabled. This option can be set by collaboration members who have the ability to run queries (analysis runners) or by members who are configured as payers.</p> <p>When <code>true</code>, metrics about query execution are collected in Amazon CloudWatch. The default value is <code>false</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.create_membership_input.CreateMembershipInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.create_membership_output.CreateMembershipOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_membership

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_membership.async_create_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_membership_input.CreateMembershipInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["query_log_status"] = query_log_status
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if tags is not None:
            input_["tags"] = tags
        if default_result_configuration is not None:
            input_["default_result_configuration"] = default_result_configuration
        if default_job_result_configuration is not None:
            input_["default_job_result_configuration"] = (
                default_job_result_configuration
            )
        if payment_configuration is not None:
            input_["payment_configuration"] = payment_configuration
        if is_metrics_enabled is not None:
            input_["is_metrics_enabled"] = is_metrics_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_membership_output.GetMembershipOutput":
        """<p>Retrieves a specified membership for an identifier.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_membership_input.GetMembershipInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_membership_output.GetMembershipOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_membership

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_membership.async_get_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_membership_input.GetMembershipInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        query_log_status: Optional[
            "aws_sdk_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus"
        ] = None,
        job_log_status: Optional[
            "aws_sdk_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
        ] = None,
        default_result_configuration: Optional[
            "aws_sdk_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
        ] = None,
        default_job_result_configuration: Optional[
            "aws_sdk_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
        ] = None,
        membership_payment_configuration: Optional[
            "aws_sdk_cleanrooms.types.update_membership_payment_configuration.UpdateMembershipPaymentConfiguration"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.update_membership_output.UpdateMembershipOutput":
        """<p>Updates a membership.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            default_result_configuration: <p>The default protected query result configuration as specified by the member who can receive results.</p>
            default_job_result_configuration: <p> The default job result configuration.</p>
            membership_payment_configuration: <p>The payment configuration to update for the membership.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.update_membership_input.UpdateMembershipInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.update_membership_output.UpdateMembershipOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_membership

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_membership.async_update_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_membership_input.UpdateMembershipInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        if query_log_status is not None:
            input_["query_log_status"] = query_log_status
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if default_result_configuration is not None:
            input_["default_result_configuration"] = default_result_configuration
        if default_job_result_configuration is not None:
            input_["default_job_result_configuration"] = (
                default_job_result_configuration
            )
        if membership_payment_configuration is not None:
            input_["membership_payment_configuration"] = (
                membership_payment_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_membership_output.DeleteMembershipOutput":
        """<p>Deletes a specified membership. All resources under a membership must be deleted.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.delete_membership_input.DeleteMembershipInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.delete_membership_output.DeleteMembershipOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_membership

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_membership.async_delete_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_membership_input.DeleteMembershipInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
        status: Optional[
            "aws_sdk_cleanrooms.types.membership_status.MembershipStatus"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.list_memberships_output.ListMembershipsOutput":
        """<p>Lists all memberships resources within the caller's account.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            status: <p>A filter which will return only memberships in the specified status.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_memberships_input.ListMembershipsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_memberships_output.ListMembershipsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_memberships

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_memberships.async_list_memberships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_memberships_input.ListMembershipsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_protected_job(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_job_identifier: "aws_sdk_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_protected_job_output.GetProtectedJobOutput":
        """<p>Returns job processing metadata.</p>

        Args:
            membership_identifier: <p> The identifier for a membership in a protected job instance.</p>
            protected_job_identifier: <p> The identifier for the protected job instance.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_protected_job_input.GetProtectedJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_protected_job_output.GetProtectedJobOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_job

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_job.async_get_protected_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_protected_job_input.GetProtectedJobInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["protected_job_identifier"] = protected_job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_protected_query(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_query_identifier: "aws_sdk_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_protected_query_output.GetProtectedQueryOutput":
        """<p>Returns query processing metadata.</p>

        Args:
            membership_identifier: <p>The identifier for a membership in a protected query instance.</p>
            protected_query_identifier: <p>The identifier for a protected query instance.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_protected_query_input.GetProtectedQueryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_protected_query_output.GetProtectedQueryOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_query

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_query.async_get_protected_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_protected_query_input.GetProtectedQueryInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["protected_query_identifier"] = protected_query_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_privacy_budgets(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_type: "aws_sdk_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
        access_budget_resource_arn: Optional[
            "aws_sdk_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.list_privacy_budgets_output.ListPrivacyBudgetsOutput"
    ):
        """<p>Returns detailed information about the privacy budgets in a specified membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget is retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_type: <p>The privacy budget type.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            access_budget_resource_arn: <p>The Amazon Resource Name (ARN) of the access budget resource to filter privacy budgets by.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_privacy_budgets_input.ListPrivacyBudgetsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_privacy_budgets_output.ListPrivacyBudgetsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budgets

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budgets.async_list_privacy_budgets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_privacy_budgets_input.ListPrivacyBudgetsInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["privacy_budget_type"] = privacy_budget_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if access_budget_resource_arn is not None:
            input_["access_budget_resource_arn"] = access_budget_resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_protected_jobs(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "aws_sdk_cleanrooms.types.protected_job_status.ProtectedJobStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_protected_jobs_output.ListProtectedJobsOutput":
        """<p>Lists protected jobs, sorted by most recent job.</p>

        Args:
            membership_identifier: <p>The identifier for the membership in the collaboration.</p>
            status: <p>A filter on the status of the protected job.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_protected_jobs_input.ListProtectedJobsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_protected_jobs_output.ListProtectedJobsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_jobs.async_list_protected_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_protected_jobs_input.ListProtectedJobsInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        if status is not None:
            input_["status"] = status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_protected_queries(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "aws_sdk_cleanrooms.types.protected_query_status.ProtectedQueryStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_protected_queries_output.ListProtectedQueriesOutput":
        """<p>Lists protected queries, sorted by the most recent query.</p>

        Args:
            membership_identifier: <p>The identifier for the membership in the collaboration.</p>
            status: <p>A filter on the status of the protected query.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_protected_queries_input.ListProtectedQueriesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_protected_queries_output.ListProtectedQueriesOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_queries

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_queries.async_list_protected_queries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_protected_queries_input.ListProtectedQueriesInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        if status is not None:
            input_["status"] = status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def preview_privacy_impact(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        parameters: "aws_sdk_cleanrooms.types.preview_privacy_impact_parameters_input.PreviewPrivacyImpactParametersInput",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.preview_privacy_impact_output.PreviewPrivacyImpactOutput":
        """<p>An estimate of the number of aggregation functions that the member who can query can run given epsilon and noise parameters.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. Accepts a membership ID.</p>
            parameters: <p>Specifies the desired epsilon and noise parameters to preview.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.preview_privacy_impact_input.PreviewPrivacyImpactInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.preview_privacy_impact_output.PreviewPrivacyImpactOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.preview_privacy_impact

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.preview_privacy_impact.async_preview_privacy_impact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.preview_privacy_impact_input.PreviewPrivacyImpactInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_protected_job(
        self,
        type: "aws_sdk_cleanrooms.types.protected_job_type.ProtectedJobType",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        job_parameters: "aws_sdk_cleanrooms.types.protected_job_parameters.ProtectedJobParameters",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        result_configuration: Optional[
            "aws_sdk_cleanrooms.types.protected_job_result_configuration_input.ProtectedJobResultConfigurationInput"
        ] = None,
        compute_configuration: Optional[
            "aws_sdk_cleanrooms.types.protected_job_compute_configuration.ProtectedJobComputeConfiguration"
        ] = None,
        job_compute_payer_account_id: Optional[
            "aws_sdk_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.start_protected_job_output.StartProtectedJobOutput":
        """<p>Creates a protected job that is started by Clean Rooms.</p>

        Args:
            type: <p> The type of protected job to start.</p>
            membership_identifier: <p>A unique identifier for the membership to run this job against. Currently accepts a membership ID.</p>
            job_parameters: <p> The job parameters.</p>
            result_configuration: <p>The details needed to write the job results.</p>
            compute_configuration: <p>The compute configuration for the protected job.</p>
            job_compute_payer_account_id: <p>The account ID of the member that pays for the job compute costs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.start_protected_job_input.StartProtectedJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.start_protected_job_output.StartProtectedJobOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_job

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_job.async_start_protected_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.start_protected_job_input.StartProtectedJobInput = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["membership_identifier"] = membership_identifier
        input_["job_parameters"] = job_parameters
        if result_configuration is not None:
            input_["result_configuration"] = result_configuration
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if job_compute_payer_account_id is not None:
            input_["job_compute_payer_account_id"] = job_compute_payer_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_protected_query(
        self,
        type: "aws_sdk_cleanrooms.types.protected_query_type.ProtectedQueryType",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        sql_parameters: "aws_sdk_cleanrooms.types.protected_query_sql_parameters.ProtectedQuerySQLParameters",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        result_configuration: Optional[
            "aws_sdk_cleanrooms.types.protected_query_result_configuration.ProtectedQueryResultConfiguration"
        ] = None,
        compute_configuration: Optional[
            "aws_sdk_cleanrooms.types.compute_configuration.ComputeConfiguration"
        ] = None,
        query_compute_payer_account_id: Optional[
            "aws_sdk_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.start_protected_query_output.StartProtectedQueryOutput":
        """<p>Creates a protected query that is started by Clean Rooms.</p>

        Args:
            type: <p>The type of the protected query to be started.</p>
            membership_identifier: <p>A unique identifier for the membership to run this query against. Currently accepts a membership ID.</p>
            sql_parameters: <p>The protected SQL query parameters.</p>
            result_configuration: <p>The details needed to write the query results.</p>
            compute_configuration: <p> The compute configuration for the protected query.</p>
            query_compute_payer_account_id: <p>The account ID of the member that pays for the query compute costs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.start_protected_query_input.StartProtectedQueryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.start_protected_query_output.StartProtectedQueryOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_query

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_query.async_start_protected_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.start_protected_query_input.StartProtectedQueryInput = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["membership_identifier"] = membership_identifier
        input_["sql_parameters"] = sql_parameters
        if result_configuration is not None:
            input_["result_configuration"] = result_configuration
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if query_compute_payer_account_id is not None:
            input_["query_compute_payer_account_id"] = query_compute_payer_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_protected_job(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_job_identifier: "aws_sdk_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier",
        target_status: "aws_sdk_cleanrooms.types.target_protected_job_status.TargetProtectedJobStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.update_protected_job_output.UpdateProtectedJobOutput"
    ):
        """<p>Updates the processing of a currently running job.</p>

        Args:
            membership_identifier: <p>The identifier for a member of a protected job instance.</p>
            protected_job_identifier: <p> The identifier of the protected job to update.</p>
            target_status: <p>The target status of a protected job. Used to update the execution status of a currently running job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.update_protected_job_input.UpdateProtectedJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.update_protected_job_output.UpdateProtectedJobOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_job

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_job.async_update_protected_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_protected_job_input.UpdateProtectedJobInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["protected_job_identifier"] = protected_job_identifier
        input_["target_status"] = target_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_protected_query(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_query_identifier: "aws_sdk_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier",
        target_status: "aws_sdk_cleanrooms.types.target_protected_query_status.TargetProtectedQueryStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.update_protected_query_output.UpdateProtectedQueryOutput":
        """<p>Updates the processing of a currently running query.</p>

        Args:
            membership_identifier: <p>The identifier for a member of a protected query instance.</p>
            protected_query_identifier: <p>The identifier for a protected query instance.</p>
            target_status: <p>The target status of a query. Used to update the execution status of a currently running query.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.update_protected_query_input.UpdateProtectedQueryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.update_protected_query_output.UpdateProtectedQueryOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_query

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_query.async_update_protected_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_protected_query_input.UpdateProtectedQueryInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["protected_query_identifier"] = protected_query_identifier
        input_["target_status"] = target_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
