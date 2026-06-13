from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import ensure_async_iterator
from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import ensure_sync_iterator
from aws_sdk_bedrock_agentcore._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore._auth._signers
import aws_sdk_bedrock_agentcore._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import BedrockAgentCoreClient, BedrockAgentCoreClientConfig
    from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import AsyncBedrockAgentCoreClient, AsyncBedrockAgentCoreClientConfig
    import aws_sdk_bedrock_agentcore.types.certificates
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_id
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_status
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_timeout
    import aws_sdk_bedrock_agentcore.types.get_code_interpreter_session_request
    import aws_sdk_bedrock_agentcore.types.get_code_interpreter_session_response
    import aws_sdk_bedrock_agentcore.types.list_code_interpreter_sessions_request
    import aws_sdk_bedrock_agentcore.types.list_code_interpreter_sessions_response
    import aws_sdk_bedrock_agentcore.types.max_results
    import aws_sdk_bedrock_agentcore.types.name
    import aws_sdk_bedrock_agentcore.types.next_token
    import aws_sdk_bedrock_agentcore.types.start_code_interpreter_session_request
    import aws_sdk_bedrock_agentcore.types.start_code_interpreter_session_response
    import aws_sdk_bedrock_agentcore.types.stop_code_interpreter_session_request
    import aws_sdk_bedrock_agentcore.types.stop_code_interpreter_session_response

class CodeInterpreterSessionResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service
    def read(self, code_interpreter_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_code_interpreter_session_response.GetCodeInterpreterSessionResponse":
        """<p>Retrieves detailed information about a specific code interpreter session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, and metadata.</p> <p>To get a code interpreter session, you must specify both the code interpreter identifier and the session ID. The response includes information about the session's timeout settings and current status.</p> <p>The following operations are related to <code>GetCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html\">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListCodeInterpreterSessions.html\">ListCodeInterpreterSessions</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html\">StopCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session.</p>
            session_id: <p>The unique identifier of the code interpreter session to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.get_code_interpreter_session_request.GetCodeInterpreterSessionRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.get_code_interpreter_session_response.GetCodeInterpreterSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_code_interpreter_session
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_code_interpreter_session.get_code_interpreter_session(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_code_interpreter_session_request.GetCodeInterpreterSessionRequest = {}  # type: ignore[typeddict-item]
        input["code_interpreter_identifier"] = code_interpreter_identifier
        input["session_id"] = session_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_code_interpreter_sessions(self, code_interpreter_identifier: str, *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.next_token.NextToken"] = None, status: Optional["aws_sdk_bedrock_agentcore.types.code_interpreter_session_status.CodeInterpreterSessionStatus"] = None) -> "aws_sdk_bedrock_agentcore.types.list_code_interpreter_sessions_response.ListCodeInterpreterSessionsResponse":
        """<p>Retrieves a list of code interpreter sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.</p> <p>You can filter the results by code interpreter identifier and session status. The operation supports pagination to handle large result sets efficiently.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.</p> <p>The following operations are related to <code>ListCodeInterpreterSessions</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html\">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html\">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter to list sessions for. If specified, only sessions for this code interpreter are returned. If not specified, sessions for all code interpreters are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.</p>
            status: <p>The status of the code interpreter sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.list_code_interpreter_sessions_request.ListCodeInterpreterSessionsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.list_code_interpreter_sessions_response.ListCodeInterpreterSessionsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_code_interpreter_sessions
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_code_interpreter_sessions.list_code_interpreter_sessions(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_code_interpreter_sessions_request.ListCodeInterpreterSessionsRequest = {}  # type: ignore[typeddict-item]
        input["code_interpreter_identifier"] = code_interpreter_identifier
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if status is not None:
            input["status"] = status

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def start_code_interpreter_session(self, code_interpreter_identifier: str, *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, trace_id: Optional[str] = None, trace_parent: Optional[str] = None, name: Optional["aws_sdk_bedrock_agentcore.types.name.Name"] = None, session_timeout_seconds: Optional["aws_sdk_bedrock_agentcore.types.code_interpreter_session_timeout.CodeInterpreterSessionTimeout"] = None, certificates: Optional["aws_sdk_bedrock_agentcore.types.certificates.Certificates"] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.start_code_interpreter_session_response.StartCodeInterpreterSessionResponse":
        """<p>Creates and initializes a code interpreter session in Amazon Bedrock AgentCore. The session enables agents to execute code as part of their response generation, supporting programming languages such as Python for data analysis, visualization, and computation tasks.</p> <p>To create a session, you must specify a code interpreter identifier and a name. The session remains active until it times out or you explicitly stop it using the <code>StopCodeInterpreterSession</code> operation.</p> <p>The following operations are related to <code>StartCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeCodeInterpreter.html\">InvokeCodeInterpreter</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html\">GetCodeInterpreterSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html\">StopCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            code_interpreter_identifier: <p>The unique identifier of the code interpreter to use for this session. This identifier specifies which code interpreter environment to initialize for the session.</p>
            name: <p>The name of the code interpreter session. This name helps you identify and manage the session. The name does not need to be unique.</p>
            session_timeout_seconds: <p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 900 seconds (15 minutes). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>
            certificates: <p>A list of certificates to install in the code interpreter session.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.start_code_interpreter_session_request.StartCodeInterpreterSessionRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.start_code_interpreter_session_response.StartCodeInterpreterSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_code_interpreter_session
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_code_interpreter_session.start_code_interpreter_session(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.start_code_interpreter_session_request.StartCodeInterpreterSessionRequest = {}  # type: ignore[typeddict-item]
        if trace_id is not None:
            input["trace_id"] = trace_id
        if trace_parent is not None:
            input["trace_parent"] = trace_parent
        input["code_interpreter_identifier"] = code_interpreter_identifier
        if name is not None:
            input["name"] = name
        if session_timeout_seconds is not None:
            input["session_timeout_seconds"] = session_timeout_seconds
        if certificates is not None:
            input["certificates"] = certificates
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def stop_code_interpreter_session(self, code_interpreter_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, trace_id: Optional[str] = None, trace_parent: Optional[str] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.stop_code_interpreter_session_response.StopCodeInterpreterSessionResponse":
        """<p>Terminates an active code interpreter session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.</p> <p>To stop a code interpreter session, you must specify both the code interpreter identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using <code>StartCodeInterpreterSession</code>.</p> <p>The following operations are related to <code>StopCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html\">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html\">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session.</p>
            session_id: <p>The unique identifier of the code interpreter session to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.stop_code_interpreter_session_request.StopCodeInterpreterSessionRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.stop_code_interpreter_session_response.StopCodeInterpreterSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_code_interpreter_session
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_code_interpreter_session.stop_code_interpreter_session(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.stop_code_interpreter_session_request.StopCodeInterpreterSessionRequest = {}  # type: ignore[typeddict-item]
        if trace_id is not None:
            input["trace_id"] = trace_id
        if trace_parent is not None:
            input["trace_parent"] = trace_parent
        input["code_interpreter_identifier"] = code_interpreter_identifier
        input["session_id"] = session_id
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncCodeInterpreterSessionResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service
    async def read(self, code_interpreter_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_code_interpreter_session_response.GetCodeInterpreterSessionResponse":
        """<p>Retrieves detailed information about a specific code interpreter session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, and metadata.</p> <p>To get a code interpreter session, you must specify both the code interpreter identifier and the session ID. The response includes information about the session's timeout settings and current status.</p> <p>The following operations are related to <code>GetCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html\">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListCodeInterpreterSessions.html\">ListCodeInterpreterSessions</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html\">StopCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session.</p>
            session_id: <p>The unique identifier of the code interpreter session to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_code_interpreter_session_request.GetCodeInterpreterSessionRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.get_code_interpreter_session_response.GetCodeInterpreterSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_code_interpreter_session
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_code_interpreter_session.async_get_code_interpreter_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_code_interpreter_session_request.GetCodeInterpreterSessionRequest = {}  # type: ignore[typeddict-item]
        input["code_interpreter_identifier"] = code_interpreter_identifier
        input["session_id"] = session_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_code_interpreter_sessions(self, code_interpreter_identifier: str, *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.next_token.NextToken"] = None, status: Optional["aws_sdk_bedrock_agentcore.types.code_interpreter_session_status.CodeInterpreterSessionStatus"] = None) -> "aws_sdk_bedrock_agentcore.types.list_code_interpreter_sessions_response.ListCodeInterpreterSessionsResponse":
        """<p>Retrieves a list of code interpreter sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.</p> <p>You can filter the results by code interpreter identifier and session status. The operation supports pagination to handle large result sets efficiently.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.</p> <p>The following operations are related to <code>ListCodeInterpreterSessions</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html\">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html\">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter to list sessions for. If specified, only sessions for this code interpreter are returned. If not specified, sessions for all code interpreters are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.</p>
            status: <p>The status of the code interpreter sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_code_interpreter_sessions_request.ListCodeInterpreterSessionsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.list_code_interpreter_sessions_response.ListCodeInterpreterSessionsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_code_interpreter_sessions
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_code_interpreter_sessions.async_list_code_interpreter_sessions(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_code_interpreter_sessions_request.ListCodeInterpreterSessionsRequest = {}  # type: ignore[typeddict-item]
        input["code_interpreter_identifier"] = code_interpreter_identifier
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if status is not None:
            input["status"] = status

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def start_code_interpreter_session(self, code_interpreter_identifier: str, *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, trace_id: Optional[str] = None, trace_parent: Optional[str] = None, name: Optional["aws_sdk_bedrock_agentcore.types.name.Name"] = None, session_timeout_seconds: Optional["aws_sdk_bedrock_agentcore.types.code_interpreter_session_timeout.CodeInterpreterSessionTimeout"] = None, certificates: Optional["aws_sdk_bedrock_agentcore.types.certificates.Certificates"] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.start_code_interpreter_session_response.StartCodeInterpreterSessionResponse":
        """<p>Creates and initializes a code interpreter session in Amazon Bedrock AgentCore. The session enables agents to execute code as part of their response generation, supporting programming languages such as Python for data analysis, visualization, and computation tasks.</p> <p>To create a session, you must specify a code interpreter identifier and a name. The session remains active until it times out or you explicitly stop it using the <code>StopCodeInterpreterSession</code> operation.</p> <p>The following operations are related to <code>StartCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeCodeInterpreter.html\">InvokeCodeInterpreter</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html\">GetCodeInterpreterSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html\">StopCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            code_interpreter_identifier: <p>The unique identifier of the code interpreter to use for this session. This identifier specifies which code interpreter environment to initialize for the session.</p>
            name: <p>The name of the code interpreter session. This name helps you identify and manage the session. The name does not need to be unique.</p>
            session_timeout_seconds: <p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 900 seconds (15 minutes). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>
            certificates: <p>A list of certificates to install in the code interpreter session.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.start_code_interpreter_session_request.StartCodeInterpreterSessionRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.start_code_interpreter_session_response.StartCodeInterpreterSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_code_interpreter_session
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_code_interpreter_session.async_start_code_interpreter_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.start_code_interpreter_session_request.StartCodeInterpreterSessionRequest = {}  # type: ignore[typeddict-item]
        if trace_id is not None:
            input["trace_id"] = trace_id
        if trace_parent is not None:
            input["trace_parent"] = trace_parent
        input["code_interpreter_identifier"] = code_interpreter_identifier
        if name is not None:
            input["name"] = name
        if session_timeout_seconds is not None:
            input["session_timeout_seconds"] = session_timeout_seconds
        if certificates is not None:
            input["certificates"] = certificates
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def stop_code_interpreter_session(self, code_interpreter_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, trace_id: Optional[str] = None, trace_parent: Optional[str] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.stop_code_interpreter_session_response.StopCodeInterpreterSessionResponse":
        """<p>Terminates an active code interpreter session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.</p> <p>To stop a code interpreter session, you must specify both the code interpreter identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using <code>StartCodeInterpreterSession</code>.</p> <p>The following operations are related to <code>StopCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html\">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html\">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session.</p>
            session_id: <p>The unique identifier of the code interpreter session to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.stop_code_interpreter_session_request.StopCodeInterpreterSessionRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.stop_code_interpreter_session_response.StopCodeInterpreterSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_code_interpreter_session
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_code_interpreter_session.async_stop_code_interpreter_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.stop_code_interpreter_session_request.StopCodeInterpreterSessionRequest = {}  # type: ignore[typeddict-item]
        if trace_id is not None:
            input["trace_id"] = trace_id
        if trace_parent is not None:
            input["trace_parent"] = trace_parent
        input["code_interpreter_identifier"] = code_interpreter_identifier
        input["session_id"] = session_id
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output