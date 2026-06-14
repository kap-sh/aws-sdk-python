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
    import aws_sdk_iot_managed_integrations.types.get_managed_thing_state_request
    import aws_sdk_iot_managed_integrations.types.get_managed_thing_state_response
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class ManagedThingStateResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def get_managed_thing_state(
        self,
        managed_thing_id: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse":
        """<p> Returns the managed thing state for the given device Id.</p>

        Args:
            managed_thing_id: <p>The id of the device.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_managed_thing_state_request.GetManagedThingStateRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_state

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_state.get_managed_thing_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_managed_thing_state_request.GetManagedThingStateRequest = {}  # type: ignore[typeddict-item]
        input_["managed_thing_id"] = managed_thing_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncManagedThingStateResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def get_managed_thing_state(
        self,
        managed_thing_id: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse":
        """<p> Returns the managed thing state for the given device Id.</p>

        Args:
            managed_thing_id: <p>The id of the device.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_managed_thing_state_request.GetManagedThingStateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_state

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_state.async_get_managed_thing_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_managed_thing_state_request.GetManagedThingStateRequest = {}  # type: ignore[typeddict-item]
        input_["managed_thing_id"] = managed_thing_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
