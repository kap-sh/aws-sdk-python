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
    import aws_sdk_bedrock.types.application_type
    import aws_sdk_bedrock.types.batch_delete_evaluation_job_request
    import aws_sdk_bedrock.types.batch_delete_evaluation_job_response
    import aws_sdk_bedrock.types.create_evaluation_job_request
    import aws_sdk_bedrock.types.create_evaluation_job_response
    import aws_sdk_bedrock.types.evaluation_config
    import aws_sdk_bedrock.types.evaluation_inference_config
    import aws_sdk_bedrock.types.evaluation_job_description
    import aws_sdk_bedrock.types.evaluation_job_identifier
    import aws_sdk_bedrock.types.evaluation_job_identifiers
    import aws_sdk_bedrock.types.evaluation_job_name
    import aws_sdk_bedrock.types.evaluation_job_status
    import aws_sdk_bedrock.types.evaluation_output_data_config
    import aws_sdk_bedrock.types.evaluation_summary
    import aws_sdk_bedrock.types.get_evaluation_job_request
    import aws_sdk_bedrock.types.get_evaluation_job_response
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.kms_key_id
    import aws_sdk_bedrock.types.list_evaluation_jobs_request
    import aws_sdk_bedrock.types.list_evaluation_jobs_response
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.role_arn
    import aws_sdk_bedrock.types.sort_jobs_by
    import aws_sdk_bedrock.types.sort_order
    import aws_sdk_bedrock.types.stop_evaluation_job_request
    import aws_sdk_bedrock.types.stop_evaluation_job_response
    import aws_sdk_bedrock.types.tag_list
    import aws_sdk_bedrock.types.timestamp
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class EvaluationJobResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def batch_delete_evaluation_job(
        self,
        job_identifiers: "aws_sdk_bedrock.types.evaluation_job_identifiers.EvaluationJobIdentifiers",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.batch_delete_evaluation_job_response.BatchDeleteEvaluationJobResponse":
        """<p>Deletes a batch of evaluation jobs. An evaluation job can only be deleted if it has following status <code>FAILED</code>, <code>COMPLETED</code>, and <code>STOPPED</code>. You can request up to 25 model evaluation jobs be deleted in a single request.</p>

        Args:
            job_identifiers: <p>A list of one or more evaluation job Amazon Resource Names (ARNs) you want to delete.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete evaluation jobs
            The following example shows a request to delete two model evaluation jobs, where one of the jobs is not found.

            >>> client.batch_delete_evaluation_job(job_identifiers=['arn:aws:bedrock:us-east-2:123456789012:evaluation-job/12rnxmplqv0v', 'arn:aws:bedrock:us-east-2:123456789012:evaluation-job/rispxmpl12rn'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.batch_delete_evaluation_job_request.BatchDeleteEvaluationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.batch_delete_evaluation_job_response.BatchDeleteEvaluationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_evaluation_job

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_evaluation_job.batch_delete_evaluation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.batch_delete_evaluation_job_request.BatchDeleteEvaluationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_identifiers"] = job_identifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_evaluation_job(
        self,
        job_name: "aws_sdk_bedrock.types.evaluation_job_name.EvaluationJobName",
        role_arn: "aws_sdk_bedrock.types.role_arn.RoleArn",
        evaluation_config: "aws_sdk_bedrock.types.evaluation_config.EvaluationConfig",
        inference_config: "aws_sdk_bedrock.types.evaluation_inference_config.EvaluationInferenceConfig",
        output_data_config: "aws_sdk_bedrock.types.evaluation_output_data_config.EvaluationOutputDataConfig",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        job_description: Optional[
            "aws_sdk_bedrock.types.evaluation_job_description.EvaluationJobDescription"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        customer_encryption_key_id: Optional[
            "aws_sdk_bedrock.types.kms_key_id.KmsKeyId"
        ] = None,
        job_tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
        application_type: Optional[
            "aws_sdk_bedrock.types.application_type.ApplicationType"
        ] = None,
    ) -> "aws_sdk_bedrock.types.create_evaluation_job_response.CreateEvaluationJobResponse":
        r"""<p>Creates an evaluation job.</p>

        Args:
            job_name: <p>A name for the evaluation job. Names must unique with your Amazon Web Services account, and your account's Amazon Web Services region.</p>
            job_description: <p>A description of the evaluation job.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. To learn more about the required permissions, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security.html\">Required permissions for model evaluations</a>.</p>
            customer_encryption_key_id: <p>Specify your customer managed encryption key Amazon Resource Name (ARN) that will be used to encrypt your evaluation job.</p>
            job_tags: <p>Tags to attach to the model evaluation job.</p>
            application_type: <p>Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).</p>
            evaluation_config: <p>Contains the configuration details of either an automated or human-based evaluation job.</p>
            inference_config: <p>Contains the configuration details of the inference model for the evaluation job.</p> <p>For model evaluation jobs, automated jobs support a single model or <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">inference profile</a>, and jobs that use human workers support two models or inference profiles.</p>
            output_data_config: <p>Contains the configuration details of the Amazon S3 bucket for storing the results of the evaluation job.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.create_evaluation_job_request.CreateEvaluationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.create_evaluation_job_response.CreateEvaluationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_evaluation_job

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_evaluation_job.create_evaluation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.create_evaluation_job_request.CreateEvaluationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
        if job_description is not None:
            input_["job_description"] = job_description
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        input_["role_arn"] = role_arn
        if customer_encryption_key_id is not None:
            input_["customer_encryption_key_id"] = customer_encryption_key_id
        if job_tags is not None:
            input_["job_tags"] = job_tags
        if application_type is not None:
            input_["application_type"] = application_type
        input_["evaluation_config"] = evaluation_config
        input_["inference_config"] = inference_config
        input_["output_data_config"] = output_data_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_evaluation_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_evaluation_job_response.GetEvaluationJobResponse":
        """<p>Gets information about an evaluation job, such as the status of the job.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the evaluation job you want get information on.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_evaluation_job_request.GetEvaluationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_evaluation_job_response.GetEvaluationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_evaluation_job

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_evaluation_job.get_evaluation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_evaluation_job_request.GetEvaluationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_identifier"] = job_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_evaluation_jobs(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        creation_time_after: Optional[
            "aws_sdk_bedrock.types.timestamp.Timestamp"
        ] = None,
        creation_time_before: Optional[
            "aws_sdk_bedrock.types.timestamp.Timestamp"
        ] = None,
        status_equals: Optional[
            "aws_sdk_bedrock.types.evaluation_job_status.EvaluationJobStatus"
        ] = None,
        application_type_equals: Optional[
            "aws_sdk_bedrock.types.application_type.ApplicationType"
        ] = None,
        name_contains: Optional[
            "aws_sdk_bedrock.types.evaluation_job_name.EvaluationJobName"
        ] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["aws_sdk_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["aws_sdk_bedrock.types.sort_order.SortOrder"] = None,
    ) -> (
        "aws_sdk_bedrock.types.list_evaluation_jobs_response.ListEvaluationJobsResponse"
    ):
        """<p>Lists all existing evaluation jobs.</p>

        Args:
            creation_time_after: <p>A filter to only list evaluation jobs created after a specified time.</p>
            creation_time_before: <p>A filter to only list evaluation jobs created before a specified time.</p>
            status_equals: <p>A filter to only list evaluation jobs that are of a certain status.</p>
            application_type_equals: <p>A filter to only list evaluation jobs that are either model evaluations or knowledge base evaluations.</p>
            name_contains: <p>A filter to only list evaluation jobs that contain a specified string in the job name.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>Continuation token from the previous response, for Amazon Bedrock to list the next set of results.</p>
            sort_by: <p>Specifies a creation time to sort the list of evaluation jobs by when they were created.</p>
            sort_order: <p>Specifies whether to sort the list of evaluation jobs by either ascending or descending order.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_evaluation_jobs_request.ListEvaluationJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_evaluation_jobs_response.ListEvaluationJobsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_evaluation_jobs

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_evaluation_jobs.list_evaluation_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.list_evaluation_jobs_request.ListEvaluationJobsRequest = {}  # type: ignore[typeddict-item]
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if application_type_equals is not None:
            input_["application_type_equals"] = application_type_equals
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

    def stop_evaluation_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.stop_evaluation_job_response.StopEvaluationJobResponse":
        """<p>Stops an evaluation job that is current being created or running.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the evaluation job you want to stop.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.stop_evaluation_job_request.StopEvaluationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.stop_evaluation_job_response.StopEvaluationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_evaluation_job

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_evaluation_job.stop_evaluation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.stop_evaluation_job_request.StopEvaluationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_identifier"] = job_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEvaluationJobResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def batch_delete_evaluation_job(
        self,
        job_identifiers: "aws_sdk_bedrock.types.evaluation_job_identifiers.EvaluationJobIdentifiers",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.batch_delete_evaluation_job_response.BatchDeleteEvaluationJobResponse":
        """<p>Deletes a batch of evaluation jobs. An evaluation job can only be deleted if it has following status <code>FAILED</code>, <code>COMPLETED</code>, and <code>STOPPED</code>. You can request up to 25 model evaluation jobs be deleted in a single request.</p>

        Args:
            job_identifiers: <p>A list of one or more evaluation job Amazon Resource Names (ARNs) you want to delete.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete evaluation jobs
            The following example shows a request to delete two model evaluation jobs, where one of the jobs is not found.

            >>> await client.batch_delete_evaluation_job(job_identifiers=['arn:aws:bedrock:us-east-2:123456789012:evaluation-job/12rnxmplqv0v', 'arn:aws:bedrock:us-east-2:123456789012:evaluation-job/rispxmpl12rn'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.batch_delete_evaluation_job_request.BatchDeleteEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.batch_delete_evaluation_job_response.BatchDeleteEvaluationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_evaluation_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_evaluation_job.async_batch_delete_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.batch_delete_evaluation_job_request.BatchDeleteEvaluationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_identifiers"] = job_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_evaluation_job(
        self,
        job_name: "aws_sdk_bedrock.types.evaluation_job_name.EvaluationJobName",
        role_arn: "aws_sdk_bedrock.types.role_arn.RoleArn",
        evaluation_config: "aws_sdk_bedrock.types.evaluation_config.EvaluationConfig",
        inference_config: "aws_sdk_bedrock.types.evaluation_inference_config.EvaluationInferenceConfig",
        output_data_config: "aws_sdk_bedrock.types.evaluation_output_data_config.EvaluationOutputDataConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        job_description: Optional[
            "aws_sdk_bedrock.types.evaluation_job_description.EvaluationJobDescription"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        customer_encryption_key_id: Optional[
            "aws_sdk_bedrock.types.kms_key_id.KmsKeyId"
        ] = None,
        job_tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
        application_type: Optional[
            "aws_sdk_bedrock.types.application_type.ApplicationType"
        ] = None,
    ) -> "aws_sdk_bedrock.types.create_evaluation_job_response.CreateEvaluationJobResponse":
        r"""<p>Creates an evaluation job.</p>

        Args:
            job_name: <p>A name for the evaluation job. Names must unique with your Amazon Web Services account, and your account's Amazon Web Services region.</p>
            job_description: <p>A description of the evaluation job.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. To learn more about the required permissions, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security.html\">Required permissions for model evaluations</a>.</p>
            customer_encryption_key_id: <p>Specify your customer managed encryption key Amazon Resource Name (ARN) that will be used to encrypt your evaluation job.</p>
            job_tags: <p>Tags to attach to the model evaluation job.</p>
            application_type: <p>Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).</p>
            evaluation_config: <p>Contains the configuration details of either an automated or human-based evaluation job.</p>
            inference_config: <p>Contains the configuration details of the inference model for the evaluation job.</p> <p>For model evaluation jobs, automated jobs support a single model or <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">inference profile</a>, and jobs that use human workers support two models or inference profiles.</p>
            output_data_config: <p>Contains the configuration details of the Amazon S3 bucket for storing the results of the evaluation job.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.create_evaluation_job_request.CreateEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.create_evaluation_job_response.CreateEvaluationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_evaluation_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_evaluation_job.async_create_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.create_evaluation_job_request.CreateEvaluationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_name"] = job_name
        if job_description is not None:
            input_["job_description"] = job_description
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        input_["role_arn"] = role_arn
        if customer_encryption_key_id is not None:
            input_["customer_encryption_key_id"] = customer_encryption_key_id
        if job_tags is not None:
            input_["job_tags"] = job_tags
        if application_type is not None:
            input_["application_type"] = application_type
        input_["evaluation_config"] = evaluation_config
        input_["inference_config"] = inference_config
        input_["output_data_config"] = output_data_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_evaluation_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_evaluation_job_response.GetEvaluationJobResponse":
        """<p>Gets information about an evaluation job, such as the status of the job.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the evaluation job you want get information on.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_evaluation_job_request.GetEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_evaluation_job_response.GetEvaluationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_evaluation_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_evaluation_job.async_get_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_evaluation_job_request.GetEvaluationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_identifier"] = job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_evaluation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional[
            "aws_sdk_bedrock.types.timestamp.Timestamp"
        ] = None,
        creation_time_before: Optional[
            "aws_sdk_bedrock.types.timestamp.Timestamp"
        ] = None,
        status_equals: Optional[
            "aws_sdk_bedrock.types.evaluation_job_status.EvaluationJobStatus"
        ] = None,
        application_type_equals: Optional[
            "aws_sdk_bedrock.types.application_type.ApplicationType"
        ] = None,
        name_contains: Optional[
            "aws_sdk_bedrock.types.evaluation_job_name.EvaluationJobName"
        ] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["aws_sdk_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["aws_sdk_bedrock.types.sort_order.SortOrder"] = None,
    ) -> (
        "aws_sdk_bedrock.types.list_evaluation_jobs_response.ListEvaluationJobsResponse"
    ):
        """<p>Lists all existing evaluation jobs.</p>

        Args:
            creation_time_after: <p>A filter to only list evaluation jobs created after a specified time.</p>
            creation_time_before: <p>A filter to only list evaluation jobs created before a specified time.</p>
            status_equals: <p>A filter to only list evaluation jobs that are of a certain status.</p>
            application_type_equals: <p>A filter to only list evaluation jobs that are either model evaluations or knowledge base evaluations.</p>
            name_contains: <p>A filter to only list evaluation jobs that contain a specified string in the job name.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>Continuation token from the previous response, for Amazon Bedrock to list the next set of results.</p>
            sort_by: <p>Specifies a creation time to sort the list of evaluation jobs by when they were created.</p>
            sort_order: <p>Specifies whether to sort the list of evaluation jobs by either ascending or descending order.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_evaluation_jobs_request.ListEvaluationJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_evaluation_jobs_response.ListEvaluationJobsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_evaluation_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_evaluation_jobs.async_list_evaluation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.list_evaluation_jobs_request.ListEvaluationJobsRequest = {}  # type: ignore[typeddict-item]
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if application_type_equals is not None:
            input_["application_type_equals"] = application_type_equals
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

    async def stop_evaluation_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.stop_evaluation_job_response.StopEvaluationJobResponse":
        """<p>Stops an evaluation job that is current being created or running.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the evaluation job you want to stop.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.stop_evaluation_job_request.StopEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.stop_evaluation_job_response.StopEvaluationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_evaluation_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_evaluation_job.async_stop_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.stop_evaluation_job_request.StopEvaluationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_identifier"] = job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
