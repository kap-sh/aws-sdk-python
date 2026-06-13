from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import ensure_async_iterator
from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import ensure_sync_iterator
from aws_sdk_bedrock_agentcore._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore._auth._signers
import aws_sdk_bedrock_agentcore._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import BedrockAgentCoreClient, BedrockAgentCoreClientConfig
    from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import AsyncBedrockAgentCoreClient, AsyncBedrockAgentCoreClientConfig
    import aws_sdk_bedrock_agentcore.types.browser_action
    import aws_sdk_bedrock_agentcore.types.browser_enterprise_policies
    import aws_sdk_bedrock_agentcore.types.browser_extensions
    import aws_sdk_bedrock_agentcore.types.browser_profile_configuration
    import aws_sdk_bedrock_agentcore.types.browser_session_id
    import aws_sdk_bedrock_agentcore.types.browser_session_status
    import aws_sdk_bedrock_agentcore.types.browser_session_timeout
    import aws_sdk_bedrock_agentcore.types.certificates
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.get_browser_session_request
    import aws_sdk_bedrock_agentcore.types.get_browser_session_response
    import aws_sdk_bedrock_agentcore.types.invoke_browser_request
    import aws_sdk_bedrock_agentcore.types.invoke_browser_response
    import aws_sdk_bedrock_agentcore.types.list_browser_sessions_request
    import aws_sdk_bedrock_agentcore.types.list_browser_sessions_response
    import aws_sdk_bedrock_agentcore.types.max_results
    import aws_sdk_bedrock_agentcore.types.name
    import aws_sdk_bedrock_agentcore.types.next_token
    import aws_sdk_bedrock_agentcore.types.proxy_configuration
    import aws_sdk_bedrock_agentcore.types.start_browser_session_request
    import aws_sdk_bedrock_agentcore.types.start_browser_session_response
    import aws_sdk_bedrock_agentcore.types.stop_browser_session_request
    import aws_sdk_bedrock_agentcore.types.stop_browser_session_response
    import aws_sdk_bedrock_agentcore.types.stream_update
    import aws_sdk_bedrock_agentcore.types.update_browser_stream_request
    import aws_sdk_bedrock_agentcore.types.update_browser_stream_response
    import aws_sdk_bedrock_agentcore.types.view_port

class BrowserSessionResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service
    def read(self, browser_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_browser_session_response.GetBrowserSessionResponse":
        """<p>Retrieves detailed information about a specific browser session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, associated streams, and metadata.</p> <p>To get a browser session, you must specify both the browser identifier and the session ID. The response includes information about the session's viewport configuration, timeout settings, and stream endpoints.</p> <p>The following operations are related to <code>GetBrowserSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html\">StartBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListBrowserSessions.html\">ListBrowserSessions</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html\">StopBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser associated with the session.</p>
            session_id: <p>The unique identifier of the browser session to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.get_browser_session_request.GetBrowserSessionRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.get_browser_session_response.GetBrowserSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_browser_session
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_browser_session.get_browser_session(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_browser_session_request.GetBrowserSessionRequest = {}  # type: ignore[typeddict-item]
        input["browser_identifier"] = browser_identifier
        input["session_id"] = session_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def invoke_browser(self, browser_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId", action: "aws_sdk_bedrock_agentcore.types.browser_action.BrowserAction", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.invoke_browser_response.InvokeBrowserResponse":
        """<p>Invokes an operating system-level action on a browser session in Amazon Bedrock AgentCore. This operation provides direct OS-level control over browser sessions, enabling mouse actions, keyboard input, and screenshots that the WebSocket-based Chrome DevTools Protocol (CDP) cannot handle — such as interacting with print dialogs, context menus, and JavaScript alerts.</p> <p>You send a request with exactly one action in the <code>BrowserAction</code> union, and receive a corresponding result in the <code>BrowserActionResult</code> union.</p> <p>The following operations are related to <code>InvokeBrowser</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html\">StartBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html\">GetBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html\">StopBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser associated with the session. This must match the identifier used when creating the session with <code>StartBrowserSession</code>.</p>
            session_id: <p>The unique identifier of the browser session on which to perform the action. This must be an active session created with <code>StartBrowserSession</code>.</p>
            action: <p>The browser action to perform. Exactly one member of the <code>BrowserAction</code> union must be set per request.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.invoke_browser_request.InvokeBrowserRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.invoke_browser_response.InvokeBrowserResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_browser
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_browser.invoke_browser(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.invoke_browser_request.InvokeBrowserRequest = {}  # type: ignore[typeddict-item]
        input["browser_identifier"] = browser_identifier
        input["session_id"] = session_id
        input["action"] = action

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_browser_sessions(self, browser_identifier: str, *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.next_token.NextToken"] = None, status: Optional["aws_sdk_bedrock_agentcore.types.browser_session_status.BrowserSessionStatus"] = None) -> "aws_sdk_bedrock_agentcore.types.list_browser_sessions_response.ListBrowserSessionsResponse":
        """<p>Retrieves a list of browser sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.</p> <p>You can filter the results by browser identifier and session status. The operation supports pagination to handle large result sets efficiently.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.</p> <p>The following operations are related to <code>ListBrowserSessions</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html\">StartBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html\">GetBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser to list sessions for. If specified, only sessions for this browser are returned. If not specified, sessions for all browsers are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.</p>
            status: <p>The status of the browser sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.list_browser_sessions_request.ListBrowserSessionsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.list_browser_sessions_response.ListBrowserSessionsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_browser_sessions
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_browser_sessions.list_browser_sessions(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_browser_sessions_request.ListBrowserSessionsRequest = {}  # type: ignore[typeddict-item]
        input["browser_identifier"] = browser_identifier
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if status is not None:
            input["status"] = status

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def start_browser_session(self, browser_identifier: str, *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, trace_id: Optional[str] = None, trace_parent: Optional[str] = None, name: Optional["aws_sdk_bedrock_agentcore.types.name.Name"] = None, session_timeout_seconds: Optional["aws_sdk_bedrock_agentcore.types.browser_session_timeout.BrowserSessionTimeout"] = None, view_port: Optional["aws_sdk_bedrock_agentcore.types.view_port.ViewPort"] = None, extensions: Optional["aws_sdk_bedrock_agentcore.types.browser_extensions.BrowserExtensions"] = None, profile_configuration: Optional["aws_sdk_bedrock_agentcore.types.browser_profile_configuration.BrowserProfileConfiguration"] = None, proxy_configuration: Optional["aws_sdk_bedrock_agentcore.types.proxy_configuration.ProxyConfiguration"] = None, enterprise_policies: Optional["aws_sdk_bedrock_agentcore.types.browser_enterprise_policies.BrowserEnterprisePolicies"] = None, certificates: Optional["aws_sdk_bedrock_agentcore.types.certificates.Certificates"] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.start_browser_session_response.StartBrowserSessionResponse":
        """<p>Creates and initializes a browser session in Amazon Bedrock AgentCore. The session enables agents to navigate and interact with web content, extract information from websites, and perform web-based tasks as part of their response generation.</p> <p>To create a session, you must specify a browser identifier and a name. You can also configure the viewport dimensions to control the visible area of web content. The session remains active until it times out or you explicitly stop it using the <code>StopBrowserSession</code> operation.</p> <p>The following operations are related to <code>StartBrowserSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html\">GetBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UpdateBrowserStream.html\">UpdateBrowserStream</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SaveBrowserSessionProfile.html\">SaveBrowserSessionProfile</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html\">StopBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeBrowser.html\">InvokeBrowser</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            browser_identifier: <p>The unique identifier of the browser to use for this session. This identifier specifies which browser environment to initialize for the session.</p>
            name: <p>The name of the browser session. This name helps you identify and manage the session. The name does not need to be unique.</p>
            session_timeout_seconds: <p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 3600 seconds (1 hour). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>
            view_port: <p>The dimensions of the browser viewport for this session. This determines the visible area of the web content and affects how web pages are rendered. If not specified, Amazon Bedrock AgentCore uses a default viewport size.</p>
            extensions: <p>A list of browser extensions to load into the browser session.</p>
            profile_configuration: <p>The browser profile configuration to use for this session. A browser profile contains persistent data such as cookies and local storage that can be reused across multiple browser sessions. If specified, the session initializes with the profile's stored data, enabling continuity for tasks that require authentication or personalized settings.</p>
            proxy_configuration: <p>Optional proxy configuration for routing browser traffic through customer-specified proxy servers. When provided, enables HTTP Basic authentication via Amazon Web Services Secrets Manager and domain-based routing rules. Requires <code>secretsmanager:GetSecretValue</code> IAM permission for the specified secret ARNs.</p>
            enterprise_policies: <p>A list of files containing enterprise policies for the browser.</p>
            certificates: <p>A list of certificates to install in the browser session.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.start_browser_session_request.StartBrowserSessionRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.start_browser_session_response.StartBrowserSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_browser_session
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_browser_session.start_browser_session(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.start_browser_session_request.StartBrowserSessionRequest = {}  # type: ignore[typeddict-item]
        if trace_id is not None:
            input["trace_id"] = trace_id
        if trace_parent is not None:
            input["trace_parent"] = trace_parent
        input["browser_identifier"] = browser_identifier
        if name is not None:
            input["name"] = name
        if session_timeout_seconds is not None:
            input["session_timeout_seconds"] = session_timeout_seconds
        if view_port is not None:
            input["view_port"] = view_port
        if extensions is not None:
            input["extensions"] = extensions
        if profile_configuration is not None:
            input["profile_configuration"] = profile_configuration
        if proxy_configuration is not None:
            input["proxy_configuration"] = proxy_configuration
        if enterprise_policies is not None:
            input["enterprise_policies"] = enterprise_policies
        if certificates is not None:
            input["certificates"] = certificates
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def stop_browser_session(self, browser_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, trace_id: Optional[str] = None, trace_parent: Optional[str] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.stop_browser_session_response.StopBrowserSessionResponse":
        """<p>Terminates an active browser session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.</p> <p>To stop a browser session, you must specify both the browser identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using <code>StartBrowserSession</code>.</p> <p>The following operations are related to <code>StopBrowserSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html\">StartBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html\">GetBrowserSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            browser_identifier: <p>The unique identifier of the browser associated with the session.</p>
            session_id: <p>The unique identifier of the browser session to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.stop_browser_session_request.StopBrowserSessionRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.stop_browser_session_response.StopBrowserSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_browser_session
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_browser_session.stop_browser_session(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.stop_browser_session_request.StopBrowserSessionRequest = {}  # type: ignore[typeddict-item]
        if trace_id is not None:
            input["trace_id"] = trace_id
        if trace_parent is not None:
            input["trace_parent"] = trace_parent
        input["browser_identifier"] = browser_identifier
        input["session_id"] = session_id
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update_browser_stream(self, browser_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId", stream_update: "aws_sdk_bedrock_agentcore.types.stream_update.StreamUpdate", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.update_browser_stream_response.UpdateBrowserStreamResponse":
        """<p>Updates a browser stream. To use this operation, you must have permissions to perform the bedrock:UpdateBrowserStream action.</p>

        Args:
            browser_identifier: <p>The identifier of the browser.</p>
            session_id: <p>The identifier of the browser session.</p>
            stream_update: <p>The update to apply to the browser stream.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.update_browser_stream_request.UpdateBrowserStreamRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.update_browser_stream_response.UpdateBrowserStreamResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_browser_stream
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_browser_stream.update_browser_stream(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.update_browser_stream_request.UpdateBrowserStreamRequest = {}  # type: ignore[typeddict-item]
        input["browser_identifier"] = browser_identifier
        input["session_id"] = session_id
        input["stream_update"] = stream_update
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncBrowserSessionResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service
    async def read(self, browser_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_browser_session_response.GetBrowserSessionResponse":
        """<p>Retrieves detailed information about a specific browser session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, associated streams, and metadata.</p> <p>To get a browser session, you must specify both the browser identifier and the session ID. The response includes information about the session's viewport configuration, timeout settings, and stream endpoints.</p> <p>The following operations are related to <code>GetBrowserSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html\">StartBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListBrowserSessions.html\">ListBrowserSessions</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html\">StopBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser associated with the session.</p>
            session_id: <p>The unique identifier of the browser session to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_browser_session_request.GetBrowserSessionRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.get_browser_session_response.GetBrowserSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_browser_session
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_browser_session.async_get_browser_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_browser_session_request.GetBrowserSessionRequest = {}  # type: ignore[typeddict-item]
        input["browser_identifier"] = browser_identifier
        input["session_id"] = session_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def invoke_browser(self, browser_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId", action: "aws_sdk_bedrock_agentcore.types.browser_action.BrowserAction", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.invoke_browser_response.InvokeBrowserResponse":
        """<p>Invokes an operating system-level action on a browser session in Amazon Bedrock AgentCore. This operation provides direct OS-level control over browser sessions, enabling mouse actions, keyboard input, and screenshots that the WebSocket-based Chrome DevTools Protocol (CDP) cannot handle — such as interacting with print dialogs, context menus, and JavaScript alerts.</p> <p>You send a request with exactly one action in the <code>BrowserAction</code> union, and receive a corresponding result in the <code>BrowserActionResult</code> union.</p> <p>The following operations are related to <code>InvokeBrowser</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html\">StartBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html\">GetBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html\">StopBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser associated with the session. This must match the identifier used when creating the session with <code>StartBrowserSession</code>.</p>
            session_id: <p>The unique identifier of the browser session on which to perform the action. This must be an active session created with <code>StartBrowserSession</code>.</p>
            action: <p>The browser action to perform. Exactly one member of the <code>BrowserAction</code> union must be set per request.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.invoke_browser_request.InvokeBrowserRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.invoke_browser_response.InvokeBrowserResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_browser
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_browser.async_invoke_browser(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.invoke_browser_request.InvokeBrowserRequest = {}  # type: ignore[typeddict-item]
        input["browser_identifier"] = browser_identifier
        input["session_id"] = session_id
        input["action"] = action

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_browser_sessions(self, browser_identifier: str, *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.next_token.NextToken"] = None, status: Optional["aws_sdk_bedrock_agentcore.types.browser_session_status.BrowserSessionStatus"] = None) -> "aws_sdk_bedrock_agentcore.types.list_browser_sessions_response.ListBrowserSessionsResponse":
        """<p>Retrieves a list of browser sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.</p> <p>You can filter the results by browser identifier and session status. The operation supports pagination to handle large result sets efficiently.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.</p> <p>The following operations are related to <code>ListBrowserSessions</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html\">StartBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html\">GetBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser to list sessions for. If specified, only sessions for this browser are returned. If not specified, sessions for all browsers are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.</p>
            status: <p>The status of the browser sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_browser_sessions_request.ListBrowserSessionsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.list_browser_sessions_response.ListBrowserSessionsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_browser_sessions
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_browser_sessions.async_list_browser_sessions(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_browser_sessions_request.ListBrowserSessionsRequest = {}  # type: ignore[typeddict-item]
        input["browser_identifier"] = browser_identifier
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if status is not None:
            input["status"] = status

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def start_browser_session(self, browser_identifier: str, *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, trace_id: Optional[str] = None, trace_parent: Optional[str] = None, name: Optional["aws_sdk_bedrock_agentcore.types.name.Name"] = None, session_timeout_seconds: Optional["aws_sdk_bedrock_agentcore.types.browser_session_timeout.BrowserSessionTimeout"] = None, view_port: Optional["aws_sdk_bedrock_agentcore.types.view_port.ViewPort"] = None, extensions: Optional["aws_sdk_bedrock_agentcore.types.browser_extensions.BrowserExtensions"] = None, profile_configuration: Optional["aws_sdk_bedrock_agentcore.types.browser_profile_configuration.BrowserProfileConfiguration"] = None, proxy_configuration: Optional["aws_sdk_bedrock_agentcore.types.proxy_configuration.ProxyConfiguration"] = None, enterprise_policies: Optional["aws_sdk_bedrock_agentcore.types.browser_enterprise_policies.BrowserEnterprisePolicies"] = None, certificates: Optional["aws_sdk_bedrock_agentcore.types.certificates.Certificates"] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.start_browser_session_response.StartBrowserSessionResponse":
        """<p>Creates and initializes a browser session in Amazon Bedrock AgentCore. The session enables agents to navigate and interact with web content, extract information from websites, and perform web-based tasks as part of their response generation.</p> <p>To create a session, you must specify a browser identifier and a name. You can also configure the viewport dimensions to control the visible area of web content. The session remains active until it times out or you explicitly stop it using the <code>StopBrowserSession</code> operation.</p> <p>The following operations are related to <code>StartBrowserSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html\">GetBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UpdateBrowserStream.html\">UpdateBrowserStream</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SaveBrowserSessionProfile.html\">SaveBrowserSessionProfile</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html\">StopBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeBrowser.html\">InvokeBrowser</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            browser_identifier: <p>The unique identifier of the browser to use for this session. This identifier specifies which browser environment to initialize for the session.</p>
            name: <p>The name of the browser session. This name helps you identify and manage the session. The name does not need to be unique.</p>
            session_timeout_seconds: <p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 3600 seconds (1 hour). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>
            view_port: <p>The dimensions of the browser viewport for this session. This determines the visible area of the web content and affects how web pages are rendered. If not specified, Amazon Bedrock AgentCore uses a default viewport size.</p>
            extensions: <p>A list of browser extensions to load into the browser session.</p>
            profile_configuration: <p>The browser profile configuration to use for this session. A browser profile contains persistent data such as cookies and local storage that can be reused across multiple browser sessions. If specified, the session initializes with the profile's stored data, enabling continuity for tasks that require authentication or personalized settings.</p>
            proxy_configuration: <p>Optional proxy configuration for routing browser traffic through customer-specified proxy servers. When provided, enables HTTP Basic authentication via Amazon Web Services Secrets Manager and domain-based routing rules. Requires <code>secretsmanager:GetSecretValue</code> IAM permission for the specified secret ARNs.</p>
            enterprise_policies: <p>A list of files containing enterprise policies for the browser.</p>
            certificates: <p>A list of certificates to install in the browser session.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.start_browser_session_request.StartBrowserSessionRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.start_browser_session_response.StartBrowserSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_browser_session
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_browser_session.async_start_browser_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.start_browser_session_request.StartBrowserSessionRequest = {}  # type: ignore[typeddict-item]
        if trace_id is not None:
            input["trace_id"] = trace_id
        if trace_parent is not None:
            input["trace_parent"] = trace_parent
        input["browser_identifier"] = browser_identifier
        if name is not None:
            input["name"] = name
        if session_timeout_seconds is not None:
            input["session_timeout_seconds"] = session_timeout_seconds
        if view_port is not None:
            input["view_port"] = view_port
        if extensions is not None:
            input["extensions"] = extensions
        if profile_configuration is not None:
            input["profile_configuration"] = profile_configuration
        if proxy_configuration is not None:
            input["proxy_configuration"] = proxy_configuration
        if enterprise_policies is not None:
            input["enterprise_policies"] = enterprise_policies
        if certificates is not None:
            input["certificates"] = certificates
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def stop_browser_session(self, browser_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, trace_id: Optional[str] = None, trace_parent: Optional[str] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.stop_browser_session_response.StopBrowserSessionResponse":
        """<p>Terminates an active browser session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.</p> <p>To stop a browser session, you must specify both the browser identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using <code>StartBrowserSession</code>.</p> <p>The following operations are related to <code>StopBrowserSession</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html\">StartBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html\">GetBrowserSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            browser_identifier: <p>The unique identifier of the browser associated with the session.</p>
            session_id: <p>The unique identifier of the browser session to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.stop_browser_session_request.StopBrowserSessionRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.stop_browser_session_response.StopBrowserSessionResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_browser_session
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_browser_session.async_stop_browser_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.stop_browser_session_request.StopBrowserSessionRequest = {}  # type: ignore[typeddict-item]
        if trace_id is not None:
            input["trace_id"] = trace_id
        if trace_parent is not None:
            input["trace_parent"] = trace_parent
        input["browser_identifier"] = browser_identifier
        input["session_id"] = session_id
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update_browser_stream(self, browser_identifier: str, session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId", stream_update: "aws_sdk_bedrock_agentcore.types.stream_update.StreamUpdate", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.update_browser_stream_response.UpdateBrowserStreamResponse":
        """<p>Updates a browser stream. To use this operation, you must have permissions to perform the bedrock:UpdateBrowserStream action.</p>

        Args:
            browser_identifier: <p>The identifier of the browser.</p>
            session_id: <p>The identifier of the browser session.</p>
            stream_update: <p>The update to apply to the browser stream.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.update_browser_stream_request.UpdateBrowserStreamRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.update_browser_stream_response.UpdateBrowserStreamResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_browser_stream
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_browser_stream.async_update_browser_stream(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.update_browser_stream_request.UpdateBrowserStreamRequest = {}  # type: ignore[typeddict-item]
        input["browser_identifier"] = browser_identifier
        input["session_id"] = session_id
        input["stream_update"] = stream_update
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output