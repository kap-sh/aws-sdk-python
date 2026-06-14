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
    import aws_sdk_iot_managed_integrations.types.get_runtime_log_configuration_request
    import aws_sdk_iot_managed_integrations.types.get_runtime_log_configuration_response
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.put_runtime_log_configuration_request
    import aws_sdk_iot_managed_integrations.types.reset_runtime_log_configuration_request
    import aws_sdk_iot_managed_integrations.types.runtime_log_configurations
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class RuntimeLogConfigurationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def get_runtime_log_configuration(
        self,
        managed_thing_id: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_runtime_log_configuration_response.GetRuntimeLogConfigurationResponse":
        """<p>Get the runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id for a managed thing.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_runtime_log_configuration_request.GetRuntimeLogConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_runtime_log_configuration_response.GetRuntimeLogConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_runtime_log_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_runtime_log_configuration.get_runtime_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_runtime_log_configuration_request.GetRuntimeLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["managed_thing_id"] = managed_thing_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_runtime_log_configuration(
        self,
        managed_thing_id: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        runtime_log_configurations: "aws_sdk_iot_managed_integrations.types.runtime_log_configurations.RuntimeLogConfigurations",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Set the runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id for a managed thing.</p>
            runtime_log_configurations: <p>The runtime log configuration for a managed thing.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.put_runtime_log_configuration_request.PutRuntimeLogConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.put_runtime_log_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.put_runtime_log_configuration.put_runtime_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.put_runtime_log_configuration_request.PutRuntimeLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["managed_thing_id"] = managed_thing_id
        input_["runtime_log_configurations"] = runtime_log_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reset_runtime_log_configuration(
        self,
        managed_thing_id: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Reset a runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id of a managed thing.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.reset_runtime_log_configuration_request.ResetRuntimeLogConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.reset_runtime_log_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.reset_runtime_log_configuration.reset_runtime_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.reset_runtime_log_configuration_request.ResetRuntimeLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["managed_thing_id"] = managed_thing_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRuntimeLogConfigurationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def get_runtime_log_configuration(
        self,
        managed_thing_id: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_runtime_log_configuration_response.GetRuntimeLogConfigurationResponse":
        """<p>Get the runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id for a managed thing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_runtime_log_configuration_request.GetRuntimeLogConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_runtime_log_configuration_response.GetRuntimeLogConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_runtime_log_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_runtime_log_configuration.async_get_runtime_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_runtime_log_configuration_request.GetRuntimeLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["managed_thing_id"] = managed_thing_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_runtime_log_configuration(
        self,
        managed_thing_id: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        runtime_log_configurations: "aws_sdk_iot_managed_integrations.types.runtime_log_configurations.RuntimeLogConfigurations",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Set the runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id for a managed thing.</p>
            runtime_log_configurations: <p>The runtime log configuration for a managed thing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.put_runtime_log_configuration_request.PutRuntimeLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.put_runtime_log_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.put_runtime_log_configuration.async_put_runtime_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.put_runtime_log_configuration_request.PutRuntimeLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["managed_thing_id"] = managed_thing_id
        input_["runtime_log_configurations"] = runtime_log_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reset_runtime_log_configuration(
        self,
        managed_thing_id: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Reset a runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id of a managed thing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.reset_runtime_log_configuration_request.ResetRuntimeLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.reset_runtime_log_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.reset_runtime_log_configuration.async_reset_runtime_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.reset_runtime_log_configuration_request.ResetRuntimeLogConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["managed_thing_id"] = managed_thing_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
