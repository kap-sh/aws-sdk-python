from __future__ import annotations

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
    import aws_sdk_iot_managed_integrations.types.create_notification_configuration_request
    import aws_sdk_iot_managed_integrations.types.create_notification_configuration_response
    import aws_sdk_iot_managed_integrations.types.delete_notification_configuration_request
    import aws_sdk_iot_managed_integrations.types.destination_name
    import aws_sdk_iot_managed_integrations.types.event_type
    import aws_sdk_iot_managed_integrations.types.get_notification_configuration_request
    import aws_sdk_iot_managed_integrations.types.get_notification_configuration_response
    import aws_sdk_iot_managed_integrations.types.list_notification_configurations_request
    import aws_sdk_iot_managed_integrations.types.list_notification_configurations_response
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.notification_configuration_summary
    import aws_sdk_iot_managed_integrations.types.tags_map
    import aws_sdk_iot_managed_integrations.types.update_notification_configuration_request
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class NotificationConfigurationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create_notification_configuration(
        self,
        event_type: "aws_sdk_iot_managed_integrations.types.event_type.EventType",
        destination_name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_notification_configuration_response.CreateNotificationConfigurationResponse":
        """<p>Creates a notification configuration. A configuration is a connection between an event type and a destination that you have already created. </p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>
            destination_name: <p>The name of the destination for the notification configuration.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the notification configuration.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_notification_configuration_response.CreateNotificationConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_notification_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_notification_configuration.create_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["event_type"] = event_type
        input_["destination_name"] = destination_name
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_notification_configuration(
        self,
        event_type: "aws_sdk_iot_managed_integrations.types.event_type.EventType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deletes a notification configuration. </p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_notification_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_notification_configuration.delete_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["event_type"] = event_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_notification_configuration(
        self,
        event_type: "aws_sdk_iot_managed_integrations.types.event_type.EventType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse":
        """<p> Get a notification configuration for a specified event type.</p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_notification_configuration_request.GetNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_notification_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_notification_configuration.get_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_notification_configuration_request.GetNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["event_type"] = event_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_notification_configurations(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_notification_configurations_response.ListNotificationConfigurationsResponse":
        """<p> List all notification configurations.</p>

        Args:
            max_results: <p>The maximum number of results to return at one time.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_notification_configurations_request.ListNotificationConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_notification_configurations_response.ListNotificationConfigurationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_notification_configurations

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_notification_configurations.list_notification_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_notification_configurations_request.ListNotificationConfigurationsRequest = {}  # type: ignore[typeddict-item]
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

    def update_notification_configuration(
        self,
        event_type: "aws_sdk_iot_managed_integrations.types.event_type.EventType",
        destination_name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p> Update a notification configuration.</p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>
            destination_name: <p>The name of the destination for the notification configuration.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_notification_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_notification_configuration.update_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["event_type"] = event_type
        input_["destination_name"] = destination_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncNotificationConfigurationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create_notification_configuration(
        self,
        event_type: "aws_sdk_iot_managed_integrations.types.event_type.EventType",
        destination_name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_notification_configuration_response.CreateNotificationConfigurationResponse":
        """<p>Creates a notification configuration. A configuration is a connection between an event type and a destination that you have already created. </p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>
            destination_name: <p>The name of the destination for the notification configuration.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the notification configuration.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_notification_configuration_response.CreateNotificationConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_notification_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_notification_configuration.async_create_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["event_type"] = event_type
        input_["destination_name"] = destination_name
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_notification_configuration(
        self,
        event_type: "aws_sdk_iot_managed_integrations.types.event_type.EventType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deletes a notification configuration. </p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_notification_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_notification_configuration.async_delete_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["event_type"] = event_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_notification_configuration(
        self,
        event_type: "aws_sdk_iot_managed_integrations.types.event_type.EventType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse":
        """<p> Get a notification configuration for a specified event type.</p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_notification_configuration_request.GetNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_notification_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_notification_configuration.async_get_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_notification_configuration_request.GetNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["event_type"] = event_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_notification_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_notification_configurations_response.ListNotificationConfigurationsResponse":
        """<p> List all notification configurations.</p>

        Args:
            max_results: <p>The maximum number of results to return at one time.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_notification_configurations_request.ListNotificationConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_notification_configurations_response.ListNotificationConfigurationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_notification_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_notification_configurations.async_list_notification_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_notification_configurations_request.ListNotificationConfigurationsRequest = {}  # type: ignore[typeddict-item]
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

    async def update_notification_configuration(
        self,
        event_type: "aws_sdk_iot_managed_integrations.types.event_type.EventType",
        destination_name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p> Update a notification configuration.</p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>
            destination_name: <p>The name of the destination for the notification configuration.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_notification_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_notification_configuration.async_update_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["event_type"] = event_type
        input_["destination_name"] = destination_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
