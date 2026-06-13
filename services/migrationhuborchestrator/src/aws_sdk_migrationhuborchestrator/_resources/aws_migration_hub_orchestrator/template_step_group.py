from typing import TYPE_CHECKING, Optional

import aws_sdk_migrationhuborchestrator._auth._signers
import aws_sdk_migrationhuborchestrator._auth._sigv4
from aws_sdk_migrationhuborchestrator._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.get_template_step_group_request
    import aws_sdk_migrationhuborchestrator.types.get_template_step_group_response
    import aws_sdk_migrationhuborchestrator.types.step_group_id
    import aws_sdk_migrationhuborchestrator.types.template_id
    from aws_sdk_migrationhuborchestrator._services.async_migration_hub_orchestrator import (
        AsyncMigrationHubOrchestratorClient,
        AsyncMigrationHubOrchestratorClientConfig,
    )
    from aws_sdk_migrationhuborchestrator._services.migration_hub_orchestrator import (
        MigrationHubOrchestratorClient,
        MigrationHubOrchestratorClientConfig,
    )


class TemplateStepGroup:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service

    def read(
        self,
        template_id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId",
        id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.get_template_step_group_response.GetTemplateStepGroupResponse":
        """<p>Get a step group in a template.</p>

        Args:
            template_id: <p>The ID of the template.</p>
            id: <p>The ID of the step group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.get_template_step_group_request.GetTemplateStepGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.get_template_step_group_response.GetTemplateStepGroupResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step_group

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step_group.get_template_step_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.get_template_step_group_request.GetTemplateStepGroupRequest = {}  # type: ignore[typeddict-item]
        input["template_id"] = template_id
        input["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTemplateStepGroup:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service

    async def read(
        self,
        template_id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId",
        id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.get_template_step_group_response.GetTemplateStepGroupResponse":
        """<p>Get a step group in a template.</p>

        Args:
            template_id: <p>The ID of the template.</p>
            id: <p>The ID of the step group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.get_template_step_group_request.GetTemplateStepGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.get_template_step_group_response.GetTemplateStepGroupResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step_group

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_template_step_group.async_get_template_step_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_migrationhuborchestrator.types.get_template_step_group_request.GetTemplateStepGroupRequest = {}  # type: ignore[typeddict-item]
        input["template_id"] = template_id
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
