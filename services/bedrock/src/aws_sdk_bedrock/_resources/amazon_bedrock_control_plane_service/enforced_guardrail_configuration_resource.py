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
    import aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id
    import aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration
    import aws_sdk_bedrock.types.account_enforced_guardrail_output_configuration
    import aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_request
    import aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_response
    import aws_sdk_bedrock.types.list_enforced_guardrails_configuration_request
    import aws_sdk_bedrock.types.list_enforced_guardrails_configuration_response
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.put_enforced_guardrail_configuration_request
    import aws_sdk_bedrock.types.put_enforced_guardrail_configuration_response
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class EnforcedGuardrailConfigurationResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def delete_enforced_guardrail_configuration(
        self,
        config_id: "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_response.DeleteEnforcedGuardrailConfigurationResponse":
        """<p>Deletes the account-level enforced guardrail configuration.</p>

        Args:
            config_id: <p>Unique ID for the account enforced configuration.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_request.DeleteEnforcedGuardrailConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_response.DeleteEnforcedGuardrailConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_enforced_guardrail_configuration

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_enforced_guardrail_configuration.delete_enforced_guardrail_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_request.DeleteEnforcedGuardrailConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["config_id"] = config_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_enforced_guardrails_configuration(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_enforced_guardrails_configuration_response.ListEnforcedGuardrailsConfigurationResponse":
        """<p>Lists the account-level enforced guardrail configurations.</p>

        Args:
            next_token: <p>Opaque continuation token of previous paginated response.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_enforced_guardrails_configuration_request.ListEnforcedGuardrailsConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_enforced_guardrails_configuration_response.ListEnforcedGuardrailsConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_enforced_guardrails_configuration

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_enforced_guardrails_configuration.list_enforced_guardrails_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.list_enforced_guardrails_configuration_request.ListEnforcedGuardrailsConfigurationRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_enforced_guardrail_configuration(
        self,
        guardrail_inference_config: "aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration.AccountEnforcedGuardrailInferenceInputConfiguration",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        config_id: Optional[
            "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId"
        ] = None,
    ) -> "aws_sdk_bedrock.types.put_enforced_guardrail_configuration_response.PutEnforcedGuardrailConfigurationResponse":
        """<p>Sets the account-level enforced guardrail configuration.</p>

        Args:
            config_id: <p>Unique ID for the account enforced configuration.</p>
            guardrail_inference_config: <p>Account-level enforced guardrail input configuration.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.put_enforced_guardrail_configuration_request.PutEnforcedGuardrailConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.put_enforced_guardrail_configuration_response.PutEnforcedGuardrailConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_enforced_guardrail_configuration

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_enforced_guardrail_configuration.put_enforced_guardrail_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.put_enforced_guardrail_configuration_request.PutEnforcedGuardrailConfigurationRequest = {}  # type: ignore[typeddict-item]
        if config_id is not None:
            input_["config_id"] = config_id
        input_["guardrail_inference_config"] = guardrail_inference_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEnforcedGuardrailConfigurationResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def delete_enforced_guardrail_configuration(
        self,
        config_id: "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_response.DeleteEnforcedGuardrailConfigurationResponse":
        """<p>Deletes the account-level enforced guardrail configuration.</p>

        Args:
            config_id: <p>Unique ID for the account enforced configuration.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_request.DeleteEnforcedGuardrailConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_response.DeleteEnforcedGuardrailConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_enforced_guardrail_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_enforced_guardrail_configuration.async_delete_enforced_guardrail_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_request.DeleteEnforcedGuardrailConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["config_id"] = config_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_enforced_guardrails_configuration(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_enforced_guardrails_configuration_response.ListEnforcedGuardrailsConfigurationResponse":
        """<p>Lists the account-level enforced guardrail configurations.</p>

        Args:
            next_token: <p>Opaque continuation token of previous paginated response.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_enforced_guardrails_configuration_request.ListEnforcedGuardrailsConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_enforced_guardrails_configuration_response.ListEnforcedGuardrailsConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_enforced_guardrails_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_enforced_guardrails_configuration.async_list_enforced_guardrails_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.list_enforced_guardrails_configuration_request.ListEnforcedGuardrailsConfigurationRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_enforced_guardrail_configuration(
        self,
        guardrail_inference_config: "aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration.AccountEnforcedGuardrailInferenceInputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        config_id: Optional[
            "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId"
        ] = None,
    ) -> "aws_sdk_bedrock.types.put_enforced_guardrail_configuration_response.PutEnforcedGuardrailConfigurationResponse":
        """<p>Sets the account-level enforced guardrail configuration.</p>

        Args:
            config_id: <p>Unique ID for the account enforced configuration.</p>
            guardrail_inference_config: <p>Account-level enforced guardrail input configuration.</p>

        Raises:
            aws_sdk_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            aws_sdk_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.put_enforced_guardrail_configuration_request.PutEnforcedGuardrailConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.put_enforced_guardrail_configuration_response.PutEnforcedGuardrailConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_enforced_guardrail_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_enforced_guardrail_configuration.async_put_enforced_guardrail_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.put_enforced_guardrail_configuration_request.PutEnforcedGuardrailConfigurationRequest = {}  # type: ignore[typeddict-item]
        if config_id is not None:
            input_["config_id"] = config_id
        input_["guardrail_inference_config"] = guardrail_inference_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
