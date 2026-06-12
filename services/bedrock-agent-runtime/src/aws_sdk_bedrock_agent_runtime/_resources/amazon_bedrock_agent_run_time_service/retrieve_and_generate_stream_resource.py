from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import ensure_async_iterator
from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import ensure_sync_iterator
from aws_sdk_bedrock_agent_runtime._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agent_runtime._auth._signers
import aws_sdk_bedrock_agent_runtime._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import BedrockAgentRuntimeClient, BedrockAgentRuntimeClientConfig
    from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import AsyncBedrockAgentRuntimeClient, AsyncBedrockAgentRuntimeClientConfig
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_request
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_response
    import aws_sdk_bedrock_agent_runtime.types.session_id

class RetrieveAndGenerateStreamResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service
    def retrieve_and_generate_stream(self, input: "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input.RetrieveAndGenerateInput", *, config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None, session_id: Optional["aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"] = None, retrieve_and_generate_configuration: Optional["aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"] = None, session_configuration: Optional["aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.RetrieveAndGenerateSessionConfiguration"] = None) -> "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse":
        """<p>Queries a knowledge base and generates responses based on the retrieved results, with output in streaming format.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>InvokeModelWithResponseStream</code>.</p> </note> <p>This operation requires permission for the <code> bedrock:RetrieveAndGenerate</code> action.</p>

        Args:
            session_id: <p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>
            input: <p>Contains the query to be made to the knowledge base.</p>
            retrieve_and_generate_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>
            session_configuration: <p>Contains details about the session with the knowledge base.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest]') -> OperationResponse["aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse"]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate_stream
            output, http_response = aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate_stream.retrieve_and_generate_stream(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest = {}  # type: ignore[typeddict-item]
        if session_id is not None:
            input["session_id"] = session_id
        input["input"] = input
        if retrieve_and_generate_configuration is not None:
            input["retrieve_and_generate_configuration"] = retrieve_and_generate_configuration
        if session_configuration is not None:
            input["session_configuration"] = session_configuration

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncRetrieveAndGenerateStreamResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service
    async def retrieve_and_generate_stream(self, input: "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input.RetrieveAndGenerateInput", *, config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None, session_id: Optional["aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"] = None, retrieve_and_generate_configuration: Optional["aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"] = None, session_configuration: Optional["aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.RetrieveAndGenerateSessionConfiguration"] = None) -> "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse":
        """<p>Queries a knowledge base and generates responses based on the retrieved results, with output in streaming format.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>InvokeModelWithResponseStream</code>.</p> </note> <p>This operation requires permission for the <code> bedrock:RetrieveAndGenerate</code> action.</p>

        Args:
            session_id: <p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>
            input: <p>Contains the query to be made to the knowledge base.</p>
            retrieve_and_generate_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>
            session_configuration: <p>Contains details about the session with the knowledge base.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse"]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate_stream
            output, http_response = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate_stream.async_retrieve_and_generate_stream(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest = {}  # type: ignore[typeddict-item]
        if session_id is not None:
            input["session_id"] = session_id
        input["input"] = input
        if retrieve_and_generate_configuration is not None:
            input["retrieve_and_generate_configuration"] = retrieve_and_generate_configuration
        if session_configuration is not None:
            input["session_configuration"] = session_configuration

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output