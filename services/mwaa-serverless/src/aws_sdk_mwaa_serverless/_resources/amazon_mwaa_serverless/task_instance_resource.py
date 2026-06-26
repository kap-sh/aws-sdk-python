from __future__ import annotations

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
    import aws_sdk_mwaa_serverless.types.get_task_instance_request
    import aws_sdk_mwaa_serverless.types.get_task_instance_response
    import aws_sdk_mwaa_serverless.types.id_string
    import aws_sdk_mwaa_serverless.types.list_task_instances_request
    import aws_sdk_mwaa_serverless.types.list_task_instances_response
    import aws_sdk_mwaa_serverless.types.task_instance_summary
    import aws_sdk_mwaa_serverless.types.workflow_arn
    from aws_sdk_mwaa_serverless._services.async_mwaa_serverless import (
        AsyncMWAAServerlessClient,
        AsyncMWAAServerlessClientConfig,
    )
    from aws_sdk_mwaa_serverless._services.mwaa_serverless import (
        MWAAServerlessClient,
        MWAAServerlessClientConfig,
    )


class TaskInstanceResource:
    def __init__(self, service: MWAAServerlessClient) -> None:
        self._service = service

    def read(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        task_instance_id: "aws_sdk_mwaa_serverless.types.id_string.IdString",
        run_id: "aws_sdk_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
    ) -> "aws_sdk_mwaa_serverless.types.get_task_instance_response.GetTaskInstanceResponse":
        """<p>Retrieves detailed information about a specific task instance within a workflow run. Task instances represent individual tasks that are executed as part of a workflow in the Amazon Managed Workflows for Apache Airflow Serverless environment. Each task instance runs in an isolated ECS container with dedicated resources and security boundaries. The service tracks task execution state, retry attempts, and provides detailed timing and error information for troubleshooting and monitoring purposes.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the task instance.</p>
            task_instance_id: <p>The unique identifier of the task instance to retrieve.</p>
            run_id: <p>The unique identifier of the workflow run that contains the task instance.</p>

        Raises:
            aws_sdk_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            aws_sdk_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            aws_sdk_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            aws_sdk_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            aws_sdk_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            aws_sdk_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            aws_sdk_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mwaa_serverless.types.get_task_instance_request.GetTaskInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mwaa_serverless.types.get_task_instance_response.GetTaskInstanceResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.get_task_instance

            output, http_response = (
                aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.get_task_instance.get_task_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.get_task_instance_request.GetTaskInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_arn"] = workflow_arn
        input_["task_instance_id"] = task_instance_id
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
        run_id: "aws_sdk_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_mwaa_serverless.types.list_task_instances_response.ListTaskInstancesResponse":
        """<p>Lists all task instances for a specific workflow run, with optional pagination support.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>
            run_id: <p>The unique identifier of the workflow run for which you want a list of task instances.</p>
            max_results: <p>The maximum number of task instances to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListTaskInstances</code>.</p>

        Raises:
            aws_sdk_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            aws_sdk_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            aws_sdk_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            aws_sdk_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            aws_sdk_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            aws_sdk_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mwaa_serverless.types.list_task_instances_request.ListTaskInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mwaa_serverless.types.list_task_instances_response.ListTaskInstancesResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_task_instances

            output, http_response = (
                aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_task_instances.list_task_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.list_task_instances_request.ListTaskInstancesRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_arn"] = workflow_arn
        input_["run_id"] = run_id
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


class AsyncTaskInstanceResource:
    def __init__(self, service: AsyncMWAAServerlessClient) -> None:
        self._service = service

    async def read(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        task_instance_id: "aws_sdk_mwaa_serverless.types.id_string.IdString",
        run_id: "aws_sdk_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
    ) -> "aws_sdk_mwaa_serverless.types.get_task_instance_response.GetTaskInstanceResponse":
        """<p>Retrieves detailed information about a specific task instance within a workflow run. Task instances represent individual tasks that are executed as part of a workflow in the Amazon Managed Workflows for Apache Airflow Serverless environment. Each task instance runs in an isolated ECS container with dedicated resources and security boundaries. The service tracks task execution state, retry attempts, and provides detailed timing and error information for troubleshooting and monitoring purposes.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the task instance.</p>
            task_instance_id: <p>The unique identifier of the task instance to retrieve.</p>
            run_id: <p>The unique identifier of the workflow run that contains the task instance.</p>

        Raises:
            aws_sdk_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            aws_sdk_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            aws_sdk_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            aws_sdk_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            aws_sdk_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            aws_sdk_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            aws_sdk_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mwaa_serverless.types.get_task_instance_request.GetTaskInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mwaa_serverless.types.get_task_instance_response.GetTaskInstanceResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.get_task_instance

            (
                output,
                http_response,
            ) = await aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.get_task_instance.async_get_task_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.get_task_instance_request.GetTaskInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_arn"] = workflow_arn
        input_["task_instance_id"] = task_instance_id
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
        run_id: "aws_sdk_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_mwaa_serverless.types.list_task_instances_response.ListTaskInstancesResponse":
        """<p>Lists all task instances for a specific workflow run, with optional pagination support.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>
            run_id: <p>The unique identifier of the workflow run for which you want a list of task instances.</p>
            max_results: <p>The maximum number of task instances to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListTaskInstances</code>.</p>

        Raises:
            aws_sdk_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            aws_sdk_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            aws_sdk_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            aws_sdk_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            aws_sdk_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            aws_sdk_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mwaa_serverless.types.list_task_instances_request.ListTaskInstancesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mwaa_serverless.types.list_task_instances_response.ListTaskInstancesResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_task_instances

            (
                output,
                http_response,
            ) = await aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_task_instances.async_list_task_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.list_task_instances_request.ListTaskInstancesRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_arn"] = workflow_arn
        input_["run_id"] = run_id
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
