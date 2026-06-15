from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
from aws_sdk_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.arn
    import aws_sdk_bedrock_agentcore_control.types.create_memory_input
    import aws_sdk_bedrock_agentcore_control.types.create_memory_output
    import aws_sdk_bedrock_agentcore_control.types.delete_memory_input
    import aws_sdk_bedrock_agentcore_control.types.delete_memory_output
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.get_memory_input
    import aws_sdk_bedrock_agentcore_control.types.get_memory_output
    import aws_sdk_bedrock_agentcore_control.types.indexed_keys_list
    import aws_sdk_bedrock_agentcore_control.types.list_memories_input
    import aws_sdk_bedrock_agentcore_control.types.list_memories_output
    import aws_sdk_bedrock_agentcore_control.types.memory_id
    import aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list
    import aws_sdk_bedrock_agentcore_control.types.memory_summary
    import aws_sdk_bedrock_agentcore_control.types.memory_view
    import aws_sdk_bedrock_agentcore_control.types.modify_memory_strategies
    import aws_sdk_bedrock_agentcore_control.types.name
    import aws_sdk_bedrock_agentcore_control.types.non_empty_string
    import aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.update_memory_input
    import aws_sdk_bedrock_agentcore_control.types.update_memory_output
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class MemoryResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.name.Name",
        event_expiry_duration: int,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.description.Description"
        ] = None,
        encryption_key_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_execution_role_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_strategies: Optional[
            "aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list.MemoryStrategyInputList"
        ] = None,
        indexed_keys: Optional[
            "aws_sdk_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
        ] = None,
        stream_delivery_resources: Optional[
            "aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput":
        """<p>Creates a new Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>
            name: <p>The name of the memory. The name must be unique within your account.</p>
            description: <p>The description of the memory.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the memory data.</p>
            memory_execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the memory to access Amazon Web Services services.</p>
            event_expiry_duration: <p>The duration after which memory events expire. Specified as an ISO 8601 duration.</p>
            memory_strategies: <p>The memory strategies to use for this memory. Strategies define how information is extracted, processed, and consolidated.</p>
            indexed_keys: <p>Metadata keys to index for filtering. Once declared, indexed keys cannot be removed.</p>
            stream_delivery_resources: <p>Configuration for streaming memory record data to external resources.</p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Memory. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_memory

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_memory.create_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if memory_execution_role_arn is not None:
            input_["memory_execution_role_arn"] = memory_execution_role_arn
        input_["event_expiry_duration"] = event_expiry_duration
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if indexed_keys is not None:
            input_["indexed_keys"] = indexed_keys
        if stream_delivery_resources is not None:
            input_["stream_delivery_resources"] = stream_delivery_resources
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        memory_id: "aws_sdk_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        view: Optional[
            "aws_sdk_bedrock_agentcore_control.types.memory_view.MemoryView"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput":
        """<p>Retrieve an existing Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            memory_id: <p>The unique identifier of the memory to retrieve.</p>
            view: <p>The level of detail to return for the memory.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_memory_input.GetMemoryInput]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_memory

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_memory.get_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_memory_input.GetMemoryInput = {}  # type: ignore[typeddict-item]
        input_["memory_id"] = memory_id
        if view is not None:
            input_["view"] = view

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        memory_id: "aws_sdk_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.description.Description"
        ] = None,
        event_expiry_duration: Optional[int] = None,
        memory_execution_role_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_strategies: Optional[
            "aws_sdk_bedrock_agentcore_control.types.modify_memory_strategies.ModifyMemoryStrategies"
        ] = None,
        add_indexed_keys: Optional[
            "aws_sdk_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
        ] = None,
        stream_delivery_resources: Optional[
            "aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput":
        """<p>Update an Amazon Bedrock AgentCore Memory resource memory.</p>

        Args:
            client_token: <p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique AWS identifier.</p>
            memory_id: <p>The unique identifier of the memory to update.</p>
            description: <p>The updated description of the AgentCore Memory resource.</p>
            event_expiry_duration: <p>The number of days after which memory events will expire, between 7 and 365 days.</p>
            memory_execution_role_arn: <p>The ARN of the IAM role that provides permissions for the AgentCore Memory resource.</p>
            memory_strategies: <p>The memory strategies to add, modify, or delete.</p>
            add_indexed_keys: <p>Additional metadata keys to index. Previously indexed keys cannot be removed.</p>
            stream_delivery_resources: <p>Configuration for streaming memory record data to external resources.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_memory

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_memory.update_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["memory_id"] = memory_id
        if description is not None:
            input_["description"] = description
        if event_expiry_duration is not None:
            input_["event_expiry_duration"] = event_expiry_duration
        if memory_execution_role_arn is not None:
            input_["memory_execution_role_arn"] = memory_execution_role_arn
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if add_indexed_keys is not None:
            input_["add_indexed_keys"] = add_indexed_keys
        if stream_delivery_resources is not None:
            input_["stream_delivery_resources"] = stream_delivery_resources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        memory_id: "aws_sdk_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_memory_output.DeleteMemoryOutput":
        """<p>Deletes an Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            client_token: <p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique AWS identifier.</p>
            memory_id: <p>The unique identifier of the memory to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_memory_input.DeleteMemoryInput]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_memory_output.DeleteMemoryOutput"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_memory

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_memory.delete_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_memory_input.DeleteMemoryInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["memory_id"] = memory_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_memories_output.ListMemoriesOutput":
        """<p>Lists the available Amazon Bedrock AgentCore Memory resources in the current Amazon Web Services Region.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_memories_input.ListMemoriesInput]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_memories_output.ListMemoriesOutput"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_memories

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_memories.list_memories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_memories_input.ListMemoriesInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncMemoryResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.name.Name",
        event_expiry_duration: int,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.description.Description"
        ] = None,
        encryption_key_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_execution_role_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_strategies: Optional[
            "aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list.MemoryStrategyInputList"
        ] = None,
        indexed_keys: Optional[
            "aws_sdk_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
        ] = None,
        stream_delivery_resources: Optional[
            "aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput":
        """<p>Creates a new Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>
            name: <p>The name of the memory. The name must be unique within your account.</p>
            description: <p>The description of the memory.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the memory data.</p>
            memory_execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the memory to access Amazon Web Services services.</p>
            event_expiry_duration: <p>The duration after which memory events expire. Specified as an ISO 8601 duration.</p>
            memory_strategies: <p>The memory strategies to use for this memory. Strategies define how information is extracted, processed, and consolidated.</p>
            indexed_keys: <p>Metadata keys to index for filtering. Once declared, indexed keys cannot be removed.</p>
            stream_delivery_resources: <p>Configuration for streaming memory record data to external resources.</p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Memory. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_memory

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_memory.async_create_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if memory_execution_role_arn is not None:
            input_["memory_execution_role_arn"] = memory_execution_role_arn
        input_["event_expiry_duration"] = event_expiry_duration
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if indexed_keys is not None:
            input_["indexed_keys"] = indexed_keys
        if stream_delivery_resources is not None:
            input_["stream_delivery_resources"] = stream_delivery_resources
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        memory_id: "aws_sdk_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        view: Optional[
            "aws_sdk_bedrock_agentcore_control.types.memory_view.MemoryView"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput":
        """<p>Retrieve an existing Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            memory_id: <p>The unique identifier of the memory to retrieve.</p>
            view: <p>The level of detail to return for the memory.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_memory_input.GetMemoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_memory

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_memory.async_get_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_memory_input.GetMemoryInput = {}  # type: ignore[typeddict-item]
        input_["memory_id"] = memory_id
        if view is not None:
            input_["view"] = view

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        memory_id: "aws_sdk_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.description.Description"
        ] = None,
        event_expiry_duration: Optional[int] = None,
        memory_execution_role_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_strategies: Optional[
            "aws_sdk_bedrock_agentcore_control.types.modify_memory_strategies.ModifyMemoryStrategies"
        ] = None,
        add_indexed_keys: Optional[
            "aws_sdk_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
        ] = None,
        stream_delivery_resources: Optional[
            "aws_sdk_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput":
        """<p>Update an Amazon Bedrock AgentCore Memory resource memory.</p>

        Args:
            client_token: <p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique AWS identifier.</p>
            memory_id: <p>The unique identifier of the memory to update.</p>
            description: <p>The updated description of the AgentCore Memory resource.</p>
            event_expiry_duration: <p>The number of days after which memory events will expire, between 7 and 365 days.</p>
            memory_execution_role_arn: <p>The ARN of the IAM role that provides permissions for the AgentCore Memory resource.</p>
            memory_strategies: <p>The memory strategies to add, modify, or delete.</p>
            add_indexed_keys: <p>Additional metadata keys to index. Previously indexed keys cannot be removed.</p>
            stream_delivery_resources: <p>Configuration for streaming memory record data to external resources.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_memory

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_memory.async_update_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["memory_id"] = memory_id
        if description is not None:
            input_["description"] = description
        if event_expiry_duration is not None:
            input_["event_expiry_duration"] = event_expiry_duration
        if memory_execution_role_arn is not None:
            input_["memory_execution_role_arn"] = memory_execution_role_arn
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if add_indexed_keys is not None:
            input_["add_indexed_keys"] = add_indexed_keys
        if stream_delivery_resources is not None:
            input_["stream_delivery_resources"] = stream_delivery_resources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        memory_id: "aws_sdk_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_memory_output.DeleteMemoryOutput":
        """<p>Deletes an Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            client_token: <p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique AWS identifier.</p>
            memory_id: <p>The unique identifier of the memory to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_memory_input.DeleteMemoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_memory_output.DeleteMemoryOutput"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_memory

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_memory.async_delete_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_memory_input.DeleteMemoryInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["memory_id"] = memory_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_memories_output.ListMemoriesOutput":
        """<p>Lists the available Amazon Bedrock AgentCore Memory resources in the current Amazon Web Services Region.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_memories_input.ListMemoriesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_memories_output.ListMemoriesOutput"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_memories

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_memories.async_list_memories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_memories_input.ListMemoriesInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
