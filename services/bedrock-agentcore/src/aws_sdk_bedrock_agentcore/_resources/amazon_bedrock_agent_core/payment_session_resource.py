from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import ensure_async_iterator
from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import ensure_sync_iterator
import datetime
from aws_sdk_bedrock_agentcore._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore._auth._signers
import aws_sdk_bedrock_agentcore._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import BedrockAgentCoreClient, BedrockAgentCoreClientConfig
    from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import AsyncBedrockAgentCoreClient, AsyncBedrockAgentCoreClientConfig
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.create_payment_session_request
    import aws_sdk_bedrock_agentcore.types.create_payment_session_response
    import aws_sdk_bedrock_agentcore.types.delete_payment_session_request
    import aws_sdk_bedrock_agentcore.types.delete_payment_session_response
    import aws_sdk_bedrock_agentcore.types.get_payment_session_request
    import aws_sdk_bedrock_agentcore.types.get_payment_session_response
    import aws_sdk_bedrock_agentcore.types.list_payment_sessions_request
    import aws_sdk_bedrock_agentcore.types.list_payment_sessions_response
    import aws_sdk_bedrock_agentcore.types.next_token
    import aws_sdk_bedrock_agentcore.types.payment_agent_name
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.payment_session_id
    import aws_sdk_bedrock_agentcore.types.payment_session_summary
    import aws_sdk_bedrock_agentcore.types.session_limits
    import aws_sdk_bedrock_agentcore.types.user_id

class PaymentSessionResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service
    def create(self, payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn", expiry_time_in_minutes: int, *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None, agent_name: Optional["aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"] = None, limits: Optional["aws_sdk_bedrock_agentcore.types.session_limits.SessionLimits"] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.create_payment_session_response.CreatePaymentSessionResponse":
        """<p>Create a new payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment session.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this session.</p>
            limits: <p>The spending limits for this payment session.</p>
            expiry_time_in_minutes: <p>The session expiry time in minutes. Must be between 15 and 480 minutes.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.create_payment_session_request.CreatePaymentSessionRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.create_payment_session_response.CreatePaymentSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_session
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_session.create_payment_session(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.create_payment_session_request.CreatePaymentSessionRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        if limits is not None:
            input_["limits"] = limits
        input_["expiry_time_in_minutes"] = expiry_time_in_minutes
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input_, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn", payment_session_id: "aws_sdk_bedrock_agentcore.types.payment_session_id.PaymentSessionId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None, agent_name: Optional["aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"] = None) -> "aws_sdk_bedrock_agentcore.types.get_payment_session_response.GetPaymentSessionResponse":
        """<p>Get a payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment session.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this session.</p>
            payment_session_id: <p>The ID of the payment session to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.get_payment_session_request.GetPaymentSessionRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.get_payment_session_response.GetPaymentSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_session
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_session.get_payment_session(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_payment_session_request.GetPaymentSessionRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_session_id"] = payment_session_id

        response = execute_pipeline(OperationRequest(input=input_, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn", payment_session_id: "aws_sdk_bedrock_agentcore.types.payment_session_id.PaymentSessionId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None) -> "aws_sdk_bedrock_agentcore.types.delete_payment_session_response.DeletePaymentSessionResponse":
        """<p>Deletes a payment session. This permanently removes the payment session record.</p>

        Args:
            user_id: <p>The user ID making the delete request. Must match the session's userId.</p>
            payment_manager_arn: <p>The payment manager ARN. Must match the session's paymentManagerArn.</p>
            payment_session_id: <p>The payment session ID to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.delete_payment_session_request.DeletePaymentSessionRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.delete_payment_session_response.DeletePaymentSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_session
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_session.delete_payment_session(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.delete_payment_session_request.DeletePaymentSessionRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_session_id"] = payment_session_id

        response = execute_pipeline(OperationRequest(input=input_, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None, agent_name: Optional["aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.next_token.NextToken"] = None, max_results: Optional[int] = None) -> "aws_sdk_bedrock_agentcore.types.list_payment_sessions_response.ListPaymentSessionsResponse":
        """<p>List payment sessions.</p>

        Args:
            user_id: <p>The user ID associated with the payment sessions.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns the sessions.</p>
            next_token: <p>Token for pagination to retrieve the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single response.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.list_payment_sessions_request.ListPaymentSessionsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.list_payment_sessions_response.ListPaymentSessionsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_sessions
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_sessions.list_payment_sessions(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.list_payment_sessions_request.ListPaymentSessionsRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input_, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncPaymentSessionResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service
    async def create(self, payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn", expiry_time_in_minutes: int, *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None, agent_name: Optional["aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"] = None, limits: Optional["aws_sdk_bedrock_agentcore.types.session_limits.SessionLimits"] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.create_payment_session_response.CreatePaymentSessionResponse":
        """<p>Create a new payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment session.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this session.</p>
            limits: <p>The spending limits for this payment session.</p>
            expiry_time_in_minutes: <p>The session expiry time in minutes. Must be between 15 and 480 minutes.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.create_payment_session_request.CreatePaymentSessionRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.create_payment_session_response.CreatePaymentSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_session
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_session.async_create_payment_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.create_payment_session_request.CreatePaymentSessionRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        if limits is not None:
            input_["limits"] = limits
        input_["expiry_time_in_minutes"] = expiry_time_in_minutes
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input_, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn", payment_session_id: "aws_sdk_bedrock_agentcore.types.payment_session_id.PaymentSessionId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None, agent_name: Optional["aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"] = None) -> "aws_sdk_bedrock_agentcore.types.get_payment_session_response.GetPaymentSessionResponse":
        """<p>Get a payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment session.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this session.</p>
            payment_session_id: <p>The ID of the payment session to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_payment_session_request.GetPaymentSessionRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.get_payment_session_response.GetPaymentSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_session
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_session.async_get_payment_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_payment_session_request.GetPaymentSessionRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_session_id"] = payment_session_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input_, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn", payment_session_id: "aws_sdk_bedrock_agentcore.types.payment_session_id.PaymentSessionId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None) -> "aws_sdk_bedrock_agentcore.types.delete_payment_session_response.DeletePaymentSessionResponse":
        """<p>Deletes a payment session. This permanently removes the payment session record.</p>

        Args:
            user_id: <p>The user ID making the delete request. Must match the session's userId.</p>
            payment_manager_arn: <p>The payment manager ARN. Must match the session's paymentManagerArn.</p>
            payment_session_id: <p>The payment session ID to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.delete_payment_session_request.DeletePaymentSessionRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.delete_payment_session_response.DeletePaymentSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_session
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_session.async_delete_payment_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.delete_payment_session_request.DeletePaymentSessionRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        input_["payment_manager_arn"] = payment_manager_arn
        input_["payment_session_id"] = payment_session_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input_, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, user_id: Optional["aws_sdk_bedrock_agentcore.types.user_id.UserId"] = None, agent_name: Optional["aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.next_token.NextToken"] = None, max_results: Optional[int] = None) -> "aws_sdk_bedrock_agentcore.types.list_payment_sessions_response.ListPaymentSessionsResponse":
        """<p>List payment sessions.</p>

        Args:
            user_id: <p>The user ID associated with the payment sessions.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns the sessions.</p>
            next_token: <p>Token for pagination to retrieve the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single response.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_payment_sessions_request.ListPaymentSessionsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.list_payment_sessions_response.ListPaymentSessionsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_sessions
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_sessions.async_list_payment_sessions(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.list_payment_sessions_request.ListPaymentSessionsRequest = {}  # type: ignore[typeddict-item]
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        input_["payment_manager_arn"] = payment_manager_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input_, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output