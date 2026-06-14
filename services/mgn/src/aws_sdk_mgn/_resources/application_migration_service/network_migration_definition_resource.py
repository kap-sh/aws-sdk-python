from typing import TYPE_CHECKING, Optional

import aws_sdk_mgn._auth._signers
import aws_sdk_mgn._auth._sigv4
from aws_sdk_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mgn.types.code_generation_output_format_types
    import aws_sdk_mgn.types.construct_id
    import aws_sdk_mgn.types.create_network_migration_definition_request
    import aws_sdk_mgn.types.delete_network_migration_definition_request
    import aws_sdk_mgn.types.delete_network_migration_definition_response
    import aws_sdk_mgn.types.get_network_migration_definition_request
    import aws_sdk_mgn.types.get_network_migration_mapper_segment_construct_request
    import aws_sdk_mgn.types.get_network_migration_mapper_segment_construct_response
    import aws_sdk_mgn.types.list_network_migration_analyses_filters
    import aws_sdk_mgn.types.list_network_migration_analyses_request
    import aws_sdk_mgn.types.list_network_migration_analyses_response
    import aws_sdk_mgn.types.list_network_migration_analysis_results_filters
    import aws_sdk_mgn.types.list_network_migration_analysis_results_request
    import aws_sdk_mgn.types.list_network_migration_analysis_results_response
    import aws_sdk_mgn.types.list_network_migration_code_generation_segments_filters
    import aws_sdk_mgn.types.list_network_migration_code_generation_segments_request
    import aws_sdk_mgn.types.list_network_migration_code_generation_segments_response
    import aws_sdk_mgn.types.list_network_migration_code_generations_filters
    import aws_sdk_mgn.types.list_network_migration_code_generations_request
    import aws_sdk_mgn.types.list_network_migration_code_generations_response
    import aws_sdk_mgn.types.list_network_migration_definitions_request
    import aws_sdk_mgn.types.list_network_migration_definitions_request_filters
    import aws_sdk_mgn.types.list_network_migration_definitions_response
    import aws_sdk_mgn.types.list_network_migration_deployed_stacks_request
    import aws_sdk_mgn.types.list_network_migration_deployed_stacks_response
    import aws_sdk_mgn.types.list_network_migration_deployer_job_filters
    import aws_sdk_mgn.types.list_network_migration_deployer_job_response
    import aws_sdk_mgn.types.list_network_migration_deployments_request
    import aws_sdk_mgn.types.list_network_migration_execution_request_filters
    import aws_sdk_mgn.types.list_network_migration_executions_request
    import aws_sdk_mgn.types.list_network_migration_executions_response
    import aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_filters
    import aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_request
    import aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_response
    import aws_sdk_mgn.types.list_network_migration_mapper_segments_filters
    import aws_sdk_mgn.types.list_network_migration_mapper_segments_request
    import aws_sdk_mgn.types.list_network_migration_mapper_segments_response
    import aws_sdk_mgn.types.list_network_migration_mapping_updates_filters
    import aws_sdk_mgn.types.list_network_migration_mapping_updates_request
    import aws_sdk_mgn.types.list_network_migration_mapping_updates_response
    import aws_sdk_mgn.types.list_network_migration_mappings_filters
    import aws_sdk_mgn.types.list_network_migration_mappings_request
    import aws_sdk_mgn.types.list_network_migration_mappings_response
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.network_migration_analysis_job_details
    import aws_sdk_mgn.types.network_migration_analysis_result
    import aws_sdk_mgn.types.network_migration_code_generation_job_details
    import aws_sdk_mgn.types.network_migration_code_generation_segment
    import aws_sdk_mgn.types.network_migration_definition
    import aws_sdk_mgn.types.network_migration_definition_description
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_definition_name
    import aws_sdk_mgn.types.network_migration_definition_summary
    import aws_sdk_mgn.types.network_migration_deployed_stack_details
    import aws_sdk_mgn.types.network_migration_deployer_job_details
    import aws_sdk_mgn.types.network_migration_execution
    import aws_sdk_mgn.types.network_migration_execution_id
    import aws_sdk_mgn.types.network_migration_mapper_segment
    import aws_sdk_mgn.types.network_migration_mapper_segment_construct
    import aws_sdk_mgn.types.network_migration_mapping_job_details
    import aws_sdk_mgn.types.network_migration_mapping_update_job_details
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.scope_tags_map
    import aws_sdk_mgn.types.security_group_mapping_strategy
    import aws_sdk_mgn.types.segment_id
    import aws_sdk_mgn.types.source_configuration_list
    import aws_sdk_mgn.types.start_network_migration_analysis_request
    import aws_sdk_mgn.types.start_network_migration_analysis_response
    import aws_sdk_mgn.types.start_network_migration_code_generation_request
    import aws_sdk_mgn.types.start_network_migration_code_generation_response
    import aws_sdk_mgn.types.start_network_migration_deployer_job_response
    import aws_sdk_mgn.types.start_network_migration_deployment_request
    import aws_sdk_mgn.types.start_network_migration_mapping_request
    import aws_sdk_mgn.types.start_network_migration_mapping_response
    import aws_sdk_mgn.types.start_network_migration_mapping_update_constructs
    import aws_sdk_mgn.types.start_network_migration_mapping_update_request
    import aws_sdk_mgn.types.start_network_migration_mapping_update_response
    import aws_sdk_mgn.types.start_network_migration_mapping_update_segments
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.target_deployment
    import aws_sdk_mgn.types.target_network
    import aws_sdk_mgn.types.target_network_update
    import aws_sdk_mgn.types.target_s3_configuration
    import aws_sdk_mgn.types.target_s3_configuration_update
    import aws_sdk_mgn.types.update_network_migration_definition_request
    import aws_sdk_mgn.types.update_network_migration_mapper_segment_request
    from aws_sdk_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from aws_sdk_mgn._services.mgn import mgnClient, mgnClientConfig


class NetworkMigrationDefinitionResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName",
        target_s3_configuration: "aws_sdk_mgn.types.target_s3_configuration.TargetS3Configuration",
        target_network: "aws_sdk_mgn.types.target_network.TargetNetwork",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        description: Optional[
            "aws_sdk_mgn.types.network_migration_definition_description.NetworkMigrationDefinitionDescription"
        ] = None,
        source_configurations: Optional[
            "aws_sdk_mgn.types.source_configuration_list.SourceConfigurationList"
        ] = None,
        target_deployment: Optional[
            "aws_sdk_mgn.types.target_deployment.TargetDeployment"
        ] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        scope_tags: Optional["aws_sdk_mgn.types.scope_tags_map.ScopeTagsMap"] = None,
    ) -> "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition":
        """<p>Creates a new network migration definition that specifies the source and target network configuration for a migration.</p>

        Args:
            name: <p>The name of the network migration definition.</p>
            description: <p>A description of the network migration definition.</p>
            source_configurations: <p>A list of source configurations for the network migration.</p>
            target_s3_configuration: <p>The S3 configuration for storing the target network artifacts.</p>
            target_network: <p>The target network configuration including topology and CIDR ranges.</p>
            target_deployment: <p>The target deployment configuration for the migrated network.</p>
            tags: <p>Tags to assign to the network migration definition.</p>
            scope_tags: <p>Scope tags for the network migration definition to control access and organization.</p>

        Examples:
            Sample CreateNetworkMigrationDefinition call

            >>> client.create(name='network1', description='network 1 description', target_deployment='SINGLE_ACCOUNT', source_configurations=[{'sourceEnvironment': 'NSX', 'sourceS3Configuration': {'s3Bucket': 'source_bucket', 's3Key': 'source_key', 's3BucketOwner': '012345678901'}}], target_s3_configuration={'s3Bucket': 'target_bucket', 's3BucketOwner': '012345678901'}, target_network={'topology': 'ISOLATED_VPC', 'inboundCidr': '192.168.1.0/24'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.create_network_migration_definition_request.CreateNetworkMigrationDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.create_network_migration_definition

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.create_network_migration_definition.create_network_migration_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.create_network_migration_definition_request.CreateNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if source_configurations is not None:
            input_["source_configurations"] = source_configurations
        input_["target_s3_configuration"] = target_s3_configuration
        input_["target_network"] = target_network
        if target_deployment is not None:
            input_["target_deployment"] = target_deployment
        if tags is not None:
            input_["tags"] = tags
        if scope_tags is not None:
            input_["scope_tags"] = scope_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional[
            "aws_sdk_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName"
        ] = None,
        description: Optional[
            "aws_sdk_mgn.types.network_migration_definition_description.NetworkMigrationDefinitionDescription"
        ] = None,
        source_configurations: Optional[
            "aws_sdk_mgn.types.source_configuration_list.SourceConfigurationList"
        ] = None,
        target_s3_configuration: Optional[
            "aws_sdk_mgn.types.target_s3_configuration_update.TargetS3ConfigurationUpdate"
        ] = None,
        target_network: Optional[
            "aws_sdk_mgn.types.target_network_update.TargetNetworkUpdate"
        ] = None,
        target_deployment: Optional[
            "aws_sdk_mgn.types.target_deployment.TargetDeployment"
        ] = None,
        scope_tags: Optional["aws_sdk_mgn.types.scope_tags_map.ScopeTagsMap"] = None,
    ) -> "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition":
        """<p>Updates an existing network migration definition with new source or target configurations.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to update.</p>
            name: <p>The updated name of the network migration definition.</p>
            description: <p>The updated description of the network migration definition.</p>
            source_configurations: <p>The updated list of source configurations.</p>
            target_s3_configuration: <p>The updated S3 configuration for storing the target network artifacts.</p>
            target_network: <p>The updated target network configuration.</p>
            target_deployment: <p>The updated target deployment configuration.</p>
            scope_tags: <p>The updated scope tags for the network migration definition.</p>

        Examples:
            Sample UpdateNetworkMigrationDefinition call

            >>> client.update(network_migration_definition_id='nmd-01234567891234567', name='network1', description='network 1 description', source_configurations=[{'sourceEnvironment': 'NSX', 'sourceS3Configuration': {'s3Bucket': 'source_bucket', 's3Key': 'source_key', 's3BucketOwner': '012345678901'}}], target_s3_configuration={'s3Bucket': 'target_bucket', 's3BucketOwner': '012345678901'}, target_network={'topology': 'ISOLATED_VPC', 'inboundCidr': '192.168.1.0/24'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.update_network_migration_definition_request.UpdateNetworkMigrationDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.update_network_migration_definition

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.update_network_migration_definition.update_network_migration_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.update_network_migration_definition_request.UpdateNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if source_configurations is not None:
            input_["source_configurations"] = source_configurations
        if target_s3_configuration is not None:
            input_["target_s3_configuration"] = target_s3_configuration
        if target_network is not None:
            input_["target_network"] = target_network
        if target_deployment is not None:
            input_["target_deployment"] = target_deployment
        if scope_tags is not None:
            input_["scope_tags"] = scope_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.delete_network_migration_definition_response.DeleteNetworkMigrationDefinitionResponse":
        """<p>Deletes a network migration definition. This operation removes the migration definition and all associated metadata.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to delete.</p>

        Examples:
            Sample DeleteNetworkMigrationDefinition call

            >>> client.delete(network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.delete_network_migration_definition_request.DeleteNetworkMigrationDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.delete_network_migration_definition_response.DeleteNetworkMigrationDefinitionResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.delete_network_migration_definition

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.delete_network_migration_definition.delete_network_migration_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.delete_network_migration_definition_request.DeleteNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_definitions_request_filters.ListNetworkMigrationDefinitionsRequestFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_definitions_response.ListNetworkMigrationDefinitionsResponse":
        """<p>Lists all network migration definitions in the account, with optional filtering.</p>

        Args:
            filters: <p>Filters to apply when listing network migration definitions.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Examples:
            Sample ListNetworkMigrationDefinitions call

            >>> client.list(filters={'networkMigrationDefinitionIDs': ['nmd-01234567891234567']})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_definitions_request.ListNetworkMigrationDefinitionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_definitions_response.ListNetworkMigrationDefinitionsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_definitions

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_definitions.list_network_migration_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_definitions_request.ListNetworkMigrationDefinitionsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    def get_network_migration_definition(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition":
        """<p>Retrieves the details of a network migration definition including source and target configurations.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to retrieve.</p>

        Examples:
            Sample GetNetworkMigrationDefinition call

            >>> client.get_network_migration_definition(network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.get_network_migration_definition_request.GetNetworkMigrationDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.get_network_migration_definition

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.get_network_migration_definition.get_network_migration_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.get_network_migration_definition_request.GetNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_network_migration_mapper_segment_construct(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        segment_id: "aws_sdk_mgn.types.segment_id.SegmentID",
        construct_id: "aws_sdk_mgn.types.construct_id.ConstructID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.get_network_migration_mapper_segment_construct_response.GetNetworkMigrationMapperSegmentConstructResponse":
        """<p>Retrieves detailed information about a specific construct within a mapper segment, including its properties and configuration data.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            segment_id: <p>The unique identifier of the mapper segment.</p>
            construct_id: <p>The unique identifier of the construct within the segment.</p>

        Examples:
            Sample GetNetworkMigrationMapperSegmentConstruct call

            >>> client.get_network_migration_mapper_segment_construct(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab', construct_id='abc45678-abcd-abcd-efab-012345678abc')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.get_network_migration_mapper_segment_construct_request.GetNetworkMigrationMapperSegmentConstructRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.get_network_migration_mapper_segment_construct_response.GetNetworkMigrationMapperSegmentConstructResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.get_network_migration_mapper_segment_construct

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.get_network_migration_mapper_segment_construct.get_network_migration_mapper_segment_construct(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.get_network_migration_mapper_segment_construct_request.GetNetworkMigrationMapperSegmentConstructRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["segment_id"] = segment_id
        input_["construct_id"] = construct_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_network_migration_analyses(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_analyses_filters.ListNetworkMigrationAnalysesFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_analyses_response.ListNetworkMigrationAnalysesResponse":
        """<p>Lists network migration analysis jobs for a specified execution. Returns information about analysis job status and results.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution to list analyses for.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing analysis jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationAnalyses call

            >>> client.list_network_migration_analyses(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_analyses_request.ListNetworkMigrationAnalysesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_analyses_response.ListNetworkMigrationAnalysesResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_analyses

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_analyses.list_network_migration_analyses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_analyses_request.ListNetworkMigrationAnalysesRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    def list_network_migration_analysis_results(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_analysis_results_filters.ListNetworkMigrationAnalysisResultsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_analysis_results_response.ListNetworkMigrationAnalysisResultsResponse":
        """<p>Lists the results of network migration analyses, showing connectivity and compatibility findings for migrated resources.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing analysis results, such as VPC IDs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationAnalysisResults call

            >>> client.list_network_migration_analysis_results(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_analysis_results_request.ListNetworkMigrationAnalysisResultsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_analysis_results_response.ListNetworkMigrationAnalysisResultsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_analysis_results

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_analysis_results.list_network_migration_analysis_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_analysis_results_request.ListNetworkMigrationAnalysisResultsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    def list_network_migration_code_generations(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_code_generations_filters.ListNetworkMigrationCodeGenerationsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_code_generations_response.ListNetworkMigrationCodeGenerationsResponse":
        """<p>Lists network migration code generation jobs, which convert network mappings into infrastructure-as-code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing code generation jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationCodeGenerations call

            >>> client.list_network_migration_code_generations(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_code_generations_request.ListNetworkMigrationCodeGenerationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_code_generations_response.ListNetworkMigrationCodeGenerationsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_code_generations

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_code_generations.list_network_migration_code_generations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_code_generations_request.ListNetworkMigrationCodeGenerationsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    def list_network_migration_code_generation_segments(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_code_generation_segments_filters.ListNetworkMigrationCodeGenerationSegmentsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_code_generation_segments_response.ListNetworkMigrationCodeGenerationSegmentsResponse":
        """<p>Lists code generation segments, which represent individual infrastructure components generated as code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing code generation segments.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationCodeGenerationSegments call

            >>> client.list_network_migration_code_generation_segments(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_code_generation_segments_request.ListNetworkMigrationCodeGenerationSegmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_code_generation_segments_response.ListNetworkMigrationCodeGenerationSegmentsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_code_generation_segments

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_code_generation_segments.list_network_migration_code_generation_segments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_code_generation_segments_request.ListNetworkMigrationCodeGenerationSegmentsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    def list_network_migration_deployed_stacks(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_deployed_stacks_response.ListNetworkMigrationDeployedStacksResponse":
        """<p>Lists CloudFormation stacks that have been deployed as part of the network migration.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationDeployedStacks call

            >>> client.list_network_migration_deployed_stacks(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_deployed_stacks_request.ListNetworkMigrationDeployedStacksRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_deployed_stacks_response.ListNetworkMigrationDeployedStacksResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_deployed_stacks

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_deployed_stacks.list_network_migration_deployed_stacks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_deployed_stacks_request.ListNetworkMigrationDeployedStacksRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
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

    def list_network_migration_deployments(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_deployer_job_filters.ListNetworkMigrationDeployerJobFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_deployer_job_response.ListNetworkMigrationDeployerJobResponse":
        """<p>Lists network migration deployment jobs and their current status.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing deployment jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationDeployments call

            >>> client.list_network_migration_deployments(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_deployments_request.ListNetworkMigrationDeploymentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_deployer_job_response.ListNetworkMigrationDeployerJobResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_deployments

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_deployments.list_network_migration_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_deployments_request.ListNetworkMigrationDeploymentsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    def list_network_migration_executions(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_execution_request_filters.ListNetworkMigrationExecutionRequestFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_executions_response.ListNetworkMigrationExecutionsResponse":
        """<p>Lists network migration execution instances for a given definition, showing the status and progress of each execution.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to list executions for.</p>
            filters: <p>Filters to apply when listing executions, such as status or execution ID.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Examples:
            Sample ListNetworkMigrationExecutions call

            >>> client.list_network_migration_executions(network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_executions_request.ListNetworkMigrationExecutionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_executions_response.ListNetworkMigrationExecutionsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_executions

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_executions.list_network_migration_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_executions_request.ListNetworkMigrationExecutionsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    def list_network_migration_mapper_segment_constructs(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        segment_id: "aws_sdk_mgn.types.segment_id.SegmentID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_filters.ListNetworkMigrationMapperSegmentConstructsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_response.ListNetworkMigrationMapperSegmentConstructsResponse":
        """<p>Lists constructs within a mapper segment, representing individual infrastructure components like VPCs, subnets, or security groups.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            segment_id: <p>The unique identifier of the segment to list constructs for.</p>
            filters: <p>Filters to apply when listing constructs, such as construct type or ID.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationMapperSegmentConstructs call with properties enabled

            >>> client.list_network_migration_mapper_segment_constructs(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab')
            Sample ListNetworkMigrationMapperSegmentConstructs call with properties disabled (default)

            >>> client.list_network_migration_mapper_segment_constructs(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_request.ListNetworkMigrationMapperSegmentConstructsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_response.ListNetworkMigrationMapperSegmentConstructsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapper_segment_constructs

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapper_segment_constructs.list_network_migration_mapper_segment_constructs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_request.ListNetworkMigrationMapperSegmentConstructsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        input_["segment_id"] = segment_id
        if filters is not None:
            input_["filters"] = filters
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

    def list_network_migration_mapper_segments(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_mapper_segments_filters.ListNetworkMigrationMapperSegmentsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_mapper_segments_response.ListNetworkMigrationMapperSegmentsResponse":
        """<p>Lists mapper segments, which represent logical groupings of network resources to be migrated together.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing segments.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationMapperSegments call

            >>> client.list_network_migration_mapper_segments(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_mapper_segments_request.ListNetworkMigrationMapperSegmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_mapper_segments_response.ListNetworkMigrationMapperSegmentsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapper_segments

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapper_segments.list_network_migration_mapper_segments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_mapper_segments_request.ListNetworkMigrationMapperSegmentsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    def list_network_migration_mappings(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_mappings_filters.ListNetworkMigrationMappingsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_mappings_response.ListNetworkMigrationMappingsResponse":
        """<p>Lists network migration mapping jobs, which analyze and create relationships between source and target network resources.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing mapping jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationMappings call

            >>> client.list_network_migration_mappings(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_mappings_request.ListNetworkMigrationMappingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_mappings_response.ListNetworkMigrationMappingsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_mappings

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_mappings.list_network_migration_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_mappings_request.ListNetworkMigrationMappingsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    def list_network_migration_mapping_updates(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_mapping_updates_filters.ListNetworkMigrationMappingUpdatesFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_mapping_updates_response.ListNetworkMigrationMappingUpdatesResponse":
        """<p>Lists mapping update jobs, which apply customer modifications to the generated network mappings.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing mapping update jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationMappingUpdates call

            >>> client.list_network_migration_mapping_updates(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_network_migration_mapping_updates_request.ListNetworkMigrationMappingUpdatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_network_migration_mapping_updates_response.ListNetworkMigrationMappingUpdatesResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapping_updates

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapping_updates.list_network_migration_mapping_updates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_mapping_updates_request.ListNetworkMigrationMappingUpdatesRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    def start_network_migration_analysis(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.start_network_migration_analysis_response.StartNetworkMigrationAnalysisResponse":
        """<p>Starts a network migration analysis job to evaluate connectivity and compatibility of the migration mappings.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution to analyze.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>

        Examples:
            Sample StartNetworkMigrationAnalysis call

            >>> client.start_network_migration_analysis(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.start_network_migration_analysis_request.StartNetworkMigrationAnalysisRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.start_network_migration_analysis_response.StartNetworkMigrationAnalysisResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_network_migration_analysis

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.start_network_migration_analysis.start_network_migration_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.start_network_migration_analysis_request.StartNetworkMigrationAnalysisRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_network_migration_code_generation(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        code_generation_output_format_types: Optional[
            "aws_sdk_mgn.types.code_generation_output_format_types.CodeGenerationOutputFormatTypes"
        ] = None,
    ) -> "aws_sdk_mgn.types.start_network_migration_code_generation_response.StartNetworkMigrationCodeGenerationResponse":
        """<p>Starts a code generation job to convert network migration mappings into infrastructure-as-code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            code_generation_output_format_types: <p>The output format types for code generation, such as CloudFormation or Terraform.</p>

        Examples:
            Sample StartNetworkMigrationCodeGeneration call

            >>> client.start_network_migration_code_generation(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.start_network_migration_code_generation_request.StartNetworkMigrationCodeGenerationRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.start_network_migration_code_generation_response.StartNetworkMigrationCodeGenerationResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_network_migration_code_generation

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.start_network_migration_code_generation.start_network_migration_code_generation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.start_network_migration_code_generation_request.StartNetworkMigrationCodeGenerationRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if code_generation_output_format_types is not None:
            input_["code_generation_output_format_types"] = (
                code_generation_output_format_types
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_network_migration_deployment(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.start_network_migration_deployer_job_response.StartNetworkMigrationDeployerJobResponse":
        """<p>Starts a deployment job to create the target network infrastructure based on the generated code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>

        Examples:
            Sample StartNetworkMigrationDeployment call

            >>> client.start_network_migration_deployment(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.start_network_migration_deployment_request.StartNetworkMigrationDeploymentRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.start_network_migration_deployer_job_response.StartNetworkMigrationDeployerJobResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_network_migration_deployment

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.start_network_migration_deployment.start_network_migration_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.start_network_migration_deployment_request.StartNetworkMigrationDeploymentRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_network_migration_mapping(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        security_group_mapping_strategy: Optional[
            "aws_sdk_mgn.types.security_group_mapping_strategy.SecurityGroupMappingStrategy"
        ] = None,
    ) -> "aws_sdk_mgn.types.start_network_migration_mapping_response.StartNetworkMigrationMappingResponse":
        """<p>Starts the network migration mapping process for a given network migration execution.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            security_group_mapping_strategy: <p>The security group mapping strategy to use.</p>

        Examples:
            Sample StartNetworkMigrationMapping call

            >>> client.start_network_migration_mapping(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.start_network_migration_mapping_request.StartNetworkMigrationMappingRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.start_network_migration_mapping_response.StartNetworkMigrationMappingResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_network_migration_mapping

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.start_network_migration_mapping.start_network_migration_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.start_network_migration_mapping_request.StartNetworkMigrationMappingRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if security_group_mapping_strategy is not None:
            input_["security_group_mapping_strategy"] = security_group_mapping_strategy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_network_migration_mapping_update(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        constructs: Optional[
            "aws_sdk_mgn.types.start_network_migration_mapping_update_constructs.StartNetworkMigrationMappingUpdateConstructs"
        ] = None,
        segments: Optional[
            "aws_sdk_mgn.types.start_network_migration_mapping_update_segments.StartNetworkMigrationMappingUpdateSegments"
        ] = None,
    ) -> "aws_sdk_mgn.types.start_network_migration_mapping_update_response.StartNetworkMigrationMappingUpdateResponse":
        """<p>Starts a job to apply customer modifications to network migration mappings, such as changing properties.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            constructs: <p>A list of construct updates to apply.</p>
            segments: <p>A list of segment updates to apply.</p>

        Examples:
            Sample StartNetworkMigrationMappingUpdate call

            >>> client.start_network_migration_mapping_update(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', constructs=[{'segmentID': '12345678-abcd-abcd-efab-0123456789ab', 'constructID': 'abc45678-abcd-abcd-efab-012345678abc', 'constructType': 'AWS::EC2::VPC', 'operation': {'update': {'properties': {'CidrBlock': '10.31.0.0/22'}}}}], segments=[{'segmentID': '12345678-abcd-abcd-efab-0123456789ab', 'targetAccount': '234567890123', 'scopeTags': {'key1': 'val1', 'key2': 'val2'}}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.start_network_migration_mapping_update_request.StartNetworkMigrationMappingUpdateRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.start_network_migration_mapping_update_response.StartNetworkMigrationMappingUpdateResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_network_migration_mapping_update

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.start_network_migration_mapping_update.start_network_migration_mapping_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.start_network_migration_mapping_update_request.StartNetworkMigrationMappingUpdateRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if constructs is not None:
            input_["constructs"] = constructs
        if segments is not None:
            input_["segments"] = segments

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_network_migration_mapper_segment(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        segment_id: "aws_sdk_mgn.types.segment_id.SegmentID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        scope_tags: Optional["aws_sdk_mgn.types.scope_tags_map.ScopeTagsMap"] = None,
    ) -> "aws_sdk_mgn.types.network_migration_mapper_segment.NetworkMigrationMapperSegment":
        """<p>Updates a mapper segment's configuration, such as changing its scope tags.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            segment_id: <p>The unique identifier of the segment to update.</p>
            scope_tags: <p>The updated scope tags for the segment.</p>

        Examples:
            Sample UpdateNetworkMigrationMapperSegment call

            >>> client.update_network_migration_mapper_segment(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.update_network_migration_mapper_segment_request.UpdateNetworkMigrationMapperSegmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.network_migration_mapper_segment.NetworkMigrationMapperSegment"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.update_network_migration_mapper_segment

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.update_network_migration_mapper_segment.update_network_migration_mapper_segment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.update_network_migration_mapper_segment_request.UpdateNetworkMigrationMapperSegmentRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["segment_id"] = segment_id
        if scope_tags is not None:
            input_["scope_tags"] = scope_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncNetworkMigrationDefinitionResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName",
        target_s3_configuration: "aws_sdk_mgn.types.target_s3_configuration.TargetS3Configuration",
        target_network: "aws_sdk_mgn.types.target_network.TargetNetwork",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        description: Optional[
            "aws_sdk_mgn.types.network_migration_definition_description.NetworkMigrationDefinitionDescription"
        ] = None,
        source_configurations: Optional[
            "aws_sdk_mgn.types.source_configuration_list.SourceConfigurationList"
        ] = None,
        target_deployment: Optional[
            "aws_sdk_mgn.types.target_deployment.TargetDeployment"
        ] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        scope_tags: Optional["aws_sdk_mgn.types.scope_tags_map.ScopeTagsMap"] = None,
    ) -> "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition":
        """<p>Creates a new network migration definition that specifies the source and target network configuration for a migration.</p>

        Args:
            name: <p>The name of the network migration definition.</p>
            description: <p>A description of the network migration definition.</p>
            source_configurations: <p>A list of source configurations for the network migration.</p>
            target_s3_configuration: <p>The S3 configuration for storing the target network artifacts.</p>
            target_network: <p>The target network configuration including topology and CIDR ranges.</p>
            target_deployment: <p>The target deployment configuration for the migrated network.</p>
            tags: <p>Tags to assign to the network migration definition.</p>
            scope_tags: <p>Scope tags for the network migration definition to control access and organization.</p>

        Examples:
            Sample CreateNetworkMigrationDefinition call

            >>> await client.create(name='network1', description='network 1 description', target_deployment='SINGLE_ACCOUNT', source_configurations=[{'sourceEnvironment': 'NSX', 'sourceS3Configuration': {'s3Bucket': 'source_bucket', 's3Key': 'source_key', 's3BucketOwner': '012345678901'}}], target_s3_configuration={'s3Bucket': 'target_bucket', 's3BucketOwner': '012345678901'}, target_network={'topology': 'ISOLATED_VPC', 'inboundCidr': '192.168.1.0/24'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.create_network_migration_definition_request.CreateNetworkMigrationDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.create_network_migration_definition

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.create_network_migration_definition.async_create_network_migration_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.create_network_migration_definition_request.CreateNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if source_configurations is not None:
            input_["source_configurations"] = source_configurations
        input_["target_s3_configuration"] = target_s3_configuration
        input_["target_network"] = target_network
        if target_deployment is not None:
            input_["target_deployment"] = target_deployment
        if tags is not None:
            input_["tags"] = tags
        if scope_tags is not None:
            input_["scope_tags"] = scope_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        name: Optional[
            "aws_sdk_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName"
        ] = None,
        description: Optional[
            "aws_sdk_mgn.types.network_migration_definition_description.NetworkMigrationDefinitionDescription"
        ] = None,
        source_configurations: Optional[
            "aws_sdk_mgn.types.source_configuration_list.SourceConfigurationList"
        ] = None,
        target_s3_configuration: Optional[
            "aws_sdk_mgn.types.target_s3_configuration_update.TargetS3ConfigurationUpdate"
        ] = None,
        target_network: Optional[
            "aws_sdk_mgn.types.target_network_update.TargetNetworkUpdate"
        ] = None,
        target_deployment: Optional[
            "aws_sdk_mgn.types.target_deployment.TargetDeployment"
        ] = None,
        scope_tags: Optional["aws_sdk_mgn.types.scope_tags_map.ScopeTagsMap"] = None,
    ) -> "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition":
        """<p>Updates an existing network migration definition with new source or target configurations.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to update.</p>
            name: <p>The updated name of the network migration definition.</p>
            description: <p>The updated description of the network migration definition.</p>
            source_configurations: <p>The updated list of source configurations.</p>
            target_s3_configuration: <p>The updated S3 configuration for storing the target network artifacts.</p>
            target_network: <p>The updated target network configuration.</p>
            target_deployment: <p>The updated target deployment configuration.</p>
            scope_tags: <p>The updated scope tags for the network migration definition.</p>

        Examples:
            Sample UpdateNetworkMigrationDefinition call

            >>> await client.update(network_migration_definition_id='nmd-01234567891234567', name='network1', description='network 1 description', source_configurations=[{'sourceEnvironment': 'NSX', 'sourceS3Configuration': {'s3Bucket': 'source_bucket', 's3Key': 'source_key', 's3BucketOwner': '012345678901'}}], target_s3_configuration={'s3Bucket': 'target_bucket', 's3BucketOwner': '012345678901'}, target_network={'topology': 'ISOLATED_VPC', 'inboundCidr': '192.168.1.0/24'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.update_network_migration_definition_request.UpdateNetworkMigrationDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.update_network_migration_definition

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.update_network_migration_definition.async_update_network_migration_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.update_network_migration_definition_request.UpdateNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if source_configurations is not None:
            input_["source_configurations"] = source_configurations
        if target_s3_configuration is not None:
            input_["target_s3_configuration"] = target_s3_configuration
        if target_network is not None:
            input_["target_network"] = target_network
        if target_deployment is not None:
            input_["target_deployment"] = target_deployment
        if scope_tags is not None:
            input_["scope_tags"] = scope_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.delete_network_migration_definition_response.DeleteNetworkMigrationDefinitionResponse":
        """<p>Deletes a network migration definition. This operation removes the migration definition and all associated metadata.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to delete.</p>

        Examples:
            Sample DeleteNetworkMigrationDefinition call

            >>> await client.delete(network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.delete_network_migration_definition_request.DeleteNetworkMigrationDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.delete_network_migration_definition_response.DeleteNetworkMigrationDefinitionResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.delete_network_migration_definition

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.delete_network_migration_definition.async_delete_network_migration_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.delete_network_migration_definition_request.DeleteNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_definitions_request_filters.ListNetworkMigrationDefinitionsRequestFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_definitions_response.ListNetworkMigrationDefinitionsResponse":
        """<p>Lists all network migration definitions in the account, with optional filtering.</p>

        Args:
            filters: <p>Filters to apply when listing network migration definitions.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Examples:
            Sample ListNetworkMigrationDefinitions call

            >>> await client.list(filters={'networkMigrationDefinitionIDs': ['nmd-01234567891234567']})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_definitions_request.ListNetworkMigrationDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_definitions_response.ListNetworkMigrationDefinitionsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_definitions

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_definitions.async_list_network_migration_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_definitions_request.ListNetworkMigrationDefinitionsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    async def get_network_migration_definition(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition":
        """<p>Retrieves the details of a network migration definition including source and target configurations.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to retrieve.</p>

        Examples:
            Sample GetNetworkMigrationDefinition call

            >>> await client.get_network_migration_definition(network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.get_network_migration_definition_request.GetNetworkMigrationDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.network_migration_definition.NetworkMigrationDefinition"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.get_network_migration_definition

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.get_network_migration_definition.async_get_network_migration_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.get_network_migration_definition_request.GetNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_network_migration_mapper_segment_construct(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        segment_id: "aws_sdk_mgn.types.segment_id.SegmentID",
        construct_id: "aws_sdk_mgn.types.construct_id.ConstructID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.get_network_migration_mapper_segment_construct_response.GetNetworkMigrationMapperSegmentConstructResponse":
        """<p>Retrieves detailed information about a specific construct within a mapper segment, including its properties and configuration data.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            segment_id: <p>The unique identifier of the mapper segment.</p>
            construct_id: <p>The unique identifier of the construct within the segment.</p>

        Examples:
            Sample GetNetworkMigrationMapperSegmentConstruct call

            >>> await client.get_network_migration_mapper_segment_construct(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab', construct_id='abc45678-abcd-abcd-efab-012345678abc')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.get_network_migration_mapper_segment_construct_request.GetNetworkMigrationMapperSegmentConstructRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.get_network_migration_mapper_segment_construct_response.GetNetworkMigrationMapperSegmentConstructResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.get_network_migration_mapper_segment_construct

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.get_network_migration_mapper_segment_construct.async_get_network_migration_mapper_segment_construct(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.get_network_migration_mapper_segment_construct_request.GetNetworkMigrationMapperSegmentConstructRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["segment_id"] = segment_id
        input_["construct_id"] = construct_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_network_migration_analyses(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_analyses_filters.ListNetworkMigrationAnalysesFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_analyses_response.ListNetworkMigrationAnalysesResponse":
        """<p>Lists network migration analysis jobs for a specified execution. Returns information about analysis job status and results.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution to list analyses for.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing analysis jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationAnalyses call

            >>> await client.list_network_migration_analyses(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_analyses_request.ListNetworkMigrationAnalysesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_analyses_response.ListNetworkMigrationAnalysesResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_analyses

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_analyses.async_list_network_migration_analyses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_analyses_request.ListNetworkMigrationAnalysesRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_network_migration_analysis_results(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_analysis_results_filters.ListNetworkMigrationAnalysisResultsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_analysis_results_response.ListNetworkMigrationAnalysisResultsResponse":
        """<p>Lists the results of network migration analyses, showing connectivity and compatibility findings for migrated resources.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing analysis results, such as VPC IDs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationAnalysisResults call

            >>> await client.list_network_migration_analysis_results(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_analysis_results_request.ListNetworkMigrationAnalysisResultsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_analysis_results_response.ListNetworkMigrationAnalysisResultsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_analysis_results

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_analysis_results.async_list_network_migration_analysis_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_analysis_results_request.ListNetworkMigrationAnalysisResultsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_network_migration_code_generations(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_code_generations_filters.ListNetworkMigrationCodeGenerationsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_code_generations_response.ListNetworkMigrationCodeGenerationsResponse":
        """<p>Lists network migration code generation jobs, which convert network mappings into infrastructure-as-code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing code generation jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationCodeGenerations call

            >>> await client.list_network_migration_code_generations(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_code_generations_request.ListNetworkMigrationCodeGenerationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_code_generations_response.ListNetworkMigrationCodeGenerationsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_code_generations

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_code_generations.async_list_network_migration_code_generations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_code_generations_request.ListNetworkMigrationCodeGenerationsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_network_migration_code_generation_segments(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_code_generation_segments_filters.ListNetworkMigrationCodeGenerationSegmentsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_code_generation_segments_response.ListNetworkMigrationCodeGenerationSegmentsResponse":
        """<p>Lists code generation segments, which represent individual infrastructure components generated as code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing code generation segments.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationCodeGenerationSegments call

            >>> await client.list_network_migration_code_generation_segments(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_code_generation_segments_request.ListNetworkMigrationCodeGenerationSegmentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_code_generation_segments_response.ListNetworkMigrationCodeGenerationSegmentsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_code_generation_segments

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_code_generation_segments.async_list_network_migration_code_generation_segments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_code_generation_segments_request.ListNetworkMigrationCodeGenerationSegmentsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_network_migration_deployed_stacks(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_deployed_stacks_response.ListNetworkMigrationDeployedStacksResponse":
        """<p>Lists CloudFormation stacks that have been deployed as part of the network migration.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationDeployedStacks call

            >>> await client.list_network_migration_deployed_stacks(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_deployed_stacks_request.ListNetworkMigrationDeployedStacksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_deployed_stacks_response.ListNetworkMigrationDeployedStacksResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_deployed_stacks

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_deployed_stacks.async_list_network_migration_deployed_stacks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_deployed_stacks_request.ListNetworkMigrationDeployedStacksRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
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

    async def list_network_migration_deployments(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_deployer_job_filters.ListNetworkMigrationDeployerJobFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_deployer_job_response.ListNetworkMigrationDeployerJobResponse":
        """<p>Lists network migration deployment jobs and their current status.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing deployment jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationDeployments call

            >>> await client.list_network_migration_deployments(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_deployments_request.ListNetworkMigrationDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_deployer_job_response.ListNetworkMigrationDeployerJobResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_deployments

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_deployments.async_list_network_migration_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_deployments_request.ListNetworkMigrationDeploymentsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_network_migration_executions(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_execution_request_filters.ListNetworkMigrationExecutionRequestFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_executions_response.ListNetworkMigrationExecutionsResponse":
        """<p>Lists network migration execution instances for a given definition, showing the status and progress of each execution.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to list executions for.</p>
            filters: <p>Filters to apply when listing executions, such as status or execution ID.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Examples:
            Sample ListNetworkMigrationExecutions call

            >>> await client.list_network_migration_executions(network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_executions_request.ListNetworkMigrationExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_executions_response.ListNetworkMigrationExecutionsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_executions

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_executions.async_list_network_migration_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_executions_request.ListNetworkMigrationExecutionsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_network_migration_mapper_segment_constructs(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        segment_id: "aws_sdk_mgn.types.segment_id.SegmentID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_filters.ListNetworkMigrationMapperSegmentConstructsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_response.ListNetworkMigrationMapperSegmentConstructsResponse":
        """<p>Lists constructs within a mapper segment, representing individual infrastructure components like VPCs, subnets, or security groups.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            segment_id: <p>The unique identifier of the segment to list constructs for.</p>
            filters: <p>Filters to apply when listing constructs, such as construct type or ID.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationMapperSegmentConstructs call with properties enabled

            >>> await client.list_network_migration_mapper_segment_constructs(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab')
            Sample ListNetworkMigrationMapperSegmentConstructs call with properties disabled (default)

            >>> await client.list_network_migration_mapper_segment_constructs(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_request.ListNetworkMigrationMapperSegmentConstructsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_response.ListNetworkMigrationMapperSegmentConstructsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapper_segment_constructs

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapper_segment_constructs.async_list_network_migration_mapper_segment_constructs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_mapper_segment_constructs_request.ListNetworkMigrationMapperSegmentConstructsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        input_["segment_id"] = segment_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_network_migration_mapper_segments(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_mapper_segments_filters.ListNetworkMigrationMapperSegmentsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_mapper_segments_response.ListNetworkMigrationMapperSegmentsResponse":
        """<p>Lists mapper segments, which represent logical groupings of network resources to be migrated together.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing segments.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationMapperSegments call

            >>> await client.list_network_migration_mapper_segments(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_mapper_segments_request.ListNetworkMigrationMapperSegmentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_mapper_segments_response.ListNetworkMigrationMapperSegmentsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapper_segments

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapper_segments.async_list_network_migration_mapper_segments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_mapper_segments_request.ListNetworkMigrationMapperSegmentsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_network_migration_mappings(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_mappings_filters.ListNetworkMigrationMappingsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_mappings_response.ListNetworkMigrationMappingsResponse":
        """<p>Lists network migration mapping jobs, which analyze and create relationships between source and target network resources.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing mapping jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationMappings call

            >>> await client.list_network_migration_mappings(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_mappings_request.ListNetworkMigrationMappingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_mappings_response.ListNetworkMigrationMappingsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_mappings

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_mappings.async_list_network_migration_mappings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_mappings_request.ListNetworkMigrationMappingsRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    async def list_network_migration_mapping_updates(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_network_migration_mapping_updates_filters.ListNetworkMigrationMappingUpdatesFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_network_migration_mapping_updates_response.ListNetworkMigrationMappingUpdatesResponse":
        """<p>Lists mapping update jobs, which apply customer modifications to the generated network mappings.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing mapping update jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Examples:
            Sample ListNetworkMigrationMappingUpdates call

            >>> await client.list_network_migration_mapping_updates(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_network_migration_mapping_updates_request.ListNetworkMigrationMappingUpdatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_network_migration_mapping_updates_response.ListNetworkMigrationMappingUpdatesResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapping_updates

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_network_migration_mapping_updates.async_list_network_migration_mapping_updates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_network_migration_mapping_updates_request.ListNetworkMigrationMappingUpdatesRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if filters is not None:
            input_["filters"] = filters
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

    async def start_network_migration_analysis(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.start_network_migration_analysis_response.StartNetworkMigrationAnalysisResponse":
        """<p>Starts a network migration analysis job to evaluate connectivity and compatibility of the migration mappings.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution to analyze.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>

        Examples:
            Sample StartNetworkMigrationAnalysis call

            >>> await client.start_network_migration_analysis(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.start_network_migration_analysis_request.StartNetworkMigrationAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.start_network_migration_analysis_response.StartNetworkMigrationAnalysisResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_network_migration_analysis

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.start_network_migration_analysis.async_start_network_migration_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.start_network_migration_analysis_request.StartNetworkMigrationAnalysisRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_network_migration_code_generation(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        code_generation_output_format_types: Optional[
            "aws_sdk_mgn.types.code_generation_output_format_types.CodeGenerationOutputFormatTypes"
        ] = None,
    ) -> "aws_sdk_mgn.types.start_network_migration_code_generation_response.StartNetworkMigrationCodeGenerationResponse":
        """<p>Starts a code generation job to convert network migration mappings into infrastructure-as-code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            code_generation_output_format_types: <p>The output format types for code generation, such as CloudFormation or Terraform.</p>

        Examples:
            Sample StartNetworkMigrationCodeGeneration call

            >>> await client.start_network_migration_code_generation(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.start_network_migration_code_generation_request.StartNetworkMigrationCodeGenerationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.start_network_migration_code_generation_response.StartNetworkMigrationCodeGenerationResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_network_migration_code_generation

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.start_network_migration_code_generation.async_start_network_migration_code_generation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.start_network_migration_code_generation_request.StartNetworkMigrationCodeGenerationRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if code_generation_output_format_types is not None:
            input_["code_generation_output_format_types"] = (
                code_generation_output_format_types
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_network_migration_deployment(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.start_network_migration_deployer_job_response.StartNetworkMigrationDeployerJobResponse":
        """<p>Starts a deployment job to create the target network infrastructure based on the generated code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>

        Examples:
            Sample StartNetworkMigrationDeployment call

            >>> await client.start_network_migration_deployment(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.start_network_migration_deployment_request.StartNetworkMigrationDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.start_network_migration_deployer_job_response.StartNetworkMigrationDeployerJobResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_network_migration_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.start_network_migration_deployment.async_start_network_migration_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.start_network_migration_deployment_request.StartNetworkMigrationDeploymentRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_network_migration_mapping(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        security_group_mapping_strategy: Optional[
            "aws_sdk_mgn.types.security_group_mapping_strategy.SecurityGroupMappingStrategy"
        ] = None,
    ) -> "aws_sdk_mgn.types.start_network_migration_mapping_response.StartNetworkMigrationMappingResponse":
        """<p>Starts the network migration mapping process for a given network migration execution.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            security_group_mapping_strategy: <p>The security group mapping strategy to use.</p>

        Examples:
            Sample StartNetworkMigrationMapping call

            >>> await client.start_network_migration_mapping(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.start_network_migration_mapping_request.StartNetworkMigrationMappingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.start_network_migration_mapping_response.StartNetworkMigrationMappingResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_network_migration_mapping

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.start_network_migration_mapping.async_start_network_migration_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.start_network_migration_mapping_request.StartNetworkMigrationMappingRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if security_group_mapping_strategy is not None:
            input_["security_group_mapping_strategy"] = security_group_mapping_strategy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_network_migration_mapping_update(
        self,
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        constructs: Optional[
            "aws_sdk_mgn.types.start_network_migration_mapping_update_constructs.StartNetworkMigrationMappingUpdateConstructs"
        ] = None,
        segments: Optional[
            "aws_sdk_mgn.types.start_network_migration_mapping_update_segments.StartNetworkMigrationMappingUpdateSegments"
        ] = None,
    ) -> "aws_sdk_mgn.types.start_network_migration_mapping_update_response.StartNetworkMigrationMappingUpdateResponse":
        """<p>Starts a job to apply customer modifications to network migration mappings, such as changing properties.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            constructs: <p>A list of construct updates to apply.</p>
            segments: <p>A list of segment updates to apply.</p>

        Examples:
            Sample StartNetworkMigrationMappingUpdate call

            >>> await client.start_network_migration_mapping_update(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', constructs=[{'segmentID': '12345678-abcd-abcd-efab-0123456789ab', 'constructID': 'abc45678-abcd-abcd-efab-012345678abc', 'constructType': 'AWS::EC2::VPC', 'operation': {'update': {'properties': {'CidrBlock': '10.31.0.0/22'}}}}], segments=[{'segmentID': '12345678-abcd-abcd-efab-0123456789ab', 'targetAccount': '234567890123', 'scopeTags': {'key1': 'val1', 'key2': 'val2'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.start_network_migration_mapping_update_request.StartNetworkMigrationMappingUpdateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.start_network_migration_mapping_update_response.StartNetworkMigrationMappingUpdateResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_network_migration_mapping_update

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.start_network_migration_mapping_update.async_start_network_migration_mapping_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.start_network_migration_mapping_update_request.StartNetworkMigrationMappingUpdateRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["network_migration_definition_id"] = network_migration_definition_id
        if constructs is not None:
            input_["constructs"] = constructs
        if segments is not None:
            input_["segments"] = segments

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_network_migration_mapper_segment(
        self,
        network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        network_migration_execution_id: "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        segment_id: "aws_sdk_mgn.types.segment_id.SegmentID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        scope_tags: Optional["aws_sdk_mgn.types.scope_tags_map.ScopeTagsMap"] = None,
    ) -> "aws_sdk_mgn.types.network_migration_mapper_segment.NetworkMigrationMapperSegment":
        """<p>Updates a mapper segment's configuration, such as changing its scope tags.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            segment_id: <p>The unique identifier of the segment to update.</p>
            scope_tags: <p>The updated scope tags for the segment.</p>

        Examples:
            Sample UpdateNetworkMigrationMapperSegment call

            >>> await client.update_network_migration_mapper_segment(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.update_network_migration_mapper_segment_request.UpdateNetworkMigrationMapperSegmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.network_migration_mapper_segment.NetworkMigrationMapperSegment"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.update_network_migration_mapper_segment

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.update_network_migration_mapper_segment.async_update_network_migration_mapper_segment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.update_network_migration_mapper_segment_request.UpdateNetworkMigrationMapperSegmentRequest = {}  # type: ignore[typeddict-item]
        input_["network_migration_definition_id"] = network_migration_definition_id
        input_["network_migration_execution_id"] = network_migration_execution_id
        input_["segment_id"] = segment_id
        if scope_tags is not None:
            input_["scope_tags"] = scope_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
