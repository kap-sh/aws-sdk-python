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
    import aws_sdk_bedrock_agent_runtime.types.agent_alias_id
    import aws_sdk_bedrock_agent_runtime.types.agent_id
    import aws_sdk_bedrock_agent_runtime.types.delete_agent_memory_request
    import aws_sdk_bedrock_agent_runtime.types.delete_agent_memory_response
    import aws_sdk_bedrock_agent_runtime.types.get_agent_memory_request
    import aws_sdk_bedrock_agent_runtime.types.get_agent_memory_response
    import aws_sdk_bedrock_agent_runtime.types.max_results
    import aws_sdk_bedrock_agent_runtime.types.memory
    import aws_sdk_bedrock_agent_runtime.types.memory_id
    import aws_sdk_bedrock_agent_runtime.types.memory_type
    import aws_sdk_bedrock_agent_runtime.types.next_token
    import aws_sdk_bedrock_agent_runtime.types.session_id
    from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class MemoryResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def delete_agent_memory(
        self,
        agent_id: "aws_sdk_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "aws_sdk_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        memory_id: Optional[
            "aws_sdk_bedrock_agent_runtime.types.memory_id.MemoryId"
        ] = None,
        session_id: Optional[
            "aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.delete_agent_memory_response.DeleteAgentMemoryResponse":
        """<p>Deletes memory from the specified memory identifier.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to which the alias belongs.</p>
            agent_alias_id: <p>The unique identifier of an alias of an agent.</p>
            memory_id: <p>The unique identifier of the memory.</p>
            session_id: <p>The unique session identifier of the memory.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent_runtime.types.delete_agent_memory_request.DeleteAgentMemoryRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.delete_agent_memory_response.DeleteAgentMemoryResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_agent_memory

            output, http_response = (
                aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_agent_memory.delete_agent_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.delete_agent_memory_request.DeleteAgentMemoryRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_alias_id"] = agent_alias_id
        if memory_id is not None:
            input_["memory_id"] = memory_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_agent_memory(
        self,
        agent_id: "aws_sdk_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "aws_sdk_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        memory_type: "aws_sdk_bedrock_agent_runtime.types.memory_type.MemoryType",
        memory_id: "aws_sdk_bedrock_agent_runtime.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        max_items: Optional[
            "aws_sdk_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.get_agent_memory_response.GetAgentMemoryResponse":
        """<p>Gets the sessions stored in the memory of the agent.</p>

        Args:
            next_token: <p>If the total number of results is greater than the maxItems value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_items: <p>The maximum number of items to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            agent_id: <p>The unique identifier of the agent to which the alias belongs.</p>
            agent_alias_id: <p>The unique identifier of an alias of an agent.</p>
            memory_type: <p>The type of memory.</p>
            memory_id: <p>The unique identifier of the memory. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent_runtime.types.get_agent_memory_request.GetAgentMemoryRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.get_agent_memory_response.GetAgentMemoryResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_agent_memory

            output, http_response = (
                aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_agent_memory.get_agent_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.get_agent_memory_request.GetAgentMemoryRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items
        input_["agent_id"] = agent_id
        input_["agent_alias_id"] = agent_alias_id
        input_["memory_type"] = memory_type
        input_["memory_id"] = memory_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncMemoryResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def delete_agent_memory(
        self,
        agent_id: "aws_sdk_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "aws_sdk_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        memory_id: Optional[
            "aws_sdk_bedrock_agent_runtime.types.memory_id.MemoryId"
        ] = None,
        session_id: Optional[
            "aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.delete_agent_memory_response.DeleteAgentMemoryResponse":
        """<p>Deletes memory from the specified memory identifier.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to which the alias belongs.</p>
            agent_alias_id: <p>The unique identifier of an alias of an agent.</p>
            memory_id: <p>The unique identifier of the memory.</p>
            session_id: <p>The unique session identifier of the memory.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.delete_agent_memory_request.DeleteAgentMemoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.delete_agent_memory_response.DeleteAgentMemoryResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_agent_memory

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_agent_memory.async_delete_agent_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.delete_agent_memory_request.DeleteAgentMemoryRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_alias_id"] = agent_alias_id
        if memory_id is not None:
            input_["memory_id"] = memory_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_agent_memory(
        self,
        agent_id: "aws_sdk_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "aws_sdk_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        memory_type: "aws_sdk_bedrock_agent_runtime.types.memory_type.MemoryType",
        memory_id: "aws_sdk_bedrock_agent_runtime.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        max_items: Optional[
            "aws_sdk_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.get_agent_memory_response.GetAgentMemoryResponse":
        """<p>Gets the sessions stored in the memory of the agent.</p>

        Args:
            next_token: <p>If the total number of results is greater than the maxItems value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_items: <p>The maximum number of items to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            agent_id: <p>The unique identifier of the agent to which the alias belongs.</p>
            agent_alias_id: <p>The unique identifier of an alias of an agent.</p>
            memory_type: <p>The type of memory.</p>
            memory_id: <p>The unique identifier of the memory. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.get_agent_memory_request.GetAgentMemoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.get_agent_memory_response.GetAgentMemoryResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_agent_memory

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_agent_memory.async_get_agent_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.get_agent_memory_request.GetAgentMemoryRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items
        input_["agent_id"] = agent_id
        input_["agent_alias_id"] = agent_alias_id
        input_["memory_type"] = memory_type
        input_["memory_id"] = memory_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
