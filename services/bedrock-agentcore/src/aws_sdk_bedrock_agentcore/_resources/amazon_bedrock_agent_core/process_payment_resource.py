from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agentcore._auth._signers
import aws_sdk_bedrock_agentcore._auth._sigv4
from aws_sdk_bedrock_agentcore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.payment_agent_name
    import aws_sdk_bedrock_agentcore.types.payment_input
    import aws_sdk_bedrock_agentcore.types.payment_instrument_id
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.payment_session_id
    import aws_sdk_bedrock_agentcore.types.payment_type
    import aws_sdk_bedrock_agentcore.types.process_payment_request
    import aws_sdk_bedrock_agentcore.types.process_payment_response
    import aws_sdk_bedrock_agentcore.types.user_id
    from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class ProcessPaymentResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def create(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_session_id: "aws_sdk_bedrock_agentcore.types.payment_session_id.PaymentSessionId",
        payment_instrument_id: "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        payment_type: "aws_sdk_bedrock_agentcore.types.payment_type.PaymentType",
        payment_input: "aws_sdk_bedrock_agentcore.types.payment_input.PaymentInput",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse":
        """<p>Processes a payment using a payment instrument within a payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager.</p>
            payment_session_id: <p>The ID of the payment session.</p>
            payment_instrument_id: <p>The ID of the payment instrument to use.</p>
            payment_type: <p>The type of payment to process.</p>
            payment_input: <p>The payment input details specific to the payment type.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            aws_sdk_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            aws_sdk_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            aws_sdk_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            aws_sdk_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.process_payment

            output, http_response = (
                aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.process_payment.process_payment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_session_id"] = payment_session_id
        input_["payment_instrument_id"] = payment_instrument_id
        input_["payment_type"] = payment_type
        input_["payment_input"] = payment_input
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncProcessPaymentResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def create(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_session_id: "aws_sdk_bedrock_agentcore.types.payment_session_id.PaymentSessionId",
        payment_instrument_id: "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        payment_type: "aws_sdk_bedrock_agentcore.types.payment_type.PaymentType",
        payment_input: "aws_sdk_bedrock_agentcore.types.payment_input.PaymentInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse":
        """<p>Processes a payment using a payment instrument within a payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager.</p>
            payment_session_id: <p>The ID of the payment session.</p>
            payment_instrument_id: <p>The ID of the payment instrument to use.</p>
            payment_type: <p>The type of payment to process.</p>
            payment_input: <p>The payment input details specific to the payment type.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            aws_sdk_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            aws_sdk_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            aws_sdk_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            aws_sdk_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            aws_sdk_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            aws_sdk_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            aws_sdk_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.process_payment

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.process_payment.async_process_payment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_session_id"] = payment_session_id
        input_["payment_instrument_id"] = payment_instrument_id
        input_["payment_type"] = payment_type
        input_["payment_input"] = payment_input
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
