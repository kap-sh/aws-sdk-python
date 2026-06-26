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
    import aws_sdk_bedrock.types.acknowledgement_form_data_body
    import aws_sdk_bedrock.types.get_use_case_for_model_access_request
    import aws_sdk_bedrock.types.get_use_case_for_model_access_response
    import aws_sdk_bedrock.types.put_use_case_for_model_access_request
    import aws_sdk_bedrock.types.put_use_case_for_model_access_response
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class AllowlistResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def get_use_case_for_model_access(
        self, *, config_overrides: Optional[BedrockClientConfig] = None
    ) -> "aws_sdk_bedrock.types.get_use_case_for_model_access_response.GetUseCaseForModelAccessResponse":
        """<p>Get usecase for model access.</p>

        Raises:
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_use_case_for_model_access_request.GetUseCaseForModelAccessRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_use_case_for_model_access_response.GetUseCaseForModelAccessResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_use_case_for_model_access

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_use_case_for_model_access.get_use_case_for_model_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_use_case_for_model_access_request.GetUseCaseForModelAccessRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_use_case_for_model_access(
        self,
        form_data: "aws_sdk_bedrock.types.acknowledgement_form_data_body.AcknowledgementFormDataBody",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.put_use_case_for_model_access_response.PutUseCaseForModelAccessResponse":
        """<p>Put usecase for model access.</p>

        Args:
            form_data: <p>Put customer profile Request.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.put_use_case_for_model_access_request.PutUseCaseForModelAccessRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.put_use_case_for_model_access_response.PutUseCaseForModelAccessResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_use_case_for_model_access

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_use_case_for_model_access.put_use_case_for_model_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.put_use_case_for_model_access_request.PutUseCaseForModelAccessRequest = {}  # type: ignore[typeddict-item]
        input_["form_data"] = form_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAllowlistResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def get_use_case_for_model_access(
        self, *, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> "aws_sdk_bedrock.types.get_use_case_for_model_access_response.GetUseCaseForModelAccessResponse":
        """<p>Get usecase for model access.</p>

        Raises:
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_use_case_for_model_access_request.GetUseCaseForModelAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_use_case_for_model_access_response.GetUseCaseForModelAccessResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_use_case_for_model_access

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_use_case_for_model_access.async_get_use_case_for_model_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_use_case_for_model_access_request.GetUseCaseForModelAccessRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_use_case_for_model_access(
        self,
        form_data: "aws_sdk_bedrock.types.acknowledgement_form_data_body.AcknowledgementFormDataBody",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.put_use_case_for_model_access_response.PutUseCaseForModelAccessResponse":
        """<p>Put usecase for model access.</p>

        Args:
            form_data: <p>Put customer profile Request.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.put_use_case_for_model_access_request.PutUseCaseForModelAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.put_use_case_for_model_access_response.PutUseCaseForModelAccessResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_use_case_for_model_access

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_use_case_for_model_access.async_put_use_case_for_model_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.put_use_case_for_model_access_request.PutUseCaseForModelAccessRequest = {}  # type: ignore[typeddict-item]
        input_["form_data"] = form_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
