from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agent._auth._signers
import aws_sdk_bedrock_agent._auth._sigv4
from aws_sdk_bedrock_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_collaborator_summary
    import aws_sdk_bedrock_agent.types.agent_descriptor
    import aws_sdk_bedrock_agent.types.associate_agent_collaborator_request
    import aws_sdk_bedrock_agent.types.associate_agent_collaborator_response
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.collaboration_instruction
    import aws_sdk_bedrock_agent.types.disassociate_agent_collaborator_request
    import aws_sdk_bedrock_agent.types.disassociate_agent_collaborator_response
    import aws_sdk_bedrock_agent.types.draft_version
    import aws_sdk_bedrock_agent.types.get_agent_collaborator_request
    import aws_sdk_bedrock_agent.types.get_agent_collaborator_response
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.list_agent_collaborators_request
    import aws_sdk_bedrock_agent.types.list_agent_collaborators_response
    import aws_sdk_bedrock_agent.types.max_results
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.next_token
    import aws_sdk_bedrock_agent.types.relay_conversation_history
    import aws_sdk_bedrock_agent.types.update_agent_collaborator_request
    import aws_sdk_bedrock_agent.types.update_agent_collaborator_response
    import aws_sdk_bedrock_agent.types.version
    from aws_sdk_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from aws_sdk_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class AgentCollaboratorResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def associate_agent_collaborator(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion",
        agent_descriptor: "aws_sdk_bedrock_agent.types.agent_descriptor.AgentDescriptor",
        collaborator_name: "aws_sdk_bedrock_agent.types.name.Name",
        collaboration_instruction: "aws_sdk_bedrock_agent.types.collaboration_instruction.CollaborationInstruction",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        relay_conversation_history: Optional[
            "aws_sdk_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse":
        """<p>Makes an agent a collaborator for another agent.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>An agent version.</p>
            agent_descriptor: <p>The alias of the collaborator agent.</p>
            collaborator_name: <p>A name for the collaborator.</p>
            collaboration_instruction: <p>Instruction for the collaborator.</p>
            relay_conversation_history: <p>A relay conversation history for the collaborator.</p>
            client_token: <p>A client token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_collaborator

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_collaborator.associate_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_version"] = agent_version
        input_["agent_descriptor"] = agent_descriptor
        input_["collaborator_name"] = collaborator_name
        input_["collaboration_instruction"] = collaboration_instruction
        if relay_conversation_history is not None:
            input_["relay_conversation_history"] = relay_conversation_history
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_agent_collaborator(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion",
        collaborator_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.disassociate_agent_collaborator_response.DisassociateAgentCollaboratorResponse":
        """<p>Disassociates an agent collaborator.</p>

        Args:
            agent_id: <p>An agent ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.disassociate_agent_collaborator_request.DisassociateAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.disassociate_agent_collaborator_response.DisassociateAgentCollaboratorResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_collaborator

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_collaborator.disassociate_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.disassociate_agent_collaborator_request.DisassociateAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_version"] = agent_version
        input_["collaborator_id"] = collaborator_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_agent_collaborator(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.version.Version",
        collaborator_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse":
        """<p>Retrieves information about an agent's collaborator.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.get_agent_collaborator_request.GetAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_collaborator

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_collaborator.get_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.get_agent_collaborator_request.GetAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_version"] = agent_version
        input_["collaborator_id"] = collaborator_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_agent_collaborators(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse":
        """<p>Retrieve a list of an agent's collaborators.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            max_results: <p>The maximum number of agent collaborators to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.list_agent_collaborators_request.ListAgentCollaboratorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_collaborators

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_collaborators.list_agent_collaborators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.list_agent_collaborators_request.ListAgentCollaboratorsRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_version"] = agent_version
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

    def update_agent_collaborator(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion",
        collaborator_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_descriptor: "aws_sdk_bedrock_agent.types.agent_descriptor.AgentDescriptor",
        collaborator_name: "aws_sdk_bedrock_agent.types.name.Name",
        collaboration_instruction: "aws_sdk_bedrock_agent.types.collaboration_instruction.CollaborationInstruction",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        relay_conversation_history: Optional[
            "aws_sdk_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse":
        """<p>Updates an agent's collaborator.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>
            agent_descriptor: <p>An agent descriptor for the agent collaborator.</p>
            collaborator_name: <p>The collaborator's name.</p>
            collaboration_instruction: <p>Instruction for the collaborator.</p>
            relay_conversation_history: <p>A relay conversation history for the collaborator.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_collaborator

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_collaborator.update_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_version"] = agent_version
        input_["collaborator_id"] = collaborator_id
        input_["agent_descriptor"] = agent_descriptor
        input_["collaborator_name"] = collaborator_name
        input_["collaboration_instruction"] = collaboration_instruction
        if relay_conversation_history is not None:
            input_["relay_conversation_history"] = relay_conversation_history

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAgentCollaboratorResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def associate_agent_collaborator(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion",
        agent_descriptor: "aws_sdk_bedrock_agent.types.agent_descriptor.AgentDescriptor",
        collaborator_name: "aws_sdk_bedrock_agent.types.name.Name",
        collaboration_instruction: "aws_sdk_bedrock_agent.types.collaboration_instruction.CollaborationInstruction",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        relay_conversation_history: Optional[
            "aws_sdk_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse":
        """<p>Makes an agent a collaborator for another agent.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>An agent version.</p>
            agent_descriptor: <p>The alias of the collaborator agent.</p>
            collaborator_name: <p>A name for the collaborator.</p>
            collaboration_instruction: <p>Instruction for the collaborator.</p>
            relay_conversation_history: <p>A relay conversation history for the collaborator.</p>
            client_token: <p>A client token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_collaborator

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_collaborator.async_associate_agent_collaborator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_version"] = agent_version
        input_["agent_descriptor"] = agent_descriptor
        input_["collaborator_name"] = collaborator_name
        input_["collaboration_instruction"] = collaboration_instruction
        if relay_conversation_history is not None:
            input_["relay_conversation_history"] = relay_conversation_history
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_agent_collaborator(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion",
        collaborator_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.disassociate_agent_collaborator_response.DisassociateAgentCollaboratorResponse":
        """<p>Disassociates an agent collaborator.</p>

        Args:
            agent_id: <p>An agent ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.disassociate_agent_collaborator_request.DisassociateAgentCollaboratorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.disassociate_agent_collaborator_response.DisassociateAgentCollaboratorResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_collaborator

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_collaborator.async_disassociate_agent_collaborator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.disassociate_agent_collaborator_request.DisassociateAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_version"] = agent_version
        input_["collaborator_id"] = collaborator_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_agent_collaborator(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.version.Version",
        collaborator_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse":
        """<p>Retrieves information about an agent's collaborator.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.get_agent_collaborator_request.GetAgentCollaboratorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_collaborator

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_collaborator.async_get_agent_collaborator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.get_agent_collaborator_request.GetAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_version"] = agent_version
        input_["collaborator_id"] = collaborator_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_agent_collaborators(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse":
        """<p>Retrieve a list of an agent's collaborators.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            max_results: <p>The maximum number of agent collaborators to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.list_agent_collaborators_request.ListAgentCollaboratorsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_collaborators

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_collaborators.async_list_agent_collaborators(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.list_agent_collaborators_request.ListAgentCollaboratorsRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_version"] = agent_version
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

    async def update_agent_collaborator(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion",
        collaborator_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_descriptor: "aws_sdk_bedrock_agent.types.agent_descriptor.AgentDescriptor",
        collaborator_name: "aws_sdk_bedrock_agent.types.name.Name",
        collaboration_instruction: "aws_sdk_bedrock_agent.types.collaboration_instruction.CollaborationInstruction",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        relay_conversation_history: Optional[
            "aws_sdk_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse":
        """<p>Updates an agent's collaborator.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>
            agent_descriptor: <p>An agent descriptor for the agent collaborator.</p>
            collaborator_name: <p>The collaborator's name.</p>
            collaboration_instruction: <p>Instruction for the collaborator.</p>
            relay_conversation_history: <p>A relay conversation history for the collaborator.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_collaborator

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_collaborator.async_update_agent_collaborator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_version"] = agent_version
        input_["collaborator_id"] = collaborator_id
        input_["agent_descriptor"] = agent_descriptor
        input_["collaborator_name"] = collaborator_name
        input_["collaboration_instruction"] = collaboration_instruction
        if relay_conversation_history is not None:
            input_["relay_conversation_history"] = relay_conversation_history

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
