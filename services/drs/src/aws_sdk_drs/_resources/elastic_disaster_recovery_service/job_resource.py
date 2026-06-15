from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_drs._auth._signers
import aws_sdk_drs._auth._sigv4
from aws_sdk_drs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_drs.types.delete_job_request
    import aws_sdk_drs.types.delete_job_response
    import aws_sdk_drs.types.describe_job_log_items_request
    import aws_sdk_drs.types.describe_job_log_items_response
    import aws_sdk_drs.types.describe_jobs_request
    import aws_sdk_drs.types.describe_jobs_request_filters
    import aws_sdk_drs.types.describe_jobs_response
    import aws_sdk_drs.types.job
    import aws_sdk_drs.types.job_id
    import aws_sdk_drs.types.job_log
    import aws_sdk_drs.types.pagination_token
    import aws_sdk_drs.types.strictly_positive_integer
    from aws_sdk_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    from aws_sdk_drs._services.drs import drsClient, drsClientConfig


class JobResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

    def delete(
        self,
        job_id: "aws_sdk_drs.types.job_id.JobID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes a single Job by ID.</p>

        Args:
            job_id: <p>The ID of the Job to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.delete_job_request.DeleteJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.delete_job_response.DeleteJobResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_job

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_job.delete_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.delete_job_request.DeleteJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[drsClientConfig] = None,
        filters: Optional[
            "aws_sdk_drs.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.describe_jobs_response.DescribeJobsResponse":
        """<p>Returns a list of Jobs. Use the JobsID and fromDate and toDate filters to limit which jobs are returned. The response is sorted by creationDataTime - latest date first. Jobs are created by the StartRecovery, TerminateRecoveryInstances and StartFailbackLaunch APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to *Support* and only used in response to relevant support tickets.</p>

        Args:
            filters: <p>A set of filters by which to return Jobs.</p>
            max_results: <p>Maximum number of Jobs to retrieve.</p>
            next_token: <p>The token of the next Job to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.describe_jobs_request.DescribeJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.describe_jobs_response.DescribeJobsResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_jobs

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_jobs.describe_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_jobs_request.DescribeJobsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    def describe_job_log_items(
        self,
        job_id: "aws_sdk_drs.types.job_id.JobID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "aws_sdk_drs.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
    ):
        """<p>Retrieves a detailed Job log with pagination.</p>

        Args:
            job_id: <p>The ID of the Job for which Job log items will be retrieved.</p>
            max_results: <p>Maximum number of Job log items to retrieve.</p>
            next_token: <p>The token of the next Job log items to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.describe_job_log_items_request.DescribeJobLogItemsRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_job_log_items

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_job_log_items.describe_job_log_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_job_log_items_request.DescribeJobLogItemsRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
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


class AsyncJobResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service

    async def delete(
        self,
        job_id: "aws_sdk_drs.types.job_id.JobID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes a single Job by ID.</p>

        Args:
            job_id: <p>The ID of the Job to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.delete_job_request.DeleteJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.delete_job_response.DeleteJobResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_job

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_job.async_delete_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.delete_job_request.DeleteJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "aws_sdk_drs.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.describe_jobs_response.DescribeJobsResponse":
        """<p>Returns a list of Jobs. Use the JobsID and fromDate and toDate filters to limit which jobs are returned. The response is sorted by creationDataTime - latest date first. Jobs are created by the StartRecovery, TerminateRecoveryInstances and StartFailbackLaunch APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to *Support* and only used in response to relevant support tickets.</p>

        Args:
            filters: <p>A set of filters by which to return Jobs.</p>
            max_results: <p>Maximum number of Jobs to retrieve.</p>
            next_token: <p>The token of the next Job to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.describe_jobs_request.DescribeJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.describe_jobs_response.DescribeJobsResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_jobs.async_describe_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_jobs_request.DescribeJobsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_job_log_items(
        self,
        job_id: "aws_sdk_drs.types.job_id.JobID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "aws_sdk_drs.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
    ):
        """<p>Retrieves a detailed Job log with pagination.</p>

        Args:
            job_id: <p>The ID of the Job for which Job log items will be retrieved.</p>
            max_results: <p>Maximum number of Job log items to retrieve.</p>
            next_token: <p>The token of the next Job log items to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.describe_job_log_items_request.DescribeJobLogItemsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_job_log_items

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_job_log_items.async_describe_job_log_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_job_log_items_request.DescribeJobLogItemsRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
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
