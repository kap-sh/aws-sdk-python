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
    import aws_sdk_migrationhuborchestrator.types.list_template_step_groups_request
    import aws_sdk_migrationhuborchestrator.types.list_template_step_groups_response
    import aws_sdk_migrationhuborchestrator.types.max_results
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.template_id
    import aws_sdk_migrationhuborchestrator.types.template_step_group_summary
    from aws_sdk_migrationhuborchestrator._services.async_migration_hub_orchestrator import (
        AsyncMigrationHubOrchestratorClient,
        AsyncMigrationHubOrchestratorClientConfig,
    )
    from aws_sdk_migrationhuborchestrator._services.migration_hub_orchestrator import (
        MigrationHubOrchestratorClient,
        MigrationHubOrchestratorClientConfig,
    )


class TemplateStepGroups:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service

    def read(
        self,
        template_id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.list_template_step_groups_response.ListTemplateStepGroupsResponse":
        """<p>List the step groups in a template.</p>

        Args:
            max_results: <p>The maximum number of results that can be returned.</p>
            next_token: <p>The pagination token.</p>
            template_id: <p>The ID of the template.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.list_template_step_groups_request.ListTemplateStepGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.list_template_step_groups_response.ListTemplateStepGroupsResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_step_groups

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_step_groups.list_template_step_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.list_template_step_groups_request.ListTemplateStepGroupsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["template_id"] = template_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTemplateStepGroups:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service

    async def read(
        self,
        template_id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.list_template_step_groups_response.ListTemplateStepGroupsResponse":
        """<p>List the step groups in a template.</p>

        Args:
            max_results: <p>The maximum number of results that can be returned.</p>
            next_token: <p>The pagination token.</p>
            template_id: <p>The ID of the template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.list_template_step_groups_request.ListTemplateStepGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.list_template_step_groups_response.ListTemplateStepGroupsResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_step_groups

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_template_step_groups.async_list_template_step_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.list_template_step_groups_request.ListTemplateStepGroupsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["template_id"] = template_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
