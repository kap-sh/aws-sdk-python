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
    import aws_sdk_datazone.types.data_source_id
    import aws_sdk_datazone.types.data_source_run_id
    import aws_sdk_datazone.types.data_source_run_status
    import aws_sdk_datazone.types.data_source_run_summary
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.get_data_source_run_input
    import aws_sdk_datazone.types.get_data_source_run_output
    import aws_sdk_datazone.types.list_data_source_runs_input
    import aws_sdk_datazone.types.list_data_source_runs_output
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.start_data_source_run_input
    import aws_sdk_datazone.types.start_data_source_run_output
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )


class DataSourceRun:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        data_source_identifier: "aws_sdk_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.start_data_source_run_output.StartDataSourceRunOutput":
        """<p>Start the run of the specified data source in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to start a data source run.</p>
            data_source_identifier: <p>The identifier of the data source.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.start_data_source_run_input.StartDataSourceRunInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.start_data_source_run_output.StartDataSourceRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.start_data_source_run

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.start_data_source_run.start_data_source_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.start_data_source_run_input.StartDataSourceRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["data_source_identifier"] = data_source_identifier
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
        identifier: "aws_sdk_datazone.types.data_source_run_id.DataSourceRunId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_data_source_run_output.GetDataSourceRunOutput":
        """<p>Gets an Amazon DataZone data source run.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which this data source run was performed.</p>
            identifier: <p>The ID of the data source run.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.get_data_source_run_input.GetDataSourceRunInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_data_source_run_output.GetDataSourceRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_data_source_run

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_data_source_run.get_data_source_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_data_source_run_input.GetDataSourceRunInput = {}  # type: ignore[typeddict-item]
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
        data_source_identifier: "aws_sdk_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        status: Optional[
            "aws_sdk_datazone.types.data_source_run_status.DataSourceRunStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_data_source_runs_output.ListDataSourceRunsOutput":
        """<p>Lists data source runs in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to invoke the <code>ListDataSourceRuns</code> action.</p>
            data_source_identifier: <p>The identifier of the data source.</p>
            status: <p>The status of the data source.</p>
            next_token: <p>When the number of runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>
            max_results: <p>The maximum number of runs to return in a single call to <code>ListDataSourceRuns</code>. When the number of runs to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.list_data_source_runs_input.ListDataSourceRunsInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.list_data_source_runs_output.ListDataSourceRunsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_data_source_runs

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.list_data_source_runs.list_data_source_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_data_source_runs_input.ListDataSourceRunsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["data_source_identifier"] = data_source_identifier
        if status is not None:
            input_["status"] = status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDataSourceRun:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        data_source_identifier: "aws_sdk_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.start_data_source_run_output.StartDataSourceRunOutput":
        """<p>Start the run of the specified data source in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to start a data source run.</p>
            data_source_identifier: <p>The identifier of the data source.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.start_data_source_run_input.StartDataSourceRunInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.start_data_source_run_output.StartDataSourceRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.start_data_source_run

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.start_data_source_run.async_start_data_source_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.start_data_source_run_input.StartDataSourceRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["data_source_identifier"] = data_source_identifier
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
        identifier: "aws_sdk_datazone.types.data_source_run_id.DataSourceRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_data_source_run_output.GetDataSourceRunOutput":
        """<p>Gets an Amazon DataZone data source run.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which this data source run was performed.</p>
            identifier: <p>The ID of the data source run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_data_source_run_input.GetDataSourceRunInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_data_source_run_output.GetDataSourceRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_data_source_run

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_data_source_run.async_get_data_source_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_data_source_run_input.GetDataSourceRunInput = {}  # type: ignore[typeddict-item]
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
        data_source_identifier: "aws_sdk_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "aws_sdk_datazone.types.data_source_run_status.DataSourceRunStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_datazone.types.list_data_source_runs_output.ListDataSourceRunsOutput":
        """<p>Lists data source runs in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to invoke the <code>ListDataSourceRuns</code> action.</p>
            data_source_identifier: <p>The identifier of the data source.</p>
            status: <p>The status of the data source.</p>
            next_token: <p>When the number of runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>
            max_results: <p>The maximum number of runs to return in a single call to <code>ListDataSourceRuns</code>. When the number of runs to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_data_source_runs_input.ListDataSourceRunsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_data_source_runs_output.ListDataSourceRunsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_data_source_runs

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_data_source_runs.async_list_data_source_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_data_source_runs_input.ListDataSourceRunsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["data_source_identifier"] = data_source_identifier
        if status is not None:
            input_["status"] = status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
