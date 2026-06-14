from typing import TYPE_CHECKING, Optional

from aws_sdk_mwaa_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.get_workflow_run_request
    import aws_sdk_mwaa_serverless.types.get_workflow_run_response
    import aws_sdk_mwaa_serverless.types.id_string
    import aws_sdk_mwaa_serverless.types.idempotency_token_string
    import aws_sdk_mwaa_serverless.types.list_workflow_runs_request
    import aws_sdk_mwaa_serverless.types.list_workflow_runs_response
    import aws_sdk_mwaa_serverless.types.object_map
    import aws_sdk_mwaa_serverless.types.start_workflow_run_request
    import aws_sdk_mwaa_serverless.types.start_workflow_run_response
    import aws_sdk_mwaa_serverless.types.stop_workflow_run_request
    import aws_sdk_mwaa_serverless.types.stop_workflow_run_response
    import aws_sdk_mwaa_serverless.types.version_id
    import aws_sdk_mwaa_serverless.types.workflow_arn
    import aws_sdk_mwaa_serverless.types.workflow_run_summary
    from aws_sdk_mwaa_serverless._services.async_mwaa_serverless import (
        AsyncMWAAServerlessClient,
        AsyncMWAAServerlessClientConfig,
    )
    from aws_sdk_mwaa_serverless._services.mwaa_serverless import (
        MWAAServerlessClient,
        MWAAServerlessClientConfig,
    )


