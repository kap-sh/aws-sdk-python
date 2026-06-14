from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agent_runtime._auth._signers
import aws_sdk_bedrock_agent_runtime._auth._sigv4
from aws_sdk_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_request
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_response
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration
    import aws_sdk_bedrock_agent_runtime.types.session_id
    from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class RetrieveAndGenerateResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def retrieve_and_generate(
        self,
        input: "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input.RetrieveAndGenerateInput",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        session_id: Optional[
            "aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"
        ] = None,
        retrieve_and_generate_configuration: Optional[
            "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"
        ] = None,
        session_configuration: Optional[
            "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.RetrieveAndGenerateSessionConfiguration"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_response.RetrieveAndGenerateResponse":
        """<p>Queries a knowledge base and generates responses based on the retrieved results and using the specified foundation model or <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">inference profile</a>. The response only cites sources that are relevant to the query.</p>

        Args:
            session_id: <p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>
            input: <p>Contains the query to be made to the knowledge base.</p>
            retrieve_and_generate_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>
            session_configuration: <p>Contains details about the session with the knowledge base.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_request.RetrieveAndGenerateRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_response.RetrieveAndGenerateResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate

            output, http_response = (
                aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate.retrieve_and_generate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_request.RetrieveAndGenerateRequest = {}  # type: ignore[typeddict-item]
        if session_id is not None:
            input_["session_id"] = session_id
        input_["input"] = input
        if retrieve_and_generate_configuration is not None:
            input_["retrieve_and_generate_configuration"] = (
                retrieve_and_generate_configuration
            )
        if session_configuration is not None:
            input_["session_configuration"] = session_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRetrieveAndGenerateResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def retrieve_and_generate(
        self,
        input: "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_input.RetrieveAndGenerateInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        session_id: Optional[
            "aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"
        ] = None,
        retrieve_and_generate_configuration: Optional[
            "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"
        ] = None,
        session_configuration: Optional[
            "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.RetrieveAndGenerateSessionConfiguration"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_response.RetrieveAndGenerateResponse":
        """<p>Queries a knowledge base and generates responses based on the retrieved results and using the specified foundation model or <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">inference profile</a>. The response only cites sources that are relevant to the query.</p>

        Args:
            session_id: <p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>
            input: <p>Contains the query to be made to the knowledge base.</p>
            retrieve_and_generate_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>
            session_configuration: <p>Contains details about the session with the knowledge base.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_request.RetrieveAndGenerateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_response.RetrieveAndGenerateResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate.async_retrieve_and_generate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_request.RetrieveAndGenerateRequest = {}  # type: ignore[typeddict-item]
        if session_id is not None:
            input_["session_id"] = session_id
        input_["input"] = input
        if retrieve_and_generate_configuration is not None:
            input_["retrieve_and_generate_configuration"] = (
                retrieve_and_generate_configuration
            )
        if session_configuration is not None:
            input_["session_configuration"] = session_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
