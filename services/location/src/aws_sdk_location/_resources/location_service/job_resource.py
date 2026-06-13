from typing import TYPE_CHECKING, Optional

import aws_sdk_location._auth._signers
import aws_sdk_location._auth._sigv4
from aws_sdk_location._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_location.types.cancel_job_request
    import aws_sdk_location.types.cancel_job_response
    import aws_sdk_location.types.client_token
    import aws_sdk_location.types.get_job_request
    import aws_sdk_location.types.get_job_response
    import aws_sdk_location.types.iam_role_arn
    import aws_sdk_location.types.job_action
    import aws_sdk_location.types.job_action_options
    import aws_sdk_location.types.job_id
    import aws_sdk_location.types.job_input_options
    import aws_sdk_location.types.job_output_options
    import aws_sdk_location.types.jobs_filter
    import aws_sdk_location.types.large_token
    import aws_sdk_location.types.list_jobs_request
    import aws_sdk_location.types.list_jobs_response
    import aws_sdk_location.types.list_jobs_response_entry
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.start_job_request
    import aws_sdk_location.types.start_job_response
    import aws_sdk_location.types.tag_map
    from aws_sdk_location._services.async_location import (
        AsyncLocationClient,
        AsyncLocationClientConfig,
    )
    from aws_sdk_location._services.location import LocationClient, LocationClientConfig


