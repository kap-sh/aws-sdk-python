from typing import TYPE_CHECKING, Optional

import aws_sdk_nova_act._auth._signers
import aws_sdk_nova_act._auth._sigv4
from aws_sdk_nova_act._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.client_info
    import aws_sdk_nova_act.types.client_token
    import aws_sdk_nova_act.types.cloud_watch_log_group_name
    import aws_sdk_nova_act.types.create_workflow_run_request
    import aws_sdk_nova_act.types.create_workflow_run_response
    import aws_sdk_nova_act.types.delete_workflow_run_request
    import aws_sdk_nova_act.types.delete_workflow_run_response
    import aws_sdk_nova_act.types.get_workflow_run_request
    import aws_sdk_nova_act.types.get_workflow_run_response
    import aws_sdk_nova_act.types.list_workflow_runs_request
    import aws_sdk_nova_act.types.list_workflow_runs_response
    import aws_sdk_nova_act.types.max_results
    import aws_sdk_nova_act.types.model_id
    import aws_sdk_nova_act.types.next_token
    import aws_sdk_nova_act.types.sort_order
    import aws_sdk_nova_act.types.update_workflow_run_request
    import aws_sdk_nova_act.types.update_workflow_run_response
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_definition_name
    import aws_sdk_nova_act.types.workflow_run_status
    import aws_sdk_nova_act.types.workflow_run_summary
    from aws_sdk_nova_act._services.async_nova_act import (
        AsyncNovaActClient,
        AsyncNovaActClientConfig,
    )
    from aws_sdk_nova_act._services.nova_act import NovaActClient, NovaActClientConfig


