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
    import aws_sdk_iot_managed_integrations.types.create_ota_task_configuration_request
    import aws_sdk_iot_managed_integrations.types.create_ota_task_configuration_response
    import aws_sdk_iot_managed_integrations.types.delete_ota_task_configuration_request
    import aws_sdk_iot_managed_integrations.types.get_ota_task_configuration_request
    import aws_sdk_iot_managed_integrations.types.get_ota_task_configuration_response
    import aws_sdk_iot_managed_integrations.types.list_ota_task_configurations_request
    import aws_sdk_iot_managed_integrations.types.list_ota_task_configurations_response
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.ota_description
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_id
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_name
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_summary
    import aws_sdk_iot_managed_integrations.types.push_config
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class OtaTaskConfigurationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create_ota_task_configuration(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_description.OtaDescription"
        ] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_task_configuration_name.OtaTaskConfigurationName"
        ] = None,
        push_config: Optional[
            "aws_sdk_iot_managed_integrations.types.push_config.PushConfig"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_ota_task_configuration_response.CreateOtaTaskConfigurationResponse":
        """<p>Create a configuraiton for the over-the-air (OTA) task.</p>

        Args:
            description: <p>A description of the over-the-air (OTA) task configuration.</p>
            name: <p>The name of the over-the-air (OTA) task.</p>
            push_config: <p>Describes the type of configuration used for the over-the-air (OTA) task.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_ota_task_configuration_response.CreateOtaTaskConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task_configuration.create_ota_task_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if push_config is not None:
            input_["push_config"] = push_config
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_ota_task_configuration(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete the over-the-air (OTA) task configuration.</p>

        Args:
            identifier: <p>The identifier of the over-the-air (OTA) task configuration.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.delete_ota_task_configuration_request.DeleteOtaTaskConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task_configuration.delete_ota_task_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_ota_task_configuration_request.DeleteOtaTaskConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_ota_task_configuration(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse":
        """<p>Get a configuraiton for the over-the-air (OTA) task.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task configuration id.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_ota_task_configuration_request.GetOtaTaskConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task_configuration.get_ota_task_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_ota_task_configuration_request.GetOtaTaskConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_ota_task_configurations(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse":
        """<p>List all of the over-the-air (OTA) task configurations.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_ota_task_configurations_request.ListOtaTaskConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_configurations

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_configurations.list_ota_task_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_ota_task_configurations_request.ListOtaTaskConfigurationsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncOtaTaskConfigurationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create_ota_task_configuration(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_description.OtaDescription"
        ] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.ota_task_configuration_name.OtaTaskConfigurationName"
        ] = None,
        push_config: Optional[
            "aws_sdk_iot_managed_integrations.types.push_config.PushConfig"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_ota_task_configuration_response.CreateOtaTaskConfigurationResponse":
        """<p>Create a configuraiton for the over-the-air (OTA) task.</p>

        Args:
            description: <p>A description of the over-the-air (OTA) task configuration.</p>
            name: <p>The name of the over-the-air (OTA) task.</p>
            push_config: <p>Describes the type of configuration used for the over-the-air (OTA) task.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_ota_task_configuration_response.CreateOtaTaskConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task_configuration.async_create_ota_task_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if push_config is not None:
            input_["push_config"] = push_config
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_ota_task_configuration(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete the over-the-air (OTA) task configuration.</p>

        Args:
            identifier: <p>The identifier of the over-the-air (OTA) task configuration.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.delete_ota_task_configuration_request.DeleteOtaTaskConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task_configuration.async_delete_ota_task_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_ota_task_configuration_request.DeleteOtaTaskConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_ota_task_configuration(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse":
        """<p>Get a configuraiton for the over-the-air (OTA) task.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task configuration id.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_ota_task_configuration_request.GetOtaTaskConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task_configuration.async_get_ota_task_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_ota_task_configuration_request.GetOtaTaskConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_ota_task_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse":
        """<p>List all of the over-the-air (OTA) task configurations.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_ota_task_configurations_request.ListOtaTaskConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_configurations.async_list_ota_task_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_ota_task_configurations_request.ListOtaTaskConfigurationsRequest = {}  # type: ignore[typeddict-item]
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
