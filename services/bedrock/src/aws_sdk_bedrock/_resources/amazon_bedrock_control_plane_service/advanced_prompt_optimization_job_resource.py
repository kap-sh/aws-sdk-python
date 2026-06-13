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
    import aws_sdk_bedrock.types.advanced_prompt_optimization_input_config
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_description
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifier
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifiers
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_name
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_summary
    import aws_sdk_bedrock.types.advanced_prompt_optimization_output_config
    import aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_request
    import aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_response
    import aws_sdk_bedrock.types.create_advanced_prompt_optimization_job_request
    import aws_sdk_bedrock.types.create_advanced_prompt_optimization_job_response
    import aws_sdk_bedrock.types.get_advanced_prompt_optimization_job_request
    import aws_sdk_bedrock.types.get_advanced_prompt_optimization_job_response
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.kms_key_arn
    import aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_request
    import aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.model_configurations
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.sort_jobs_by
    import aws_sdk_bedrock.types.sort_order
    import aws_sdk_bedrock.types.stop_advanced_prompt_optimization_job_request
    import aws_sdk_bedrock.types.stop_advanced_prompt_optimization_job_response
    import aws_sdk_bedrock.types.tag_list
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class AdvancedPromptOptimizationJobResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def batch_delete_advanced_prompt_optimization_job(
        self,
        job_identifiers: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifiers.AdvancedPromptOptimizationJobIdentifiers",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_response.BatchDeleteAdvancedPromptOptimizationJobResponse":
        """<p>Deletes one or more advanced prompt optimization jobs.</p>

        Args:
            job_identifiers: <p>A list of advanced prompt optimization job identifiers (ARNs or IDs) to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_request.BatchDeleteAdvancedPromptOptimizationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_response.BatchDeleteAdvancedPromptOptimizationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_advanced_prompt_optimization_job

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_advanced_prompt_optimization_job.batch_delete_advanced_prompt_optimization_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_request.BatchDeleteAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
        input["job_identifiers"] = job_identifiers

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_advanced_prompt_optimization_job(
        self,
        job_name: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_name.AdvancedPromptOptimizationJobName",
        input_config: "aws_sdk_bedrock.types.advanced_prompt_optimization_input_config.AdvancedPromptOptimizationInputConfig",
        output_config: "aws_sdk_bedrock.types.advanced_prompt_optimization_output_config.AdvancedPromptOptimizationOutputConfig",
        model_configurations: "aws_sdk_bedrock.types.model_configurations.ModelConfigurations",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        job_description: Optional[
            "aws_sdk_bedrock.types.advanced_prompt_optimization_job_description.AdvancedPromptOptimizationJobDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        encryption_key_arn: Optional[
            "aws_sdk_bedrock.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock.types.create_advanced_prompt_optimization_job_response.CreateAdvancedPromptOptimizationJobResponse":
        """<p>Creates an advanced prompt optimization job. The job optimizes your prompt templates for specific models using your evaluation dataset and criteria.</p>

        Args:
            job_name: <p>A name for the advanced prompt optimization job.</p>
            job_description: <p>A description of the advanced prompt optimization job.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>
            input_config: <p>Specifies the S3 location of your JSONL input file containing prompt templates and evaluation samples.</p>
            output_config: <p>Specifies the S3 location where optimization results will be stored.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used for encrypting the output data. If not specified, the output is encrypted with an Amazon-owned KMS key.</p>
            tags: <p>Tags to associate with the advanced prompt optimization job.</p>
            model_configurations: <p>A list of model configurations specifying the target models for prompt optimization. You can specify up to 5 models.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.create_advanced_prompt_optimization_job_request.CreateAdvancedPromptOptimizationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.create_advanced_prompt_optimization_job_response.CreateAdvancedPromptOptimizationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_advanced_prompt_optimization_job

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_advanced_prompt_optimization_job.create_advanced_prompt_optimization_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_advanced_prompt_optimization_job_request.CreateAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
        input["job_name"] = job_name
        if job_description is not None:
            input["job_description"] = job_description
        if client_token is not None:
            input["client_token"] = client_token
        input["input_config"] = input_config
        input["output_config"] = output_config
        if encryption_key_arn is not None:
            input["encryption_key_arn"] = encryption_key_arn
        if tags is not None:
            input["tags"] = tags
        input["model_configurations"] = model_configurations

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_advanced_prompt_optimization_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_advanced_prompt_optimization_job_response.GetAdvancedPromptOptimizationJobResponse":
        """<p>Gets information about an advanced prompt optimization job.</p>

        Args:
            job_identifier: <p>The ARN or ID of the advanced prompt optimization job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_advanced_prompt_optimization_job_request.GetAdvancedPromptOptimizationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_advanced_prompt_optimization_job_response.GetAdvancedPromptOptimizationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_advanced_prompt_optimization_job

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_advanced_prompt_optimization_job.get_advanced_prompt_optimization_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_advanced_prompt_optimization_job_request.GetAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
        input["job_identifier"] = job_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_advanced_prompt_optimization_jobs(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["aws_sdk_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["aws_sdk_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse":
        """<p>Lists the advanced prompt optimization jobs in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token in a subsequent request to get the next set of results.</p>
            sort_by: <p>The field to sort the results by.</p>
            sort_order: <p>The sort order for the results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_advanced_prompt_optimization_jobs

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_advanced_prompt_optimization_jobs.list_advanced_prompt_optimization_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort_by is not None:
            input["sort_by"] = sort_by
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_advanced_prompt_optimization_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.stop_advanced_prompt_optimization_job_response.StopAdvancedPromptOptimizationJobResponse":
        """<p>Stops an advanced prompt optimization job that is in progress.</p>

        Args:
            job_identifier: <p>The ARN or ID of the advanced prompt optimization job to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.stop_advanced_prompt_optimization_job_request.StopAdvancedPromptOptimizationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.stop_advanced_prompt_optimization_job_response.StopAdvancedPromptOptimizationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_advanced_prompt_optimization_job

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_advanced_prompt_optimization_job.stop_advanced_prompt_optimization_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.stop_advanced_prompt_optimization_job_request.StopAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
        input["job_identifier"] = job_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAdvancedPromptOptimizationJobResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def batch_delete_advanced_prompt_optimization_job(
        self,
        job_identifiers: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifiers.AdvancedPromptOptimizationJobIdentifiers",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_response.BatchDeleteAdvancedPromptOptimizationJobResponse":
        """<p>Deletes one or more advanced prompt optimization jobs.</p>

        Args:
            job_identifiers: <p>A list of advanced prompt optimization job identifiers (ARNs or IDs) to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_request.BatchDeleteAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_response.BatchDeleteAdvancedPromptOptimizationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_advanced_prompt_optimization_job.async_batch_delete_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.batch_delete_advanced_prompt_optimization_job_request.BatchDeleteAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
        input["job_identifiers"] = job_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_advanced_prompt_optimization_job(
        self,
        job_name: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_name.AdvancedPromptOptimizationJobName",
        input_config: "aws_sdk_bedrock.types.advanced_prompt_optimization_input_config.AdvancedPromptOptimizationInputConfig",
        output_config: "aws_sdk_bedrock.types.advanced_prompt_optimization_output_config.AdvancedPromptOptimizationOutputConfig",
        model_configurations: "aws_sdk_bedrock.types.model_configurations.ModelConfigurations",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        job_description: Optional[
            "aws_sdk_bedrock.types.advanced_prompt_optimization_job_description.AdvancedPromptOptimizationJobDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        encryption_key_arn: Optional[
            "aws_sdk_bedrock.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock.types.create_advanced_prompt_optimization_job_response.CreateAdvancedPromptOptimizationJobResponse":
        """<p>Creates an advanced prompt optimization job. The job optimizes your prompt templates for specific models using your evaluation dataset and criteria.</p>

        Args:
            job_name: <p>A name for the advanced prompt optimization job.</p>
            job_description: <p>A description of the advanced prompt optimization job.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>
            input_config: <p>Specifies the S3 location of your JSONL input file containing prompt templates and evaluation samples.</p>
            output_config: <p>Specifies the S3 location where optimization results will be stored.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used for encrypting the output data. If not specified, the output is encrypted with an Amazon-owned KMS key.</p>
            tags: <p>Tags to associate with the advanced prompt optimization job.</p>
            model_configurations: <p>A list of model configurations specifying the target models for prompt optimization. You can specify up to 5 models.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.create_advanced_prompt_optimization_job_request.CreateAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.create_advanced_prompt_optimization_job_response.CreateAdvancedPromptOptimizationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_advanced_prompt_optimization_job.async_create_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_advanced_prompt_optimization_job_request.CreateAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
        input["job_name"] = job_name
        if job_description is not None:
            input["job_description"] = job_description
        if client_token is not None:
            input["client_token"] = client_token
        input["input_config"] = input_config
        input["output_config"] = output_config
        if encryption_key_arn is not None:
            input["encryption_key_arn"] = encryption_key_arn
        if tags is not None:
            input["tags"] = tags
        input["model_configurations"] = model_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_advanced_prompt_optimization_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_advanced_prompt_optimization_job_response.GetAdvancedPromptOptimizationJobResponse":
        """<p>Gets information about an advanced prompt optimization job.</p>

        Args:
            job_identifier: <p>The ARN or ID of the advanced prompt optimization job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_advanced_prompt_optimization_job_request.GetAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_advanced_prompt_optimization_job_response.GetAdvancedPromptOptimizationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_advanced_prompt_optimization_job.async_get_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_advanced_prompt_optimization_job_request.GetAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
        input["job_identifier"] = job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_advanced_prompt_optimization_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["aws_sdk_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["aws_sdk_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse":
        """<p>Lists the advanced prompt optimization jobs in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token in a subsequent request to get the next set of results.</p>
            sort_by: <p>The field to sort the results by.</p>
            sort_order: <p>The sort order for the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_advanced_prompt_optimization_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_advanced_prompt_optimization_jobs.async_list_advanced_prompt_optimization_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort_by is not None:
            input["sort_by"] = sort_by
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_advanced_prompt_optimization_job(
        self,
        job_identifier: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.stop_advanced_prompt_optimization_job_response.StopAdvancedPromptOptimizationJobResponse":
        """<p>Stops an advanced prompt optimization job that is in progress.</p>

        Args:
            job_identifier: <p>The ARN or ID of the advanced prompt optimization job to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.stop_advanced_prompt_optimization_job_request.StopAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.stop_advanced_prompt_optimization_job_response.StopAdvancedPromptOptimizationJobResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.stop_advanced_prompt_optimization_job.async_stop_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.stop_advanced_prompt_optimization_job_request.StopAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
        input["job_identifier"] = job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
