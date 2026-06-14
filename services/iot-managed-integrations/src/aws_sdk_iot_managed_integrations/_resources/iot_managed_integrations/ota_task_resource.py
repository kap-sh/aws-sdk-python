from typing import TYPE_CHECKING, Optional

import aws_sdk_iot_managed_integrations._auth._signers
import aws_sdk_iot_managed_integrations._auth._sigv4
from aws_sdk_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.client_token
    import aws_sdk_iot_managed_integrations.types.create_ota_task_request
    import aws_sdk_iot_managed_integrations.types.create_ota_task_response
    import aws_sdk_iot_managed_integrations.types.delete_ota_task_request
    import aws_sdk_iot_managed_integrations.types.get_ota_task_request
    import aws_sdk_iot_managed_integrations.types.get_ota_task_response
    import aws_sdk_iot_managed_integrations.types.list_ota_task_executions_request
    import aws_sdk_iot_managed_integrations.types.list_ota_task_executions_response
    import aws_sdk_iot_managed_integrations.types.list_ota_tasks_request
    import aws_sdk_iot_managed_integrations.types.list_ota_tasks_response
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.ota_description
    import aws_sdk_iot_managed_integrations.types.ota_mechanism
    import aws_sdk_iot_managed_integrations.types.ota_next_token
    import aws_sdk_iot_managed_integrations.types.ota_protocol
    import aws_sdk_iot_managed_integrations.types.ota_target_query_string
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_id
    import aws_sdk_iot_managed_integrations.types.ota_task_execution_retry_config
    import aws_sdk_iot_managed_integrations.types.ota_task_execution_summaries
    import aws_sdk_iot_managed_integrations.types.ota_task_id
    import aws_sdk_iot_managed_integrations.types.ota_task_scheduling_config
    import aws_sdk_iot_managed_integrations.types.ota_task_summary
    import aws_sdk_iot_managed_integrations.types.ota_type
    import aws_sdk_iot_managed_integrations.types.s3_url
    import aws_sdk_iot_managed_integrations.types.tags_map
    import aws_sdk_iot_managed_integrations.types.target
    import aws_sdk_iot_managed_integrations.types.update_ota_task_request
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class OtaTaskResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        s3_url: "aws_sdk_iot_managed_integrations.types.s3_url.S3Url",
        ota_type: "aws_sdk_iot_managed_integrations.types.ota_type.OtaType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_description.OtaDescription"
        ] = None,
        protocol: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_protocol.OtaProtocol"
        ] = None,
        target: Optional["aws_sdk_iot_managed_integrations.types.target.Target"] = None,
        task_configuration_id: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
        ] = None,
        ota_mechanism: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_mechanism.OtaMechanism"
        ] = None,
        ota_target_query_string: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_target_query_string.OtaTargetQueryString"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        ota_scheduling_config: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_task_scheduling_config.OtaTaskSchedulingConfig"
        ] = None,
        ota_task_execution_retry_config: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_task_execution_retry_config.OtaTaskExecutionRetryConfig"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_ota_task_response.CreateOtaTaskResponse":
        """<p>Create an over-the-air (OTA) task to target a device.</p>

        Args:
            description: <p>The description of the over-the-air (OTA) task.</p>
            s3_url: <p>The URL to the Amazon S3 bucket where the over-the-air (OTA) task is stored.</p>
            protocol: <p>The connection protocol the over-the-air (OTA) task uses to update the device.</p>
            target: <p>The device targeted for the over-the-air (OTA) task.</p>
            task_configuration_id: <p>The identifier for the over-the-air (OTA) task configuration.</p>
            ota_mechanism: <p>The deployment mechanism for the over-the-air (OTA) task.</p>
            ota_type: <p>The frequency type for the over-the-air (OTA) task.</p>
            ota_target_query_string: <p>The query string to add things to the thing group.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the over-the-air (OTA) task.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.create_ota_task_request.CreateOtaTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_ota_task_response.CreateOtaTaskResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task.create_ota_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_ota_task_request.CreateOtaTaskRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["s3_url"] = s3_url
        if protocol is not None:
            input_["protocol"] = protocol
        if target is not None:
            input_["target"] = target
        if task_configuration_id is not None:
            input_["task_configuration_id"] = task_configuration_id
        if ota_mechanism is not None:
            input_["ota_mechanism"] = ota_mechanism
        input_["ota_type"] = ota_type
        if ota_target_query_string is not None:
            input_["ota_target_query_string"] = ota_target_query_string
        if client_token is not None:
            input_["client_token"] = client_token
        if ota_scheduling_config is not None:
            input_["ota_scheduling_config"] = ota_scheduling_config
        if ota_task_execution_retry_config is not None:
            input_["ota_task_execution_retry_config"] = ota_task_execution_retry_config
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
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_ota_task_response.GetOtaTaskResponse":
        """<p>Get details of the over-the-air (OTA) task by its task id.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task id.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_ota_task_request.GetOtaTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_ota_task_response.GetOtaTaskResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task.get_ota_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_ota_task_request.GetOtaTaskRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_description.OtaDescription"
        ] = None,
        task_configuration_id: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
        ] = None,
    ) -> None:
        """<p>Update an over-the-air (OTA) task.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task id.</p>
            description: <p>The description of the over-the-air (OTA) task.</p>
            task_configuration_id: <p>The identifier for the over-the-air (OTA) task configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.update_ota_task_request.UpdateOtaTaskRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_ota_task

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_ota_task.update_ota_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.update_ota_task_request.UpdateOtaTaskRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if description is not None:
            input_["description"] = description
        if task_configuration_id is not None:
            input_["task_configuration_id"] = task_configuration_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete the over-the-air (OTA) task.</p>

        Args:
            identifier: <p>The identifier of the over-the-air (OTA) task.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.delete_ota_task_request.DeleteOtaTaskRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task.delete_ota_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_ota_task_request.DeleteOtaTaskRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_next_token.OtaNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_ota_tasks_response.ListOtaTasksResponse":
        """<p>List all of the over-the-air (OTA) tasks.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_ota_tasks_request.ListOtaTasksRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_ota_tasks_response.ListOtaTasksResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_tasks

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_tasks.list_ota_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_ota_tasks_request.ListOtaTasksRequest = {}  # type: ignore[typeddict-item]
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

    def list_ota_task_executions(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_next_token.OtaNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_ota_task_executions_response.ListOtaTaskExecutionsResponse":
        """<p>List all of the over-the-air (OTA) task executions.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task id.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_ota_task_executions_request.ListOtaTaskExecutionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_ota_task_executions_response.ListOtaTaskExecutionsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_executions

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_executions.list_ota_task_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_ota_task_executions_request.ListOtaTaskExecutionsRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
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


class AsyncOtaTaskResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        s3_url: "aws_sdk_iot_managed_integrations.types.s3_url.S3Url",
        ota_type: "aws_sdk_iot_managed_integrations.types.ota_type.OtaType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_description.OtaDescription"
        ] = None,
        protocol: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_protocol.OtaProtocol"
        ] = None,
        target: Optional["aws_sdk_iot_managed_integrations.types.target.Target"] = None,
        task_configuration_id: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
        ] = None,
        ota_mechanism: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_mechanism.OtaMechanism"
        ] = None,
        ota_target_query_string: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_target_query_string.OtaTargetQueryString"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        ota_scheduling_config: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_task_scheduling_config.OtaTaskSchedulingConfig"
        ] = None,
        ota_task_execution_retry_config: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_task_execution_retry_config.OtaTaskExecutionRetryConfig"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_ota_task_response.CreateOtaTaskResponse":
        """<p>Create an over-the-air (OTA) task to target a device.</p>

        Args:
            description: <p>The description of the over-the-air (OTA) task.</p>
            s3_url: <p>The URL to the Amazon S3 bucket where the over-the-air (OTA) task is stored.</p>
            protocol: <p>The connection protocol the over-the-air (OTA) task uses to update the device.</p>
            target: <p>The device targeted for the over-the-air (OTA) task.</p>
            task_configuration_id: <p>The identifier for the over-the-air (OTA) task configuration.</p>
            ota_mechanism: <p>The deployment mechanism for the over-the-air (OTA) task.</p>
            ota_type: <p>The frequency type for the over-the-air (OTA) task.</p>
            ota_target_query_string: <p>The query string to add things to the thing group.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the over-the-air (OTA) task.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.create_ota_task_request.CreateOtaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_ota_task_response.CreateOtaTaskResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task.async_create_ota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_ota_task_request.CreateOtaTaskRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["s3_url"] = s3_url
        if protocol is not None:
            input_["protocol"] = protocol
        if target is not None:
            input_["target"] = target
        if task_configuration_id is not None:
            input_["task_configuration_id"] = task_configuration_id
        if ota_mechanism is not None:
            input_["ota_mechanism"] = ota_mechanism
        input_["ota_type"] = ota_type
        if ota_target_query_string is not None:
            input_["ota_target_query_string"] = ota_target_query_string
        if client_token is not None:
            input_["client_token"] = client_token
        if ota_scheduling_config is not None:
            input_["ota_scheduling_config"] = ota_scheduling_config
        if ota_task_execution_retry_config is not None:
            input_["ota_task_execution_retry_config"] = ota_task_execution_retry_config
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
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_ota_task_response.GetOtaTaskResponse":
        """<p>Get details of the over-the-air (OTA) task by its task id.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task id.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_ota_task_request.GetOtaTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_ota_task_response.GetOtaTaskResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task.async_get_ota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_ota_task_request.GetOtaTaskRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_description.OtaDescription"
        ] = None,
        task_configuration_id: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
        ] = None,
    ) -> None:
        """<p>Update an over-the-air (OTA) task.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task id.</p>
            description: <p>The description of the over-the-air (OTA) task.</p>
            task_configuration_id: <p>The identifier for the over-the-air (OTA) task configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.update_ota_task_request.UpdateOtaTaskRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_ota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_ota_task.async_update_ota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.update_ota_task_request.UpdateOtaTaskRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if description is not None:
            input_["description"] = description
        if task_configuration_id is not None:
            input_["task_configuration_id"] = task_configuration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete the over-the-air (OTA) task.</p>

        Args:
            identifier: <p>The identifier of the over-the-air (OTA) task.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.delete_ota_task_request.DeleteOtaTaskRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task.async_delete_ota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_ota_task_request.DeleteOtaTaskRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_next_token.OtaNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_ota_tasks_response.ListOtaTasksResponse":
        """<p>List all of the over-the-air (OTA) tasks.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_ota_tasks_request.ListOtaTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_ota_tasks_response.ListOtaTasksResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_tasks.async_list_ota_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_ota_tasks_request.ListOtaTasksRequest = {}  # type: ignore[typeddict-item]
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

    async def list_ota_task_executions(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_next_token.OtaNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_ota_task_executions_response.ListOtaTaskExecutionsResponse":
        """<p>List all of the over-the-air (OTA) task executions.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task id.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_ota_task_executions_request.ListOtaTaskExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_ota_task_executions_response.ListOtaTaskExecutionsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_executions

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_executions.async_list_ota_task_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_ota_task_executions_request.ListOtaTaskExecutionsRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
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
