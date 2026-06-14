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
    import aws_sdk_iot_managed_integrations.types.create_event_log_configuration_request
    import aws_sdk_iot_managed_integrations.types.create_event_log_configuration_response
    import aws_sdk_iot_managed_integrations.types.delete_event_log_configuration_request
    import aws_sdk_iot_managed_integrations.types.event_log_configuration_summary
    import aws_sdk_iot_managed_integrations.types.get_event_log_configuration_request
    import aws_sdk_iot_managed_integrations.types.get_event_log_configuration_response
    import aws_sdk_iot_managed_integrations.types.list_event_log_configurations_request
    import aws_sdk_iot_managed_integrations.types.list_event_log_configurations_response
    import aws_sdk_iot_managed_integrations.types.log_configuration_id
    import aws_sdk_iot_managed_integrations.types.log_level
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.smart_home_resource_id
    import aws_sdk_iot_managed_integrations.types.smart_home_resource_type
    import aws_sdk_iot_managed_integrations.types.update_event_log_configuration_request
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class EventLogConfigurationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create_event_log_configuration(
        self,
        resource_type: "aws_sdk_iot_managed_integrations.types.smart_home_resource_type.SmartHomeResourceType",
        event_log_level: "aws_sdk_iot_managed_integrations.types.log_level.LogLevel",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        resource_id: Optional[
            "aws_sdk_iot_managed_integrations.types.smart_home_resource_id.SmartHomeResourceId"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_event_log_configuration_response.CreateEventLogConfigurationResponse":
        """<p>Set the event log configuration for the account, resource type, or specific resource.</p>

        Args:
            resource_type: <p>The type of resource for the event log configuration.</p>
            resource_id: <p>The identifier of the resource for the event log configuration.</p>
            event_log_level: <p>The logging level for the event log configuration.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.create_event_log_configuration_request.CreateEventLogConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_event_log_configuration_response.CreateEventLogConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_event_log_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_event_log_configuration.create_event_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_event_log_configuration_request.CreateEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_type"] = resource_type
        if resource_id is not None:
            input_["resource_id"] = resource_id
        input_["event_log_level"] = event_log_level
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_event_log_configuration(
        self,
        id: "aws_sdk_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete an event log configuration.</p>

        Args:
            id: <p>The identifier of the event log configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.delete_event_log_configuration_request.DeleteEventLogConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_event_log_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_event_log_configuration.delete_event_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_event_log_configuration_request.DeleteEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_event_log_configuration(
        self,
        id: "aws_sdk_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_event_log_configuration_response.GetEventLogConfigurationResponse":
        """<p>Get an event log configuration.</p>

        Args:
            id: <p>The identifier of the event log configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_event_log_configuration_request.GetEventLogConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_event_log_configuration_response.GetEventLogConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_event_log_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_event_log_configuration.get_event_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_event_log_configuration_request.GetEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_event_log_configurations(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_event_log_configurations_response.ListEventLogConfigurationsResponse":
        """<p>List all event log configurations for an account.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_event_log_configurations_request.ListEventLogConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_event_log_configurations_response.ListEventLogConfigurationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_event_log_configurations

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_event_log_configurations.list_event_log_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_event_log_configurations_request.ListEventLogConfigurationsRequest = {}  # type: ignore[typeddict-item]
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

    def update_event_log_configuration(
        self,
        id: "aws_sdk_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        event_log_level: "aws_sdk_iot_managed_integrations.types.log_level.LogLevel",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Update an event log configuration by log configuration ID.</p>

        Args:
            id: <p>The log configuration id.</p>
            event_log_level: <p>The log level for the event in terms of severity.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.update_event_log_configuration_request.UpdateEventLogConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_event_log_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_event_log_configuration.update_event_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.update_event_log_configuration_request.UpdateEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["event_log_level"] = event_log_level

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEventLogConfigurationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create_event_log_configuration(
        self,
        resource_type: "aws_sdk_iot_managed_integrations.types.smart_home_resource_type.SmartHomeResourceType",
        event_log_level: "aws_sdk_iot_managed_integrations.types.log_level.LogLevel",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        resource_id: Optional[
            "aws_sdk_iot_managed_integrations.types.smart_home_resource_id.SmartHomeResourceId"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_event_log_configuration_response.CreateEventLogConfigurationResponse":
        """<p>Set the event log configuration for the account, resource type, or specific resource.</p>

        Args:
            resource_type: <p>The type of resource for the event log configuration.</p>
            resource_id: <p>The identifier of the resource for the event log configuration.</p>
            event_log_level: <p>The logging level for the event log configuration.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.create_event_log_configuration_request.CreateEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_event_log_configuration_response.CreateEventLogConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_event_log_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_event_log_configuration.async_create_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_event_log_configuration_request.CreateEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_type"] = resource_type
        if resource_id is not None:
            input_["resource_id"] = resource_id
        input_["event_log_level"] = event_log_level
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_event_log_configuration(
        self,
        id: "aws_sdk_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete an event log configuration.</p>

        Args:
            id: <p>The identifier of the event log configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.delete_event_log_configuration_request.DeleteEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_event_log_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_event_log_configuration.async_delete_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_event_log_configuration_request.DeleteEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_event_log_configuration(
        self,
        id: "aws_sdk_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_event_log_configuration_response.GetEventLogConfigurationResponse":
        """<p>Get an event log configuration.</p>

        Args:
            id: <p>The identifier of the event log configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_event_log_configuration_request.GetEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_event_log_configuration_response.GetEventLogConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_event_log_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_event_log_configuration.async_get_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_event_log_configuration_request.GetEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_event_log_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_event_log_configurations_response.ListEventLogConfigurationsResponse":
        """<p>List all event log configurations for an account.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_event_log_configurations_request.ListEventLogConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_event_log_configurations_response.ListEventLogConfigurationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_event_log_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_event_log_configurations.async_list_event_log_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_event_log_configurations_request.ListEventLogConfigurationsRequest = {}  # type: ignore[typeddict-item]
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

    async def update_event_log_configuration(
        self,
        id: "aws_sdk_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        event_log_level: "aws_sdk_iot_managed_integrations.types.log_level.LogLevel",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Update an event log configuration by log configuration ID.</p>

        Args:
            id: <p>The log configuration id.</p>
            event_log_level: <p>The log level for the event in terms of severity.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.update_event_log_configuration_request.UpdateEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_event_log_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_event_log_configuration.async_update_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.update_event_log_configuration_request.UpdateEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["event_log_level"] = event_log_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
