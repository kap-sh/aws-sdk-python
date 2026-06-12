from typing import Optional, TYPE_CHECKING
from aws_sdk_migrationhuborchestrator._services.async_migration_hub_orchestrator import ensure_async_iterator
from aws_sdk_migrationhuborchestrator._services.migration_hub_orchestrator import ensure_sync_iterator
from aws_sdk_migrationhuborchestrator._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_migrationhuborchestrator._auth._signers
import aws_sdk_migrationhuborchestrator._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_migrationhuborchestrator._services.migration_hub_orchestrator import MigrationHubOrchestratorClient, MigrationHubOrchestratorClientConfig
    from aws_sdk_migrationhuborchestrator._services.async_migration_hub_orchestrator import AsyncMigrationHubOrchestratorClient, AsyncMigrationHubOrchestratorClientConfig
    import aws_sdk_migrationhuborchestrator.types.get_template_step_request
    import aws_sdk_migrationhuborchestrator.types.get_template_step_response
    import aws_sdk_migrationhuborchestrator.types.list_template_steps_request
    import aws_sdk_migrationhuborchestrator.types.list_template_steps_response
    import aws_sdk_migrationhuborchestrator.types.max_results
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.step_group_id
    import aws_sdk_migrationhuborchestrator.types.step_id
    import aws_sdk_migrationhuborchestrator.types.template_id
    import aws_sdk_migrationhuborchestrator.types.template_step_summary

class TemplateStep:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service
    def read(self, id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId", template_id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId", step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId", *, config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None) -> "aws_sdk_migrationhuborchestrator.types.get_template_step_response.GetTemplateStepResponse":
        """<p>Get a specific step in a template.</p>

        Args:
            id: <p>The ID of the step.</p>
            template_id: <p>The ID of the template.</p>
            step_group_id: <p>The ID of the step group.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_migrationhuborchestrator.types.get_template_step_request.GetTemplateStepRequest]') -> OperationResponse["aws_sdk_migrationhuborchestrator.types.get_template_step_response.GetTemplateStepResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step
            output, http_response = aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step.get_template_step(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.get_template_step_request.GetTemplateStepRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["template_id"] = template_id
        input["step_group_id"] = step_group_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, template_id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId", step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId", *, config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None, max_results: Optional["aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_migrationhuborchestrator.types.next_token.NextToken"] = None) -> "aws_sdk_migrationhuborchestrator.types.list_template_steps_response.ListTemplateStepsResponse":
        """<p>List the steps in a template.</p>

        Args:
            max_results: <p>The maximum number of results that can be returned.</p>
            next_token: <p>The pagination token.</p>
            template_id: <p>The ID of the template.</p>
            step_group_id: <p>The ID of the step group.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_migrationhuborchestrator.types.list_template_steps_request.ListTemplateStepsRequest]') -> OperationResponse["aws_sdk_migrationhuborchestrator.types.list_template_steps_response.ListTemplateStepsResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_steps
            output, http_response = aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_steps.list_template_steps(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.list_template_steps_request.ListTemplateStepsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["template_id"] = template_id
        input["step_group_id"] = step_group_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncTemplateStep:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service
    async def read(self, id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId", template_id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId", step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId", *, config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None) -> "aws_sdk_migrationhuborchestrator.types.get_template_step_response.GetTemplateStepResponse":
        """<p>Get a specific step in a template.</p>

        Args:
            id: <p>The ID of the step.</p>
            template_id: <p>The ID of the template.</p>
            step_group_id: <p>The ID of the step group.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.get_template_step_request.GetTemplateStepRequest]') -> AsyncOperationResponse["aws_sdk_migrationhuborchestrator.types.get_template_step_response.GetTemplateStepResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step
            output, http_response = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step.async_get_template_step(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.get_template_step_request.GetTemplateStepRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["template_id"] = template_id
        input["step_group_id"] = step_group_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, template_id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId", step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId", *, config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None, max_results: Optional["aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_migrationhuborchestrator.types.next_token.NextToken"] = None) -> "aws_sdk_migrationhuborchestrator.types.list_template_steps_response.ListTemplateStepsResponse":
        """<p>List the steps in a template.</p>

        Args:
            max_results: <p>The maximum number of results that can be returned.</p>
            next_token: <p>The pagination token.</p>
            template_id: <p>The ID of the template.</p>
            step_group_id: <p>The ID of the step group.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.list_template_steps_request.ListTemplateStepsRequest]') -> AsyncOperationResponse["aws_sdk_migrationhuborchestrator.types.list_template_steps_response.ListTemplateStepsResponse"]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_steps
            output, http_response = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_steps.async_list_template_steps(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.list_template_steps_request.ListTemplateStepsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["template_id"] = template_id
        input["step_group_id"] = step_group_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output