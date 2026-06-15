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
    import aws_sdk_bedrock_agentcore.types.blockchain_chain_id
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.create_payment_instrument_request
    import aws_sdk_bedrock_agentcore.types.create_payment_instrument_response
    import aws_sdk_bedrock_agentcore.types.delete_payment_instrument_request
    import aws_sdk_bedrock_agentcore.types.delete_payment_instrument_response
    import aws_sdk_bedrock_agentcore.types.get_payment_instrument_balance_request
    import aws_sdk_bedrock_agentcore.types.get_payment_instrument_balance_response
    import aws_sdk_bedrock_agentcore.types.get_payment_instrument_request
    import aws_sdk_bedrock_agentcore.types.get_payment_instrument_response
    import aws_sdk_bedrock_agentcore.types.instrument_balance_token
    import aws_sdk_bedrock_agentcore.types.list_payment_instruments_request
    import aws_sdk_bedrock_agentcore.types.list_payment_instruments_response
    import aws_sdk_bedrock_agentcore.types.next_token
    import aws_sdk_bedrock_agentcore.types.payment_agent_name
    import aws_sdk_bedrock_agentcore.types.payment_connector_id
    import aws_sdk_bedrock_agentcore.types.payment_instrument_details
    import aws_sdk_bedrock_agentcore.types.payment_instrument_id
    import aws_sdk_bedrock_agentcore.types.payment_instrument_summary
    import aws_sdk_bedrock_agentcore.types.payment_instrument_type
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.user_id
    from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class PaymentInstrumentResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def create(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_type: "aws_sdk_bedrock_agentcore.types.payment_instrument_type.PaymentInstrumentType",
        payment_instrument_details: "aws_sdk_bedrock_agentcore.types.payment_instrument_details.PaymentInstrumentDetails",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse":
        """<p>Create a new payment instrument for a connector.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector to use for this instrument.</p>
            payment_instrument_type: <p>The type of payment instrument being created.</p>
            payment_instrument_details: <p>The details of the payment instrument.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_instrument

            output, http_response = (
                aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_instrument.create_payment_instrument(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_connector_id"] = payment_connector_id
        input_["payment_instrument_type"] = payment_instrument_type
        input_["payment_instrument_details"] = payment_instrument_details
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_instrument_id: "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        payment_connector_id: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse":
        """<p>Get a payment instrument by ID.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector.</p>
            payment_instrument_id: <p>The ID of the payment instrument to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore.types.get_payment_instrument_request.GetPaymentInstrumentRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument

            output, http_response = (
                aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument.get_payment_instrument(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_payment_instrument_request.GetPaymentInstrumentRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        if payment_connector_id is not None:
            input_["payment_connector_id"] = payment_connector_id
        input_["payment_instrument_id"] = payment_instrument_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_id: "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.delete_payment_instrument_response.DeletePaymentInstrumentResponse":
        """<p>Deletes a payment instrument. This is a soft delete operation that preserves the record for audit and compliance purposes.</p>

        Args:
            user_id: <p>The user ID making the delete request. Must match the instrument's userId.</p>
            payment_manager_arn: <p>The payment manager ARN. Must match the instrument's paymentManagerArn.</p>
            payment_connector_id: <p>The payment connector ID. Must match the instrument's paymentConnectorId.</p>
            payment_instrument_id: <p>The payment instrument ID to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore.types.delete_payment_instrument_request.DeletePaymentInstrumentRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore.types.delete_payment_instrument_response.DeletePaymentInstrumentResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_instrument

            output, http_response = (
                aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_instrument.delete_payment_instrument(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.delete_payment_instrument_request.DeletePaymentInstrumentRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_connector_id"] = payment_connector_id
        input_["payment_instrument_id"] = payment_instrument_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        payment_connector_id: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.list_payment_instruments_response.ListPaymentInstrumentsResponse":
        """<p>List payment instruments for a manager.</p>

        Args:
            user_id: <p>The user ID associated with the payment instruments.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns the payment instruments.</p>
            payment_connector_id: <p>The ID of the payment connector to filter by.</p>
            next_token: <p>Token for pagination to retrieve the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore.types.list_payment_instruments_request.ListPaymentInstrumentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore.types.list_payment_instruments_response.ListPaymentInstrumentsResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_instruments

            output, http_response = (
                aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_instruments.list_payment_instruments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.list_payment_instruments_request.ListPaymentInstrumentsRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        if payment_connector_id is not None:
            input_["payment_connector_id"] = payment_connector_id
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

    def get_payment_instrument_balance(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_id: "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        chain: "aws_sdk_bedrock_agentcore.types.blockchain_chain_id.BlockchainChainId",
        token: "aws_sdk_bedrock_agentcore.types.instrument_balance_token.InstrumentBalanceToken",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.get_payment_instrument_balance_response.GetPaymentInstrumentBalanceResponse":
        """<p>Get the balance of a payment instrument.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector associated with this instrument.</p>
            payment_instrument_id: <p>The ID of the payment instrument to query balance for.</p>
            chain: <p>The specific blockchain chain to query balance on. Required because balances are chain-specific.</p>
            token: <p>The token to query balance for. Only tokens supported for X402 payments are returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore.types.get_payment_instrument_balance_request.GetPaymentInstrumentBalanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore.types.get_payment_instrument_balance_response.GetPaymentInstrumentBalanceResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument_balance

            output, http_response = (
                aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument_balance.get_payment_instrument_balance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_payment_instrument_balance_request.GetPaymentInstrumentBalanceRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_connector_id"] = payment_connector_id
        input_["payment_instrument_id"] = payment_instrument_id
        input_["chain"] = chain
        input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncPaymentInstrumentResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def create(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_type: "aws_sdk_bedrock_agentcore.types.payment_instrument_type.PaymentInstrumentType",
        payment_instrument_details: "aws_sdk_bedrock_agentcore.types.payment_instrument_details.PaymentInstrumentDetails",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse":
        """<p>Create a new payment instrument for a connector.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector to use for this instrument.</p>
            payment_instrument_type: <p>The type of payment instrument being created.</p>
            payment_instrument_details: <p>The details of the payment instrument.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_instrument

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_instrument.async_create_payment_instrument(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_connector_id"] = payment_connector_id
        input_["payment_instrument_type"] = payment_instrument_type
        input_["payment_instrument_details"] = payment_instrument_details
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_instrument_id: "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        payment_connector_id: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse":
        """<p>Get a payment instrument by ID.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector.</p>
            payment_instrument_id: <p>The ID of the payment instrument to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_payment_instrument_request.GetPaymentInstrumentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument.async_get_payment_instrument(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_payment_instrument_request.GetPaymentInstrumentRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        if payment_connector_id is not None:
            input_["payment_connector_id"] = payment_connector_id
        input_["payment_instrument_id"] = payment_instrument_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_id: "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.delete_payment_instrument_response.DeletePaymentInstrumentResponse":
        """<p>Deletes a payment instrument. This is a soft delete operation that preserves the record for audit and compliance purposes.</p>

        Args:
            user_id: <p>The user ID making the delete request. Must match the instrument's userId.</p>
            payment_manager_arn: <p>The payment manager ARN. Must match the instrument's paymentManagerArn.</p>
            payment_connector_id: <p>The payment connector ID. Must match the instrument's paymentConnectorId.</p>
            payment_instrument_id: <p>The payment instrument ID to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.delete_payment_instrument_request.DeletePaymentInstrumentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.delete_payment_instrument_response.DeletePaymentInstrumentResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_instrument

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_instrument.async_delete_payment_instrument(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.delete_payment_instrument_request.DeletePaymentInstrumentRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_connector_id"] = payment_connector_id
        input_["payment_instrument_id"] = payment_instrument_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        payment_connector_id: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.list_payment_instruments_response.ListPaymentInstrumentsResponse":
        """<p>List payment instruments for a manager.</p>

        Args:
            user_id: <p>The user ID associated with the payment instruments.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns the payment instruments.</p>
            payment_connector_id: <p>The ID of the payment connector to filter by.</p>
            next_token: <p>Token for pagination to retrieve the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_payment_instruments_request.ListPaymentInstrumentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.list_payment_instruments_response.ListPaymentInstrumentsResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_instruments

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_instruments.async_list_payment_instruments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.list_payment_instruments_request.ListPaymentInstrumentsRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        if payment_connector_id is not None:
            input_["payment_connector_id"] = payment_connector_id
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

    async def get_payment_instrument_balance(
        self,
        payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_id: "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        chain: "aws_sdk_bedrock_agentcore.types.blockchain_chain_id.BlockchainChainId",
        token: "aws_sdk_bedrock_agentcore.types.instrument_balance_token.InstrumentBalanceToken",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.get_payment_instrument_balance_response.GetPaymentInstrumentBalanceResponse":
        """<p>Get the balance of a payment instrument.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector associated with this instrument.</p>
            payment_instrument_id: <p>The ID of the payment instrument to query balance for.</p>
            chain: <p>The specific blockchain chain to query balance on. Required because balances are chain-specific.</p>
            token: <p>The token to query balance for. Only tokens supported for X402 payments are returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_payment_instrument_balance_request.GetPaymentInstrumentBalanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.get_payment_instrument_balance_response.GetPaymentInstrumentBalanceResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument_balance

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument_balance.async_get_payment_instrument_balance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_payment_instrument_balance_request.GetPaymentInstrumentBalanceRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_connector_id"] = payment_connector_id
        input_["payment_instrument_id"] = payment_instrument_id
        input_["chain"] = chain
        input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
