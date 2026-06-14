from __future__ import annotations

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
    import aws_sdk_migrationhuborchestrator.types.create_workflow_step_request
    import aws_sdk_migrationhuborchestrator.types.create_workflow_step_response
    import aws_sdk_migrationhuborchestrator.types.delete_workflow_step_request
    import aws_sdk_migrationhuborchestrator.types.delete_workflow_step_response
    import aws_sdk_migrationhuborchestrator.types.get_workflow_step_request
    import aws_sdk_migrationhuborchestrator.types.get_workflow_step_response
    import aws_sdk_migrationhuborchestrator.types.list_workflow_steps_request
    import aws_sdk_migrationhuborchestrator.types.list_workflow_steps_response
    import aws_sdk_migrationhuborchestrator.types.max_results
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_description
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_name
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.retry_workflow_step_request
    import aws_sdk_migrationhuborchestrator.types.retry_workflow_step_response
    import aws_sdk_migrationhuborchestrator.types.step_action_type
    import aws_sdk_migrationhuborchestrator.types.step_description
    import aws_sdk_migrationhuborchestrator.types.step_group_id
    import aws_sdk_migrationhuborchestrator.types.step_id
    import aws_sdk_migrationhuborchestrator.types.step_name
    import aws_sdk_migrationhuborchestrator.types.step_status
    import aws_sdk_migrationhuborchestrator.types.string_list
    import aws_sdk_migrationhuborchestrator.types.update_workflow_step_request
    import aws_sdk_migrationhuborchestrator.types.update_workflow_step_response
    import aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration
    import aws_sdk_migrationhuborchestrator.types.workflow_step_output_list
    import aws_sdk_migrationhuborchestrator.types.workflow_step_summary
    from aws_sdk_migrationhuborchestrator._services.async_migration_hub_orchestrator import (
        AsyncMigrationHubOrchestratorClient,
        AsyncMigrationHubOrchestratorClientConfig,
    )
    from aws_sdk_migrationhuborchestrator._services.migration_hub_orchestrator import (
        MigrationHubOrchestratorClient,
        MigrationHubOrchestratorClientConfig,
    )


