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
    import aws_sdk_migrationhuborchestrator.types.create_workflow_step_group_request
    import aws_sdk_migrationhuborchestrator.types.create_workflow_step_group_response
    import aws_sdk_migrationhuborchestrator.types.delete_workflow_step_group_request
    import aws_sdk_migrationhuborchestrator.types.delete_workflow_step_group_response
    import aws_sdk_migrationhuborchestrator.types.get_workflow_step_group_request
    import aws_sdk_migrationhuborchestrator.types.get_workflow_step_group_response
    import aws_sdk_migrationhuborchestrator.types.list_workflow_step_groups_request
    import aws_sdk_migrationhuborchestrator.types.list_workflow_step_groups_response
    import aws_sdk_migrationhuborchestrator.types.max_results
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.step_group_description
    import aws_sdk_migrationhuborchestrator.types.step_group_id
    import aws_sdk_migrationhuborchestrator.types.step_group_name
    import aws_sdk_migrationhuborchestrator.types.string_list
    import aws_sdk_migrationhuborchestrator.types.update_workflow_step_group_request
    import aws_sdk_migrationhuborchestrator.types.update_workflow_step_group_response
    import aws_sdk_migrationhuborchestrator.types.workflow_step_group_summary
    from aws_sdk_migrationhuborchestrator._services.async_migration_hub_orchestrator import (
        AsyncMigrationHubOrchestratorClient,
        AsyncMigrationHubOrchestratorClientConfig,
    )
    from aws_sdk_migrationhuborchestrator._services.migration_hub_orchestrator import (
        MigrationHubOrchestratorClient,
        MigrationHubOrchestratorClientConfig,
    )


