from typing import Optional, TYPE_CHECKING
from aws_sdk_mgn._services.async_mgn import ensure_async_iterator
from aws_sdk_mgn._services.mgn import ensure_sync_iterator
from aws_sdk_mgn._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_mgn._auth._signers
import aws_sdk_mgn._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_mgn._services.mgn import mgnClient, mgnClientConfig
    from aws_sdk_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    import aws_sdk_mgn.types.connector
    import aws_sdk_mgn.types.connector_id
    import aws_sdk_mgn.types.connector_name
    import aws_sdk_mgn.types.connector_ssm_command_config
    import aws_sdk_mgn.types.create_connector_request
    import aws_sdk_mgn.types.delete_connector_request
    import aws_sdk_mgn.types.list_connectors_request
    import aws_sdk_mgn.types.list_connectors_request_filters
    import aws_sdk_mgn.types.list_connectors_response
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.ssm_instance_id
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.update_connector_request

class ConnectorResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service
    def create(self, name: "aws_sdk_mgn.types.connector_name.ConnectorName", ssm_instance_id: "aws_sdk_mgn.types.ssm_instance_id.SsmInstanceID", *, config_overrides: Optional[mgnClientConfig] = None, tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None, ssm_command_config: Optional["aws_sdk_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"] = None) -> "aws_sdk_mgn.types.connector.Connector":
        """<p>Create Connector.</p>

        Args:
            name: <p>Create Connector request name.</p>
            ssm_instance_id: <p>Create Connector request SSM instance ID.</p>
            tags: <p>Create Connector request tags.</p>
            ssm_command_config: <p>Create Connector request SSM command config.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.create_connector_request.CreateConnectorRequest]') -> OperationResponse["aws_sdk_mgn.types.connector.Connector"]:
            import aws_sdk_mgn._operations.application_migration_service.create_connector
            output, http_response = aws_sdk_mgn._operations.application_migration_service.create_connector.create_connector(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.create_connector_request.CreateConnectorRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["ssm_instance_id"] = ssm_instance_id
        if tags is not None:
            input["tags"] = tags
        if ssm_command_config is not None:
            input["ssm_command_config"] = ssm_command_config

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, connector_id: "aws_sdk_mgn.types.connector_id.ConnectorID", *, config_overrides: Optional[mgnClientConfig] = None, name: Optional["aws_sdk_mgn.types.connector_name.ConnectorName"] = None, ssm_command_config: Optional["aws_sdk_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"] = None) -> "aws_sdk_mgn.types.connector.Connector":
        """<p>Update Connector.</p>

        Args:
            connector_id: <p>Update Connector request connector ID.</p>
            name: <p>Update Connector request name.</p>
            ssm_command_config: <p>Update Connector request SSM command config.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.update_connector_request.UpdateConnectorRequest]') -> OperationResponse["aws_sdk_mgn.types.connector.Connector"]:
            import aws_sdk_mgn._operations.application_migration_service.update_connector
            output, http_response = aws_sdk_mgn._operations.application_migration_service.update_connector.update_connector(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_connector_request.UpdateConnectorRequest = {}  # type: ignore[typeddict-item]
        input["connector_id"] = connector_id
        if name is not None:
            input["name"] = name
        if ssm_command_config is not None:
            input["ssm_command_config"] = ssm_command_config

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, connector_id: "aws_sdk_mgn.types.connector_id.ConnectorID", *, config_overrides: Optional[mgnClientConfig] = None) -> None:
        """<p>Delete Connector.</p>

        Args:
            connector_id: <p>Delete Connector request connector ID.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.delete_connector_request.DeleteConnectorRequest]') -> OperationResponse[None]:
            import aws_sdk_mgn._operations.application_migration_service.delete_connector
            output, http_response = aws_sdk_mgn._operations.application_migration_service.delete_connector.delete_connector(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.delete_connector_request.DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
        input["connector_id"] = connector_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[mgnClientConfig] = None, filters: Optional["aws_sdk_mgn.types.list_connectors_request_filters.ListConnectorsRequestFilters"] = None, max_results: Optional["aws_sdk_mgn.types.max_results_type.MaxResultsType"] = None, next_token: Optional["aws_sdk_mgn.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_mgn.types.list_connectors_response.ListConnectorsResponse":
        """<p>List Connectors.</p>

        Args:
            filters: <p>List Connectors Request filters.</p>
            max_results: <p>List Connectors Request max results.</p>
            next_token: <p>List Connectors Request next token.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.list_connectors_request.ListConnectorsRequest]') -> OperationResponse["aws_sdk_mgn.types.list_connectors_response.ListConnectorsResponse"]:
            import aws_sdk_mgn._operations.application_migration_service.list_connectors
            output, http_response = aws_sdk_mgn._operations.application_migration_service.list_connectors.list_connectors(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.list_connectors_request.ListConnectorsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncConnectorResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service
    async def create(self, name: "aws_sdk_mgn.types.connector_name.ConnectorName", ssm_instance_id: "aws_sdk_mgn.types.ssm_instance_id.SsmInstanceID", *, config_overrides: Optional[AsyncmgnClientConfig] = None, tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None, ssm_command_config: Optional["aws_sdk_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"] = None) -> "aws_sdk_mgn.types.connector.Connector":
        """<p>Create Connector.</p>

        Args:
            name: <p>Create Connector request name.</p>
            ssm_instance_id: <p>Create Connector request SSM instance ID.</p>
            tags: <p>Create Connector request tags.</p>
            ssm_command_config: <p>Create Connector request SSM command config.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.create_connector_request.CreateConnectorRequest]') -> AsyncOperationResponse["aws_sdk_mgn.types.connector.Connector"]:
            import aws_sdk_mgn._operations.application_migration_service.create_connector
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.create_connector.async_create_connector(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.create_connector_request.CreateConnectorRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["ssm_instance_id"] = ssm_instance_id
        if tags is not None:
            input["tags"] = tags
        if ssm_command_config is not None:
            input["ssm_command_config"] = ssm_command_config

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, connector_id: "aws_sdk_mgn.types.connector_id.ConnectorID", *, config_overrides: Optional[AsyncmgnClientConfig] = None, name: Optional["aws_sdk_mgn.types.connector_name.ConnectorName"] = None, ssm_command_config: Optional["aws_sdk_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"] = None) -> "aws_sdk_mgn.types.connector.Connector":
        """<p>Update Connector.</p>

        Args:
            connector_id: <p>Update Connector request connector ID.</p>
            name: <p>Update Connector request name.</p>
            ssm_command_config: <p>Update Connector request SSM command config.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.update_connector_request.UpdateConnectorRequest]') -> AsyncOperationResponse["aws_sdk_mgn.types.connector.Connector"]:
            import aws_sdk_mgn._operations.application_migration_service.update_connector
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.update_connector.async_update_connector(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_connector_request.UpdateConnectorRequest = {}  # type: ignore[typeddict-item]
        input["connector_id"] = connector_id
        if name is not None:
            input["name"] = name
        if ssm_command_config is not None:
            input["ssm_command_config"] = ssm_command_config

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, connector_id: "aws_sdk_mgn.types.connector_id.ConnectorID", *, config_overrides: Optional[AsyncmgnClientConfig] = None) -> None:
        """<p>Delete Connector.</p>

        Args:
            connector_id: <p>Delete Connector request connector ID.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.delete_connector_request.DeleteConnectorRequest]') -> AsyncOperationResponse[None]:
            import aws_sdk_mgn._operations.application_migration_service.delete_connector
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.delete_connector.async_delete_connector(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.delete_connector_request.DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
        input["connector_id"] = connector_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncmgnClientConfig] = None, filters: Optional["aws_sdk_mgn.types.list_connectors_request_filters.ListConnectorsRequestFilters"] = None, max_results: Optional["aws_sdk_mgn.types.max_results_type.MaxResultsType"] = None, next_token: Optional["aws_sdk_mgn.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_mgn.types.list_connectors_response.ListConnectorsResponse":
        """<p>List Connectors.</p>

        Args:
            filters: <p>List Connectors Request filters.</p>
            max_results: <p>List Connectors Request max results.</p>
            next_token: <p>List Connectors Request next token.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.list_connectors_request.ListConnectorsRequest]') -> AsyncOperationResponse["aws_sdk_mgn.types.list_connectors_response.ListConnectorsResponse"]:
            import aws_sdk_mgn._operations.application_migration_service.list_connectors
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.list_connectors.async_list_connectors(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.list_connectors_request.ListConnectorsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output