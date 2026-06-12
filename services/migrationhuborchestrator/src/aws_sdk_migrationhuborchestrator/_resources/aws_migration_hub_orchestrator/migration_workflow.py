from typing import Optional, TYPE_CHECKING
from aws_sdk_migrationhuborchestrator._services.async_migration_hub_orchestrator import ensure_async_iterator
from aws_sdk_migrationhuborchestrator._services.migration_hub_orchestrator import ensure_sync_iterator
from aws_sdk_migrationhuborchestrator._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_migrationhuborchestrator._auth._signers
import aws_sdk_migrationhuborchestrator._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_migrationhuborchestrator._services.migration_hub_orchestrator import MigrationHubOrchestratorClient, MigrationHubOrchestratorClientConfig
    from aws_sdk_migrationhuborchestrator._services.async_migration_hub_orchestrator import AsyncMigrationHubOrchestratorClient, AsyncMigrationHubOrchestratorClientConfig
    import aws_sdk_migrationhuborchestrator.types.application_configuration_name
    import aws_sdk_migrationhuborchestrator.types.create_migration_workflow_request
    import aws_sdk_migrationhuborchestrator.types.create_migration_workflow_response
    import aws_sdk_migrationhuborchestrator.types.delete_migration_workflow_request
    import aws_sdk_migrationhuborchestrator.types.delete_migration_workflow_response
    import aws_sdk_migrationhuborchestrator.types.get_migration_workflow_request
    import aws_sdk_migrationhuborchestrator.types.get_migration_workflow_response
    import aws_sdk_migrationhuborchestrator.types.list_migration_workflows_request
    import aws_sdk_migrationhuborchestrator.types.list_migration_workflows_response
    import aws_sdk_migrationhuborchestrator.types.max_results
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_status_enum
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_summary
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.start_migration_workflow_request
    import aws_sdk_migrationhuborchestrator.types.start_migration_workflow_response
    import aws_sdk_migrationhuborchestrator.types.step_input_parameters
    import aws_sdk_migrationhuborchestrator.types.stop_migration_workflow_request
    import aws_sdk_migrationhuborchestrator.types.stop_migration_workflow_response
    import aws_sdk_migrationhuborchestrator.types.string_list
    import aws_sdk_migrationhuborchestrator.types.string_map
    import aws_sdk_migrationhuborchestrator.types.template_id
    import aws_sdk_migrationhuborchestrator.types.update_migration_workflow_request
    import aws_sdk_migrationhuborchestrator.types.update_migration_workflow_response

