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
    import aws_sdk_cleanrooms.types.allowed_column_list
    import aws_sdk_cleanrooms.types.analysis_method
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type
    import aws_sdk_cleanrooms.types.configured_table_identifier
    import aws_sdk_cleanrooms.types.create_configured_table_analysis_rule_input
    import aws_sdk_cleanrooms.types.create_configured_table_analysis_rule_output
    import aws_sdk_cleanrooms.types.create_configured_table_input
    import aws_sdk_cleanrooms.types.create_configured_table_output
    import aws_sdk_cleanrooms.types.delete_configured_table_analysis_rule_input
    import aws_sdk_cleanrooms.types.delete_configured_table_analysis_rule_output
    import aws_sdk_cleanrooms.types.delete_configured_table_input
    import aws_sdk_cleanrooms.types.delete_configured_table_output
    import aws_sdk_cleanrooms.types.display_name
    import aws_sdk_cleanrooms.types.get_configured_table_analysis_rule_input
    import aws_sdk_cleanrooms.types.get_configured_table_analysis_rule_output
    import aws_sdk_cleanrooms.types.get_configured_table_input
    import aws_sdk_cleanrooms.types.get_configured_table_output
    import aws_sdk_cleanrooms.types.list_configured_tables_input
    import aws_sdk_cleanrooms.types.list_configured_tables_output
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.selected_analysis_methods
    import aws_sdk_cleanrooms.types.table_description
    import aws_sdk_cleanrooms.types.table_reference
    import aws_sdk_cleanrooms.types.tag_map
    import aws_sdk_cleanrooms.types.update_configured_table_analysis_rule_input
    import aws_sdk_cleanrooms.types.update_configured_table_analysis_rule_output
    import aws_sdk_cleanrooms.types.update_configured_table_input
    import aws_sdk_cleanrooms.types.update_configured_table_output
    from aws_sdk_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from aws_sdk_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class ConfiguredTableResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_cleanrooms.types.display_name.DisplayName",
        table_reference: "aws_sdk_cleanrooms.types.table_reference.TableReference",
        allowed_columns: "aws_sdk_cleanrooms.types.allowed_column_list.AllowedColumnList",
        analysis_method: "aws_sdk_cleanrooms.types.analysis_method.AnalysisMethod",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.table_description.TableDescription"
        ] = None,
        selected_analysis_methods: Optional[
            "aws_sdk_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
        ] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_cleanrooms.types.create_configured_table_output.CreateConfiguredTableOutput":
        """<p>Creates a new configured table resource.</p>

        Args:
            name: <p>The name of the configured table.</p>
            description: <p>A description for the configured table.</p>
            table_reference: <p>A reference to the table being configured.</p>
            allowed_columns: <p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>
            analysis_method: <p>The analysis method allowed for the configured tables.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>
            selected_analysis_methods: <p> The analysis methods to enable for the configured table. When configured, you must specify at least two analysis methods.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>

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
            req: "OperationRequest[aws_sdk_cleanrooms.types.create_configured_table_input.CreateConfiguredTableInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.create_configured_table_output.CreateConfiguredTableOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table.create_configured_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_configured_table_input.CreateConfiguredTableInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["table_reference"] = table_reference
        input_["allowed_columns"] = allowed_columns
        input_["analysis_method"] = analysis_method
        if selected_analysis_methods is not None:
            input_["selected_analysis_methods"] = selected_analysis_methods
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.get_configured_table_output.GetConfiguredTableOutput"
    ):
        """<p>Retrieves a configured table.</p>

        Args:
            configured_table_identifier: <p>The unique ID for the configured table to retrieve.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_configured_table_input.GetConfiguredTableInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_configured_table_output.GetConfiguredTableOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table.get_configured_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_configured_table_input.GetConfiguredTableInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        name: Optional["aws_sdk_cleanrooms.types.display_name.DisplayName"] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.table_description.TableDescription"
        ] = None,
        table_reference: Optional[
            "aws_sdk_cleanrooms.types.table_reference.TableReference"
        ] = None,
        allowed_columns: Optional[
            "aws_sdk_cleanrooms.types.allowed_column_list.AllowedColumnList"
        ] = None,
        analysis_method: Optional[
            "aws_sdk_cleanrooms.types.analysis_method.AnalysisMethod"
        ] = None,
        selected_analysis_methods: Optional[
            "aws_sdk_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.update_configured_table_output.UpdateConfiguredTableOutput":
        """<p>Updates a configured table.</p>

        Args:
            configured_table_identifier: <p>The identifier for the configured table to update. Currently accepts the configured table ID.</p>
            name: <p>A new name for the configured table.</p>
            description: <p>A new description for the configured table.</p>
            allowed_columns: <p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>
            analysis_method: <p> The analysis method for the configured table.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>
            selected_analysis_methods: <p> The selected analysis methods for the table configuration update.</p>

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
            req: "OperationRequest[aws_sdk_cleanrooms.types.update_configured_table_input.UpdateConfiguredTableInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.update_configured_table_output.UpdateConfiguredTableOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table.update_configured_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_configured_table_input.UpdateConfiguredTableInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if table_reference is not None:
            input_["table_reference"] = table_reference
        if allowed_columns is not None:
            input_["allowed_columns"] = allowed_columns
        if analysis_method is not None:
            input_["analysis_method"] = analysis_method
        if selected_analysis_methods is not None:
            input_["selected_analysis_methods"] = selected_analysis_methods

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_configured_table_output.DeleteConfiguredTableOutput":
        """<p>Deletes a configured table.</p>

        Args:
            configured_table_identifier: <p>The unique ID for the configured table to delete.</p>

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
            req: "OperationRequest[aws_sdk_cleanrooms.types.delete_configured_table_input.DeleteConfiguredTableInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.delete_configured_table_output.DeleteConfiguredTableOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table.delete_configured_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_configured_table_input.DeleteConfiguredTableInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier

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
    ) -> "aws_sdk_cleanrooms.types.list_configured_tables_output.ListConfiguredTablesOutput":
        """<p>Lists configured tables.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_configured_tables_input.ListConfiguredTablesInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_configured_tables_output.ListConfiguredTablesOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_tables

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_tables.list_configured_tables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_configured_tables_input.ListConfiguredTablesInput = {}  # type: ignore[typeddict-item]
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

    def create_configured_table_analysis_rule(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        analysis_rule_policy: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.create_configured_table_analysis_rule_output.CreateConfiguredTableAnalysisRuleOutput":
        """<p>Creates a new analysis rule for a configured table. Currently, only one analysis rule can be created for a given configured table.</p>

        Args:
            configured_table_identifier: <p>The identifier for the configured table to create the analysis rule for. Currently accepts the configured table ID. </p>
            analysis_rule_type: <p>The type of analysis rule.</p>
            analysis_rule_policy: <p>The analysis rule policy that was created for the configured table.</p>

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
            req: "OperationRequest[aws_sdk_cleanrooms.types.create_configured_table_analysis_rule_input.CreateConfiguredTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.create_configured_table_analysis_rule_output.CreateConfiguredTableAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_analysis_rule

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_analysis_rule.create_configured_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_configured_table_analysis_rule_input.CreateConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier
        input_["analysis_rule_type"] = analysis_rule_type
        input_["analysis_rule_policy"] = analysis_rule_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_configured_table_analysis_rule(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_configured_table_analysis_rule_output.DeleteConfiguredTableAnalysisRuleOutput":
        """<p>Deletes a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule type to be deleted. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>

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
            req: "OperationRequest[aws_sdk_cleanrooms.types.delete_configured_table_analysis_rule_input.DeleteConfiguredTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.delete_configured_table_analysis_rule_output.DeleteConfiguredTableAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_analysis_rule

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_analysis_rule.delete_configured_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_configured_table_analysis_rule_input.DeleteConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier
        input_["analysis_rule_type"] = analysis_rule_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_configured_table_analysis_rule(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_configured_table_analysis_rule_output.GetConfiguredTableAnalysisRuleOutput":
        """<p>Retrieves a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table to retrieve. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule to be retrieved. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_configured_table_analysis_rule_input.GetConfiguredTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_configured_table_analysis_rule_output.GetConfiguredTableAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_analysis_rule

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_analysis_rule.get_configured_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_configured_table_analysis_rule_input.GetConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier
        input_["analysis_rule_type"] = analysis_rule_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_configured_table_analysis_rule(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        analysis_rule_policy: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.update_configured_table_analysis_rule_output.UpdateConfiguredTableAnalysisRuleOutput":
        """<p>Updates a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule type to be updated. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>
            analysis_rule_policy: <p>The new analysis rule policy for the configured table analysis rule.</p>

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
            req: "OperationRequest[aws_sdk_cleanrooms.types.update_configured_table_analysis_rule_input.UpdateConfiguredTableAnalysisRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.update_configured_table_analysis_rule_output.UpdateConfiguredTableAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_analysis_rule

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_analysis_rule.update_configured_table_analysis_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_configured_table_analysis_rule_input.UpdateConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier
        input_["analysis_rule_type"] = analysis_rule_type
        input_["analysis_rule_policy"] = analysis_rule_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncConfiguredTableResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_cleanrooms.types.display_name.DisplayName",
        table_reference: "aws_sdk_cleanrooms.types.table_reference.TableReference",
        allowed_columns: "aws_sdk_cleanrooms.types.allowed_column_list.AllowedColumnList",
        analysis_method: "aws_sdk_cleanrooms.types.analysis_method.AnalysisMethod",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.table_description.TableDescription"
        ] = None,
        selected_analysis_methods: Optional[
            "aws_sdk_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
        ] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_cleanrooms.types.create_configured_table_output.CreateConfiguredTableOutput":
        """<p>Creates a new configured table resource.</p>

        Args:
            name: <p>The name of the configured table.</p>
            description: <p>A description for the configured table.</p>
            table_reference: <p>A reference to the table being configured.</p>
            allowed_columns: <p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>
            analysis_method: <p>The analysis method allowed for the configured tables.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>
            selected_analysis_methods: <p> The analysis methods to enable for the configured table. When configured, you must specify at least two analysis methods.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>

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
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.create_configured_table_input.CreateConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.create_configured_table_output.CreateConfiguredTableOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table.async_create_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_configured_table_input.CreateConfiguredTableInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["table_reference"] = table_reference
        input_["allowed_columns"] = allowed_columns
        input_["analysis_method"] = analysis_method
        if selected_analysis_methods is not None:
            input_["selected_analysis_methods"] = selected_analysis_methods
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> (
        "aws_sdk_cleanrooms.types.get_configured_table_output.GetConfiguredTableOutput"
    ):
        """<p>Retrieves a configured table.</p>

        Args:
            configured_table_identifier: <p>The unique ID for the configured table to retrieve.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_configured_table_input.GetConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_configured_table_output.GetConfiguredTableOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table.async_get_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_configured_table_input.GetConfiguredTableInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        name: Optional["aws_sdk_cleanrooms.types.display_name.DisplayName"] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.table_description.TableDescription"
        ] = None,
        table_reference: Optional[
            "aws_sdk_cleanrooms.types.table_reference.TableReference"
        ] = None,
        allowed_columns: Optional[
            "aws_sdk_cleanrooms.types.allowed_column_list.AllowedColumnList"
        ] = None,
        analysis_method: Optional[
            "aws_sdk_cleanrooms.types.analysis_method.AnalysisMethod"
        ] = None,
        selected_analysis_methods: Optional[
            "aws_sdk_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.update_configured_table_output.UpdateConfiguredTableOutput":
        """<p>Updates a configured table.</p>

        Args:
            configured_table_identifier: <p>The identifier for the configured table to update. Currently accepts the configured table ID.</p>
            name: <p>A new name for the configured table.</p>
            description: <p>A new description for the configured table.</p>
            allowed_columns: <p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>
            analysis_method: <p> The analysis method for the configured table.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>
            selected_analysis_methods: <p> The selected analysis methods for the table configuration update.</p>

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
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.update_configured_table_input.UpdateConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.update_configured_table_output.UpdateConfiguredTableOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table.async_update_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_configured_table_input.UpdateConfiguredTableInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if table_reference is not None:
            input_["table_reference"] = table_reference
        if allowed_columns is not None:
            input_["allowed_columns"] = allowed_columns
        if analysis_method is not None:
            input_["analysis_method"] = analysis_method
        if selected_analysis_methods is not None:
            input_["selected_analysis_methods"] = selected_analysis_methods

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_configured_table_output.DeleteConfiguredTableOutput":
        """<p>Deletes a configured table.</p>

        Args:
            configured_table_identifier: <p>The unique ID for the configured table to delete.</p>

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
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.delete_configured_table_input.DeleteConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.delete_configured_table_output.DeleteConfiguredTableOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table.async_delete_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_configured_table_input.DeleteConfiguredTableInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier

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
    ) -> "aws_sdk_cleanrooms.types.list_configured_tables_output.ListConfiguredTablesOutput":
        """<p>Lists configured tables.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_configured_tables_input.ListConfiguredTablesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_configured_tables_output.ListConfiguredTablesOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_tables

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_tables.async_list_configured_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_configured_tables_input.ListConfiguredTablesInput = {}  # type: ignore[typeddict-item]
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

    async def create_configured_table_analysis_rule(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        analysis_rule_policy: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.create_configured_table_analysis_rule_output.CreateConfiguredTableAnalysisRuleOutput":
        """<p>Creates a new analysis rule for a configured table. Currently, only one analysis rule can be created for a given configured table.</p>

        Args:
            configured_table_identifier: <p>The identifier for the configured table to create the analysis rule for. Currently accepts the configured table ID. </p>
            analysis_rule_type: <p>The type of analysis rule.</p>
            analysis_rule_policy: <p>The analysis rule policy that was created for the configured table.</p>

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
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.create_configured_table_analysis_rule_input.CreateConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.create_configured_table_analysis_rule_output.CreateConfiguredTableAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_analysis_rule.async_create_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_configured_table_analysis_rule_input.CreateConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier
        input_["analysis_rule_type"] = analysis_rule_type
        input_["analysis_rule_policy"] = analysis_rule_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_configured_table_analysis_rule(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_configured_table_analysis_rule_output.DeleteConfiguredTableAnalysisRuleOutput":
        """<p>Deletes a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule type to be deleted. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>

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
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.delete_configured_table_analysis_rule_input.DeleteConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.delete_configured_table_analysis_rule_output.DeleteConfiguredTableAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_analysis_rule.async_delete_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_configured_table_analysis_rule_input.DeleteConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier
        input_["analysis_rule_type"] = analysis_rule_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_configured_table_analysis_rule(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_configured_table_analysis_rule_output.GetConfiguredTableAnalysisRuleOutput":
        """<p>Retrieves a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table to retrieve. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule to be retrieved. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>

        Raises:
            aws_sdk_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            aws_sdk_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_configured_table_analysis_rule_input.GetConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_configured_table_analysis_rule_output.GetConfiguredTableAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_analysis_rule.async_get_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_configured_table_analysis_rule_input.GetConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier
        input_["analysis_rule_type"] = analysis_rule_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_configured_table_analysis_rule(
        self,
        configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        analysis_rule_policy: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.update_configured_table_analysis_rule_output.UpdateConfiguredTableAnalysisRuleOutput":
        """<p>Updates a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule type to be updated. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>
            analysis_rule_policy: <p>The new analysis rule policy for the configured table analysis rule.</p>

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
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.update_configured_table_analysis_rule_input.UpdateConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.update_configured_table_analysis_rule_output.UpdateConfiguredTableAnalysisRuleOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_analysis_rule.async_update_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_configured_table_analysis_rule_input.UpdateConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input_["configured_table_identifier"] = configured_table_identifier
        input_["analysis_rule_type"] = analysis_rule_type
        input_["analysis_rule_policy"] = analysis_rule_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
