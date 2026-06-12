from typing import Optional, TYPE_CHECKING
from aws_sdk_cleanrooms._services.async_clean_rooms import ensure_async_iterator
from aws_sdk_cleanrooms._services.clean_rooms import ensure_sync_iterator
from aws_sdk_cleanrooms._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_cleanrooms._auth._signers
import aws_sdk_cleanrooms._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_cleanrooms._services.clean_rooms import CleanRoomsClient, CleanRoomsClientConfig
    from aws_sdk_cleanrooms._services.async_clean_rooms import AsyncCleanRoomsClient, AsyncCleanRoomsClientConfig
    import aws_sdk_cleanrooms.types.create_id_mapping_table_input
    import aws_sdk_cleanrooms.types.create_id_mapping_table_output
    import aws_sdk_cleanrooms.types.delete_id_mapping_table_input
    import aws_sdk_cleanrooms.types.delete_id_mapping_table_output
    import aws_sdk_cleanrooms.types.get_id_mapping_table_input
    import aws_sdk_cleanrooms.types.get_id_mapping_table_output
    import aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config
    import aws_sdk_cleanrooms.types.id_mapping_table_summary
    import aws_sdk_cleanrooms.types.job_type
    import aws_sdk_cleanrooms.types.kms_key_arn
    import aws_sdk_cleanrooms.types.list_id_mapping_tables_input
    import aws_sdk_cleanrooms.types.list_id_mapping_tables_output
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.populate_id_mapping_table_input
    import aws_sdk_cleanrooms.types.populate_id_mapping_table_output
    import aws_sdk_cleanrooms.types.resource_alias
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.tag_map
    import aws_sdk_cleanrooms.types.update_id_mapping_table_input
    import aws_sdk_cleanrooms.types.update_id_mapping_table_output
    import aws_sdk_cleanrooms.types.uuid

class IdMappingTableResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service
    def create(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", name: "aws_sdk_cleanrooms.types.resource_alias.ResourceAlias", input_reference_config: "aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config.IdMappingTableInputReferenceConfig", *, config_overrides: Optional[CleanRoomsClientConfig] = None, description: Optional["aws_sdk_cleanrooms.types.resource_description.ResourceDescription"] = None, tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None, kms_key_arn: Optional["aws_sdk_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None) -> "aws_sdk_cleanrooms.types.create_id_mapping_table_output.CreateIdMappingTableOutput":
        """<p>Creates an ID mapping table.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table.</p>
            name: <p>A name for the ID mapping table.</p>
            description: <p>A description of the ID mapping table.</p>
            input_reference_config: <p>The input reference configuration needed to create the ID mapping table.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key. This value is used to encrypt the mapping table data that is stored by Clean Rooms.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.create_id_mapping_table_input.CreateIdMappingTableInput]') -> OperationResponse["aws_sdk_cleanrooms.types.create_id_mapping_table_output.CreateIdMappingTableOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_mapping_table
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_mapping_table.create_id_mapping_table(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.create_id_mapping_table_input.CreateIdMappingTableInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["input_reference_config"] = input_reference_config
        if tags is not None:
            input["tags"] = tags
        if kms_key_arn is not None:
            input["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, id_mapping_table_identifier: "aws_sdk_cleanrooms.types.uuid.UUID", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[CleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.get_id_mapping_table_output.GetIdMappingTableOutput":
        """<p>Retrieves an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table identifier that you want to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.get_id_mapping_table_input.GetIdMappingTableInput]') -> OperationResponse["aws_sdk_cleanrooms.types.get_id_mapping_table_output.GetIdMappingTableOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_mapping_table
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_mapping_table.get_id_mapping_table(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.get_id_mapping_table_input.GetIdMappingTableInput = {}  # type: ignore[typeddict-item]
        input["id_mapping_table_identifier"] = id_mapping_table_identifier
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, id_mapping_table_identifier: "aws_sdk_cleanrooms.types.uuid.UUID", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[CleanRoomsClientConfig] = None, description: Optional["aws_sdk_cleanrooms.types.resource_description.ResourceDescription"] = None, kms_key_arn: Optional["aws_sdk_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None) -> "aws_sdk_cleanrooms.types.update_id_mapping_table_output.UpdateIdMappingTableOutput":
        """<p>Provides the details that are necessary to update an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to update.</p>
            description: <p>A new description for the ID mapping table.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.update_id_mapping_table_input.UpdateIdMappingTableInput]') -> OperationResponse["aws_sdk_cleanrooms.types.update_id_mapping_table_output.UpdateIdMappingTableOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_mapping_table
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_mapping_table.update_id_mapping_table(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.update_id_mapping_table_input.UpdateIdMappingTableInput = {}  # type: ignore[typeddict-item]
        input["id_mapping_table_identifier"] = id_mapping_table_identifier
        input["membership_identifier"] = membership_identifier
        if description is not None:
            input["description"] = description
        if kms_key_arn is not None:
            input["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, id_mapping_table_identifier: "aws_sdk_cleanrooms.types.uuid.UUID", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[CleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.delete_id_mapping_table_output.DeleteIdMappingTableOutput":
        """<p>Deletes an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to delete.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.delete_id_mapping_table_input.DeleteIdMappingTableInput]') -> OperationResponse["aws_sdk_cleanrooms.types.delete_id_mapping_table_output.DeleteIdMappingTableOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_mapping_table
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_mapping_table.delete_id_mapping_table(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.delete_id_mapping_table_input.DeleteIdMappingTableInput = {}  # type: ignore[typeddict-item]
        input["id_mapping_table_identifier"] = id_mapping_table_identifier
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[CleanRoomsClientConfig] = None, next_token: Optional["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"] = None, max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None) -> "aws_sdk_cleanrooms.types.list_id_mapping_tables_output.ListIdMappingTablesOutput":
        """<p>Returns a list of ID mapping tables.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping tables that you want to view.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.list_id_mapping_tables_input.ListIdMappingTablesInput]') -> OperationResponse["aws_sdk_cleanrooms.types.list_id_mapping_tables_output.ListIdMappingTablesOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_mapping_tables
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_mapping_tables.list_id_mapping_tables(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.list_id_mapping_tables_input.ListIdMappingTablesInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def populate_id_mapping_table(self, id_mapping_table_identifier: "aws_sdk_cleanrooms.types.uuid.UUID", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[CleanRoomsClientConfig] = None, job_type: Optional["aws_sdk_cleanrooms.types.job_type.JobType"] = None) -> "aws_sdk_cleanrooms.types.populate_id_mapping_table_output.PopulateIdMappingTableOutput":
        """<p>Defines the information that's necessary to populate an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to populate.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to populate.</p>
            job_type: <p>The job type of the rule-based ID mapping job. Valid values include:</p> <p> <code>INCREMENTAL</code>: Processes only new or changed data since the last job run. This is the default job type if the ID mapping workflow was created in Entity Resolution with <code>incrementalRunConfig</code> specified.</p> <p> <code>BATCH</code>: Processes all data from the input source, regardless of previous job runs. This is the default job type if the ID mapping workflow was created in Entity Resolution but <code>incrementalRunConfig</code> wasn't specified.</p> <p> <code>DELETE_ONLY</code>: Processes only deletion requests from <code>BatchDeleteUniqueId</code>, which is set in Entity Resolution.</p> <p>For more information about <code>incrementalRunConfig</code> and <code>BatchDeleteUniqueId</code>, see the <a href=\"https://docs.aws.amazon.com/entityresolution/latest/apireference/Welcome.html\">Entity Resolution API Reference</a>.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanrooms.types.populate_id_mapping_table_input.PopulateIdMappingTableInput]') -> OperationResponse["aws_sdk_cleanrooms.types.populate_id_mapping_table_output.PopulateIdMappingTableOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_id_mapping_table
            output, http_response = aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_id_mapping_table.populate_id_mapping_table(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.populate_id_mapping_table_input.PopulateIdMappingTableInput = {}  # type: ignore[typeddict-item]
        input["id_mapping_table_identifier"] = id_mapping_table_identifier
        input["membership_identifier"] = membership_identifier
        if job_type is not None:
            input["job_type"] = job_type

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncIdMappingTableResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service
    async def create(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", name: "aws_sdk_cleanrooms.types.resource_alias.ResourceAlias", input_reference_config: "aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config.IdMappingTableInputReferenceConfig", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None, description: Optional["aws_sdk_cleanrooms.types.resource_description.ResourceDescription"] = None, tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None, kms_key_arn: Optional["aws_sdk_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None) -> "aws_sdk_cleanrooms.types.create_id_mapping_table_output.CreateIdMappingTableOutput":
        """<p>Creates an ID mapping table.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table.</p>
            name: <p>A name for the ID mapping table.</p>
            description: <p>A description of the ID mapping table.</p>
            input_reference_config: <p>The input reference configuration needed to create the ID mapping table.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key. This value is used to encrypt the mapping table data that is stored by Clean Rooms.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.create_id_mapping_table_input.CreateIdMappingTableInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.create_id_mapping_table_output.CreateIdMappingTableOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_mapping_table
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_mapping_table.async_create_id_mapping_table(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.create_id_mapping_table_input.CreateIdMappingTableInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["input_reference_config"] = input_reference_config
        if tags is not None:
            input["tags"] = tags
        if kms_key_arn is not None:
            input["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, id_mapping_table_identifier: "aws_sdk_cleanrooms.types.uuid.UUID", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.get_id_mapping_table_output.GetIdMappingTableOutput":
        """<p>Retrieves an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table identifier that you want to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.get_id_mapping_table_input.GetIdMappingTableInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.get_id_mapping_table_output.GetIdMappingTableOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_mapping_table
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_mapping_table.async_get_id_mapping_table(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.get_id_mapping_table_input.GetIdMappingTableInput = {}  # type: ignore[typeddict-item]
        input["id_mapping_table_identifier"] = id_mapping_table_identifier
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, id_mapping_table_identifier: "aws_sdk_cleanrooms.types.uuid.UUID", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None, description: Optional["aws_sdk_cleanrooms.types.resource_description.ResourceDescription"] = None, kms_key_arn: Optional["aws_sdk_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None) -> "aws_sdk_cleanrooms.types.update_id_mapping_table_output.UpdateIdMappingTableOutput":
        """<p>Provides the details that are necessary to update an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to update.</p>
            description: <p>A new description for the ID mapping table.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.update_id_mapping_table_input.UpdateIdMappingTableInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.update_id_mapping_table_output.UpdateIdMappingTableOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_mapping_table
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_mapping_table.async_update_id_mapping_table(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.update_id_mapping_table_input.UpdateIdMappingTableInput = {}  # type: ignore[typeddict-item]
        input["id_mapping_table_identifier"] = id_mapping_table_identifier
        input["membership_identifier"] = membership_identifier
        if description is not None:
            input["description"] = description
        if kms_key_arn is not None:
            input["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, id_mapping_table_identifier: "aws_sdk_cleanrooms.types.uuid.UUID", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None) -> "aws_sdk_cleanrooms.types.delete_id_mapping_table_output.DeleteIdMappingTableOutput":
        """<p>Deletes an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to delete.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.delete_id_mapping_table_input.DeleteIdMappingTableInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.delete_id_mapping_table_output.DeleteIdMappingTableOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_mapping_table
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_mapping_table.async_delete_id_mapping_table(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.delete_id_mapping_table_input.DeleteIdMappingTableInput = {}  # type: ignore[typeddict-item]
        input["id_mapping_table_identifier"] = id_mapping_table_identifier
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None, next_token: Optional["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"] = None, max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None) -> "aws_sdk_cleanrooms.types.list_id_mapping_tables_output.ListIdMappingTablesOutput":
        """<p>Returns a list of ID mapping tables.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping tables that you want to view.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.list_id_mapping_tables_input.ListIdMappingTablesInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.list_id_mapping_tables_output.ListIdMappingTablesOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_mapping_tables
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_mapping_tables.async_list_id_mapping_tables(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.list_id_mapping_tables_input.ListIdMappingTablesInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def populate_id_mapping_table(self, id_mapping_table_identifier: "aws_sdk_cleanrooms.types.uuid.UUID", membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier", *, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None, job_type: Optional["aws_sdk_cleanrooms.types.job_type.JobType"] = None) -> "aws_sdk_cleanrooms.types.populate_id_mapping_table_output.PopulateIdMappingTableOutput":
        """<p>Defines the information that's necessary to populate an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to populate.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to populate.</p>
            job_type: <p>The job type of the rule-based ID mapping job. Valid values include:</p> <p> <code>INCREMENTAL</code>: Processes only new or changed data since the last job run. This is the default job type if the ID mapping workflow was created in Entity Resolution with <code>incrementalRunConfig</code> specified.</p> <p> <code>BATCH</code>: Processes all data from the input source, regardless of previous job runs. This is the default job type if the ID mapping workflow was created in Entity Resolution but <code>incrementalRunConfig</code> wasn't specified.</p> <p> <code>DELETE_ONLY</code>: Processes only deletion requests from <code>BatchDeleteUniqueId</code>, which is set in Entity Resolution.</p> <p>For more information about <code>incrementalRunConfig</code> and <code>BatchDeleteUniqueId</code>, see the <a href=\"https://docs.aws.amazon.com/entityresolution/latest/apireference/Welcome.html\">Entity Resolution API Reference</a>.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanrooms.types.populate_id_mapping_table_input.PopulateIdMappingTableInput]') -> AsyncOperationResponse["aws_sdk_cleanrooms.types.populate_id_mapping_table_output.PopulateIdMappingTableOutput"]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_id_mapping_table
            output, http_response = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_id_mapping_table.async_populate_id_mapping_table(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.populate_id_mapping_table_input.PopulateIdMappingTableInput = {}  # type: ignore[typeddict-item]
        input["id_mapping_table_identifier"] = id_mapping_table_identifier
        input["membership_identifier"] = membership_identifier
        if job_type is not None:
            input["job_type"] = job_type

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output