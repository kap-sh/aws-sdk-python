from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_mgn._auth._signers
import aws_sdk_mgn._auth._sigv4
from aws_sdk_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.delete_job_request
    import aws_sdk_mgn.types.delete_job_response
    import aws_sdk_mgn.types.describe_job_log_items_request
    import aws_sdk_mgn.types.describe_job_log_items_response
    import aws_sdk_mgn.types.describe_jobs_request
    import aws_sdk_mgn.types.describe_jobs_request_filters
    import aws_sdk_mgn.types.describe_jobs_response
    import aws_sdk_mgn.types.job
    import aws_sdk_mgn.types.job_id
    import aws_sdk_mgn.types.job_log
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token
    from aws_sdk_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from aws_sdk_mgn._services.mgn import mgnClient, mgnClientConfig


class JobResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def delete(
        self,
        job_id: "aws_sdk_mgn.types.job_id.JobID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes a single Job by ID.</p>

        Args:
            job_id: <p>Request to delete Job from service by Job ID.</p>
            account_id: <p>Request to delete Job from service by Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.delete_job_request.DeleteJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.delete_job_response.DeleteJobResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.delete_job

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.delete_job.delete_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.delete_job_request.DeleteJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.describe_jobs_response.DescribeJobsResponse":
        """<p>Returns a list of Jobs. Use the JobsID and fromDate and toData filters to limit which jobs are returned. The response is sorted by creationDataTime - latest date first. Jobs are normally created by the StartTest, StartCutover, and TerminateTargetInstances APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to *Support* and only used in response to relevant support tickets.</p>

        Args:
            filters: <p>Request to describe Job log filters.</p>
            max_results: <p>Request to describe job log items by max results.</p>
            next_token: <p>Request to describe job log items by next token.</p>
            account_id: <p>Request to describe job log items by Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.describe_jobs_request.DescribeJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.describe_jobs_response.DescribeJobsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.describe_jobs

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.describe_jobs.describe_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.describe_jobs_request.DescribeJobsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_job_log_items(
        self,
        job_id: "aws_sdk_mgn.types.job_id.JobID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> (
        "aws_sdk_mgn.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
    ):
        """<p>Retrieves detailed job log items with paging.</p>

        Args:
            job_id: <p>Request to describe Job log job ID.</p>
            max_results: <p>Request to describe Job log item maximum results.</p>
            next_token: <p>Request to describe Job log next token.</p>
            account_id: <p>Request to describe Job log Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.describe_job_log_items_request.DescribeJobLogItemsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.describe_job_log_items

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.describe_job_log_items.describe_job_log_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.describe_job_log_items_request.DescribeJobLogItemsRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncJobResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def delete(
        self,
        job_id: "aws_sdk_mgn.types.job_id.JobID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes a single Job by ID.</p>

        Args:
            job_id: <p>Request to delete Job from service by Job ID.</p>
            account_id: <p>Request to delete Job from service by Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.delete_job_request.DeleteJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.delete_job_response.DeleteJobResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.delete_job

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.delete_job.async_delete_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.delete_job_request.DeleteJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.describe_jobs_response.DescribeJobsResponse":
        """<p>Returns a list of Jobs. Use the JobsID and fromDate and toData filters to limit which jobs are returned. The response is sorted by creationDataTime - latest date first. Jobs are normally created by the StartTest, StartCutover, and TerminateTargetInstances APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to *Support* and only used in response to relevant support tickets.</p>

        Args:
            filters: <p>Request to describe Job log filters.</p>
            max_results: <p>Request to describe job log items by max results.</p>
            next_token: <p>Request to describe job log items by next token.</p>
            account_id: <p>Request to describe job log items by Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.describe_jobs_request.DescribeJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.describe_jobs_response.DescribeJobsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.describe_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.describe_jobs.async_describe_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.describe_jobs_request.DescribeJobsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_job_log_items(
        self,
        job_id: "aws_sdk_mgn.types.job_id.JobID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> (
        "aws_sdk_mgn.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
    ):
        """<p>Retrieves detailed job log items with paging.</p>

        Args:
            job_id: <p>Request to describe Job log job ID.</p>
            max_results: <p>Request to describe Job log item maximum results.</p>
            next_token: <p>Request to describe Job log next token.</p>
            account_id: <p>Request to describe Job log Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.describe_job_log_items_request.DescribeJobLogItemsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.describe_job_log_items

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.describe_job_log_items.async_describe_job_log_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.describe_job_log_items_request.DescribeJobLogItemsRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