class WorkflowStep:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_migrationhuborchestrator.types.migration_workflow_name.MigrationWorkflowName",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_action_type: "aws_sdk_migrationhuborchestrator.types.step_action_type.StepActionType",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
        description: Optional[
            "aws_sdk_migrationhuborchestrator.types.migration_workflow_description.MigrationWorkflowDescription"
        ] = None,
        workflow_step_automation_configuration: Optional[
            "aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration.WorkflowStepAutomationConfiguration"
        ] = None,
        step_target: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        outputs: Optional[
            "aws_sdk_migrationhuborchestrator.types.workflow_step_output_list.WorkflowStepOutputList"
        ] = None,
        previous: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        next: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.create_workflow_step_response.CreateWorkflowStepResponse":
        """<p>Create a step in the migration workflow.</p>

        Args:
            name: <p>The name of the step.</p>
            step_group_id: <p>The ID of the step group.</p>
            workflow_id: <p>The ID of the migration workflow.</p>
            step_action_type: <p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>
            description: <p>The description of the step.</p>
            workflow_step_automation_configuration: <p>The custom script to run tests on source or target environments.</p>
            step_target: <p>The servers on which a step will be run.</p>
            outputs: <p>The key value pairs added for the expected output.</p>
            previous: <p>The previous step.</p>
            next: <p>The next step.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.create_workflow_step_request.CreateWorkflowStepRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.create_workflow_step_response.CreateWorkflowStepResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step.create_workflow_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.create_workflow_step_request.CreateWorkflowStepRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["step_group_id"] = step_group_id
        input_["workflow_id"] = workflow_id
        input_["step_action_type"] = step_action_type
        if description is not None:
            input_["description"] = description
        if workflow_step_automation_configuration is not None:
            input_["workflow_step_automation_configuration"] = (
                workflow_step_automation_configuration
            )
        if step_target is not None:
            input_["step_target"] = step_target
        if outputs is not None:
            input_["outputs"] = outputs
        if previous is not None:
            input_["previous"] = previous
        if next is not None:
            input_["next"] = next

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.get_workflow_step_response.GetWorkflowStepResponse":
        """<p>Get a step in the migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            step_group_id: <p>The ID of the step group.</p>
            id: <p>The ID of the step.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.get_workflow_step_request.GetWorkflowStepRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.get_workflow_step_response.GetWorkflowStepResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step.get_workflow_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.get_workflow_step_request.GetWorkflowStepRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id
        input_["step_group_id"] = step_group_id
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
        name: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_name.StepName"
        ] = None,
        description: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_description.StepDescription"
        ] = None,
        step_action_type: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_action_type.StepActionType"
        ] = None,
        workflow_step_automation_configuration: Optional[
            "aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration.WorkflowStepAutomationConfiguration"
        ] = None,
        step_target: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        outputs: Optional[
            "aws_sdk_migrationhuborchestrator.types.workflow_step_output_list.WorkflowStepOutputList"
        ] = None,
        previous: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        next: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        status: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_status.StepStatus"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.update_workflow_step_response.UpdateWorkflowStepResponse":
        """<p>Update a step in a migration workflow.</p>

        Args:
            id: <p>The ID of the step.</p>
            step_group_id: <p>The ID of the step group.</p>
            workflow_id: <p>The ID of the migration workflow.</p>
            name: <p>The name of the step.</p>
            description: <p>The description of the step.</p>
            step_action_type: <p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>
            workflow_step_automation_configuration: <p>The custom script to run tests on the source and target environments.</p>
            step_target: <p>The servers on which a step will be run.</p>
            outputs: <p>The outputs of a step.</p>
            previous: <p>The previous step.</p>
            next: <p>The next step.</p>
            status: <p>The status of the step.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.update_workflow_step_request.UpdateWorkflowStepRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.update_workflow_step_response.UpdateWorkflowStepResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step.update_workflow_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.update_workflow_step_request.UpdateWorkflowStepRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["step_group_id"] = step_group_id
        input_["workflow_id"] = workflow_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if step_action_type is not None:
            input_["step_action_type"] = step_action_type
        if workflow_step_automation_configuration is not None:
            input_["workflow_step_automation_configuration"] = (
                workflow_step_automation_configuration
            )
        if step_target is not None:
            input_["step_target"] = step_target
        if outputs is not None:
            input_["outputs"] = outputs
        if previous is not None:
            input_["previous"] = previous
        if next is not None:
            input_["next"] = next
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.delete_workflow_step_response.DeleteWorkflowStepResponse":
        """<p>Delete a step in a migration workflow. Pause the workflow to delete a running step.</p>

        Args:
            id: <p>The ID of the step you want to delete.</p>
            step_group_id: <p>The ID of the step group that contains the step you want to delete.</p>
            workflow_id: <p>The ID of the migration workflow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.delete_workflow_step_request.DeleteWorkflowStepRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.delete_workflow_step_response.DeleteWorkflowStepResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step.delete_workflow_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.delete_workflow_step_request.DeleteWorkflowStepRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["step_group_id"] = step_group_id
        input_["workflow_id"] = workflow_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
        next_token: Optional[
            "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.list_workflow_steps_response.ListWorkflowStepsResponse":
        """<p>List the steps in a workflow.</p>

        Args:
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results that can be returned.</p>
            workflow_id: <p>The ID of the migration workflow.</p>
            step_group_id: <p>The ID of the step group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.list_workflow_steps_request.ListWorkflowStepsRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.list_workflow_steps_response.ListWorkflowStepsResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_steps

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_steps.list_workflow_steps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.list_workflow_steps_request.ListWorkflowStepsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["workflow_id"] = workflow_id
        input_["step_group_id"] = step_group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def retry_workflow_step(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.retry_workflow_step_response.RetryWorkflowStepResponse":
        """<p>Retry a failed step in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            step_group_id: <p>The ID of the step group.</p>
            id: <p>The ID of the step.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.retry_workflow_step_request.RetryWorkflowStepRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.retry_workflow_step_response.RetryWorkflowStepResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.retry_workflow_step

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.retry_workflow_step.retry_workflow_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.retry_workflow_step_request.RetryWorkflowStepRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id
        input_["step_group_id"] = step_group_id
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncWorkflowStep:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_migrationhuborchestrator.types.migration_workflow_name.MigrationWorkflowName",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_action_type: "aws_sdk_migrationhuborchestrator.types.step_action_type.StepActionType",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        description: Optional[
            "aws_sdk_migrationhuborchestrator.types.migration_workflow_description.MigrationWorkflowDescription"
        ] = None,
        workflow_step_automation_configuration: Optional[
            "aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration.WorkflowStepAutomationConfiguration"
        ] = None,
        step_target: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        outputs: Optional[
            "aws_sdk_migrationhuborchestrator.types.workflow_step_output_list.WorkflowStepOutputList"
        ] = None,
        previous: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        next: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.create_workflow_step_response.CreateWorkflowStepResponse":
        """<p>Create a step in the migration workflow.</p>

        Args:
            name: <p>The name of the step.</p>
            step_group_id: <p>The ID of the step group.</p>
            workflow_id: <p>The ID of the migration workflow.</p>
            step_action_type: <p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>
            description: <p>The description of the step.</p>
            workflow_step_automation_configuration: <p>The custom script to run tests on source or target environments.</p>
            step_target: <p>The servers on which a step will be run.</p>
            outputs: <p>The key value pairs added for the expected output.</p>
            previous: <p>The previous step.</p>
            next: <p>The next step.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.create_workflow_step_request.CreateWorkflowStepRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.create_workflow_step_response.CreateWorkflowStepResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step.async_create_workflow_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.create_workflow_step_request.CreateWorkflowStepRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["step_group_id"] = step_group_id
        input_["workflow_id"] = workflow_id
        input_["step_action_type"] = step_action_type
        if description is not None:
            input_["description"] = description
        if workflow_step_automation_configuration is not None:
            input_["workflow_step_automation_configuration"] = (
                workflow_step_automation_configuration
            )
        if step_target is not None:
            input_["step_target"] = step_target
        if outputs is not None:
            input_["outputs"] = outputs
        if previous is not None:
            input_["previous"] = previous
        if next is not None:
            input_["next"] = next

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.get_workflow_step_response.GetWorkflowStepResponse":
        """<p>Get a step in the migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            step_group_id: <p>The ID of the step group.</p>
            id: <p>The ID of the step.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.get_workflow_step_request.GetWorkflowStepRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.get_workflow_step_response.GetWorkflowStepResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step.async_get_workflow_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.get_workflow_step_request.GetWorkflowStepRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id
        input_["step_group_id"] = step_group_id
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        name: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_name.StepName"
        ] = None,
        description: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_description.StepDescription"
        ] = None,
        step_action_type: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_action_type.StepActionType"
        ] = None,
        workflow_step_automation_configuration: Optional[
            "aws_sdk_migrationhuborchestrator.types.workflow_step_automation_configuration.WorkflowStepAutomationConfiguration"
        ] = None,
        step_target: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        outputs: Optional[
            "aws_sdk_migrationhuborchestrator.types.workflow_step_output_list.WorkflowStepOutputList"
        ] = None,
        previous: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        next: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        status: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_status.StepStatus"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.update_workflow_step_response.UpdateWorkflowStepResponse":
        """<p>Update a step in a migration workflow.</p>

        Args:
            id: <p>The ID of the step.</p>
            step_group_id: <p>The ID of the step group.</p>
            workflow_id: <p>The ID of the migration workflow.</p>
            name: <p>The name of the step.</p>
            description: <p>The description of the step.</p>
            step_action_type: <p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>
            workflow_step_automation_configuration: <p>The custom script to run tests on the source and target environments.</p>
            step_target: <p>The servers on which a step will be run.</p>
            outputs: <p>The outputs of a step.</p>
            previous: <p>The previous step.</p>
            next: <p>The next step.</p>
            status: <p>The status of the step.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.update_workflow_step_request.UpdateWorkflowStepRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.update_workflow_step_response.UpdateWorkflowStepResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step.async_update_workflow_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.update_workflow_step_request.UpdateWorkflowStepRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["step_group_id"] = step_group_id
        input_["workflow_id"] = workflow_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if step_action_type is not None:
            input_["step_action_type"] = step_action_type
        if workflow_step_automation_configuration is not None:
            input_["workflow_step_automation_configuration"] = (
                workflow_step_automation_configuration
            )
        if step_target is not None:
            input_["step_target"] = step_target
        if outputs is not None:
            input_["outputs"] = outputs
        if previous is not None:
            input_["previous"] = previous
        if next is not None:
            input_["next"] = next
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.delete_workflow_step_response.DeleteWorkflowStepResponse":
        """<p>Delete a step in a migration workflow. Pause the workflow to delete a running step.</p>

        Args:
            id: <p>The ID of the step you want to delete.</p>
            step_group_id: <p>The ID of the step group that contains the step you want to delete.</p>
            workflow_id: <p>The ID of the migration workflow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.delete_workflow_step_request.DeleteWorkflowStepRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.delete_workflow_step_response.DeleteWorkflowStepResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step.async_delete_workflow_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.delete_workflow_step_request.DeleteWorkflowStepRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["step_group_id"] = step_group_id
        input_["workflow_id"] = workflow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        next_token: Optional[
            "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.list_workflow_steps_response.ListWorkflowStepsResponse":
        """<p>List the steps in a workflow.</p>

        Args:
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results that can be returned.</p>
            workflow_id: <p>The ID of the migration workflow.</p>
            step_group_id: <p>The ID of the step group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.list_workflow_steps_request.ListWorkflowStepsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.list_workflow_steps_response.ListWorkflowStepsResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_steps

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_steps.async_list_workflow_steps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.list_workflow_steps_request.ListWorkflowStepsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["workflow_id"] = workflow_id
        input_["step_group_id"] = step_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def retry_workflow_step(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.retry_workflow_step_response.RetryWorkflowStepResponse":
        """<p>Retry a failed step in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            step_group_id: <p>The ID of the step group.</p>
            id: <p>The ID of the step.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.retry_workflow_step_request.RetryWorkflowStepRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.retry_workflow_step_response.RetryWorkflowStepResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.retry_workflow_step

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.retry_workflow_step.async_retry_workflow_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.retry_workflow_step_request.RetryWorkflowStepRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id
        input_["step_group_id"] = step_group_id
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
