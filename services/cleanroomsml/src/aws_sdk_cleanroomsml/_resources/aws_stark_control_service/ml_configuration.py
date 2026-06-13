from typing import TYPE_CHECKING, Optional

import aws_sdk_cleanroomsml._auth._signers
import aws_sdk_cleanroomsml._auth._sigv4
from aws_sdk_cleanroomsml._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.delete_ml_configuration_request
    import aws_sdk_cleanroomsml.types.get_ml_configuration_request
    import aws_sdk_cleanroomsml.types.get_ml_configuration_response
    import aws_sdk_cleanroomsml.types.ml_output_configuration
    import aws_sdk_cleanroomsml.types.put_ml_configuration_request
    import aws_sdk_cleanroomsml.types.uuid
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class MLConfiguration:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def put(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        default_output_location: "aws_sdk_cleanroomsml.types.ml_output_configuration.MLOutputConfiguration",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Assigns information about an ML configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is being configured.</p>
            default_output_location: <p>The default Amazon S3 location where ML output is stored for the specified member.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.put_ml_configuration_request.PutMLConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.put_ml_configuration

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.put_ml_configuration.put_ml_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.put_ml_configuration_request.PutMLConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["default_output_location"] = default_output_location

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_ml_configuration_response.GetMLConfigurationResponse":
        """<p>Returns information about a specific ML configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that owns the ML configuration you want to return information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.get_ml_configuration_request.GetMLConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.get_ml_configuration_response.GetMLConfigurationResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_ml_configuration

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_ml_configuration.get_ml_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_ml_configuration_request.GetMLConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes a ML modeling configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the of the member that is deleting the ML modeling configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.delete_ml_configuration_request.DeleteMLConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_ml_configuration

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_ml_configuration.delete_ml_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.delete_ml_configuration_request.DeleteMLConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncMLConfiguration:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def put(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        default_output_location: "aws_sdk_cleanroomsml.types.ml_output_configuration.MLOutputConfiguration",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Assigns information about an ML configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is being configured.</p>
            default_output_location: <p>The default Amazon S3 location where ML output is stored for the specified member.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.put_ml_configuration_request.PutMLConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.put_ml_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.put_ml_configuration.async_put_ml_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.put_ml_configuration_request.PutMLConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["default_output_location"] = default_output_location

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_ml_configuration_response.GetMLConfigurationResponse":
        """<p>Returns information about a specific ML configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that owns the ML configuration you want to return information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_ml_configuration_request.GetMLConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.get_ml_configuration_response.GetMLConfigurationResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_ml_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_ml_configuration.async_get_ml_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_ml_configuration_request.GetMLConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes a ML modeling configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the of the member that is deleting the ML modeling configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.delete_ml_configuration_request.DeleteMLConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_ml_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_ml_configuration.async_delete_ml_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.delete_ml_configuration_request.DeleteMLConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
