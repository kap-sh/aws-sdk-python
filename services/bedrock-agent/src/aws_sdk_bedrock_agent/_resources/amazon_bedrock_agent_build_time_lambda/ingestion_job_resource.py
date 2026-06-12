from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agent._auth._signers
import aws_sdk_bedrock_agent._auth._sigv4
from aws_sdk_bedrock_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.get_ingestion_job_request
    import aws_sdk_bedrock_agent.types.get_ingestion_job_response
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.ingestion_job_filters
    import aws_sdk_bedrock_agent.types.ingestion_job_sort_by
    import aws_sdk_bedrock_agent.types.ingestion_job_summary
    import aws_sdk_bedrock_agent.types.list_ingestion_jobs_request
    import aws_sdk_bedrock_agent.types.list_ingestion_jobs_response
    import aws_sdk_bedrock_agent.types.max_results
    import aws_sdk_bedrock_agent.types.next_token
    import aws_sdk_bedrock_agent.types.start_ingestion_job_request
    import aws_sdk_bedrock_agent.types.start_ingestion_job_response
    import aws_sdk_bedrock_agent.types.stop_ingestion_job_request
    import aws_sdk_bedrock_agent.types.stop_ingestion_job_response
    from aws_sdk_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from aws_sdk_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class IngestionJobResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def get_ingestion_job(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        ingestion_job_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock_agent.types.get_ingestion_job_response.GetIngestionJobResponse"
    ):
        """<p>Gets information about a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job you want to get information on.</p>
            data_source_id: <p>The unique identifier of the data source for the data ingestion job you want to get information on.</p>
            ingestion_job_id: <p>The unique identifier of the data ingestion job you want to get information on.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.get_ingestion_job_request.GetIngestionJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.get_ingestion_job_response.GetIngestionJobResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_ingestion_job

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_ingestion_job.get_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.get_ingestion_job_request.GetIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input["knowledge_base_id"] = knowledge_base_id
        input["data_source_id"] = data_source_id
        input["ingestion_job_id"] = ingestion_job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_ingestion_jobs(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        filters: Optional[
            "aws_sdk_bedrock_agent.types.ingestion_job_filters.IngestionJobFilters"
        ] = None,
        sort_by: Optional[
            "aws_sdk_bedrock_agent.types.ingestion_job_sort_by.IngestionJobSortBy"
        ] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_ingestion_jobs_response.ListIngestionJobsResponse":
        """<p>Lists the data ingestion jobs for a data source. The list also includes information about each job.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the list of data ingestion jobs.</p>
            data_source_id: <p>The unique identifier of the data source for the list of data ingestion jobs.</p>
            filters: <p>Contains information about the filters for filtering the data.</p>
            sort_by: <p>Contains details about how to sort the data.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.list_ingestion_jobs_request.ListIngestionJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.list_ingestion_jobs_response.ListIngestionJobsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_ingestion_jobs

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_ingestion_jobs.list_ingestion_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.list_ingestion_jobs_request.ListIngestionJobsRequest = {}  # type: ignore[typeddict-item]
        input["knowledge_base_id"] = knowledge_base_id
        input["data_source_id"] = data_source_id
        if filters is not None:
            input["filters"] = filters
        if sort_by is not None:
            input["sort_by"] = sort_by
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

    def start_ingestion_job(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.description.Description"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.start_ingestion_job_response.StartIngestionJobResponse":
        """<p>Begins a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job.</p>
            data_source_id: <p>The unique identifier of the data source you want to ingest into your knowledge base.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            description: <p>A description of the data ingestion job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.start_ingestion_job_request.StartIngestionJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.start_ingestion_job_response.StartIngestionJobResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.start_ingestion_job

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.start_ingestion_job.start_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.start_ingestion_job_request.StartIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input["knowledge_base_id"] = knowledge_base_id
        input["data_source_id"] = data_source_id
        if client_token is not None:
            input["client_token"] = client_token
        if description is not None:
            input["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_ingestion_job(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        ingestion_job_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.stop_ingestion_job_response.StopIngestionJobResponse":
        """<p>Stops a currently running data ingestion job. You can send a <code>StartIngestionJob</code> request again to ingest the rest of your data when you are ready.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job you want to stop.</p>
            data_source_id: <p>The unique identifier of the data source for the data ingestion job you want to stop.</p>
            ingestion_job_id: <p>The unique identifier of the data ingestion job you want to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.stop_ingestion_job_request.StopIngestionJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.stop_ingestion_job_response.StopIngestionJobResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.stop_ingestion_job

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.stop_ingestion_job.stop_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.stop_ingestion_job_request.StopIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input["knowledge_base_id"] = knowledge_base_id
        input["data_source_id"] = data_source_id
        input["ingestion_job_id"] = ingestion_job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncIngestionJobResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def get_ingestion_job(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        ingestion_job_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock_agent.types.get_ingestion_job_response.GetIngestionJobResponse"
    ):
        """<p>Gets information about a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job you want to get information on.</p>
            data_source_id: <p>The unique identifier of the data source for the data ingestion job you want to get information on.</p>
            ingestion_job_id: <p>The unique identifier of the data ingestion job you want to get information on.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.get_ingestion_job_request.GetIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.get_ingestion_job_response.GetIngestionJobResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_ingestion_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_ingestion_job.async_get_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.get_ingestion_job_request.GetIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input["knowledge_base_id"] = knowledge_base_id
        input["data_source_id"] = data_source_id
        input["ingestion_job_id"] = ingestion_job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_ingestion_jobs(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        filters: Optional[
            "aws_sdk_bedrock_agent.types.ingestion_job_filters.IngestionJobFilters"
        ] = None,
        sort_by: Optional[
            "aws_sdk_bedrock_agent.types.ingestion_job_sort_by.IngestionJobSortBy"
        ] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_ingestion_jobs_response.ListIngestionJobsResponse":
        """<p>Lists the data ingestion jobs for a data source. The list also includes information about each job.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the list of data ingestion jobs.</p>
            data_source_id: <p>The unique identifier of the data source for the list of data ingestion jobs.</p>
            filters: <p>Contains information about the filters for filtering the data.</p>
            sort_by: <p>Contains details about how to sort the data.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.list_ingestion_jobs_request.ListIngestionJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.list_ingestion_jobs_response.ListIngestionJobsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_ingestion_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_ingestion_jobs.async_list_ingestion_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.list_ingestion_jobs_request.ListIngestionJobsRequest = {}  # type: ignore[typeddict-item]
        input["knowledge_base_id"] = knowledge_base_id
        input["data_source_id"] = data_source_id
        if filters is not None:
            input["filters"] = filters
        if sort_by is not None:
            input["sort_by"] = sort_by
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

    async def start_ingestion_job(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.description.Description"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.start_ingestion_job_response.StartIngestionJobResponse":
        """<p>Begins a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job.</p>
            data_source_id: <p>The unique identifier of the data source you want to ingest into your knowledge base.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            description: <p>A description of the data ingestion job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.start_ingestion_job_request.StartIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.start_ingestion_job_response.StartIngestionJobResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.start_ingestion_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.start_ingestion_job.async_start_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.start_ingestion_job_request.StartIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input["knowledge_base_id"] = knowledge_base_id
        input["data_source_id"] = data_source_id
        if client_token is not None:
            input["client_token"] = client_token
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_ingestion_job(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        ingestion_job_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.stop_ingestion_job_response.StopIngestionJobResponse":
        """<p>Stops a currently running data ingestion job. You can send a <code>StartIngestionJob</code> request again to ingest the rest of your data when you are ready.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job you want to stop.</p>
            data_source_id: <p>The unique identifier of the data source for the data ingestion job you want to stop.</p>
            ingestion_job_id: <p>The unique identifier of the data ingestion job you want to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.stop_ingestion_job_request.StopIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.stop_ingestion_job_response.StopIngestionJobResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.stop_ingestion_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.stop_ingestion_job.async_stop_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.stop_ingestion_job_request.StopIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input["knowledge_base_id"] = knowledge_base_id
        input["data_source_id"] = data_source_id
        input["ingestion_job_id"] = ingestion_job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
