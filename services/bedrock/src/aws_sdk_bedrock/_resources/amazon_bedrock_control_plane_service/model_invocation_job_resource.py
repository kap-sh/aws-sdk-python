from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock._auth._signers
import aws_sdk_bedrock._auth._sigv4
from aws_sdk_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.create_model_invocation_job_request
    import aws_sdk_bedrock.types.create_model_invocation_job_response
    import aws_sdk_bedrock.types.get_model_invocation_job_request
    import aws_sdk_bedrock.types.get_model_invocation_job_response
    import aws_sdk_bedrock.types.list_model_invocation_jobs_request
    import aws_sdk_bedrock.types.list_model_invocation_jobs_response
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.model_id
    import aws_sdk_bedrock.types.model_invocation_idempotency_token
    import aws_sdk_bedrock.types.model_invocation_job_identifier
    import aws_sdk_bedrock.types.model_invocation_job_input_data_config
    import aws_sdk_bedrock.types.model_invocation_job_name
    import aws_sdk_bedrock.types.model_invocation_job_output_data_config
    import aws_sdk_bedrock.types.model_invocation_job_status
    import aws_sdk_bedrock.types.model_invocation_job_summary
    import aws_sdk_bedrock.types.model_invocation_job_timeout_duration_in_hours
    import aws_sdk_bedrock.types.model_invocation_type
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.role_arn
    import aws_sdk_bedrock.types.sort_jobs_by
    import aws_sdk_bedrock.types.sort_order
    import aws_sdk_bedrock.types.stop_model_invocation_job_request
    import aws_sdk_bedrock.types.stop_model_invocation_job_response
    import aws_sdk_bedrock.types.tag_list
    import aws_sdk_bedrock.types.timestamp
    import aws_sdk_bedrock.types.vpc_config
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class ModelInvocationJobResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create_model_invocation_job(
        self,
        job_name: "aws_sdk_bedrock.types.model_invocation_job_name.ModelInvocationJobName",
        role_arn: "aws_sdk_bedrock.types.role_arn.RoleArn",
        model_id: "aws_sdk_bedrock.types.model_id.ModelId",
        input_data_config: "aws_sdk_bedrock.types.model_invocation_job_input_data_config.ModelInvocationJobInputDataConfig",
        output_data_config: "aws_sdk_bedrock.types.model_invocation_job_output_data_config.ModelInvocationJobOutputDataConfig",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.model_invocation_idempotency_token.ModelInvocationIdempotencyToken"
        ] = None,
        vpc_config: Optional["aws_sdk_bedrock.types.vpc_config.VpcConfig"] = None,
        timeout_duration_in_hours: Optional[
            "aws_sdk_bedrock.types.model_invocation_job_timeout_duration_in_hours.ModelInvocationJobTimeoutDurationInHours"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
        model_invocation_type: Optional[
            "aws_sdk_bedrock.types.model_invocation_type.ModelInvocationType"
        ] = None,
    ) -> "aws_sdk_bedrock.types.create_model_invocation_job_response.CreateModelInvocationJobResponse":
        r"""<p>Creates a batch inference job to invoke a model on multiple prompts. Format your data according to <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data\">Format your inference data</a> and upload it to an Amazon S3 bucket. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html\">Process multiple prompts with batch inference</a>.</p> <p>The response returns a <code>jobArn</code> that you can use to stop or get details about the job.</p>

        Args:
            job_name: <p>A name to give the batch inference job.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html\">Create a service role for batch inference</a>.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            model_id: <p>The unique identifier of the foundation model to use for the batch inference job.</p>
            input_data_config: <p>Details about the location of the input to the batch inference job.</p>
            output_data_config: <p>Details about the location of the output of the batch inference job.</p>
            vpc_config: <p>The configuration of the Virtual Private Cloud (VPC) for the data in the batch inference job. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-vpc\">Protect batch inference jobs using a VPC</a>.</p>
            timeout_duration_in_hours: <p>The number of hours after which to force the batch inference job to time out.</p>
            tags: <p>Any tags to associate with the batch inference job. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html\">Tagging Amazon Bedrock resources</a>.</p>
            model_invocation_type: <p>The invocation endpoint for ModelInvocationJob</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.create_model_invocation_job_request.CreateModelInvocationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.create_model_invocation_job_response.CreateModelInvocationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_model_invocation_job

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_model_invocation_job.create_model_invocation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.create_model_invocation_job_request.CreateModelInvocationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
        input_["role_arn"] = role_arn
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        input_["model_id"] = model_id
        input_["input_data_config"] = input_data_config
        input_["output_data_config"] = output_data_config
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if timeout_duration_in_hours is not None:
            input_["timeout_duration_in_hours"] = timeout_duration_in_hours
        if tags is not None:
            input_["tags"] = tags
        if model_invocation_type is not None:
            input_["model_invocation_type"] = model_invocation_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_model_invocation_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.model_invocation_job_identifier.ModelInvocationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_model_invocation_job_response.GetModelInvocationJobResponse":
        r"""<p>Gets details about a batch inference job. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-monitor\">Monitor batch inference jobs</a> </p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the batch inference job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_model_invocation_job_request.GetModelInvocationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_model_invocation_job_response.GetModelInvocationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_job

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_job.get_model_invocation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_model_invocation_job_request.GetModelInvocationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_identifier"] = job_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_model_invocation_jobs(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        submit_time_after: Optional["aws_sdk_bedrock.types.timestamp.Timestamp"] = None,
        submit_time_before: Optional[
            "aws_sdk_bedrock.types.timestamp.Timestamp"
        ] = None,
        status_equals: Optional[
            "aws_sdk_bedrock.types.model_invocation_job_status.ModelInvocationJobStatus"
        ] = None,
        name_contains: Optional[
            "aws_sdk_bedrock.types.model_invocation_job_name.ModelInvocationJobName"
        ] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["aws_sdk_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["aws_sdk_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_bedrock.types.list_model_invocation_jobs_response.ListModelInvocationJobsResponse":
        r"""<p>Lists all batch inference jobs in the account. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-view.html\">View details about a batch inference job</a>.</p>

        Args:
            submit_time_after: <p>Specify a time to filter for batch inference jobs that were submitted after the time you specify.</p>
            submit_time_before: <p>Specify a time to filter for batch inference jobs that were submitted before the time you specify.</p>
            status_equals: <p>Specify a status to filter for batch inference jobs whose statuses match the string you specify.</p> <p>The following statuses are possible:</p> <ul> <li> <p>Submitted – This job has been submitted to a queue for validation.</p> </li> <li> <p>Validating – This job is being validated for the requirements described in <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html\">Format and upload your batch inference data</a>. The criteria include the following:</p> <ul> <li> <p>Your IAM service role has access to the Amazon S3 buckets containing your files.</p> </li> <li> <p>Your files are .jsonl files and each individual record is a JSON object in the correct format. Note that validation doesn't check if the <code>modelInput</code> value matches the request body for the model.</p> </li> <li> <p>Your files fulfill the requirements for file size and number of records. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html\">Quotas for Amazon Bedrock</a>.</p> </li> </ul> </li> <li> <p>Scheduled – This job has been validated and is now in a queue. The job will automatically start when it reaches its turn.</p> </li> <li> <p>Expired – This job timed out because it was scheduled but didn't begin before the set timeout duration. Submit a new job request.</p> </li> <li> <p>InProgress – This job has begun. You can start viewing the results in the output S3 location.</p> </li> <li> <p>Completed – This job has successfully completed. View the output files in the output S3 location.</p> </li> <li> <p>PartiallyCompleted – This job has partially completed. Not all of your records could be processed in time. View the output files in the output S3 location.</p> </li> <li> <p>Failed – This job has failed. Check the failure message for any further details. For further assistance, reach out to the <a href=\"https://console.aws.amazon.com/support/home/\">Amazon Web Services Support Center</a>.</p> </li> <li> <p>Stopped – This job was stopped by a user.</p> </li> <li> <p>Stopping – This job is being stopped by a user.</p> </li> </ul>
            name_contains: <p>Specify a string to filter for batch inference jobs whose names contain the string.</p>
            max_results: <p>The maximum number of results to return. If there are more results than the number that you specify, a <code>nextToken</code> value is returned. Use the <code>nextToken</code> in a request to return the next batch of results.</p>
            next_token: <p>If there were more results than the value you specified in the <code>maxResults</code> field in a previous <code>ListModelInvocationJobs</code> request, the response would have returned a <code>nextToken</code> value. To see the next batch of results, send the <code>nextToken</code> value in another request.</p>
            sort_by: <p>An attribute by which to sort the results.</p>
            sort_order: <p>Specifies whether to sort the results by ascending or descending order.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_model_invocation_jobs_request.ListModelInvocationJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_model_invocation_jobs_response.ListModelInvocationJobsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_model_invocation_jobs

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_model_invocation_jobs.list_model_invocation_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.list_model_invocation_jobs_request.ListModelInvocationJobsRequest = {}  # type: ignore[typeddict-item]
        if submit_time_after is not None:
            input_["submit_time_after"] = submit_time_after
        if submit_time_before is not None:
            input_["submit_time_before"] = submit_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_model_invocation_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.model_invocation_job_identifier.ModelInvocationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.stop_model_invocation_job_response.StopModelInvocationJobResponse":
        r"""<p>Stops a batch inference job. You're only charged for tokens that were already processed. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-stop.html\">Stop a batch inference job</a>.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the batch inference job to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.stop_model_invocation_job_request.StopModelInvocationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.stop_model_invocation_job_response.StopModelInvocationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_invocation_job

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_invocation_job.stop_model_invocation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.stop_model_invocation_job_request.StopModelInvocationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_identifier"] = job_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncModelInvocationJobResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create_model_invocation_job(
        self,
        job_name: "aws_sdk_bedrock.types.model_invocation_job_name.ModelInvocationJobName",
        role_arn: "aws_sdk_bedrock.types.role_arn.RoleArn",
        model_id: "aws_sdk_bedrock.types.model_id.ModelId",
        input_data_config: "aws_sdk_bedrock.types.model_invocation_job_input_data_config.ModelInvocationJobInputDataConfig",
        output_data_config: "aws_sdk_bedrock.types.model_invocation_job_output_data_config.ModelInvocationJobOutputDataConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.model_invocation_idempotency_token.ModelInvocationIdempotencyToken"
        ] = None,
        vpc_config: Optional["aws_sdk_bedrock.types.vpc_config.VpcConfig"] = None,
        timeout_duration_in_hours: Optional[
            "aws_sdk_bedrock.types.model_invocation_job_timeout_duration_in_hours.ModelInvocationJobTimeoutDurationInHours"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
        model_invocation_type: Optional[
            "aws_sdk_bedrock.types.model_invocation_type.ModelInvocationType"
        ] = None,
    ) -> "aws_sdk_bedrock.types.create_model_invocation_job_response.CreateModelInvocationJobResponse":
        r"""<p>Creates a batch inference job to invoke a model on multiple prompts. Format your data according to <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data\">Format your inference data</a> and upload it to an Amazon S3 bucket. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html\">Process multiple prompts with batch inference</a>.</p> <p>The response returns a <code>jobArn</code> that you can use to stop or get details about the job.</p>

        Args:
            job_name: <p>A name to give the batch inference job.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html\">Create a service role for batch inference</a>.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            model_id: <p>The unique identifier of the foundation model to use for the batch inference job.</p>
            input_data_config: <p>Details about the location of the input to the batch inference job.</p>
            output_data_config: <p>Details about the location of the output of the batch inference job.</p>
            vpc_config: <p>The configuration of the Virtual Private Cloud (VPC) for the data in the batch inference job. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-vpc\">Protect batch inference jobs using a VPC</a>.</p>
            timeout_duration_in_hours: <p>The number of hours after which to force the batch inference job to time out.</p>
            tags: <p>Any tags to associate with the batch inference job. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html\">Tagging Amazon Bedrock resources</a>.</p>
            model_invocation_type: <p>The invocation endpoint for ModelInvocationJob</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.create_model_invocation_job_request.CreateModelInvocationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.create_model_invocation_job_response.CreateModelInvocationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_model_invocation_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_model_invocation_job.async_create_model_invocation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.create_model_invocation_job_request.CreateModelInvocationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
        input_["role_arn"] = role_arn
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        input_["model_id"] = model_id
        input_["input_data_config"] = input_data_config
        input_["output_data_config"] = output_data_config
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if timeout_duration_in_hours is not None:
            input_["timeout_duration_in_hours"] = timeout_duration_in_hours
        if tags is not None:
            input_["tags"] = tags
        if model_invocation_type is not None:
            input_["model_invocation_type"] = model_invocation_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_model_invocation_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.model_invocation_job_identifier.ModelInvocationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_model_invocation_job_response.GetModelInvocationJobResponse":
        r"""<p>Gets details about a batch inference job. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-monitor\">Monitor batch inference jobs</a> </p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the batch inference job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_model_invocation_job_request.GetModelInvocationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_model_invocation_job_response.GetModelInvocationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_job.async_get_model_invocation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_model_invocation_job_request.GetModelInvocationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_identifier"] = job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_model_invocation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        submit_time_after: Optional["aws_sdk_bedrock.types.timestamp.Timestamp"] = None,
        submit_time_before: Optional[
            "aws_sdk_bedrock.types.timestamp.Timestamp"
        ] = None,
        status_equals: Optional[
            "aws_sdk_bedrock.types.model_invocation_job_status.ModelInvocationJobStatus"
        ] = None,
        name_contains: Optional[
            "aws_sdk_bedrock.types.model_invocation_job_name.ModelInvocationJobName"
        ] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["aws_sdk_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["aws_sdk_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_bedrock.types.list_model_invocation_jobs_response.ListModelInvocationJobsResponse":
        r"""<p>Lists all batch inference jobs in the account. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-view.html\">View details about a batch inference job</a>.</p>

        Args:
            submit_time_after: <p>Specify a time to filter for batch inference jobs that were submitted after the time you specify.</p>
            submit_time_before: <p>Specify a time to filter for batch inference jobs that were submitted before the time you specify.</p>
            status_equals: <p>Specify a status to filter for batch inference jobs whose statuses match the string you specify.</p> <p>The following statuses are possible:</p> <ul> <li> <p>Submitted – This job has been submitted to a queue for validation.</p> </li> <li> <p>Validating – This job is being validated for the requirements described in <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html\">Format and upload your batch inference data</a>. The criteria include the following:</p> <ul> <li> <p>Your IAM service role has access to the Amazon S3 buckets containing your files.</p> </li> <li> <p>Your files are .jsonl files and each individual record is a JSON object in the correct format. Note that validation doesn't check if the <code>modelInput</code> value matches the request body for the model.</p> </li> <li> <p>Your files fulfill the requirements for file size and number of records. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html\">Quotas for Amazon Bedrock</a>.</p> </li> </ul> </li> <li> <p>Scheduled – This job has been validated and is now in a queue. The job will automatically start when it reaches its turn.</p> </li> <li> <p>Expired – This job timed out because it was scheduled but didn't begin before the set timeout duration. Submit a new job request.</p> </li> <li> <p>InProgress – This job has begun. You can start viewing the results in the output S3 location.</p> </li> <li> <p>Completed – This job has successfully completed. View the output files in the output S3 location.</p> </li> <li> <p>PartiallyCompleted – This job has partially completed. Not all of your records could be processed in time. View the output files in the output S3 location.</p> </li> <li> <p>Failed – This job has failed. Check the failure message for any further details. For further assistance, reach out to the <a href=\"https://console.aws.amazon.com/support/home/\">Amazon Web Services Support Center</a>.</p> </li> <li> <p>Stopped – This job was stopped by a user.</p> </li> <li> <p>Stopping – This job is being stopped by a user.</p> </li> </ul>
            name_contains: <p>Specify a string to filter for batch inference jobs whose names contain the string.</p>
            max_results: <p>The maximum number of results to return. If there are more results than the number that you specify, a <code>nextToken</code> value is returned. Use the <code>nextToken</code> in a request to return the next batch of results.</p>
            next_token: <p>If there were more results than the value you specified in the <code>maxResults</code> field in a previous <code>ListModelInvocationJobs</code> request, the response would have returned a <code>nextToken</code> value. To see the next batch of results, send the <code>nextToken</code> value in another request.</p>
            sort_by: <p>An attribute by which to sort the results.</p>
            sort_order: <p>Specifies whether to sort the results by ascending or descending order.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_model_invocation_jobs_request.ListModelInvocationJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_model_invocation_jobs_response.ListModelInvocationJobsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_model_invocation_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_model_invocation_jobs.async_list_model_invocation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.list_model_invocation_jobs_request.ListModelInvocationJobsRequest = {}  # type: ignore[typeddict-item]
        if submit_time_after is not None:
            input_["submit_time_after"] = submit_time_after
        if submit_time_before is not None:
            input_["submit_time_before"] = submit_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_model_invocation_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.model_invocation_job_identifier.ModelInvocationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.stop_model_invocation_job_response.StopModelInvocationJobResponse":
        r"""<p>Stops a batch inference job. You're only charged for tokens that were already processed. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-stop.html\">Stop a batch inference job</a>.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the batch inference job to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.stop_model_invocation_job_request.StopModelInvocationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.stop_model_invocation_job_response.StopModelInvocationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_invocation_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_invocation_job.async_stop_model_invocation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.stop_model_invocation_job_request.StopModelInvocationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_identifier"] = job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
