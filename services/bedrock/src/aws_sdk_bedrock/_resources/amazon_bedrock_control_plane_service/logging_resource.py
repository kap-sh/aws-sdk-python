from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock._auth._signers
import aws_sdk_bedrock._auth._sigv4
from aws_sdk_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.delete_model_invocation_logging_configuration_request
    import aws_sdk_bedrock.types.delete_model_invocation_logging_configuration_response
    import aws_sdk_bedrock.types.get_model_invocation_logging_configuration_request
    import aws_sdk_bedrock.types.get_model_invocation_logging_configuration_response
    import aws_sdk_bedrock.types.logging_config
    import aws_sdk_bedrock.types.put_model_invocation_logging_configuration_request
    import aws_sdk_bedrock.types.put_model_invocation_logging_configuration_response
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class LoggingResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def delete_model_invocation_logging_configuration(
        self, *, config_overrides: Optional[BedrockClientConfig] = None
    ) -> "aws_sdk_bedrock.types.delete_model_invocation_logging_configuration_response.DeleteModelInvocationLoggingConfigurationResponse":
        """<p>Delete the invocation logging. </p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.delete_model_invocation_logging_configuration_request.DeleteModelInvocationLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.delete_model_invocation_logging_configuration_response.DeleteModelInvocationLoggingConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_model_invocation_logging_configuration

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_model_invocation_logging_configuration.delete_model_invocation_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.delete_model_invocation_logging_configuration_request.DeleteModelInvocationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_model_invocation_logging_configuration(
        self, *, config_overrides: Optional[BedrockClientConfig] = None
    ) -> "aws_sdk_bedrock.types.get_model_invocation_logging_configuration_response.GetModelInvocationLoggingConfigurationResponse":
        """<p>Get the current configuration values for model invocation logging.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_model_invocation_logging_configuration_request.GetModelInvocationLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_model_invocation_logging_configuration_response.GetModelInvocationLoggingConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_logging_configuration

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_logging_configuration.get_model_invocation_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_model_invocation_logging_configuration_request.GetModelInvocationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_model_invocation_logging_configuration(
        self,
        logging_config: "aws_sdk_bedrock.types.logging_config.LoggingConfig",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.put_model_invocation_logging_configuration_response.PutModelInvocationLoggingConfigurationResponse":
        """<p>Set the configuration values for model invocation logging.</p>

        Args:
            logging_config: <p>The logging configuration values to set.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.put_model_invocation_logging_configuration_request.PutModelInvocationLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.put_model_invocation_logging_configuration_response.PutModelInvocationLoggingConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_model_invocation_logging_configuration

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_model_invocation_logging_configuration.put_model_invocation_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.put_model_invocation_logging_configuration_request.PutModelInvocationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["logging_config"] = logging_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncLoggingResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def delete_model_invocation_logging_configuration(
        self, *, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> "aws_sdk_bedrock.types.delete_model_invocation_logging_configuration_response.DeleteModelInvocationLoggingConfigurationResponse":
        """<p>Delete the invocation logging. </p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.delete_model_invocation_logging_configuration_request.DeleteModelInvocationLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.delete_model_invocation_logging_configuration_response.DeleteModelInvocationLoggingConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_model_invocation_logging_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_model_invocation_logging_configuration.async_delete_model_invocation_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.delete_model_invocation_logging_configuration_request.DeleteModelInvocationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_model_invocation_logging_configuration(
        self, *, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> "aws_sdk_bedrock.types.get_model_invocation_logging_configuration_response.GetModelInvocationLoggingConfigurationResponse":
        """<p>Get the current configuration values for model invocation logging.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_model_invocation_logging_configuration_request.GetModelInvocationLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_model_invocation_logging_configuration_response.GetModelInvocationLoggingConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_logging_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_logging_configuration.async_get_model_invocation_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_model_invocation_logging_configuration_request.GetModelInvocationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_model_invocation_logging_configuration(
        self,
        logging_config: "aws_sdk_bedrock.types.logging_config.LoggingConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.put_model_invocation_logging_configuration_response.PutModelInvocationLoggingConfigurationResponse":
        """<p>Set the configuration values for model invocation logging.</p>

        Args:
            logging_config: <p>The logging configuration values to set.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.put_model_invocation_logging_configuration_request.PutModelInvocationLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.put_model_invocation_logging_configuration_response.PutModelInvocationLoggingConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_model_invocation_logging_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_model_invocation_logging_configuration.async_put_model_invocation_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.put_model_invocation_logging_configuration_request.PutModelInvocationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["logging_config"] = logging_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
