from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_data_automation._auth._signers
import aws_sdk_bedrock_data_automation._auth._sigv4
from aws_sdk_bedrock_data_automation._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.client_token
    import aws_sdk_bedrock_data_automation.types.data_automation_library_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summary
    import aws_sdk_bedrock_data_automation.types.entity_type
    import aws_sdk_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request
    import aws_sdk_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response
    import aws_sdk_bedrock_data_automation.types.input_configuration
    import aws_sdk_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request
    import aws_sdk_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response
    import aws_sdk_bedrock_data_automation.types.library_ingestion_job_operation_type
    import aws_sdk_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request
    import aws_sdk_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response
    import aws_sdk_bedrock_data_automation.types.max_results
    import aws_sdk_bedrock_data_automation.types.next_token
    import aws_sdk_bedrock_data_automation.types.notification_configuration
    import aws_sdk_bedrock_data_automation.types.output_configuration
    import aws_sdk_bedrock_data_automation.types.tag_list
    from aws_sdk_bedrock_data_automation._services.async_bedrock_data_automation import (
        AsyncBedrockDataAutomationClient,
        AsyncBedrockDataAutomationClientConfig,
    )
    from aws_sdk_bedrock_data_automation._services.bedrock_data_automation import (
        BedrockDataAutomationClient,
        BedrockDataAutomationClientConfig,
    )


class DataAutomationLibraryIngestionJobResource:
    def __init__(self, service: BedrockDataAutomationClient) -> None:
        self._service = service

    def create(
        self,
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        input_configuration: "aws_sdk_bedrock_data_automation.types.input_configuration.InputConfiguration",
        entity_type: "aws_sdk_bedrock_data_automation.types.entity_type.EntityType",
        operation_type: "aws_sdk_bedrock_data_automation.types.library_ingestion_job_operation_type.LibraryIngestionJobOperationType",
        output_configuration: "aws_sdk_bedrock_data_automation.types.output_configuration.OutputConfiguration",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        notification_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.notification_configuration.NotificationConfiguration"
        ] = None,
        tags: Optional["aws_sdk_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response.InvokeDataAutomationLibraryIngestionJobResponse":
        """Async API: Invoke data automation library ingestion job

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            client_token: Idempotency token
            input_configuration: Input configuration of DataAutomationLibraryIngestionJob request
            entity_type: The entity type for which DataAutomationLibraryIngestionJob is being run
            operation_type: The operation to be performed by DataAutomationLibraryIngestionJob
            output_configuration: Output configuration of DataAutomationLibraryIngestionJob
            notification_configuration: Notification configuration.
            tags: List of tags
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response.InvokeDataAutomationLibraryIngestionJobResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_data_automation_library_ingestion_job

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_data_automation_library_ingestion_job.invoke_data_automation_library_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn
        if client_token is not None:
            input_["client_token"] = client_token
        input_["input_configuration"] = input_configuration
        input_["entity_type"] = entity_type
        input_["operation_type"] = operation_type
        input_["output_configuration"] = output_configuration
        if notification_configuration is not None:
            input_["notification_configuration"] = notification_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        job_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_arn.DataAutomationLibraryIngestionJobArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response.GetDataAutomationLibraryIngestionJobResponse":
        """API used to get status of data automation library ingestion job

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            job_arn: ARN of the DataAutomationLibraryIngestionJob
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request.GetDataAutomationLibraryIngestionJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response.GetDataAutomationLibraryIngestionJobResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_ingestion_job

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_ingestion_job.get_data_automation_library_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request.GetDataAutomationLibraryIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn
        input_["job_arn"] = job_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response.ListDataAutomationLibraryIngestionJobsResponse":
        """Lists all data automation library ingestion jobs

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            next_token: Pagination token for retrieving the next set of results
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request.ListDataAutomationLibraryIngestionJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response.ListDataAutomationLibraryIngestionJobsResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_ingestion_jobs

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_ingestion_jobs.list_data_automation_library_ingestion_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request.ListDataAutomationLibraryIngestionJobsRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn
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


class AsyncDataAutomationLibraryIngestionJobResource:
    def __init__(self, service: AsyncBedrockDataAutomationClient) -> None:
        self._service = service

    async def create(
        self,
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        input_configuration: "aws_sdk_bedrock_data_automation.types.input_configuration.InputConfiguration",
        entity_type: "aws_sdk_bedrock_data_automation.types.entity_type.EntityType",
        operation_type: "aws_sdk_bedrock_data_automation.types.library_ingestion_job_operation_type.LibraryIngestionJobOperationType",
        output_configuration: "aws_sdk_bedrock_data_automation.types.output_configuration.OutputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        notification_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.notification_configuration.NotificationConfiguration"
        ] = None,
        tags: Optional["aws_sdk_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response.InvokeDataAutomationLibraryIngestionJobResponse":
        """Async API: Invoke data automation library ingestion job

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            client_token: Idempotency token
            input_configuration: Input configuration of DataAutomationLibraryIngestionJob request
            entity_type: The entity type for which DataAutomationLibraryIngestionJob is being run
            operation_type: The operation to be performed by DataAutomationLibraryIngestionJob
            output_configuration: Output configuration of DataAutomationLibraryIngestionJob
            notification_configuration: Notification configuration.
            tags: List of tags
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response.InvokeDataAutomationLibraryIngestionJobResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_data_automation_library_ingestion_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_data_automation_library_ingestion_job.async_invoke_data_automation_library_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn
        if client_token is not None:
            input_["client_token"] = client_token
        input_["input_configuration"] = input_configuration
        input_["entity_type"] = entity_type
        input_["operation_type"] = operation_type
        input_["output_configuration"] = output_configuration
        if notification_configuration is not None:
            input_["notification_configuration"] = notification_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        job_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_arn.DataAutomationLibraryIngestionJobArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response.GetDataAutomationLibraryIngestionJobResponse":
        """API used to get status of data automation library ingestion job

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            job_arn: ARN of the DataAutomationLibraryIngestionJob
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request.GetDataAutomationLibraryIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response.GetDataAutomationLibraryIngestionJobResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_ingestion_job

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_ingestion_job.async_get_data_automation_library_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request.GetDataAutomationLibraryIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn
        input_["job_arn"] = job_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response.ListDataAutomationLibraryIngestionJobsResponse":
        """Lists all data automation library ingestion jobs

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            next_token: Pagination token for retrieving the next set of results
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request.ListDataAutomationLibraryIngestionJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response.ListDataAutomationLibraryIngestionJobsResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_ingestion_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_ingestion_jobs.async_list_data_automation_library_ingestion_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request.ListDataAutomationLibraryIngestionJobsRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn
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
