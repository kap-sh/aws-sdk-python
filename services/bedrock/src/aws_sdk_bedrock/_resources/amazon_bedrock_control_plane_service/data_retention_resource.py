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
    import aws_sdk_bedrock.types.data_retention_mode
    import aws_sdk_bedrock.types.get_account_data_retention_request
    import aws_sdk_bedrock.types.get_account_data_retention_response
    import aws_sdk_bedrock.types.put_account_data_retention_request
    import aws_sdk_bedrock.types.put_account_data_retention_response
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class DataRetentionResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def get_account_data_retention(
        self, *, config_overrides: Optional[BedrockClientConfig] = None
    ) -> "aws_sdk_bedrock.types.get_account_data_retention_response.GetAccountDataRetentionResponse":
        """<p>Returns the account-wide data retention mode for Amazon Bedrock.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_account_data_retention_request.GetAccountDataRetentionRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_account_data_retention_response.GetAccountDataRetentionResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_account_data_retention

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_account_data_retention.get_account_data_retention(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_account_data_retention_request.GetAccountDataRetentionRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_account_data_retention(
        self,
        mode: "aws_sdk_bedrock.types.data_retention_mode.DataRetentionMode",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.put_account_data_retention_response.PutAccountDataRetentionResponse":
        """<p>Sets the account-wide data retention mode for Amazon Bedrock.</p>

        Args:
            mode: <p>The data retention mode to set for the account.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.put_account_data_retention_request.PutAccountDataRetentionRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.put_account_data_retention_response.PutAccountDataRetentionResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_account_data_retention

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_account_data_retention.put_account_data_retention(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.put_account_data_retention_request.PutAccountDataRetentionRequest = {}  # type: ignore[typeddict-item]
        input_["mode"] = mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDataRetentionResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def get_account_data_retention(
        self, *, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> "aws_sdk_bedrock.types.get_account_data_retention_response.GetAccountDataRetentionResponse":
        """<p>Returns the account-wide data retention mode for Amazon Bedrock.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_account_data_retention_request.GetAccountDataRetentionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_account_data_retention_response.GetAccountDataRetentionResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_account_data_retention

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_account_data_retention.async_get_account_data_retention(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_account_data_retention_request.GetAccountDataRetentionRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_account_data_retention(
        self,
        mode: "aws_sdk_bedrock.types.data_retention_mode.DataRetentionMode",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.put_account_data_retention_response.PutAccountDataRetentionResponse":
        """<p>Sets the account-wide data retention mode for Amazon Bedrock.</p>

        Args:
            mode: <p>The data retention mode to set for the account.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.put_account_data_retention_request.PutAccountDataRetentionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.put_account_data_retention_response.PutAccountDataRetentionResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_account_data_retention

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_account_data_retention.async_put_account_data_retention(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.put_account_data_retention_request.PutAccountDataRetentionRequest = {}  # type: ignore[typeddict-item]
        input_["mode"] = mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
