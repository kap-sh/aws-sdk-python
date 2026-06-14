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
    import aws_sdk_migrationhuborchestrator.types.list_plugins_request
    import aws_sdk_migrationhuborchestrator.types.list_plugins_response
    import aws_sdk_migrationhuborchestrator.types.max_results
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.plugin_summary
    from aws_sdk_migrationhuborchestrator._services.async_migration_hub_orchestrator import (
        AsyncMigrationHubOrchestratorClient,
        AsyncMigrationHubOrchestratorClientConfig,
    )
    from aws_sdk_migrationhuborchestrator._services.migration_hub_orchestrator import (
        MigrationHubOrchestratorClient,
        MigrationHubOrchestratorClientConfig,
    )


class Plugin:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service

    def list(
        self,
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.list_plugins_response.ListPluginsResponse":
        """<p>List AWS Migration Hub Orchestrator plugins.</p>

        Args:
            max_results: <p>The maximum number of plugins that can be returned.</p>
            next_token: <p>The pagination token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.list_plugins_request.ListPluginsRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.list_plugins_response.ListPluginsResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_plugins

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_plugins.list_plugins(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.list_plugins_request.ListPluginsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncPlugin:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.list_plugins_response.ListPluginsResponse":
        """<p>List AWS Migration Hub Orchestrator plugins.</p>

        Args:
            max_results: <p>The maximum number of plugins that can be returned.</p>
            next_token: <p>The pagination token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migrationhuborchestrator.types.list_plugins_request.ListPluginsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migrationhuborchestrator.types.list_plugins_response.ListPluginsResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_plugins

            (
                output,
                http_response,
            ) = await aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_plugins.async_list_plugins(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.list_plugins_request.ListPluginsRequest = {}  # type: ignore[typeddict-item]
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
