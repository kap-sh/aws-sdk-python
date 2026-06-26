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
    import aws_sdk_cleanrooms.types.allowed_result_regions
    import aws_sdk_cleanrooms.types.analysis_rule_type
    import aws_sdk_cleanrooms.types.analysis_template_arn
    import aws_sdk_cleanrooms.types.analysis_template_arn_list
    import aws_sdk_cleanrooms.types.analytics_engine
    import aws_sdk_cleanrooms.types.auto_approved_change_type_list
    import aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_input
    import aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_output
    import aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_input
    import aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_output
    import aws_sdk_cleanrooms.types.batch_get_schema_input
    import aws_sdk_cleanrooms.types.batch_get_schema_output
    import aws_sdk_cleanrooms.types.budgeted_resource_arn
    import aws_sdk_cleanrooms.types.change_input_list
    import aws_sdk_cleanrooms.types.change_request_action
    import aws_sdk_cleanrooms.types.change_request_status
    import aws_sdk_cleanrooms.types.collaboration_change_request_identifier
    import aws_sdk_cleanrooms.types.collaboration_change_request_summary
    import aws_sdk_cleanrooms.types.collaboration_configured_audience_model_association_summary
    import aws_sdk_cleanrooms.types.collaboration_description
    import aws_sdk_cleanrooms.types.collaboration_id_namespace_association_summary
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.collaboration_job_log_status
    import aws_sdk_cleanrooms.types.collaboration_name
    import aws_sdk_cleanrooms.types.collaboration_privacy_budget_summary
    import aws_sdk_cleanrooms.types.collaboration_privacy_budget_template_summary
    import aws_sdk_cleanrooms.types.collaboration_query_log_status
    import aws_sdk_cleanrooms.types.configured_audience_model_association_identifier
    import aws_sdk_cleanrooms.types.create_collaboration_change_request_input
    import aws_sdk_cleanrooms.types.create_collaboration_change_request_output
    import aws_sdk_cleanrooms.types.create_collaboration_input
    import aws_sdk_cleanrooms.types.create_collaboration_output
    import aws_sdk_cleanrooms.types.data_encryption_metadata
    import aws_sdk_cleanrooms.types.delete_collaboration_input
    import aws_sdk_cleanrooms.types.delete_collaboration_output
    import aws_sdk_cleanrooms.types.delete_member_input
    import aws_sdk_cleanrooms.types.delete_member_output
    import aws_sdk_cleanrooms.types.display_name
    import aws_sdk_cleanrooms.types.filterable_member_status
    import aws_sdk_cleanrooms.types.get_collaboration_analysis_template_input
    import aws_sdk_cleanrooms.types.get_collaboration_analysis_template_output
    import aws_sdk_cleanrooms.types.get_collaboration_change_request_input
    import aws_sdk_cleanrooms.types.get_collaboration_change_request_output
    import aws_sdk_cleanrooms.types.get_collaboration_configured_audience_model_association_input
    import aws_sdk_cleanrooms.types.get_collaboration_configured_audience_model_association_output
    import aws_sdk_cleanrooms.types.get_collaboration_id_namespace_association_input
    import aws_sdk_cleanrooms.types.get_collaboration_id_namespace_association_output
    import aws_sdk_cleanrooms.types.get_collaboration_input
    import aws_sdk_cleanrooms.types.get_collaboration_output
    import aws_sdk_cleanrooms.types.get_collaboration_privacy_budget_template_input
    import aws_sdk_cleanrooms.types.get_collaboration_privacy_budget_template_output
    import aws_sdk_cleanrooms.types.get_schema_analysis_rule_input
    import aws_sdk_cleanrooms.types.get_schema_analysis_rule_output
    import aws_sdk_cleanrooms.types.get_schema_input
    import aws_sdk_cleanrooms.types.get_schema_output
    import aws_sdk_cleanrooms.types.id_namespace_association_identifier
    import aws_sdk_cleanrooms.types.list_collaboration_analysis_templates_input
    import aws_sdk_cleanrooms.types.list_collaboration_analysis_templates_output
    import aws_sdk_cleanrooms.types.list_collaboration_change_requests_input
    import aws_sdk_cleanrooms.types.list_collaboration_change_requests_output
    import aws_sdk_cleanrooms.types.list_collaboration_configured_audience_model_associations_input
    import aws_sdk_cleanrooms.types.list_collaboration_configured_audience_model_associations_output
    import aws_sdk_cleanrooms.types.list_collaboration_id_namespace_associations_input
    import aws_sdk_cleanrooms.types.list_collaboration_id_namespace_associations_output
    import aws_sdk_cleanrooms.types.list_collaboration_privacy_budget_templates_input
    import aws_sdk_cleanrooms.types.list_collaboration_privacy_budget_templates_output
    import aws_sdk_cleanrooms.types.list_collaboration_privacy_budgets_input
    import aws_sdk_cleanrooms.types.list_collaboration_privacy_budgets_output
    import aws_sdk_cleanrooms.types.list_collaborations_input
    import aws_sdk_cleanrooms.types.list_collaborations_output
    import aws_sdk_cleanrooms.types.list_members_input
    import aws_sdk_cleanrooms.types.list_members_output
    import aws_sdk_cleanrooms.types.list_schemas_input
    import aws_sdk_cleanrooms.types.list_schemas_output
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.member_abilities
    import aws_sdk_cleanrooms.types.member_list
    import aws_sdk_cleanrooms.types.ml_member_abilities
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.payment_configuration
    import aws_sdk_cleanrooms.types.privacy_budget_template_identifier
    import aws_sdk_cleanrooms.types.privacy_budget_type
    import aws_sdk_cleanrooms.types.schema_analysis_rule_request_list
    import aws_sdk_cleanrooms.types.schema_type
    import aws_sdk_cleanrooms.types.table_alias
    import aws_sdk_cleanrooms.types.table_alias_list
    import aws_sdk_cleanrooms.types.tag_map
    import aws_sdk_cleanrooms.types.update_collaboration_change_request_input
    import aws_sdk_cleanrooms.types.update_collaboration_change_request_output
    import aws_sdk_cleanrooms.types.update_collaboration_input
    import aws_sdk_cleanrooms.types.update_collaboration_output
    from aws_sdk_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from aws_sdk_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class CollaborationResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        members: "aws_sdk_cleanrooms.types.member_list.MemberList",
        name: "aws_sdk_cleanrooms.types.collaboration_name.CollaborationName",
        description: "aws_sdk_cleanrooms.types.collaboration_description.CollaborationDescription",
        creator_member_abilities: "aws_sdk_cleanrooms.types.member_abilities.MemberAbilities",
        creator_display_name: "aws_sdk_cleanrooms.types.display_name.DisplayName",
        query_log_status: "aws_sdk_cleanrooms.types.collaboration_query_log_status.CollaborationQueryLogStatus",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        creator_ml_member_abilities: Optional[
            "aws_sdk_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
        ] = None,
        data_encryption_metadata: Optional[
            "aws_sdk_cleanrooms.types.data_encryption_metadata.DataEncryptionMetadata"
        ] = None,
        job_log_status: Optional[
            "aws_sdk_cleanrooms.types.collaboration_job_log_status.CollaborationJobLogStatus"
        ] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
        creator_payment_configuration: Optional[
            "aws_sdk_cleanrooms.types.payment_configuration.PaymentConfiguration"
        ] = None,
        analytics_engine: Optional[
            "aws_sdk_cleanrooms.types.analytics_engine.AnalyticsEngine"
        ] = None,
        auto_approved_change_request_types: Optional[
            "aws_sdk_cleanrooms.types.auto_approved_change_type_list.AutoApprovedChangeTypeList"
        ] = None,
        allowed_result_regions: Optional[
            "aws_sdk_cleanrooms.types.allowed_result_regions.AllowedResultRegions"
        ] = None,
        is_metrics_enabled: Optional[bool] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.create_collaboration_output.CreateCollaborationOutput"
    ):
        """<p>Creates a new collaboration.</p>

        Args:
            members: <p>A list of initial members, not including the creator. This list is immutable.</p>
            name: <p>The display name for a collaboration.</p>
            description: <p>A description of the collaboration provided by the collaboration owner.</p>
            creator_member_abilities: <p>The abilities granted to the collaboration creator.</p>
            creator_ml_member_abilities: <p>The ML abilities granted to the collaboration creator.</p>
            creator_display_name: <p>The display name of the collaboration creator.</p>
            data_encryption_metadata: <p>The settings for client-side encryption with Cryptographic Computing for Clean Rooms.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the collaboration.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>Specifies whether job logs are enabled for this collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration; those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            creator_payment_configuration: <p>The collaboration creator's payment responsibilities set by the collaboration creator. </p> <p>If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer.</p>
            analytics_engine: <p> The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>
            auto_approved_change_request_types: <p>The types of change requests that are automatically approved for this collaboration.</p>
            allowed_result_regions: <p>The Amazon Web Services Regions where collaboration query results can be stored. When specified, results can only be written to these Regions. This parameter enables you to meet your compliance and data governance requirements, and implement regional data governance policies.</p>
            is_metrics_enabled: <p>An indicator as to whether metrics have been enabled or disabled for the collaboration.</p> <p>When <code>true</code>, collaboration members can opt in to Amazon CloudWatch metrics for their membership queries. The default value is <code>false</code>.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.create_collaboration_input.CreateCollaborationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.create_collaboration_output.CreateCollaborationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration.create_collaboration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_collaboration_input.CreateCollaborationInput = {}  # type: ignore[typeddict-item]
        input_["members"] = members
        input_["name"] = name
        input_["description"] = description
        input_["creator_member_abilities"] = creator_member_abilities
        if creator_ml_member_abilities is not None:
            input_["creator_ml_member_abilities"] = creator_ml_member_abilities
        input_["creator_display_name"] = creator_display_name
        if data_encryption_metadata is not None:
            input_["data_encryption_metadata"] = data_encryption_metadata
        input_["query_log_status"] = query_log_status
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if tags is not None:
            input_["tags"] = tags
        if creator_payment_configuration is not None:
            input_["creator_payment_configuration"] = creator_payment_configuration
        if analytics_engine is not None:
            input_["analytics_engine"] = analytics_engine
        if auto_approved_change_request_types is not None:
            input_["auto_approved_change_request_types"] = (
                auto_approved_change_request_types
            )
        if allowed_result_regions is not None:
            input_["allowed_result_regions"] = allowed_result_regions
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
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_output.GetCollaborationOutput":
        """<p>Returns metadata about a collaboration.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_collaboration_input.GetCollaborationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_output.GetCollaborationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration.get_collaboration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_input.GetCollaborationInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        name: Optional[
            "aws_sdk_cleanrooms.types.collaboration_name.CollaborationName"
        ] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.collaboration_description.CollaborationDescription"
        ] = None,
        analytics_engine: Optional[
            "aws_sdk_cleanrooms.types.analytics_engine.AnalyticsEngine"
        ] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.update_collaboration_output.UpdateCollaborationOutput"
    ):
        """<p>Updates collaboration metadata and can only be called by the collaboration owner.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>
            name: <p>A human-readable identifier provided by the collaboration owner. Display names are not unique.</p>
            description: <p>A description of the collaboration.</p>
            analytics_engine: <p>The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.update_collaboration_input.UpdateCollaborationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.update_collaboration_output.UpdateCollaborationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration.update_collaboration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_collaboration_input.UpdateCollaborationInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if analytics_engine is not None:
            input_["analytics_engine"] = analytics_engine

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.delete_collaboration_output.DeleteCollaborationOutput"
    ):
        """<p>Deletes a collaboration. It can only be called by the collaboration owner.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.delete_collaboration_input.DeleteCollaborationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.delete_collaboration_output.DeleteCollaborationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_collaboration

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_collaboration.delete_collaboration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_collaboration_input.DeleteCollaborationInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier

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
        member_status: Optional[
            "aws_sdk_cleanrooms.types.filterable_member_status.FilterableMemberStatus"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaborations_output.ListCollaborationsOutput":
        """<p>Lists collaborations the caller owns, is active in, or has been invited to.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            member_status: <p>The caller's status in a collaboration.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_collaborations_input.ListCollaborationsInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_collaborations_output.ListCollaborationsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaborations

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaborations.list_collaborations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaborations_input.ListCollaborationsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if member_status is not None:
            input_["member_status"] = member_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_collaboration_analysis_template(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        analysis_template_arns: "aws_sdk_cleanrooms.types.analysis_template_arn_list.AnalysisTemplateArnList",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput":
        """<p>Retrieves multiple analysis templates within a collaboration by their Amazon Resource Names (ARNs).</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            analysis_template_arns: <p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_input.BatchGetCollaborationAnalysisTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_collaboration_analysis_template

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_collaboration_analysis_template.batch_get_collaboration_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_input.BatchGetCollaborationAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["analysis_template_arns"] = analysis_template_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_schema(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        names: "aws_sdk_cleanrooms.types.table_alias_list.TableAliasList",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.batch_get_schema_output.BatchGetSchemaOutput":
        """<p>Retrieves multiple schemas by their identifiers.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schemas belong to. Currently accepts collaboration ID.</p>
            names: <p>The names for the schema objects to retrieve.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.batch_get_schema_input.BatchGetSchemaInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.batch_get_schema_output.BatchGetSchemaOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema.batch_get_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.batch_get_schema_input.BatchGetSchemaInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["names"] = names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_schema_analysis_rule(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        schema_analysis_rule_requests: "aws_sdk_cleanrooms.types.schema_analysis_rule_request_list.SchemaAnalysisRuleRequestList",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_output.BatchGetSchemaAnalysisRuleOutput":
        """<p>Retrieves multiple analysis rule schemas.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the schema analysis rule.</p>
            schema_analysis_rule_requests: <p>The information that's necessary to retrieve a schema analysis rule.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_input.BatchGetSchemaAnalysisRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_output.BatchGetSchemaAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema_analysis_rule

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema_analysis_rule.batch_get_schema_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_input.BatchGetSchemaAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["schema_analysis_rule_requests"] = schema_analysis_rule_requests

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_collaboration_change_request(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        changes: "aws_sdk_cleanrooms.types.change_input_list.ChangeInputList",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.create_collaboration_change_request_output.CreateCollaborationChangeRequestOutput":
        """<p>Creates a new change request to modify an existing collaboration. This enables post-creation modifications to collaborations through a structured API-driven approach.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            changes: <p>The list of changes to apply to the collaboration. Each change specifies the type of modification and the details of what should be changed.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.create_collaboration_change_request_input.CreateCollaborationChangeRequestInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.create_collaboration_change_request_output.CreateCollaborationChangeRequestOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration_change_request

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration_change_request.create_collaboration_change_request(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_collaboration_change_request_input.CreateCollaborationChangeRequestInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["changes"] = changes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_member(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        account_id: "aws_sdk_cleanrooms.types.account_id.AccountId",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_member_output.DeleteMemberOutput":
        """<p>Removes the specified member from a collaboration. The removed member is placed in the Removed status and can't interact with the collaboration. The removed member's data is inaccessible to active members of the collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier for the associated collaboration.</p>
            account_id: <p>The account ID of the member to remove.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.delete_member_input.DeleteMemberInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.delete_member_output.DeleteMemberOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_member

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_member.delete_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_member_input.DeleteMemberInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_collaboration_analysis_template(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        analysis_template_arn: "aws_sdk_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput":
        """<p>Retrieves an analysis template within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            analysis_template_arn: <p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_collaboration_analysis_template_input.GetCollaborationAnalysisTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_analysis_template

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_analysis_template.get_collaboration_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_analysis_template_input.GetCollaborationAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["analysis_template_arn"] = analysis_template_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_collaboration_change_request(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        change_request_identifier: "aws_sdk_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_change_request_output.GetCollaborationChangeRequestOutput":
        """<p>Retrieves detailed information about a specific collaboration change request.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            change_request_identifier: <p>A unique identifier for the change request to retrieve.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_collaboration_change_request_input.GetCollaborationChangeRequestInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_change_request_output.GetCollaborationChangeRequestOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_change_request

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_change_request.get_collaboration_change_request(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_change_request_input.GetCollaborationChangeRequestInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["change_request_identifier"] = change_request_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_collaboration_configured_audience_model_association(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        configured_audience_model_association_identifier: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_configured_audience_model_association_output.GetCollaborationConfiguredAudienceModelAssociationOutput":
        """<p>Retrieves a configured audience model association within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.</p>
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to retrieve.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_collaboration_configured_audience_model_association_input.GetCollaborationConfiguredAudienceModelAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_configured_audience_model_association_output.GetCollaborationConfiguredAudienceModelAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_configured_audience_model_association

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_configured_audience_model_association.get_collaboration_configured_audience_model_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_configured_audience_model_association_input.GetCollaborationConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["configured_audience_model_association_identifier"] = (
            configured_audience_model_association_identifier
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_collaboration_id_namespace_association(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        id_namespace_association_identifier: "aws_sdk_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_id_namespace_association_output.GetCollaborationIdNamespaceAssociationOutput":
        """<p>Retrieves an ID namespace association from a specific collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the ID namespace association that you want to retrieve.</p>
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to retrieve.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_collaboration_id_namespace_association_input.GetCollaborationIdNamespaceAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_id_namespace_association_output.GetCollaborationIdNamespaceAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_id_namespace_association

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_id_namespace_association.get_collaboration_id_namespace_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_id_namespace_association_input.GetCollaborationIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["id_namespace_association_identifier"] = (
            id_namespace_association_identifier
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_collaboration_privacy_budget_template(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        privacy_budget_template_identifier: "aws_sdk_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_privacy_budget_template_output.GetCollaborationPrivacyBudgetTemplateOutput":
        """<p>Returns details about a specified privacy budget template.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            privacy_budget_template_identifier: <p>A unique identifier for one of your privacy budget templates.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_collaboration_privacy_budget_template_input.GetCollaborationPrivacyBudgetTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_privacy_budget_template_output.GetCollaborationPrivacyBudgetTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_privacy_budget_template

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_privacy_budget_template.get_collaboration_privacy_budget_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_privacy_budget_template_input.GetCollaborationPrivacyBudgetTemplateInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["privacy_budget_template_identifier"] = (
            privacy_budget_template_identifier
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_schema(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        name: "aws_sdk_cleanrooms.types.table_alias.TableAlias",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_schema_output.GetSchemaOutput":
        """<p>Retrieves the schema for a relation within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            name: <p>The name of the relation to retrieve the schema for.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_schema_input.GetSchemaInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_schema_output.GetSchemaOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema.get_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_schema_input.GetSchemaInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_schema_analysis_rule(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        name: "aws_sdk_cleanrooms.types.table_alias.TableAlias",
        type: "aws_sdk_cleanrooms.types.analysis_rule_type.AnalysisRuleType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_schema_analysis_rule_output.GetSchemaAnalysisRuleOutput":
        """<p>Retrieves a schema analysis rule.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            name: <p>The name of the schema to retrieve the analysis rule for.</p>
            type: <p>The type of the schema analysis rule to retrieve. Schema analysis rules are uniquely identified by a combination of the collaboration, the schema name, and their type.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_schema_analysis_rule_input.GetSchemaAnalysisRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_schema_analysis_rule_output.GetSchemaAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema_analysis_rule

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema_analysis_rule.get_schema_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_schema_analysis_rule_input.GetSchemaAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["name"] = name
        input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_collaboration_analysis_templates(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_analysis_templates_output.ListCollaborationAnalysisTemplatesOutput":
        """<p>Lists analysis templates within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_collaboration_analysis_templates_input.ListCollaborationAnalysisTemplatesInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_analysis_templates_output.ListCollaborationAnalysisTemplatesOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_analysis_templates

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_analysis_templates.list_collaboration_analysis_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_analysis_templates_input.ListCollaborationAnalysisTemplatesInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    def list_collaboration_change_requests(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        status: Optional[
            "aws_sdk_cleanrooms.types.change_request_status.ChangeRequestStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_change_requests_output.ListCollaborationChangeRequestsOutput":
        """<p>Lists all change requests for a collaboration with pagination support. Returns change requests sorted by creation time.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            status: <p>A filter to only return change requests with the specified status.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_collaboration_change_requests_input.ListCollaborationChangeRequestsInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_change_requests_output.ListCollaborationChangeRequestsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_change_requests

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_change_requests.list_collaboration_change_requests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_change_requests_input.ListCollaborationChangeRequestsInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    def list_collaboration_configured_audience_model_associations(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_configured_audience_model_associations_output.ListCollaborationConfiguredAudienceModelAssociationsOutput":
        """<p>Lists configured audience model associations within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_collaboration_configured_audience_model_associations_input.ListCollaborationConfiguredAudienceModelAssociationsInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_configured_audience_model_associations_output.ListCollaborationConfiguredAudienceModelAssociationsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_configured_audience_model_associations

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_configured_audience_model_associations.list_collaboration_configured_audience_model_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_configured_audience_model_associations_input.ListCollaborationConfiguredAudienceModelAssociationsInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    def list_collaboration_id_namespace_associations(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_id_namespace_associations_output.ListCollaborationIdNamespaceAssociationsOutput":
        """<p>Returns a list of the ID namespace associations in a collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the ID namespace associations that you want to retrieve.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.&gt;</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_collaboration_id_namespace_associations_input.ListCollaborationIdNamespaceAssociationsInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_id_namespace_associations_output.ListCollaborationIdNamespaceAssociationsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_id_namespace_associations

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_id_namespace_associations.list_collaboration_id_namespace_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_id_namespace_associations_input.ListCollaborationIdNamespaceAssociationsInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    def list_collaboration_privacy_budgets(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        privacy_budget_type: "aws_sdk_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        access_budget_resource_arn: Optional[
            "aws_sdk_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_privacy_budgets_output.ListCollaborationPrivacyBudgetsOutput":
        """<p>Returns an array that summarizes each privacy budget in a specified collaboration. The summary includes the collaboration ARN, creation time, creating account, and privacy budget details.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            privacy_budget_type: <p>Specifies the type of the privacy budget.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            access_budget_resource_arn: <p>The Amazon Resource Name (ARN) of the Configured Table Association (ConfiguredTableAssociation) used to filter privacy budgets.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_collaboration_privacy_budgets_input.ListCollaborationPrivacyBudgetsInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_privacy_budgets_output.ListCollaborationPrivacyBudgetsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budgets

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budgets.list_collaboration_privacy_budgets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_privacy_budgets_input.ListCollaborationPrivacyBudgetsInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["privacy_budget_type"] = privacy_budget_type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if access_budget_resource_arn is not None:
            input_["access_budget_resource_arn"] = access_budget_resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_collaboration_privacy_budget_templates(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_privacy_budget_templates_output.ListCollaborationPrivacyBudgetTemplatesOutput":
        """<p>Returns an array that summarizes each privacy budget template in a specified collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_collaboration_privacy_budget_templates_input.ListCollaborationPrivacyBudgetTemplatesInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_privacy_budget_templates_output.ListCollaborationPrivacyBudgetTemplatesOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budget_templates

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budget_templates.list_collaboration_privacy_budget_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_privacy_budget_templates_input.ListCollaborationPrivacyBudgetTemplatesInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    def list_members(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_members_output.ListMembersOutput":
        """<p>Lists all members within a collaboration.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration in which the members are listed.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_members_input.ListMembersInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_members_output.ListMembersOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_members

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_members.list_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_members_input.ListMembersInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    def list_schemas(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        schema_type: Optional["aws_sdk_cleanrooms.types.schema_type.SchemaType"] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_schemas_output.ListSchemasOutput":
        """<p>Lists the schemas for relations within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            schema_type: <p>If present, filter schemas by schema type.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_schemas_input.ListSchemasInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_schemas_output.ListSchemasOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_schemas

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_schemas.list_schemas(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_schemas_input.ListSchemasInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        if schema_type is not None:
            input_["schema_type"] = schema_type
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

    def update_collaboration_change_request(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        change_request_identifier: "aws_sdk_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier",
        action: "aws_sdk_cleanrooms.types.change_request_action.ChangeRequestAction",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.update_collaboration_change_request_output.UpdateCollaborationChangeRequestOutput":
        """<p>Updates an existing collaboration change request. This operation allows approval actions for pending change requests in collaborations (APPROVE, DENY, CANCEL, COMMIT).</p> <p>For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the change request to be updated.</p>
            change_request_identifier: <p>The unique identifier of the specific change request to be updated within the collaboration.</p>
            action: <p>The action to perform on the change request. Valid values include APPROVE (approve the change), DENY (reject the change), CANCEL (cancel the request), and COMMIT (commit after the request is approved).</p> <p>For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.update_collaboration_change_request_input.UpdateCollaborationChangeRequestInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.update_collaboration_change_request_output.UpdateCollaborationChangeRequestOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration_change_request

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration_change_request.update_collaboration_change_request(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_collaboration_change_request_input.UpdateCollaborationChangeRequestInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["change_request_identifier"] = change_request_identifier
        input_["action"] = action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCollaborationResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        members: "aws_sdk_cleanrooms.types.member_list.MemberList",
        name: "aws_sdk_cleanrooms.types.collaboration_name.CollaborationName",
        description: "aws_sdk_cleanrooms.types.collaboration_description.CollaborationDescription",
        creator_member_abilities: "aws_sdk_cleanrooms.types.member_abilities.MemberAbilities",
        creator_display_name: "aws_sdk_cleanrooms.types.display_name.DisplayName",
        query_log_status: "aws_sdk_cleanrooms.types.collaboration_query_log_status.CollaborationQueryLogStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        creator_ml_member_abilities: Optional[
            "aws_sdk_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
        ] = None,
        data_encryption_metadata: Optional[
            "aws_sdk_cleanrooms.types.data_encryption_metadata.DataEncryptionMetadata"
        ] = None,
        job_log_status: Optional[
            "aws_sdk_cleanrooms.types.collaboration_job_log_status.CollaborationJobLogStatus"
        ] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
        creator_payment_configuration: Optional[
            "aws_sdk_cleanrooms.types.payment_configuration.PaymentConfiguration"
        ] = None,
        analytics_engine: Optional[
            "aws_sdk_cleanrooms.types.analytics_engine.AnalyticsEngine"
        ] = None,
        auto_approved_change_request_types: Optional[
            "aws_sdk_cleanrooms.types.auto_approved_change_type_list.AutoApprovedChangeTypeList"
        ] = None,
        allowed_result_regions: Optional[
            "aws_sdk_cleanrooms.types.allowed_result_regions.AllowedResultRegions"
        ] = None,
        is_metrics_enabled: Optional[bool] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.create_collaboration_output.CreateCollaborationOutput"
    ):
        """<p>Creates a new collaboration.</p>

        Args:
            members: <p>A list of initial members, not including the creator. This list is immutable.</p>
            name: <p>The display name for a collaboration.</p>
            description: <p>A description of the collaboration provided by the collaboration owner.</p>
            creator_member_abilities: <p>The abilities granted to the collaboration creator.</p>
            creator_ml_member_abilities: <p>The ML abilities granted to the collaboration creator.</p>
            creator_display_name: <p>The display name of the collaboration creator.</p>
            data_encryption_metadata: <p>The settings for client-side encryption with Cryptographic Computing for Clean Rooms.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the collaboration.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>Specifies whether job logs are enabled for this collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration; those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            creator_payment_configuration: <p>The collaboration creator's payment responsibilities set by the collaboration creator. </p> <p>If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer.</p>
            analytics_engine: <p> The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>
            auto_approved_change_request_types: <p>The types of change requests that are automatically approved for this collaboration.</p>
            allowed_result_regions: <p>The Amazon Web Services Regions where collaboration query results can be stored. When specified, results can only be written to these Regions. This parameter enables you to meet your compliance and data governance requirements, and implement regional data governance policies.</p>
            is_metrics_enabled: <p>An indicator as to whether metrics have been enabled or disabled for the collaboration.</p> <p>When <code>true</code>, collaboration members can opt in to Amazon CloudWatch metrics for their membership queries. The default value is <code>false</code>.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.create_collaboration_input.CreateCollaborationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.create_collaboration_output.CreateCollaborationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration.async_create_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_collaboration_input.CreateCollaborationInput = {}  # type: ignore[typeddict-item]
        input_["members"] = members
        input_["name"] = name
        input_["description"] = description
        input_["creator_member_abilities"] = creator_member_abilities
        if creator_ml_member_abilities is not None:
            input_["creator_ml_member_abilities"] = creator_ml_member_abilities
        input_["creator_display_name"] = creator_display_name
        if data_encryption_metadata is not None:
            input_["data_encryption_metadata"] = data_encryption_metadata
        input_["query_log_status"] = query_log_status
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if tags is not None:
            input_["tags"] = tags
        if creator_payment_configuration is not None:
            input_["creator_payment_configuration"] = creator_payment_configuration
        if analytics_engine is not None:
            input_["analytics_engine"] = analytics_engine
        if auto_approved_change_request_types is not None:
            input_["auto_approved_change_request_types"] = (
                auto_approved_change_request_types
            )
        if allowed_result_regions is not None:
            input_["allowed_result_regions"] = allowed_result_regions
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
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_output.GetCollaborationOutput":
        """<p>Returns metadata about a collaboration.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_collaboration_input.GetCollaborationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_output.GetCollaborationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration.async_get_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_input.GetCollaborationInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        name: Optional[
            "aws_sdk_cleanrooms.types.collaboration_name.CollaborationName"
        ] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.collaboration_description.CollaborationDescription"
        ] = None,
        analytics_engine: Optional[
            "aws_sdk_cleanrooms.types.analytics_engine.AnalyticsEngine"
        ] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.update_collaboration_output.UpdateCollaborationOutput"
    ):
        """<p>Updates collaboration metadata and can only be called by the collaboration owner.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>
            name: <p>A human-readable identifier provided by the collaboration owner. Display names are not unique.</p>
            description: <p>A description of the collaboration.</p>
            analytics_engine: <p>The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.update_collaboration_input.UpdateCollaborationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.update_collaboration_output.UpdateCollaborationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration.async_update_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_collaboration_input.UpdateCollaborationInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if analytics_engine is not None:
            input_["analytics_engine"] = analytics_engine

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.delete_collaboration_output.DeleteCollaborationOutput"
    ):
        """<p>Deletes a collaboration. It can only be called by the collaboration owner.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.delete_collaboration_input.DeleteCollaborationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.delete_collaboration_output.DeleteCollaborationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_collaboration

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_collaboration.async_delete_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_collaboration_input.DeleteCollaborationInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier

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
        member_status: Optional[
            "aws_sdk_cleanrooms.types.filterable_member_status.FilterableMemberStatus"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaborations_output.ListCollaborationsOutput":
        """<p>Lists collaborations the caller owns, is active in, or has been invited to.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            member_status: <p>The caller's status in a collaboration.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_collaborations_input.ListCollaborationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_collaborations_output.ListCollaborationsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaborations

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaborations.async_list_collaborations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaborations_input.ListCollaborationsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if member_status is not None:
            input_["member_status"] = member_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_collaboration_analysis_template(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        analysis_template_arns: "aws_sdk_cleanrooms.types.analysis_template_arn_list.AnalysisTemplateArnList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput":
        """<p>Retrieves multiple analysis templates within a collaboration by their Amazon Resource Names (ARNs).</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            analysis_template_arns: <p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_input.BatchGetCollaborationAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_collaboration_analysis_template

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_collaboration_analysis_template.async_batch_get_collaboration_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_input.BatchGetCollaborationAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["analysis_template_arns"] = analysis_template_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_schema(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        names: "aws_sdk_cleanrooms.types.table_alias_list.TableAliasList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.batch_get_schema_output.BatchGetSchemaOutput":
        """<p>Retrieves multiple schemas by their identifiers.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schemas belong to. Currently accepts collaboration ID.</p>
            names: <p>The names for the schema objects to retrieve.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.batch_get_schema_input.BatchGetSchemaInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.batch_get_schema_output.BatchGetSchemaOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema.async_batch_get_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.batch_get_schema_input.BatchGetSchemaInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["names"] = names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_schema_analysis_rule(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        schema_analysis_rule_requests: "aws_sdk_cleanrooms.types.schema_analysis_rule_request_list.SchemaAnalysisRuleRequestList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_output.BatchGetSchemaAnalysisRuleOutput":
        """<p>Retrieves multiple analysis rule schemas.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the schema analysis rule.</p>
            schema_analysis_rule_requests: <p>The information that's necessary to retrieve a schema analysis rule.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_input.BatchGetSchemaAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_output.BatchGetSchemaAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema_analysis_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema_analysis_rule.async_batch_get_schema_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_input.BatchGetSchemaAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["schema_analysis_rule_requests"] = schema_analysis_rule_requests

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_collaboration_change_request(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        changes: "aws_sdk_cleanrooms.types.change_input_list.ChangeInputList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.create_collaboration_change_request_output.CreateCollaborationChangeRequestOutput":
        """<p>Creates a new change request to modify an existing collaboration. This enables post-creation modifications to collaborations through a structured API-driven approach.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            changes: <p>The list of changes to apply to the collaboration. Each change specifies the type of modification and the details of what should be changed.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.create_collaboration_change_request_input.CreateCollaborationChangeRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.create_collaboration_change_request_output.CreateCollaborationChangeRequestOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration_change_request

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration_change_request.async_create_collaboration_change_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_collaboration_change_request_input.CreateCollaborationChangeRequestInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["changes"] = changes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_member(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        account_id: "aws_sdk_cleanrooms.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_member_output.DeleteMemberOutput":
        """<p>Removes the specified member from a collaboration. The removed member is placed in the Removed status and can't interact with the collaboration. The removed member's data is inaccessible to active members of the collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier for the associated collaboration.</p>
            account_id: <p>The account ID of the member to remove.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.delete_member_input.DeleteMemberInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.delete_member_output.DeleteMemberOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_member

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_member.async_delete_member(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_member_input.DeleteMemberInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_collaboration_analysis_template(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        analysis_template_arn: "aws_sdk_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput":
        """<p>Retrieves an analysis template within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            analysis_template_arn: <p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_collaboration_analysis_template_input.GetCollaborationAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_analysis_template

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_analysis_template.async_get_collaboration_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_analysis_template_input.GetCollaborationAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["analysis_template_arn"] = analysis_template_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_collaboration_change_request(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        change_request_identifier: "aws_sdk_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_change_request_output.GetCollaborationChangeRequestOutput":
        """<p>Retrieves detailed information about a specific collaboration change request.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            change_request_identifier: <p>A unique identifier for the change request to retrieve.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_collaboration_change_request_input.GetCollaborationChangeRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_change_request_output.GetCollaborationChangeRequestOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_change_request

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_change_request.async_get_collaboration_change_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_change_request_input.GetCollaborationChangeRequestInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["change_request_identifier"] = change_request_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_collaboration_configured_audience_model_association(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        configured_audience_model_association_identifier: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_configured_audience_model_association_output.GetCollaborationConfiguredAudienceModelAssociationOutput":
        """<p>Retrieves a configured audience model association within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.</p>
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to retrieve.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_collaboration_configured_audience_model_association_input.GetCollaborationConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_configured_audience_model_association_output.GetCollaborationConfiguredAudienceModelAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_configured_audience_model_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_configured_audience_model_association.async_get_collaboration_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_configured_audience_model_association_input.GetCollaborationConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["configured_audience_model_association_identifier"] = (
            configured_audience_model_association_identifier
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_collaboration_id_namespace_association(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        id_namespace_association_identifier: "aws_sdk_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_id_namespace_association_output.GetCollaborationIdNamespaceAssociationOutput":
        """<p>Retrieves an ID namespace association from a specific collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the ID namespace association that you want to retrieve.</p>
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to retrieve.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_collaboration_id_namespace_association_input.GetCollaborationIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_id_namespace_association_output.GetCollaborationIdNamespaceAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_id_namespace_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_id_namespace_association.async_get_collaboration_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_id_namespace_association_input.GetCollaborationIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["id_namespace_association_identifier"] = (
            id_namespace_association_identifier
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_collaboration_privacy_budget_template(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        privacy_budget_template_identifier: "aws_sdk_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_collaboration_privacy_budget_template_output.GetCollaborationPrivacyBudgetTemplateOutput":
        """<p>Returns details about a specified privacy budget template.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            privacy_budget_template_identifier: <p>A unique identifier for one of your privacy budget templates.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_collaboration_privacy_budget_template_input.GetCollaborationPrivacyBudgetTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_collaboration_privacy_budget_template_output.GetCollaborationPrivacyBudgetTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_privacy_budget_template

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_privacy_budget_template.async_get_collaboration_privacy_budget_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_collaboration_privacy_budget_template_input.GetCollaborationPrivacyBudgetTemplateInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["privacy_budget_template_identifier"] = (
            privacy_budget_template_identifier
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_schema(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        name: "aws_sdk_cleanrooms.types.table_alias.TableAlias",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_schema_output.GetSchemaOutput":
        """<p>Retrieves the schema for a relation within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            name: <p>The name of the relation to retrieve the schema for.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_schema_input.GetSchemaInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_schema_output.GetSchemaOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema.async_get_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_schema_input.GetSchemaInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_schema_analysis_rule(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        name: "aws_sdk_cleanrooms.types.table_alias.TableAlias",
        type: "aws_sdk_cleanrooms.types.analysis_rule_type.AnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_schema_analysis_rule_output.GetSchemaAnalysisRuleOutput":
        """<p>Retrieves a schema analysis rule.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            name: <p>The name of the schema to retrieve the analysis rule for.</p>
            type: <p>The type of the schema analysis rule to retrieve. Schema analysis rules are uniquely identified by a combination of the collaboration, the schema name, and their type.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_schema_analysis_rule_input.GetSchemaAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_schema_analysis_rule_output.GetSchemaAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema_analysis_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema_analysis_rule.async_get_schema_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_schema_analysis_rule_input.GetSchemaAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["name"] = name
        input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_collaboration_analysis_templates(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_analysis_templates_output.ListCollaborationAnalysisTemplatesOutput":
        """<p>Lists analysis templates within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_collaboration_analysis_templates_input.ListCollaborationAnalysisTemplatesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_analysis_templates_output.ListCollaborationAnalysisTemplatesOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_analysis_templates

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_analysis_templates.async_list_collaboration_analysis_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_analysis_templates_input.ListCollaborationAnalysisTemplatesInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    async def list_collaboration_change_requests(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "aws_sdk_cleanrooms.types.change_request_status.ChangeRequestStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_change_requests_output.ListCollaborationChangeRequestsOutput":
        """<p>Lists all change requests for a collaboration with pagination support. Returns change requests sorted by creation time.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            status: <p>A filter to only return change requests with the specified status.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_collaboration_change_requests_input.ListCollaborationChangeRequestsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_change_requests_output.ListCollaborationChangeRequestsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_change_requests

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_change_requests.async_list_collaboration_change_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_change_requests_input.ListCollaborationChangeRequestsInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    async def list_collaboration_configured_audience_model_associations(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_configured_audience_model_associations_output.ListCollaborationConfiguredAudienceModelAssociationsOutput":
        """<p>Lists configured audience model associations within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_collaboration_configured_audience_model_associations_input.ListCollaborationConfiguredAudienceModelAssociationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_configured_audience_model_associations_output.ListCollaborationConfiguredAudienceModelAssociationsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_configured_audience_model_associations

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_configured_audience_model_associations.async_list_collaboration_configured_audience_model_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_configured_audience_model_associations_input.ListCollaborationConfiguredAudienceModelAssociationsInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    async def list_collaboration_id_namespace_associations(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_id_namespace_associations_output.ListCollaborationIdNamespaceAssociationsOutput":
        """<p>Returns a list of the ID namespace associations in a collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the ID namespace associations that you want to retrieve.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.&gt;</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_collaboration_id_namespace_associations_input.ListCollaborationIdNamespaceAssociationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_id_namespace_associations_output.ListCollaborationIdNamespaceAssociationsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_id_namespace_associations

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_id_namespace_associations.async_list_collaboration_id_namespace_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_id_namespace_associations_input.ListCollaborationIdNamespaceAssociationsInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    async def list_collaboration_privacy_budgets(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        privacy_budget_type: "aws_sdk_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        access_budget_resource_arn: Optional[
            "aws_sdk_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_privacy_budgets_output.ListCollaborationPrivacyBudgetsOutput":
        """<p>Returns an array that summarizes each privacy budget in a specified collaboration. The summary includes the collaboration ARN, creation time, creating account, and privacy budget details.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            privacy_budget_type: <p>Specifies the type of the privacy budget.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            access_budget_resource_arn: <p>The Amazon Resource Name (ARN) of the Configured Table Association (ConfiguredTableAssociation) used to filter privacy budgets.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_collaboration_privacy_budgets_input.ListCollaborationPrivacyBudgetsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_privacy_budgets_output.ListCollaborationPrivacyBudgetsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budgets

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budgets.async_list_collaboration_privacy_budgets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_privacy_budgets_input.ListCollaborationPrivacyBudgetsInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["privacy_budget_type"] = privacy_budget_type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if access_budget_resource_arn is not None:
            input_["access_budget_resource_arn"] = access_budget_resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_collaboration_privacy_budget_templates(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_collaboration_privacy_budget_templates_output.ListCollaborationPrivacyBudgetTemplatesOutput":
        """<p>Returns an array that summarizes each privacy budget template in a specified collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_collaboration_privacy_budget_templates_input.ListCollaborationPrivacyBudgetTemplatesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_collaboration_privacy_budget_templates_output.ListCollaborationPrivacyBudgetTemplatesOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budget_templates

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budget_templates.async_list_collaboration_privacy_budget_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_collaboration_privacy_budget_templates_input.ListCollaborationPrivacyBudgetTemplatesInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    async def list_members(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_members_output.ListMembersOutput":
        """<p>Lists all members within a collaboration.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration in which the members are listed.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_members_input.ListMembersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_members_output.ListMembersOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_members

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_members.async_list_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_members_input.ListMembersInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
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

    async def list_schemas(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        schema_type: Optional["aws_sdk_cleanrooms.types.schema_type.SchemaType"] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_schemas_output.ListSchemasOutput":
        """<p>Lists the schemas for relations within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            schema_type: <p>If present, filter schemas by schema type.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_schemas_input.ListSchemasInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_schemas_output.ListSchemasOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_schemas

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_schemas.async_list_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_schemas_input.ListSchemasInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        if schema_type is not None:
            input_["schema_type"] = schema_type
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

    async def update_collaboration_change_request(
        self,
        collaboration_identifier: "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        change_request_identifier: "aws_sdk_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier",
        action: "aws_sdk_cleanrooms.types.change_request_action.ChangeRequestAction",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.update_collaboration_change_request_output.UpdateCollaborationChangeRequestOutput":
        """<p>Updates an existing collaboration change request. This operation allows approval actions for pending change requests in collaborations (APPROVE, DENY, CANCEL, COMMIT).</p> <p>For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the change request to be updated.</p>
            change_request_identifier: <p>The unique identifier of the specific change request to be updated within the collaboration.</p>
            action: <p>The action to perform on the change request. Valid values include APPROVE (approve the change), DENY (reject the change), CANCEL (cancel the request), and COMMIT (commit after the request is approved).</p> <p>For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.update_collaboration_change_request_input.UpdateCollaborationChangeRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.update_collaboration_change_request_output.UpdateCollaborationChangeRequestOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration_change_request

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration_change_request.async_update_collaboration_change_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_collaboration_change_request_input.UpdateCollaborationChangeRequestInput = {}  # type: ignore[typeddict-item]
        input_["collaboration_identifier"] = collaboration_identifier
        input_["change_request_identifier"] = change_request_identifier
        input_["action"] = action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