class JobResource:
    def __init__(self, service: LocationClient) -> None:
        self._service = service

    def create(
        self,
        action: "aws_sdk_location.types.job_action.JobAction",
        execution_role_arn: "aws_sdk_location.types.iam_role_arn.IamRoleArn",
        input_options: "aws_sdk_location.types.job_input_options.JobInputOptions",
        output_options: "aws_sdk_location.types.job_output_options.JobOutputOptions",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_location.types.client_token.ClientToken"
        ] = None,
        action_options: Optional[
            "aws_sdk_location.types.job_action_options.JobActionOptions"
        ] = None,
        name: Optional["aws_sdk_location.types.resource_name.ResourceName"] = None,
        tags: Optional["aws_sdk_location.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_location.types.start_job_response.StartJobResponse":
        """<p> <code>StartJob</code> starts a new asynchronous bulk processing job. You specify the input data location in Amazon S3, the action to perform, and the output location where results are written.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html\">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            client_token: <p>A unique identifier for this request to ensure idempotency.</p>
            action: <p>The action to perform on the input data.</p>
            action_options: <p>Additional parameters that can be requested for each result.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that Amazon Location Service assumes during job processing. Amazon Location Service uses this role to access the input and output locations specified for the job.</p> <note> <p>The IAM role must be created in the same Amazon Web Services account where you plan to run your job.</p> </note> <p>For more information about configuring IAM roles for Amazon Location jobs, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/configure-iam-role-policy-credentials.html\">Configure IAM permissions</a> in the <i>Amazon Location Service Developer Guide</i>.</p>
            input_options: <p>Configuration for input data location and format.</p> <note> <p>Input files have a limitation of 10gb per file, and 1gb per Parquet row-group within the file.</p> </note>
            name: <p>An optional name for the job resource.</p>
            output_options: <p>Configuration for output data location and format.</p>
            tags: <p>Tags and corresponding values to be associated with the job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_location.types.start_job_request.StartJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_location.types.start_job_response.StartJobResponse"
        ]:
            import aws_sdk_location._operations.location_service.start_job

            output, http_response = (
                aws_sdk_location._operations.location_service.start_job.start_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_location.types.start_job_request.StartJobRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["action"] = action
        if action_options is not None:
            input["action_options"] = action_options
        input["execution_role_arn"] = execution_role_arn
        input["input_options"] = input_options
        if name is not None:
            input["name"] = name
        input["output_options"] = output_options
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        job_id: "aws_sdk_location.types.job_id.JobId",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "aws_sdk_location.types.get_job_response.GetJobResponse":
        """<p> <code>GetJob</code> retrieves detailed information about a specific job, including its current status, configuration, and error information if the job failed.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html\">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            job_id: <p>The unique identifier of the job to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_location.types.get_job_request.GetJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_location.types.get_job_response.GetJobResponse"
        ]:
            import aws_sdk_location._operations.location_service.get_job

            output, http_response = (
                aws_sdk_location._operations.location_service.get_job.get_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_location.types.get_job_request.GetJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        filter: Optional["aws_sdk_location.types.jobs_filter.JobsFilter"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_location.types.large_token.LargeToken"] = None,
    ) -> "aws_sdk_location.types.list_jobs_response.ListJobsResponse":
        """<p> <code>ListJobs</code> retrieves a list of jobs with optional filtering and pagination support.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html\">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            filter: <p>An optional structure containing criteria by which to filter job results.</p>
            max_results: <p>Maximum number of jobs to return.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_location.types.list_jobs_request.ListJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_location.types.list_jobs_response.ListJobsResponse"
        ]:
            import aws_sdk_location._operations.location_service.list_jobs

            output, http_response = (
                aws_sdk_location._operations.location_service.list_jobs.list_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_location.types.list_jobs_request.ListJobsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input["filter"] = filter
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_job(
        self,
        job_id: "aws_sdk_location.types.job_id.JobId",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "aws_sdk_location.types.cancel_job_response.CancelJobResponse":
        """<p> <code>CancelJob</code> cancels a job that is currently running or pending. If the job is already in a terminal state (<code>Completed</code>, <code>Failed</code>, or <code>Cancelled</code>), the operation returns successfully with the current status.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html\">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            job_id: <p>The unique identifier of the job to cancel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_location.types.cancel_job_request.CancelJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_location.types.cancel_job_response.CancelJobResponse"
        ]:
            import aws_sdk_location._operations.location_service.cancel_job

            output, http_response = (
                aws_sdk_location._operations.location_service.cancel_job.cancel_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_location.types.cancel_job_request.CancelJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncJobResource:
    def __init__(self, service: AsyncLocationClient) -> None:
        self._service = service

    async def create(
        self,
        action: "aws_sdk_location.types.job_action.JobAction",
        execution_role_arn: "aws_sdk_location.types.iam_role_arn.IamRoleArn",
        input_options: "aws_sdk_location.types.job_input_options.JobInputOptions",
        output_options: "aws_sdk_location.types.job_output_options.JobOutputOptions",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_location.types.client_token.ClientToken"
        ] = None,
        action_options: Optional[
            "aws_sdk_location.types.job_action_options.JobActionOptions"
        ] = None,
        name: Optional["aws_sdk_location.types.resource_name.ResourceName"] = None,
        tags: Optional["aws_sdk_location.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_location.types.start_job_response.StartJobResponse":
        """<p> <code>StartJob</code> starts a new asynchronous bulk processing job. You specify the input data location in Amazon S3, the action to perform, and the output location where results are written.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html\">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            client_token: <p>A unique identifier for this request to ensure idempotency.</p>
            action: <p>The action to perform on the input data.</p>
            action_options: <p>Additional parameters that can be requested for each result.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that Amazon Location Service assumes during job processing. Amazon Location Service uses this role to access the input and output locations specified for the job.</p> <note> <p>The IAM role must be created in the same Amazon Web Services account where you plan to run your job.</p> </note> <p>For more information about configuring IAM roles for Amazon Location jobs, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/configure-iam-role-policy-credentials.html\">Configure IAM permissions</a> in the <i>Amazon Location Service Developer Guide</i>.</p>
            input_options: <p>Configuration for input data location and format.</p> <note> <p>Input files have a limitation of 10gb per file, and 1gb per Parquet row-group within the file.</p> </note>
            name: <p>An optional name for the job resource.</p>
            output_options: <p>Configuration for output data location and format.</p>
            tags: <p>Tags and corresponding values to be associated with the job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_location.types.start_job_request.StartJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_location.types.start_job_response.StartJobResponse"
        ]:
            import aws_sdk_location._operations.location_service.start_job

            (
                output,
                http_response,
            ) = await aws_sdk_location._operations.location_service.start_job.async_start_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_location.types.start_job_request.StartJobRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["action"] = action
        if action_options is not None:
            input["action_options"] = action_options
        input["execution_role_arn"] = execution_role_arn
        input["input_options"] = input_options
        if name is not None:
            input["name"] = name
        input["output_options"] = output_options
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        job_id: "aws_sdk_location.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
    ) -> "aws_sdk_location.types.get_job_response.GetJobResponse":
        """<p> <code>GetJob</code> retrieves detailed information about a specific job, including its current status, configuration, and error information if the job failed.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html\">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            job_id: <p>The unique identifier of the job to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_location.types.get_job_request.GetJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_location.types.get_job_response.GetJobResponse"
        ]:
            import aws_sdk_location._operations.location_service.get_job

            (
                output,
                http_response,
            ) = await aws_sdk_location._operations.location_service.get_job.async_get_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_location.types.get_job_request.GetJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        filter: Optional["aws_sdk_location.types.jobs_filter.JobsFilter"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_location.types.large_token.LargeToken"] = None,
    ) -> "aws_sdk_location.types.list_jobs_response.ListJobsResponse":
        """<p> <code>ListJobs</code> retrieves a list of jobs with optional filtering and pagination support.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html\">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            filter: <p>An optional structure containing criteria by which to filter job results.</p>
            max_results: <p>Maximum number of jobs to return.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_location.types.list_jobs_request.ListJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_location.types.list_jobs_response.ListJobsResponse"
        ]:
            import aws_sdk_location._operations.location_service.list_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_location._operations.location_service.list_jobs.async_list_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_location.types.list_jobs_request.ListJobsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input["filter"] = filter
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_job(
        self,
        job_id: "aws_sdk_location.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
    ) -> "aws_sdk_location.types.cancel_job_response.CancelJobResponse":
        """<p> <code>CancelJob</code> cancels a job that is currently running or pending. If the job is already in a terminal state (<code>Completed</code>, <code>Failed</code>, or <code>Cancelled</code>), the operation returns successfully with the current status.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html\">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            job_id: <p>The unique identifier of the job to cancel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_location.types.cancel_job_request.CancelJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_location.types.cancel_job_response.CancelJobResponse"
        ]:
            import aws_sdk_location._operations.location_service.cancel_job

            (
                output,
                http_response,
            ) = await aws_sdk_location._operations.location_service.cancel_job.async_cancel_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_location.types.cancel_job_request.CancelJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
