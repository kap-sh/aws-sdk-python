from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4
from aws_sdk_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.compute_config
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.get_notebook_run_input
    import aws_sdk_datazone.types.get_notebook_run_output
    import aws_sdk_datazone.types.list_notebook_runs_input
    import aws_sdk_datazone.types.list_notebook_runs_output
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.metadata
    import aws_sdk_datazone.types.network_config
    import aws_sdk_datazone.types.notebook_id
    import aws_sdk_datazone.types.notebook_run_id
    import aws_sdk_datazone.types.notebook_run_status
    import aws_sdk_datazone.types.notebook_run_summary
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.parameters
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.schedule_id
    import aws_sdk_datazone.types.sort_order
    import aws_sdk_datazone.types.start_notebook_run_input
    import aws_sdk_datazone.types.start_notebook_run_output
    import aws_sdk_datazone.types.stop_notebook_run_input
    import aws_sdk_datazone.types.stop_notebook_run_output
    import aws_sdk_datazone.types.timeout_config
    import aws_sdk_datazone.types.trigger_source
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )


class NotebookRun:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        notebook_identifier: "aws_sdk_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        schedule_identifier: Optional[
            "aws_sdk_datazone.types.schedule_id.ScheduleId"
        ] = None,
        compute_configuration: Optional[
            "aws_sdk_datazone.types.compute_config.ComputeConfig"
        ] = None,
        network_configuration: Optional[
            "aws_sdk_datazone.types.network_config.NetworkConfig"
        ] = None,
        timeout_configuration: Optional[
            "aws_sdk_datazone.types.timeout_config.TimeoutConfig"
        ] = None,
        trigger_source: Optional[
            "aws_sdk_datazone.types.trigger_source.TriggerSource"
        ] = None,
        metadata: Optional["aws_sdk_datazone.types.metadata.Metadata"] = None,
        parameters: Optional["aws_sdk_datazone.types.parameters.Parameters"] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.start_notebook_run_output.StartNotebookRunOutput":
        r"""<p>Starts a notebook run in Amazon SageMaker Unified Studio. A notebook run represents the execution of an <a href=\"https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html\">Amazon SageMaker notebook</a> within a project. You can configure compute, network, timeout, and environment settings for the run.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is started.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook run.</p>
            notebook_identifier: <p>The identifier of the notebook to run.</p>
            schedule_identifier: <p>The identifier of the schedule associated with the notebook run.</p>
            compute_configuration: <p>The compute configuration for the notebook run, including instance type and environment version.</p>
            network_configuration: <p>The network configuration for the notebook run, including network access type and optional VPC settings.</p>
            timeout_configuration: <p>The timeout configuration for the notebook run. The default timeout is 720 minutes (12 hours) and the maximum is 1440 minutes (24 hours).</p>
            trigger_source: <p>The source that triggered the notebook run.</p>
            metadata: <p>The metadata for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            parameters: <p>The sensitive parameters for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.start_notebook_run_input.StartNotebookRunInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.start_notebook_run_output.StartNotebookRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.start_notebook_run

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.start_notebook_run.start_notebook_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.start_notebook_run_input.StartNotebookRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["owning_project_identifier"] = owning_project_identifier
        input_["notebook_identifier"] = notebook_identifier
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if timeout_configuration is not None:
            input_["timeout_configuration"] = timeout_configuration
        if trigger_source is not None:
            input_["trigger_source"] = trigger_source
        if metadata is not None:
            input_["metadata"] = metadata
        if parameters is not None:
            input_["parameters"] = parameters
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.notebook_run_id.NotebookRunId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_notebook_run_output.GetNotebookRunOutput":
        r"""<p>Gets the details of a <a href=\"https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html\">notebook run</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run exists.</p>
            identifier: <p>The identifier of the notebook run.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.get_notebook_run_input.GetNotebookRunInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_notebook_run_output.GetNotebookRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_notebook_run

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_notebook_run.get_notebook_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_notebook_run_input.GetNotebookRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        notebook_identifier: Optional[
            "aws_sdk_datazone.types.notebook_id.NotebookId"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.notebook_run_status.NotebookRunStatus"
        ] = None,
        schedule_identifier: Optional[
            "aws_sdk_datazone.types.schedule_id.ScheduleId"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_notebook_runs_output.ListNotebookRunsOutput":
        r"""<p>Lists <a href=\"https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html\">notebook runs</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to list notebook runs.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook runs.</p>
            notebook_identifier: <p>The identifier of the notebook to filter runs by.</p>
            status: <p>The status to filter notebook runs by.</p>
            schedule_identifier: <p>The identifier of the schedule to filter notebook runs by.</p>
            max_results: <p>The maximum number of notebook runs to return in a single call. When the number of notebook runs exceeds the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value.</p>
            sort_order: <p>The sort order for the results.</p>
            next_token: <p>When the number of notebook runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebook runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebookRuns</code> to list the next set of notebook runs.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.list_notebook_runs_input.ListNotebookRunsInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.list_notebook_runs_output.ListNotebookRunsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_notebook_runs

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.list_notebook_runs.list_notebook_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_notebook_runs_input.ListNotebookRunsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["owning_project_identifier"] = owning_project_identifier
        if notebook_identifier is not None:
            input_["notebook_identifier"] = notebook_identifier
        if status is not None:
            input_["status"] = status
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_notebook_run(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.notebook_run_id.NotebookRunId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.stop_notebook_run_output.StopNotebookRunOutput":
        r"""<p>Stops a running <a href=\"https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html\">notebook run</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is stopped.</p>
            identifier: <p>The identifier of the notebook run to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.stop_notebook_run_input.StopNotebookRunInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.stop_notebook_run_output.StopNotebookRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.stop_notebook_run

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.stop_notebook_run.stop_notebook_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.stop_notebook_run_input.StopNotebookRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncNotebookRun:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        notebook_identifier: "aws_sdk_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        schedule_identifier: Optional[
            "aws_sdk_datazone.types.schedule_id.ScheduleId"
        ] = None,
        compute_configuration: Optional[
            "aws_sdk_datazone.types.compute_config.ComputeConfig"
        ] = None,
        network_configuration: Optional[
            "aws_sdk_datazone.types.network_config.NetworkConfig"
        ] = None,
        timeout_configuration: Optional[
            "aws_sdk_datazone.types.timeout_config.TimeoutConfig"
        ] = None,
        trigger_source: Optional[
            "aws_sdk_datazone.types.trigger_source.TriggerSource"
        ] = None,
        metadata: Optional["aws_sdk_datazone.types.metadata.Metadata"] = None,
        parameters: Optional["aws_sdk_datazone.types.parameters.Parameters"] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.start_notebook_run_output.StartNotebookRunOutput":
        r"""<p>Starts a notebook run in Amazon SageMaker Unified Studio. A notebook run represents the execution of an <a href=\"https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html\">Amazon SageMaker notebook</a> within a project. You can configure compute, network, timeout, and environment settings for the run.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is started.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook run.</p>
            notebook_identifier: <p>The identifier of the notebook to run.</p>
            schedule_identifier: <p>The identifier of the schedule associated with the notebook run.</p>
            compute_configuration: <p>The compute configuration for the notebook run, including instance type and environment version.</p>
            network_configuration: <p>The network configuration for the notebook run, including network access type and optional VPC settings.</p>
            timeout_configuration: <p>The timeout configuration for the notebook run. The default timeout is 720 minutes (12 hours) and the maximum is 1440 minutes (24 hours).</p>
            trigger_source: <p>The source that triggered the notebook run.</p>
            metadata: <p>The metadata for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            parameters: <p>The sensitive parameters for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.start_notebook_run_input.StartNotebookRunInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.start_notebook_run_output.StartNotebookRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.start_notebook_run

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.start_notebook_run.async_start_notebook_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.start_notebook_run_input.StartNotebookRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["owning_project_identifier"] = owning_project_identifier
        input_["notebook_identifier"] = notebook_identifier
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if timeout_configuration is not None:
            input_["timeout_configuration"] = timeout_configuration
        if trigger_source is not None:
            input_["trigger_source"] = trigger_source
        if metadata is not None:
            input_["metadata"] = metadata
        if parameters is not None:
            input_["parameters"] = parameters
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.notebook_run_id.NotebookRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_notebook_run_output.GetNotebookRunOutput":
        r"""<p>Gets the details of a <a href=\"https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html\">notebook run</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run exists.</p>
            identifier: <p>The identifier of the notebook run.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_notebook_run_input.GetNotebookRunInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_notebook_run_output.GetNotebookRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_notebook_run

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_notebook_run.async_get_notebook_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_notebook_run_input.GetNotebookRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        notebook_identifier: Optional[
            "aws_sdk_datazone.types.notebook_id.NotebookId"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.notebook_run_status.NotebookRunStatus"
        ] = None,
        schedule_identifier: Optional[
            "aws_sdk_datazone.types.schedule_id.ScheduleId"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        sort_order: Optional["aws_sdk_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_notebook_runs_output.ListNotebookRunsOutput":
        r"""<p>Lists <a href=\"https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html\">notebook runs</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to list notebook runs.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook runs.</p>
            notebook_identifier: <p>The identifier of the notebook to filter runs by.</p>
            status: <p>The status to filter notebook runs by.</p>
            schedule_identifier: <p>The identifier of the schedule to filter notebook runs by.</p>
            max_results: <p>The maximum number of notebook runs to return in a single call. When the number of notebook runs exceeds the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value.</p>
            sort_order: <p>The sort order for the results.</p>
            next_token: <p>When the number of notebook runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebook runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebookRuns</code> to list the next set of notebook runs.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_notebook_runs_input.ListNotebookRunsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_notebook_runs_output.ListNotebookRunsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_notebook_runs

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_notebook_runs.async_list_notebook_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_notebook_runs_input.ListNotebookRunsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["owning_project_identifier"] = owning_project_identifier
        if notebook_identifier is not None:
            input_["notebook_identifier"] = notebook_identifier
        if status is not None:
            input_["status"] = status
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_notebook_run(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.notebook_run_id.NotebookRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.stop_notebook_run_output.StopNotebookRunOutput":
        r"""<p>Stops a running <a href=\"https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html\">notebook run</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is stopped.</p>
            identifier: <p>The identifier of the notebook run to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.stop_notebook_run_input.StopNotebookRunInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.stop_notebook_run_output.StopNotebookRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.stop_notebook_run

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.stop_notebook_run.async_stop_notebook_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.stop_notebook_run_input.StopNotebookRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
