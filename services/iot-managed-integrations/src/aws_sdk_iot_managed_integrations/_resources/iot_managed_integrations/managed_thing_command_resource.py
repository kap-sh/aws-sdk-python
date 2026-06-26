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
    import aws_sdk_iot_managed_integrations.types.account_association_id
    import aws_sdk_iot_managed_integrations.types.command_endpoints
    import aws_sdk_iot_managed_integrations.types.connector_association_id
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.send_managed_thing_command_request
    import aws_sdk_iot_managed_integrations.types.send_managed_thing_command_response
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class ManagedThingCommandResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def send_managed_thing_command(
        self,
        managed_thing_id: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        endpoints: "aws_sdk_iot_managed_integrations.types.command_endpoints.CommandEndpoints",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        connector_association_id: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_association_id.ConnectorAssociationId"
        ] = None,
        account_association_id: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.send_managed_thing_command_response.SendManagedThingCommandResponse":
        """<p>Send the command to the device represented by the managed thing. </p>

        Args:
            managed_thing_id: <p>The id of the device.</p>
            endpoints: <p>The device endpoint.</p>
            connector_association_id: <p>The ID tracking the current discovery process for one connector association.</p>
            account_association_id: <p>The identifier of the account association to use when sending a command to a managed thing.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.send_managed_thing_command_request.SendManagedThingCommandRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.send_managed_thing_command_response.SendManagedThingCommandResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.send_managed_thing_command

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.send_managed_thing_command.send_managed_thing_command(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.send_managed_thing_command_request.SendManagedThingCommandRequest = {}  # type: ignore[typeddict-item]
        input_["managed_thing_id"] = managed_thing_id
        input_["endpoints"] = endpoints
        if connector_association_id is not None:
            input_["connector_association_id"] = connector_association_id
        if account_association_id is not None:
            input_["account_association_id"] = account_association_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncManagedThingCommandResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def send_managed_thing_command(
        self,
        managed_thing_id: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        endpoints: "aws_sdk_iot_managed_integrations.types.command_endpoints.CommandEndpoints",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        connector_association_id: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_association_id.ConnectorAssociationId"
        ] = None,
        account_association_id: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.send_managed_thing_command_response.SendManagedThingCommandResponse":
        """<p>Send the command to the device represented by the managed thing. </p>

        Args:
            managed_thing_id: <p>The id of the device.</p>
            endpoints: <p>The device endpoint.</p>
            connector_association_id: <p>The ID tracking the current discovery process for one connector association.</p>
            account_association_id: <p>The identifier of the account association to use when sending a command to a managed thing.</p>

        Raises:
            aws_sdk_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            aws_sdk_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            aws_sdk_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            aws_sdk_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            aws_sdk_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            aws_sdk_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.send_managed_thing_command_request.SendManagedThingCommandRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.send_managed_thing_command_response.SendManagedThingCommandResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.send_managed_thing_command

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.send_managed_thing_command.async_send_managed_thing_command(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.send_managed_thing_command_request.SendManagedThingCommandRequest = {}  # type: ignore[typeddict-item]
        input_["managed_thing_id"] = managed_thing_id
        input_["endpoints"] = endpoints
        if connector_association_id is not None:
            input_["connector_association_id"] = connector_association_id
        if account_association_id is not None:
            input_["account_association_id"] = account_association_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
