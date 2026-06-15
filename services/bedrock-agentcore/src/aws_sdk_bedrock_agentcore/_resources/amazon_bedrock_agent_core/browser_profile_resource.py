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
    import aws_sdk_bedrock_agentcore.types.browser_profile_id
    import aws_sdk_bedrock_agentcore.types.browser_session_id
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.save_browser_session_profile_request
    import aws_sdk_bedrock_agentcore.types.save_browser_session_profile_response
    from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class BrowserProfileResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def save_browser_session_profile(
        self,
        profile_identifier: "aws_sdk_bedrock_agentcore.types.browser_profile_id.BrowserProfileId",
        browser_identifier: str,
        session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.save_browser_session_profile_response.SaveBrowserSessionProfileResponse":
        r"""<p>Saves the current state of a browser session as a reusable profile in Amazon Bedrock AgentCore. A browser profile captures persistent browser data such as cookies and local storage from an active session, enabling you to reuse this data in future browser sessions.</p> <p>To save a browser session profile, you must specify the profile identifier, browser identifier, and session ID. The session must be active when saving the profile. Once saved, the profile can be used with the <code>StartBrowserSession</code> operation to initialize new sessions with the stored browser state.</p> <p>Browser profiles are useful for scenarios that require persistent authentication, maintaining user preferences across sessions, or continuing tasks that depend on previously stored browser data.</p> <p>The following operations are related to <code>SaveBrowserSessionProfile</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html\">StartBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html\">GetBrowserSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            profile_identifier: <p>The unique identifier for the browser profile. This identifier is used to reference the profile when starting new browser sessions. The identifier must follow the pattern of an alphanumeric name (up to 48 characters) followed by a hyphen and a 10-character alphanumeric suffix.</p>
            browser_identifier: <p>The unique identifier of the browser associated with the session from which to save the profile.</p>
            session_id: <p>The unique identifier of the browser session from which to save the profile. The session must be active when saving the profile.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore.types.save_browser_session_profile_request.SaveBrowserSessionProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore.types.save_browser_session_profile_response.SaveBrowserSessionProfileResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.save_browser_session_profile

            output, http_response = (
                aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.save_browser_session_profile.save_browser_session_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.save_browser_session_profile_request.SaveBrowserSessionProfileRequest = {}  # type: ignore[typeddict-item]
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        input_["profile_identifier"] = profile_identifier
        input_["browser_identifier"] = browser_identifier
        input_["session_id"] = session_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncBrowserProfileResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def save_browser_session_profile(
        self,
        profile_identifier: "aws_sdk_bedrock_agentcore.types.browser_profile_id.BrowserProfileId",
        browser_identifier: str,
        session_id: "aws_sdk_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.save_browser_session_profile_response.SaveBrowserSessionProfileResponse":
        r"""<p>Saves the current state of a browser session as a reusable profile in Amazon Bedrock AgentCore. A browser profile captures persistent browser data such as cookies and local storage from an active session, enabling you to reuse this data in future browser sessions.</p> <p>To save a browser session profile, you must specify the profile identifier, browser identifier, and session ID. The session must be active when saving the profile. Once saved, the profile can be used with the <code>StartBrowserSession</code> operation to initialize new sessions with the stored browser state.</p> <p>Browser profiles are useful for scenarios that require persistent authentication, maintaining user preferences across sessions, or continuing tasks that depend on previously stored browser data.</p> <p>The following operations are related to <code>SaveBrowserSessionProfile</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html\">StartBrowserSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html\">GetBrowserSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            profile_identifier: <p>The unique identifier for the browser profile. This identifier is used to reference the profile when starting new browser sessions. The identifier must follow the pattern of an alphanumeric name (up to 48 characters) followed by a hyphen and a 10-character alphanumeric suffix.</p>
            browser_identifier: <p>The unique identifier of the browser associated with the session from which to save the profile.</p>
            session_id: <p>The unique identifier of the browser session from which to save the profile. The session must be active when saving the profile.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.save_browser_session_profile_request.SaveBrowserSessionProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.save_browser_session_profile_response.SaveBrowserSessionProfileResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.save_browser_session_profile

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.save_browser_session_profile.async_save_browser_session_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.save_browser_session_profile_request.SaveBrowserSessionProfileRequest = {}  # type: ignore[typeddict-item]
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        input_["profile_identifier"] = profile_identifier
        input_["browser_identifier"] = browser_identifier
        input_["session_id"] = session_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