class MigrationWorkflow:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service
    def create(self, name: str, template_id: str, input_parameters: "aws_sdk_migrationhuborchestrator.types.step_input_parameters.StepInputParameters", *, config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None, description: Optional[str] = None, application_configuration_id: Optional[str] = None, step_targets: Optional["aws_sdk_migrationhuborchestrator.types.string_list.StringList"] = None, tags: Optional["aws_sdk_migrationhuborchestrator.types.string_map.StringMap"] = None) -> "aws_sdk_migrationhuborchestrator.types.create_migration_workflow_response.CreateMigrationWorkflowResponse":
        """<p>Create a workflow to orchestrate your migrations.</p>

        Args:
            name: <p>The name of the migration workflow.</p>
            description: <p>The description of the migration workflow.</p>
            template_id: <p>The ID of the template.</p>
            application_configuration_id: <p>The configuration ID of the application configured in Application Discovery Service.</p>
            input_parameters: <p>The input parameters required to create a migration workflow.</p>
            step_targets: <p>The servers on which a step will be run.</p>
            tags: <p>The tags to add on a migration workflow.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_migrationhuborchestrator.types.create_migration_workflow_request.CreateMigrationWorkflowRequest]') -> OperationResponse["aws_sdk_migrationhuborchestrator.types.create_migration_workflow_response.CreateMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow
            output, http_response = aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow.create_workflow(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.create_migration_workflow_request.CreateMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["template_id"] = template_id
        if application_configuration_id is not None:
            input["application_configuration_id"] = application_configuration_id
        input["input_parameters"] = input_parameters
        if step_targets is not None:
            input["step_targets"] = step_targets
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId", *, config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None) -> "aws_sdk_migrationhuborchestrator.types.get_migration_workflow_response.GetMigrationWorkflowResponse":
        """<p>Get migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_migrationhuborchestrator.types.get_migration_workflow_request.GetMigrationWorkflowRequest]') -> OperationResponse["aws_sdk_migrationhuborchestrator.types.get_migration_workflow_response.GetMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow
            output, http_response = aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow.get_workflow(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.get_migration_workflow_request.GetMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId", *, config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None, name: Optional[str] = None, description: Optional[str] = None, input_parameters: Optional["aws_sdk_migrationhuborchestrator.types.step_input_parameters.StepInputParameters"] = None, step_targets: Optional["aws_sdk_migrationhuborchestrator.types.string_list.StringList"] = None) -> "aws_sdk_migrationhuborchestrator.types.update_migration_workflow_response.UpdateMigrationWorkflowResponse":
        """<p>Update a migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>
            name: <p>The name of the migration workflow.</p>
            description: <p>The description of the migration workflow.</p>
            input_parameters: <p>The input parameters required to update a migration workflow.</p>
            step_targets: <p>The servers on which a step will be run.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_migrationhuborchestrator.types.update_migration_workflow_request.UpdateMigrationWorkflowRequest]') -> OperationResponse["aws_sdk_migrationhuborchestrator.types.update_migration_workflow_response.UpdateMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow
            output, http_response = aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow.update_workflow(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.update_migration_workflow_request.UpdateMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if input_parameters is not None:
            input["input_parameters"] = input_parameters
        if step_targets is not None:
            input["step_targets"] = step_targets

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId", *, config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None) -> "aws_sdk_migrationhuborchestrator.types.delete_migration_workflow_response.DeleteMigrationWorkflowResponse":
        """<p>Delete a migration workflow. You must pause a running workflow in Migration Hub Orchestrator console to delete it.</p>

        Args:
            id: <p>The ID of the migration workflow you want to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_migrationhuborchestrator.types.delete_migration_workflow_request.DeleteMigrationWorkflowRequest]') -> OperationResponse["aws_sdk_migrationhuborchestrator.types.delete_migration_workflow_response.DeleteMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow
            output, http_response = aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow.delete_workflow(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.delete_migration_workflow_request.DeleteMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None, max_results: Optional["aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_migrationhuborchestrator.types.next_token.NextToken"] = None, template_id: Optional["aws_sdk_migrationhuborchestrator.types.template_id.TemplateId"] = None, ads_application_configuration_name: Optional["aws_sdk_migrationhuborchestrator.types.application_configuration_name.ApplicationConfigurationName"] = None, status: Optional["aws_sdk_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"] = None, name: Optional[str] = None) -> "aws_sdk_migrationhuborchestrator.types.list_migration_workflows_response.ListMigrationWorkflowsResponse":
        """<p>List the migration workflows.</p>

        Args:
            max_results: <p>The maximum number of results that can be returned.</p>
            next_token: <p>The pagination token.</p>
            template_id: <p>The ID of the template.</p>
            ads_application_configuration_name: <p>The name of the application configured in Application Discovery Service.</p>
            status: <p>The status of the migration workflow.</p>
            name: <p>The name of the migration workflow.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_migrationhuborchestrator.types.list_migration_workflows_request.ListMigrationWorkflowsRequest]') -> OperationResponse["aws_sdk_migrationhuborchestrator.types.list_migration_workflows_response.ListMigrationWorkflowsResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflows
            output, http_response = aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflows.list_workflows(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.list_migration_workflows_request.ListMigrationWorkflowsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if template_id is not None:
            input["template_id"] = template_id
        if ads_application_configuration_name is not None:
            input["ads_application_configuration_name"] = ads_application_configuration_name
        if status is not None:
            input["status"] = status
        if name is not None:
            input["name"] = name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def start_workflow(self, id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId", *, config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None) -> "aws_sdk_migrationhuborchestrator.types.start_migration_workflow_response.StartMigrationWorkflowResponse":
        """<p>Start a migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_migrationhuborchestrator.types.start_migration_workflow_request.StartMigrationWorkflowRequest]') -> OperationResponse["aws_sdk_migrationhuborchestrator.types.start_migration_workflow_response.StartMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.start_workflow
            output, http_response = aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.start_workflow.start_workflow(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.start_migration_workflow_request.StartMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def stop_workflow(self, id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId", *, config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None) -> "aws_sdk_migrationhuborchestrator.types.stop_migration_workflow_response.StopMigrationWorkflowResponse":
        """<p>Stop an ongoing migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_migrationhuborchestrator.types.stop_migration_workflow_request.StopMigrationWorkflowRequest]') -> OperationResponse["aws_sdk_migrationhuborchestrator.types.stop_migration_workflow_response.StopMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.stop_workflow
            output, http_response = aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.stop_workflow.stop_workflow(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.stop_migration_workflow_request.StopMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncMigrationWorkflow:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service
    async def create(self, name: str, template_id: str, input_parameters: "aws_sdk_migrationhuborchestrator.types.step_input_parameters.StepInputParameters", *, config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None, description: Optional[str] = None, application_configuration_id: Optional[str] = None, step_targets: Optional["aws_sdk_migrationhuborchestrator.types.string_list.StringList"] = None, tags: Optional["aws_sdk_migrationhuborchestrator.types.string_map.StringMap"] = None) -> "aws_sdk_migrationhuborchestrator.types.create_migration_workflow_response.CreateMigrationWorkflowResponse":
        """<p>Create a workflow to orchestrate your migrations.</p>

        Args:
            name: <p>The name of the migration workflow.</p>
            description: <p>The description of the migration workflow.</p>
            template_id: <p>The ID of the template.</p>
            application_configuration_id: <p>The configuration ID of the application configured in Application Discovery Service.</p>
            input_parameters: <p>The input parameters required to create a migration workflow.</p>
            step_targets: <p>The servers on which a step will be run.</p>
            tags: <p>The tags to add on a migration workflow.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.create_migration_workflow_request.CreateMigrationWorkflowRequest]') -> AsyncOperationResponse["aws_sdk_migrationhuborchestrator.types.create_migration_workflow_response.CreateMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow
            output, http_response = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow.async_create_workflow(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.create_migration_workflow_request.CreateMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["template_id"] = template_id
        if application_configuration_id is not None:
            input["application_configuration_id"] = application_configuration_id
        input["input_parameters"] = input_parameters
        if step_targets is not None:
            input["step_targets"] = step_targets
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId", *, config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None) -> "aws_sdk_migrationhuborchestrator.types.get_migration_workflow_response.GetMigrationWorkflowResponse":
        """<p>Get migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.get_migration_workflow_request.GetMigrationWorkflowRequest]') -> AsyncOperationResponse["aws_sdk_migrationhuborchestrator.types.get_migration_workflow_response.GetMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow
            output, http_response = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow.async_get_workflow(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.get_migration_workflow_request.GetMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId", *, config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None, name: Optional[str] = None, description: Optional[str] = None, input_parameters: Optional["aws_sdk_migrationhuborchestrator.types.step_input_parameters.StepInputParameters"] = None, step_targets: Optional["aws_sdk_migrationhuborchestrator.types.string_list.StringList"] = None) -> "aws_sdk_migrationhuborchestrator.types.update_migration_workflow_response.UpdateMigrationWorkflowResponse":
        """<p>Update a migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>
            name: <p>The name of the migration workflow.</p>
            description: <p>The description of the migration workflow.</p>
            input_parameters: <p>The input parameters required to update a migration workflow.</p>
            step_targets: <p>The servers on which a step will be run.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.update_migration_workflow_request.UpdateMigrationWorkflowRequest]') -> AsyncOperationResponse["aws_sdk_migrationhuborchestrator.types.update_migration_workflow_response.UpdateMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow
            output, http_response = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow.async_update_workflow(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.update_migration_workflow_request.UpdateMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if input_parameters is not None:
            input["input_parameters"] = input_parameters
        if step_targets is not None:
            input["step_targets"] = step_targets

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId", *, config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None) -> "aws_sdk_migrationhuborchestrator.types.delete_migration_workflow_response.DeleteMigrationWorkflowResponse":
        """<p>Delete a migration workflow. You must pause a running workflow in Migration Hub Orchestrator console to delete it.</p>

        Args:
            id: <p>The ID of the migration workflow you want to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.delete_migration_workflow_request.DeleteMigrationWorkflowRequest]') -> AsyncOperationResponse["aws_sdk_migrationhuborchestrator.types.delete_migration_workflow_response.DeleteMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow
            output, http_response = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow.async_delete_workflow(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.delete_migration_workflow_request.DeleteMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None, max_results: Optional["aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_migrationhuborchestrator.types.next_token.NextToken"] = None, template_id: Optional["aws_sdk_migrationhuborchestrator.types.template_id.TemplateId"] = None, ads_application_configuration_name: Optional["aws_sdk_migrationhuborchestrator.types.application_configuration_name.ApplicationConfigurationName"] = None, status: Optional["aws_sdk_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"] = None, name: Optional[str] = None) -> "aws_sdk_migrationhuborchestrator.types.list_migration_workflows_response.ListMigrationWorkflowsResponse":
        """<p>List the migration workflows.</p>

        Args:
            max_results: <p>The maximum number of results that can be returned.</p>
            next_token: <p>The pagination token.</p>
            template_id: <p>The ID of the template.</p>
            ads_application_configuration_name: <p>The name of the application configured in Application Discovery Service.</p>
            status: <p>The status of the migration workflow.</p>
            name: <p>The name of the migration workflow.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.list_migration_workflows_request.ListMigrationWorkflowsRequest]') -> AsyncOperationResponse["aws_sdk_migrationhuborchestrator.types.list_migration_workflows_response.ListMigrationWorkflowsResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflows
            output, http_response = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflows.async_list_workflows(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.list_migration_workflows_request.ListMigrationWorkflowsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if template_id is not None:
            input["template_id"] = template_id
        if ads_application_configuration_name is not None:
            input["ads_application_configuration_name"] = ads_application_configuration_name
        if status is not None:
            input["status"] = status
        if name is not None:
            input["name"] = name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def start_workflow(self, id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId", *, config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None) -> "aws_sdk_migrationhuborchestrator.types.start_migration_workflow_response.StartMigrationWorkflowResponse":
        """<p>Start a migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.start_migration_workflow_request.StartMigrationWorkflowRequest]') -> AsyncOperationResponse["aws_sdk_migrationhuborchestrator.types.start_migration_workflow_response.StartMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.start_workflow
            output, http_response = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.start_workflow.async_start_workflow(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.start_migration_workflow_request.StartMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def stop_workflow(self, id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId", *, config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None) -> "aws_sdk_migrationhuborchestrator.types.stop_migration_workflow_response.StopMigrationWorkflowResponse":
        """<p>Stop an ongoing migration workflow.</p>

        Args:
            id: <p>The ID of the migration workflow.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.stop_migration_workflow_request.StopMigrationWorkflowRequest]') -> AsyncOperationResponse["aws_sdk_migrationhuborchestrator.types.stop_migration_workflow_response.StopMigrationWorkflowResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.stop_workflow
            output, http_response = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.stop_workflow.async_stop_workflow(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.stop_migration_workflow_request.StopMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output