class WorkflowRunResource:
    def __init__(self, service: NovaActClient) -> None:
        self._service = service

    def create(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        model_id: "aws_sdk_nova_act.types.model_id.ModelId",
        client_info: "aws_sdk_nova_act.types.client_info.ClientInfo",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        client_token: Optional[
            "aws_sdk_nova_act.types.client_token.ClientToken"
        ] = None,
        log_group_name: Optional[
            "aws_sdk_nova_act.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
        ] = None,
    ) -> (
        "aws_sdk_nova_act.types.create_workflow_run_response.CreateWorkflowRunResponse"
    ):
        """<p>Creates a new execution instance of a workflow definition with specified parameters.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to execute.</p>
            model_id: <p>The ID of the AI model to use for workflow execution.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            log_group_name: <p>The CloudWatch log group name for storing workflow execution logs.</p>
            client_info: <p>Information about the client making the request, including compatibility version and SDK version.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.create_workflow_run_request.CreateWorkflowRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.create_workflow_run_response.CreateWorkflowRunResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_run

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_run.create_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.create_workflow_run_request.CreateWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["model_id"] = model_id
        if client_token is not None:
            input["client_token"] = client_token
        if log_group_name is not None:
            input["log_group_name"] = log_group_name
        input["client_info"] = client_info

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "aws_sdk_nova_act.types.get_workflow_run_response.GetWorkflowRunResponse":
        """<p>Retrieves the current state, configuration, and execution details of a workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_run

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_run.get_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.get_workflow_run_request.GetWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["workflow_run_id"] = workflow_run_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        status: "aws_sdk_nova_act.types.workflow_run_status.WorkflowRunStatus",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> (
        "aws_sdk_nova_act.types.update_workflow_run_response.UpdateWorkflowRunResponse"
    ):
        """<p>Updates the configuration or state of an active workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to update.</p>
            status: <p>The new status to set for the workflow run.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.update_workflow_run_request.UpdateWorkflowRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.update_workflow_run_response.UpdateWorkflowRunResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.update_workflow_run

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.update_workflow_run.update_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.update_workflow_run_request.UpdateWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["workflow_run_id"] = workflow_run_id
        input["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> (
        "aws_sdk_nova_act.types.delete_workflow_run_response.DeleteWorkflowRunResponse"
    ):
        """<p>Terminates and cleans up a workflow run, stopping all associated acts and sessions.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.delete_workflow_run_request.DeleteWorkflowRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.delete_workflow_run_response.DeleteWorkflowRunResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_run

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_run.delete_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.delete_workflow_run_request.DeleteWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["workflow_run_id"] = workflow_run_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["aws_sdk_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["aws_sdk_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_nova_act.types.list_workflow_runs_response.ListWorkflowRunsResponse":
        """<p>Lists all workflow runs for a specific workflow definition with optional filtering and pagination.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to list workflow runs for.</p>
            max_results: <p>The maximum number of workflow runs to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned workflow runs (ascending or descending).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.list_workflow_runs_request.ListWorkflowRunsRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.list_workflow_runs_response.ListWorkflowRunsResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_runs

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_runs.list_workflow_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.list_workflow_runs_request.ListWorkflowRunsRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncWorkflowRunResource:
    def __init__(self, service: AsyncNovaActClient) -> None:
        self._service = service

    async def create(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        model_id: "aws_sdk_nova_act.types.model_id.ModelId",
        client_info: "aws_sdk_nova_act.types.client_info.ClientInfo",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        client_token: Optional[
            "aws_sdk_nova_act.types.client_token.ClientToken"
        ] = None,
        log_group_name: Optional[
            "aws_sdk_nova_act.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
        ] = None,
    ) -> (
        "aws_sdk_nova_act.types.create_workflow_run_response.CreateWorkflowRunResponse"
    ):
        """<p>Creates a new execution instance of a workflow definition with specified parameters.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to execute.</p>
            model_id: <p>The ID of the AI model to use for workflow execution.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            log_group_name: <p>The CloudWatch log group name for storing workflow execution logs.</p>
            client_info: <p>Information about the client making the request, including compatibility version and SDK version.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.create_workflow_run_request.CreateWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.create_workflow_run_response.CreateWorkflowRunResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_run

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_run.async_create_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.create_workflow_run_request.CreateWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["model_id"] = model_id
        if client_token is not None:
            input["client_token"] = client_token
        if log_group_name is not None:
            input["log_group_name"] = log_group_name
        input["client_info"] = client_info

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> "aws_sdk_nova_act.types.get_workflow_run_response.GetWorkflowRunResponse":
        """<p>Retrieves the current state, configuration, and execution details of a workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_run

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_run.async_get_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.get_workflow_run_request.GetWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["workflow_run_id"] = workflow_run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        status: "aws_sdk_nova_act.types.workflow_run_status.WorkflowRunStatus",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> (
        "aws_sdk_nova_act.types.update_workflow_run_response.UpdateWorkflowRunResponse"
    ):
        """<p>Updates the configuration or state of an active workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to update.</p>
            status: <p>The new status to set for the workflow run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.update_workflow_run_request.UpdateWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.update_workflow_run_response.UpdateWorkflowRunResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.update_workflow_run

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.update_workflow_run.async_update_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.update_workflow_run_request.UpdateWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["workflow_run_id"] = workflow_run_id
        input["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> (
        "aws_sdk_nova_act.types.delete_workflow_run_response.DeleteWorkflowRunResponse"
    ):
        """<p>Terminates and cleans up a workflow run, stopping all associated acts and sessions.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.delete_workflow_run_request.DeleteWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.delete_workflow_run_response.DeleteWorkflowRunResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_run

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_run.async_delete_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.delete_workflow_run_request.DeleteWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["workflow_run_id"] = workflow_run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        max_results: Optional["aws_sdk_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["aws_sdk_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_nova_act.types.list_workflow_runs_response.ListWorkflowRunsResponse":
        """<p>Lists all workflow runs for a specific workflow definition with optional filtering and pagination.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to list workflow runs for.</p>
            max_results: <p>The maximum number of workflow runs to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned workflow runs (ascending or descending).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.list_workflow_runs_request.ListWorkflowRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.list_workflow_runs_response.ListWorkflowRunsResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_runs

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_runs.async_list_workflow_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.list_workflow_runs_request.ListWorkflowRunsRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