class WorkflowStepGroup:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service

    def create(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        name: "aws_sdk_migrationhuborchestrator.types.step_group_name.StepGroupName",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
        description: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_group_description.StepGroupDescription"
        ] = None,
        next: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        previous: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.create_workflow_step_group_response.CreateWorkflowStepGroupResponse":
        """<p>Create a step group in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow that will contain the step group.</p>
            name: <p>The name of the step group.</p>
            description: <p>The description of the step group.</p>
            next: <p>The next step group.</p>
            previous: <p>The previous step group.</p>

        Raises:
            aws_sdk_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            aws_sdk_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.create_workflow_step_group_request.CreateWorkflowStepGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.create_workflow_step_group_response.CreateWorkflowStepGroupResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step_group

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step_group.create_workflow_step_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.create_workflow_step_group_request.CreateWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if next is not None:
            input_["next"] = next
        if previous is not None:
            input_["previous"] = previous

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.get_workflow_step_group_response.GetWorkflowStepGroupResponse":
        """<p>Get the step group of a migration workflow.</p>

        Args:
            id: <p>The ID of the step group.</p>
            workflow_id: <p>The ID of the migration workflow.</p>

        Raises:
            aws_sdk_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            aws_sdk_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            aws_sdk_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.get_workflow_step_group_request.GetWorkflowStepGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.get_workflow_step_group_response.GetWorkflowStepGroupResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step_group

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step_group.get_workflow_step_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.get_workflow_step_group_request.GetWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["workflow_id"] = workflow_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
        name: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_group_name.StepGroupName"
        ] = None,
        description: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_group_description.StepGroupDescription"
        ] = None,
        next: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        previous: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.update_workflow_step_group_response.UpdateWorkflowStepGroupResponse":
        """<p>Update the step group in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            id: <p>The ID of the step group.</p>
            name: <p>The name of the step group.</p>
            description: <p>The description of the step group.</p>
            next: <p>The next step group.</p>
            previous: <p>The previous step group.</p>

        Raises:
            aws_sdk_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            aws_sdk_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            aws_sdk_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.update_workflow_step_group_request.UpdateWorkflowStepGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.update_workflow_step_group_response.UpdateWorkflowStepGroupResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step_group

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step_group.update_workflow_step_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.update_workflow_step_group_request.UpdateWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id
        input_["id"] = id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if next is not None:
            input_["next"] = next
        if previous is not None:
            input_["previous"] = previous

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.delete_workflow_step_group_response.DeleteWorkflowStepGroupResponse":
        """<p>Delete a step group in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            id: <p>The ID of the step group you want to delete.</p>

        Raises:
            aws_sdk_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            aws_sdk_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            aws_sdk_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.delete_workflow_step_group_request.DeleteWorkflowStepGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.delete_workflow_step_group_response.DeleteWorkflowStepGroupResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step_group

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step_group.delete_workflow_step_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.delete_workflow_step_group_request.DeleteWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
        next_token: Optional[
            "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.list_workflow_step_groups_response.ListWorkflowStepGroupsResponse":
        """<p>List the step groups in a migration workflow.</p>

        Args:
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results that can be returned.</p>
            workflow_id: <p>The ID of the migration workflow.</p>

        Raises:
            aws_sdk_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            aws_sdk_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            aws_sdk_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.list_workflow_step_groups_request.ListWorkflowStepGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.list_workflow_step_groups_response.ListWorkflowStepGroupsResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_step_groups

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_step_groups.list_workflow_step_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.list_workflow_step_groups_request.ListWorkflowStepGroupsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["workflow_id"] = workflow_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncWorkflowStepGroup:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service

    async def create(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        name: "aws_sdk_migrationhuborchestrator.types.step_group_name.StepGroupName",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        description: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_group_description.StepGroupDescription"
        ] = None,
        next: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        previous: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.create_workflow_step_group_response.CreateWorkflowStepGroupResponse":
        """<p>Create a step group in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow that will contain the step group.</p>
            name: <p>The name of the step group.</p>
            description: <p>The description of the step group.</p>
            next: <p>The next step group.</p>
            previous: <p>The previous step group.</p>

        Raises:
            aws_sdk_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            aws_sdk_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.create_workflow_step_group_request.CreateWorkflowStepGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.create_workflow_step_group_response.CreateWorkflowStepGroupResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step_group

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.create_workflow_step_group.async_create_workflow_step_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.create_workflow_step_group_request.CreateWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if next is not None:
            input_["next"] = next
        if previous is not None:
            input_["previous"] = previous

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.get_workflow_step_group_response.GetWorkflowStepGroupResponse":
        """<p>Get the step group of a migration workflow.</p>

        Args:
            id: <p>The ID of the step group.</p>
            workflow_id: <p>The ID of the migration workflow.</p>

        Raises:
            aws_sdk_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            aws_sdk_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            aws_sdk_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.get_workflow_step_group_request.GetWorkflowStepGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.get_workflow_step_group_response.GetWorkflowStepGroupResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step_group

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.get_workflow_step_group.async_get_workflow_step_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.get_workflow_step_group_request.GetWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["workflow_id"] = workflow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        name: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_group_name.StepGroupName"
        ] = None,
        description: Optional[
            "aws_sdk_migrationhuborchestrator.types.step_group_description.StepGroupDescription"
        ] = None,
        next: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
        previous: Optional[
            "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.update_workflow_step_group_response.UpdateWorkflowStepGroupResponse":
        """<p>Update the step group in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            id: <p>The ID of the step group.</p>
            name: <p>The name of the step group.</p>
            description: <p>The description of the step group.</p>
            next: <p>The next step group.</p>
            previous: <p>The previous step group.</p>

        Raises:
            aws_sdk_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            aws_sdk_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            aws_sdk_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.update_workflow_step_group_request.UpdateWorkflowStepGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.update_workflow_step_group_response.UpdateWorkflowStepGroupResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step_group

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.update_workflow_step_group.async_update_workflow_step_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.update_workflow_step_group_request.UpdateWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id
        input_["id"] = id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if next is not None:
            input_["next"] = next
        if previous is not None:
            input_["previous"] = previous

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.delete_workflow_step_group_response.DeleteWorkflowStepGroupResponse":
        """<p>Delete a step group in a migration workflow.</p>

        Args:
            workflow_id: <p>The ID of the migration workflow.</p>
            id: <p>The ID of the step group you want to delete.</p>

        Raises:
            aws_sdk_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            aws_sdk_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            aws_sdk_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.delete_workflow_step_group_request.DeleteWorkflowStepGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.delete_workflow_step_group_response.DeleteWorkflowStepGroupResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step_group

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.delete_workflow_step_group.async_delete_workflow_step_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.delete_workflow_step_group_request.DeleteWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        next_token: Optional[
            "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.list_workflow_step_groups_response.ListWorkflowStepGroupsResponse":
        """<p>List the step groups in a migration workflow.</p>

        Args:
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results that can be returned.</p>
            workflow_id: <p>The ID of the migration workflow.</p>

        Raises:
            aws_sdk_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            aws_sdk_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            aws_sdk_migrationhuborchestrator.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.list_workflow_step_groups_request.ListWorkflowStepGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.list_workflow_step_groups_response.ListWorkflowStepGroupsResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_step_groups

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_workflow_step_groups.async_list_workflow_step_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.list_workflow_step_groups_request.ListWorkflowStepGroupsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["workflow_id"] = workflow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