class WorkflowRunResource:
    def __init__(self, service: MWAAServerlessClient) -> None:
        self._service = service

    def create(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mwaa_serverless.types.idempotency_token_string.IdempotencyTokenString"
        ] = None,
        override_parameters: Optional[
            "aws_sdk_mwaa_serverless.types.object_map.ObjectMap"
        ] = None,
        workflow_version: Optional[
            "aws_sdk_mwaa_serverless.types.version_id.VersionId"
        ] = None,
    ) -> "aws_sdk_mwaa_serverless.types.start_workflow_run_response.StartWorkflowRunResponse":
        """<p>Starts a new execution of a workflow. This operation creates a workflow run that executes the tasks that are defined in the workflow. Amazon Managed Workflows for Apache Airflow Serverless schedules the workflow execution across its managed Airflow environment, automatically scaling ECS worker tasks based on the workload. The service handles task isolation, dependency resolution, and provides comprehensive monitoring and logging throughout the execution lifecycle.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to run.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow run requests.</p>
            override_parameters: <p>Optional parameters to override default workflow parameters for this specific run. These parameters are passed to the workflow during execution and can be used to customize behavior without modifying the workflow definition. Parameters are made available as environment variables to tasks and you can reference them within the YAML workflow definition using standard parameter substitution syntax.</p>
            workflow_version: <p>Optional. The specific version of the workflow to execute. If not specified, the latest version is used.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_mwaa_serverless.types.start_workflow_run_response.StartWorkflowRunResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.start_workflow_run

            output, http_response = (
                aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.start_workflow_run.start_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_arn"] = workflow_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if override_parameters is not None:
            input_["override_parameters"] = override_parameters
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "aws_sdk_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
    ) -> (
        "aws_sdk_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse"
    ):
        """<p>Retrieves detailed information about a specific workflow run, including its status, execution details, and task instances.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>
            run_id: <p>The unique identifier of the workflow run to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow_run

            output, http_response = (
                aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow_run.get_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_arn"] = workflow_arn
        input_["run_id"] = run_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "aws_sdk_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
    ) -> "aws_sdk_mwaa_serverless.types.stop_workflow_run_response.StopWorkflowRunResponse":
        """<p>Stops a running workflow execution. This operation terminates all running tasks and prevents new tasks from starting. Amazon Managed Workflows for Apache Airflow Serverless gracefully shuts down the workflow execution by stopping task scheduling and terminating active ECS worker containers. The operation transitions the workflow run to a <code>STOPPING</code> state and then to <code>STOPPED</code> once all cleanup is complete. In-flight tasks may complete or be terminated depending on their current execution state.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run you want to stop.</p>
            run_id: <p>The unique identifier of the workflow run to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mwaa_serverless.types.stop_workflow_run_request.StopWorkflowRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_mwaa_serverless.types.stop_workflow_run_response.StopWorkflowRunResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.stop_workflow_run

            output, http_response = (
                aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.stop_workflow_run.stop_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.stop_workflow_run_request.StopWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_arn"] = workflow_arn
        input_["run_id"] = run_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        workflow_version: Optional[
            "aws_sdk_mwaa_serverless.types.version_id.VersionId"
        ] = None,
    ) -> "aws_sdk_mwaa_serverless.types.list_workflow_runs_response.ListWorkflowRunsResponse":
        """<p>Lists all runs for a specified workflow, with optional pagination and filtering support.</p>

        Args:
            max_results: <p>The maximum number of workflow runs to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowRuns</code>.</p>
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow for which you want a list of runs.</p>
            workflow_version: <p>Optional. The specific version of the workflow for which you want a list of runs. If not specified, runs for all versions are returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mwaa_serverless.types.list_workflow_runs_request.ListWorkflowRunsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mwaa_serverless.types.list_workflow_runs_response.ListWorkflowRunsResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_runs

            output, http_response = (
                aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_runs.list_workflow_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.list_workflow_runs_request.ListWorkflowRunsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["workflow_arn"] = workflow_arn
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncWorkflowRunResource:
    def __init__(self, service: AsyncMWAAServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mwaa_serverless.types.idempotency_token_string.IdempotencyTokenString"
        ] = None,
        override_parameters: Optional[
            "aws_sdk_mwaa_serverless.types.object_map.ObjectMap"
        ] = None,
        workflow_version: Optional[
            "aws_sdk_mwaa_serverless.types.version_id.VersionId"
        ] = None,
    ) -> "aws_sdk_mwaa_serverless.types.start_workflow_run_response.StartWorkflowRunResponse":
        """<p>Starts a new execution of a workflow. This operation creates a workflow run that executes the tasks that are defined in the workflow. Amazon Managed Workflows for Apache Airflow Serverless schedules the workflow execution across its managed Airflow environment, automatically scaling ECS worker tasks based on the workload. The service handles task isolation, dependency resolution, and provides comprehensive monitoring and logging throughout the execution lifecycle.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to run.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow run requests.</p>
            override_parameters: <p>Optional parameters to override default workflow parameters for this specific run. These parameters are passed to the workflow during execution and can be used to customize behavior without modifying the workflow definition. Parameters are made available as environment variables to tasks and you can reference them within the YAML workflow definition using standard parameter substitution syntax.</p>
            workflow_version: <p>Optional. The specific version of the workflow to execute. If not specified, the latest version is used.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mwaa_serverless.types.start_workflow_run_response.StartWorkflowRunResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.start_workflow_run

            (
                output,
                http_response,
            ) = await aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.start_workflow_run.async_start_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_arn"] = workflow_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if override_parameters is not None:
            input_["override_parameters"] = override_parameters
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "aws_sdk_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
    ) -> (
        "aws_sdk_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse"
    ):
        """<p>Retrieves detailed information about a specific workflow run, including its status, execution details, and task instances.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>
            run_id: <p>The unique identifier of the workflow run to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow_run

            (
                output,
                http_response,
            ) = await aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow_run.async_get_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_arn"] = workflow_arn
        input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "aws_sdk_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
    ) -> "aws_sdk_mwaa_serverless.types.stop_workflow_run_response.StopWorkflowRunResponse":
        """<p>Stops a running workflow execution. This operation terminates all running tasks and prevents new tasks from starting. Amazon Managed Workflows for Apache Airflow Serverless gracefully shuts down the workflow execution by stopping task scheduling and terminating active ECS worker containers. The operation transitions the workflow run to a <code>STOPPING</code> state and then to <code>STOPPED</code> once all cleanup is complete. In-flight tasks may complete or be terminated depending on their current execution state.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run you want to stop.</p>
            run_id: <p>The unique identifier of the workflow run to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mwaa_serverless.types.stop_workflow_run_request.StopWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mwaa_serverless.types.stop_workflow_run_response.StopWorkflowRunResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.stop_workflow_run

            (
                output,
                http_response,
            ) = await aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.stop_workflow_run.async_stop_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.stop_workflow_run_request.StopWorkflowRunRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_arn"] = workflow_arn
        input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        workflow_version: Optional[
            "aws_sdk_mwaa_serverless.types.version_id.VersionId"
        ] = None,
    ) -> "aws_sdk_mwaa_serverless.types.list_workflow_runs_response.ListWorkflowRunsResponse":
        """<p>Lists all runs for a specified workflow, with optional pagination and filtering support.</p>

        Args:
            max_results: <p>The maximum number of workflow runs to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowRuns</code>.</p>
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow for which you want a list of runs.</p>
            workflow_version: <p>Optional. The specific version of the workflow for which you want a list of runs. If not specified, runs for all versions are returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mwaa_serverless.types.list_workflow_runs_request.ListWorkflowRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mwaa_serverless.types.list_workflow_runs_response.ListWorkflowRunsResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_runs

            (
                output,
                http_response,
            ) = await aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_runs.async_list_workflow_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.list_workflow_runs_request.ListWorkflowRunsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["workflow_arn"] = workflow_arn
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
