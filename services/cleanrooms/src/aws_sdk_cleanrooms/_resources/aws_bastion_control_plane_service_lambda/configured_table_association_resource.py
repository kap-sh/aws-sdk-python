from typing import Optional, TYPE_CHECKING
from aws_sdk_cleanrooms._services.async_clean_rooms import ensure_async_iterator
from aws_sdk_cleanrooms._services.clean_rooms import ensure_sync_iterator
from aws_sdk_cleanrooms._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_cleanrooms._auth._signers
import aws_sdk_cleanrooms._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_cleanrooms._services.clean_rooms import CleanRoomsClient, CleanRoomsClientConfig
    from aws_sdk_cleanrooms._services.async_clean_rooms import AsyncCleanRoomsClient, AsyncCleanRoomsClientConfig
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type
    import aws_sdk_cleanrooms.types.configured_table_association_identifier
    import aws_sdk_cleanrooms.types.configured_table_identifier
    import aws_sdk_cleanrooms.types.create_configured_table_association_analysis_rule_input
    import aws_sdk_cleanrooms.types.create_configured_table_association_analysis_rule_output
    import aws_sdk_cleanrooms.types.create_configured_table_association_input
    import aws_sdk_cleanrooms.types.create_configured_table_association_output
    import aws_sdk_cleanrooms.types.delete_configured_table_association_analysis_rule_input
    import aws_sdk_cleanrooms.types.delete_configured_table_association_analysis_rule_output
    import aws_sdk_cleanrooms.types.delete_configured_table_association_input
    import aws_sdk_cleanrooms.types.delete_configured_table_association_output
    import aws_sdk_cleanrooms.types.get_configured_table_association_analysis_rule_input
    import aws_sdk_cleanrooms.types.get_configured_table_association_analysis_rule_output
    import aws_sdk_cleanrooms.types.get_configured_table_association_input
    import aws_sdk_cleanrooms.types.get_configured_table_association_output
    import aws_sdk_cleanrooms.types.list_configured_table_associations_input
    import aws_sdk_cleanrooms.types.list_configured_table_associations_output
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.role_arn
    import aws_sdk_cleanrooms.types.table_alias
    import aws_sdk_cleanrooms.types.table_description
    import aws_sdk_cleanrooms.types.tag_map
    import aws_sdk_cleanrooms.types.update_configured_table_association_analysis_rule_input
    import aws_sdk_cleanrooms.types.update_configured_table_association_analysis_rule_output
    import aws_sdk_cleanrooms.types.update_configured_table_association_input
    import aws_sdk_cleanrooms.types.update_configured_table_association_output

class ConfiguredTableAssociationResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service
    def create(self, name: "aws_sdk_cleanrooms.types.table_alias.TableAlias", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier", role_arn: "aws_sdk_cleanrooms.types.role_arn.RoleArn", *, config_overrides: Optional[CleanRoomsClientConfig] = None, description: Optional["aws_sdk_cleanrooms.types.table_description.TableDescription"] = None, tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None) -> "aws_sdk_cleanrooms.types.create_configured_table_association_output.CreateConfiguredTableAssociationOutput":
        """<p>Creates a configured table association. A configured table association links a configured table with a collaboration.</p>

        Args:
            name: <p>The name of the configured table association. This name is used to query the underlying configured table.</p>
            description: <p>A description for the configured table association.</p>
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The configured table is associated to the collaboration that this membership belongs to. Currently accepts a membership ID.</p>
            configured_table_identifier: <p>A unique identifier for the configured table to be associated to. Currently accepts a configured table ID.</p>
            role_arn: <p>The service will assume this role to access catalog metadata and query the table.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.create_configured_table_association_input.CreateConfiguredTableAssociationInput]') -> OperationResponse["aws_sdk_cleanrooms.types.create_configured_table_association_output.CreateConfiguredTableAssociationOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association.create_configured_table_association(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.create_configured_table_association_input.CreateConfiguredTableAssociationInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["membership_identifier"] = membership_identifier
        input["configured_table_identifier"] = configured_table_identifier
        input["role_arn"] = role_arn
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[CleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.get_configured_table_association_output.GetConfiguredTableAssociationOutput":
        """<p>Retrieves a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique ID for the configured table association to retrieve. Currently accepts the configured table ID.</p>
            membership_identifier: <p>A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.get_configured_table_association_input.GetConfiguredTableAssociationInput]') -> OperationResponse["aws_sdk_cleanrooms.types.get_configured_table_association_output.GetConfiguredTableAssociationOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association.get_configured_table_association(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.get_configured_table_association_input.GetConfiguredTableAssociationInput = {}  # type: ignore[typeddict-item]
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[CleanRoomsClientConfig] = None, description: Optional["aws_sdk_cleanrooms.types.table_description.TableDescription"] = None, role_arn: Optional["aws_sdk_cleanrooms.types.role_arn.RoleArn"] = None) -> "aws_sdk_cleanrooms.types.update_configured_table_association_output.UpdateConfiguredTableAssociationOutput":
        """<p>Updates a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique identifier for the configured table association to update. Currently accepts the configured table association ID.</p>
            membership_identifier: <p>The unique ID for the membership that the configured table association belongs to.</p>
            description: <p>A new description for the configured table association.</p>
            role_arn: <p>The service will assume this role to access catalog metadata and query the table.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.update_configured_table_association_input.UpdateConfiguredTableAssociationInput]') -> OperationResponse["aws_sdk_cleanrooms.types.update_configured_table_association_output.UpdateConfiguredTableAssociationOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association.update_configured_table_association(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.update_configured_table_association_input.UpdateConfiguredTableAssociationInput = {}  # type: ignore[typeddict-item]
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["membership_identifier"] = membership_identifier
        if description is not None:
            input["description"] = description
        if role_arn is not None:
            input["role_arn"] = role_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[CleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.delete_configured_table_association_output.DeleteConfiguredTableAssociationOutput":
        """<p>Deletes a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique ID for the configured table association to be deleted. Currently accepts the configured table ID.</p>
            membership_identifier: <p>A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.delete_configured_table_association_input.DeleteConfiguredTableAssociationInput]') -> OperationResponse["aws_sdk_cleanrooms.types.delete_configured_table_association_output.DeleteConfiguredTableAssociationOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association.delete_configured_table_association(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.delete_configured_table_association_input.DeleteConfiguredTableAssociationInput = {}  # type: ignore[typeddict-item]
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[CleanRoomsClientConfig] = None, next_token: Optional["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"] = None, max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None) -> "aws_sdk_cleanrooms.types.list_configured_table_associations_output.ListConfiguredTableAssociationsOutput":
        """<p>Lists configured table associations for a membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership to list configured table associations for. Currently accepts the membership ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.list_configured_table_associations_input.ListConfiguredTableAssociationsInput]') -> OperationResponse["aws_sdk_cleanrooms.types.list_configured_table_associations_output.ListConfiguredTableAssociationsOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_table_associations
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_table_associations.list_configured_table_associations(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.list_configured_table_associations_input.ListConfiguredTableAssociationsInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def create_configured_table_association_analysis_rule(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType", analysis_rule_policy: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy", *, config_overrides: Optional[CleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.create_configured_table_association_analysis_rule_output.CreateConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Creates a new analysis rule for an associated configured table.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The unique ID for the configured table association. Currently accepts the configured table association ID.</p>
            analysis_rule_type: <p> The type of analysis rule.</p>
            analysis_rule_policy: <p>The analysis rule policy that was created for the configured table association.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.create_configured_table_association_analysis_rule_input.CreateConfiguredTableAssociationAnalysisRuleInput]') -> OperationResponse["aws_sdk_cleanrooms.types.create_configured_table_association_analysis_rule_output.CreateConfiguredTableAssociationAnalysisRuleOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association_analysis_rule
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association_analysis_rule.create_configured_table_association_analysis_rule(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.create_configured_table_association_analysis_rule_input.CreateConfiguredTableAssociationAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["analysis_rule_type"] = analysis_rule_type
        input["analysis_rule_policy"] = analysis_rule_policy

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete_configured_table_association_analysis_rule(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType", *, config_overrides: Optional[CleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.delete_configured_table_association_analysis_rule_output.DeleteConfiguredTableAssociationAnalysisRuleOutput":
        """<p>Deletes an analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p>The identiﬁer for the conﬁgured table association that's related to the analysis rule that you want to delete.</p>
            analysis_rule_type: <p>The type of the analysis rule that you want to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.delete_configured_table_association_analysis_rule_input.DeleteConfiguredTableAssociationAnalysisRuleInput]') -> OperationResponse["aws_sdk_cleanrooms.types.delete_configured_table_association_analysis_rule_output.DeleteConfiguredTableAssociationAnalysisRuleOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association_analysis_rule
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association_analysis_rule.delete_configured_table_association_analysis_rule(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.delete_configured_table_association_analysis_rule_input.DeleteConfiguredTableAssociationAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["analysis_rule_type"] = analysis_rule_type

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_configured_table_association_analysis_rule(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType", *, config_overrides: Optional[CleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.get_configured_table_association_analysis_rule_output.GetConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Retrieves the analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The identiﬁer for the conﬁgured table association that's related to the analysis rule.</p>
            analysis_rule_type: <p> The type of analysis rule that you want to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.get_configured_table_association_analysis_rule_input.GetConfiguredTableAssociationAnalysisRuleInput]') -> OperationResponse["aws_sdk_cleanrooms.types.get_configured_table_association_analysis_rule_output.GetConfiguredTableAssociationAnalysisRuleOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association_analysis_rule
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association_analysis_rule.get_configured_table_association_analysis_rule(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.get_configured_table_association_analysis_rule_input.GetConfiguredTableAssociationAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["analysis_rule_type"] = analysis_rule_type

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update_configured_table_association_analysis_rule(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType", analysis_rule_policy: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy", *, config_overrides: Optional[CleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.update_configured_table_association_analysis_rule_output.UpdateConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Updates the analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The identifier for the configured table association to update.</p>
            analysis_rule_type: <p> The analysis rule type that you want to update.</p>
            analysis_rule_policy: <p> The updated analysis rule policy for the conﬁgured table association.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.update_configured_table_association_analysis_rule_input.UpdateConfiguredTableAssociationAnalysisRuleInput]') -> OperationResponse["aws_sdk_cleanrooms.types.update_configured_table_association_analysis_rule_output.UpdateConfiguredTableAssociationAnalysisRuleOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association_analysis_rule
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association_analysis_rule.update_configured_table_association_analysis_rule(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.update_configured_table_association_analysis_rule_input.UpdateConfiguredTableAssociationAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["analysis_rule_type"] = analysis_rule_type
        input["analysis_rule_policy"] = analysis_rule_policy

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncConfiguredTableAssociationResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service
    async def create(self, name: "aws_sdk_cleanrooms.types.table_alias.TableAlias", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", configured_table_identifier: "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier", role_arn: "aws_sdk_cleanrooms.types.role_arn.RoleArn", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None, description: Optional["aws_sdk_cleanrooms.types.table_description.TableDescription"] = None, tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None) -> "aws_sdk_cleanrooms.types.create_configured_table_association_output.CreateConfiguredTableAssociationOutput":
        """<p>Creates a configured table association. A configured table association links a configured table with a collaboration.</p>

        Args:
            name: <p>The name of the configured table association. This name is used to query the underlying configured table.</p>
            description: <p>A description for the configured table association.</p>
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The configured table is associated to the collaboration that this membership belongs to. Currently accepts a membership ID.</p>
            configured_table_identifier: <p>A unique identifier for the configured table to be associated to. Currently accepts a configured table ID.</p>
            role_arn: <p>The service will assume this role to access catalog metadata and query the table.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.create_configured_table_association_input.CreateConfiguredTableAssociationInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.create_configured_table_association_output.CreateConfiguredTableAssociationOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association.async_create_configured_table_association(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.create_configured_table_association_input.CreateConfiguredTableAssociationInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["membership_identifier"] = membership_identifier
        input["configured_table_identifier"] = configured_table_identifier
        input["role_arn"] = role_arn
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.get_configured_table_association_output.GetConfiguredTableAssociationOutput":
        """<p>Retrieves a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique ID for the configured table association to retrieve. Currently accepts the configured table ID.</p>
            membership_identifier: <p>A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.get_configured_table_association_input.GetConfiguredTableAssociationInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.get_configured_table_association_output.GetConfiguredTableAssociationOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association.async_get_configured_table_association(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.get_configured_table_association_input.GetConfiguredTableAssociationInput = {}  # type: ignore[typeddict-item]
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None, description: Optional["aws_sdk_cleanrooms.types.table_description.TableDescription"] = None, role_arn: Optional["aws_sdk_cleanrooms.types.role_arn.RoleArn"] = None) -> "aws_sdk_cleanrooms.types.update_configured_table_association_output.UpdateConfiguredTableAssociationOutput":
        """<p>Updates a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique identifier for the configured table association to update. Currently accepts the configured table association ID.</p>
            membership_identifier: <p>The unique ID for the membership that the configured table association belongs to.</p>
            description: <p>A new description for the configured table association.</p>
            role_arn: <p>The service will assume this role to access catalog metadata and query the table.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.update_configured_table_association_input.UpdateConfiguredTableAssociationInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.update_configured_table_association_output.UpdateConfiguredTableAssociationOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association.async_update_configured_table_association(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.update_configured_table_association_input.UpdateConfiguredTableAssociationInput = {}  # type: ignore[typeddict-item]
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["membership_identifier"] = membership_identifier
        if description is not None:
            input["description"] = description
        if role_arn is not None:
            input["role_arn"] = role_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.delete_configured_table_association_output.DeleteConfiguredTableAssociationOutput":
        """<p>Deletes a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique ID for the configured table association to be deleted. Currently accepts the configured table ID.</p>
            membership_identifier: <p>A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.delete_configured_table_association_input.DeleteConfiguredTableAssociationInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.delete_configured_table_association_output.DeleteConfiguredTableAssociationOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association.async_delete_configured_table_association(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.delete_configured_table_association_input.DeleteConfiguredTableAssociationInput = {}  # type: ignore[typeddict-item]
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None, next_token: Optional["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"] = None, max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None) -> "aws_sdk_cleanrooms.types.list_configured_table_associations_output.ListConfiguredTableAssociationsOutput":
        """<p>Lists configured table associations for a membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership to list configured table associations for. Currently accepts the membership ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.list_configured_table_associations_input.ListConfiguredTableAssociationsInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.list_configured_table_associations_output.ListConfiguredTableAssociationsOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_table_associations
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_table_associations.async_list_configured_table_associations(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.list_configured_table_associations_input.ListConfiguredTableAssociationsInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def create_configured_table_association_analysis_rule(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType", analysis_rule_policy: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.create_configured_table_association_analysis_rule_output.CreateConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Creates a new analysis rule for an associated configured table.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The unique ID for the configured table association. Currently accepts the configured table association ID.</p>
            analysis_rule_type: <p> The type of analysis rule.</p>
            analysis_rule_policy: <p>The analysis rule policy that was created for the configured table association.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.create_configured_table_association_analysis_rule_input.CreateConfiguredTableAssociationAnalysisRuleInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.create_configured_table_association_analysis_rule_output.CreateConfiguredTableAssociationAnalysisRuleOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association_analysis_rule
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association_analysis_rule.async_create_configured_table_association_analysis_rule(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.create_configured_table_association_analysis_rule_input.CreateConfiguredTableAssociationAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["analysis_rule_type"] = analysis_rule_type
        input["analysis_rule_policy"] = analysis_rule_policy

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete_configured_table_association_analysis_rule(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.delete_configured_table_association_analysis_rule_output.DeleteConfiguredTableAssociationAnalysisRuleOutput":
        """<p>Deletes an analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p>The identiﬁer for the conﬁgured table association that's related to the analysis rule that you want to delete.</p>
            analysis_rule_type: <p>The type of the analysis rule that you want to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.delete_configured_table_association_analysis_rule_input.DeleteConfiguredTableAssociationAnalysisRuleInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.delete_configured_table_association_analysis_rule_output.DeleteConfiguredTableAssociationAnalysisRuleOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association_analysis_rule
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association_analysis_rule.async_delete_configured_table_association_analysis_rule(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.delete_configured_table_association_analysis_rule_input.DeleteConfiguredTableAssociationAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["analysis_rule_type"] = analysis_rule_type

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_configured_table_association_analysis_rule(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.get_configured_table_association_analysis_rule_output.GetConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Retrieves the analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The identiﬁer for the conﬁgured table association that's related to the analysis rule.</p>
            analysis_rule_type: <p> The type of analysis rule that you want to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.get_configured_table_association_analysis_rule_input.GetConfiguredTableAssociationAnalysisRuleInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.get_configured_table_association_analysis_rule_output.GetConfiguredTableAssociationAnalysisRuleOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association_analysis_rule
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association_analysis_rule.async_get_configured_table_association_analysis_rule(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.get_configured_table_association_analysis_rule_input.GetConfiguredTableAssociationAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["analysis_rule_type"] = analysis_rule_type

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update_configured_table_association_analysis_rule(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier", analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType", analysis_rule_policy: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.update_configured_table_association_analysis_rule_output.UpdateConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Updates the analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The identifier for the configured table association to update.</p>
            analysis_rule_type: <p> The analysis rule type that you want to update.</p>
            analysis_rule_policy: <p> The updated analysis rule policy for the conﬁgured table association.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.update_configured_table_association_analysis_rule_input.UpdateConfiguredTableAssociationAnalysisRuleInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.update_configured_table_association_analysis_rule_output.UpdateConfiguredTableAssociationAnalysisRuleOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association_analysis_rule
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association_analysis_rule.async_update_configured_table_association_analysis_rule(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.update_configured_table_association_analysis_rule_input.UpdateConfiguredTableAssociationAnalysisRuleInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["configured_table_association_identifier"] = configured_table_association_identifier
        input["analysis_rule_type"] = analysis_rule_type
        input["analysis_rule_policy"] = analysis_rule_policy

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output