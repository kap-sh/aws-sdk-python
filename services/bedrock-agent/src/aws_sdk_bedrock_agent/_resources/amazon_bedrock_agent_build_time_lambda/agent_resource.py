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
    import aws_sdk_bedrock_agent.types.agent_collaboration
    import aws_sdk_bedrock_agent.types.agent_role_arn
    import aws_sdk_bedrock_agent.types.agent_summary
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.create_agent_request
    import aws_sdk_bedrock_agent.types.create_agent_response
    import aws_sdk_bedrock_agent.types.custom_orchestration
    import aws_sdk_bedrock_agent.types.delete_agent_request
    import aws_sdk_bedrock_agent.types.delete_agent_response
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.get_agent_request
    import aws_sdk_bedrock_agent.types.get_agent_response
    import aws_sdk_bedrock_agent.types.guardrail_configuration
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.instruction
    import aws_sdk_bedrock_agent.types.kms_key_arn
    import aws_sdk_bedrock_agent.types.list_agents_request
    import aws_sdk_bedrock_agent.types.list_agents_response
    import aws_sdk_bedrock_agent.types.max_results
    import aws_sdk_bedrock_agent.types.memory_configuration
    import aws_sdk_bedrock_agent.types.model_identifier
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.next_token
    import aws_sdk_bedrock_agent.types.orchestration_type
    import aws_sdk_bedrock_agent.types.prepare_agent_request
    import aws_sdk_bedrock_agent.types.prepare_agent_response
    import aws_sdk_bedrock_agent.types.prompt_override_configuration
    import aws_sdk_bedrock_agent.types.session_ttl
    import aws_sdk_bedrock_agent.types.tags_map
    import aws_sdk_bedrock_agent.types.update_agent_request
    import aws_sdk_bedrock_agent.types.update_agent_response
    from aws_sdk_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from aws_sdk_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class AgentResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def create_agent(
        self,
        agent_name: "aws_sdk_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        instruction: Optional[
            "aws_sdk_bedrock_agent.types.instruction.Instruction"
        ] = None,
        foundation_model: Optional[
            "aws_sdk_bedrock_agent.types.model_identifier.ModelIdentifier"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.description.Description"
        ] = None,
        orchestration_type: Optional[
            "aws_sdk_bedrock_agent.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "aws_sdk_bedrock_agent.types.custom_orchestration.CustomOrchestration"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "aws_sdk_bedrock_agent.types.session_ttl.SessionTTL"
        ] = None,
        agent_resource_role_arn: Optional[
            "aws_sdk_bedrock_agent.types.agent_role_arn.AgentRoleArn"
        ] = None,
        customer_encryption_key_arn: Optional[
            "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_bedrock_agent.types.tags_map.TagsMap"] = None,
        prompt_override_configuration: Optional[
            "aws_sdk_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "aws_sdk_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        memory_configuration: Optional[
            "aws_sdk_bedrock_agent.types.memory_configuration.MemoryConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "aws_sdk_bedrock_agent.types.agent_collaboration.AgentCollaboration"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.create_agent_response.CreateAgentResponse":
        """<p>Creates an agent that orchestrates interactions between foundation models, data sources, software applications, user conversations, and APIs to carry out tasks to help customers.</p> <ul> <li> <p>Specify the following fields for security purposes.</p> <ul> <li> <p> <code>agentResourceRoleArn</code> – The Amazon Resource Name (ARN) of the role with permissions to invoke API operations on an agent.</p> </li> <li> <p>(Optional) <code>customerEncryptionKeyArn</code> – The Amazon Resource Name (ARN) of a KMS key to encrypt the creation of the agent.</p> </li> <li> <p>(Optional) <code>idleSessionTTLinSeconds</code> – Specify the number of seconds for which the agent should maintain session information. After this time expires, the subsequent <code>InvokeAgent</code> request begins a new session.</p> </li> </ul> </li> <li> <p>To enable your agent to retain conversational context across multiple sessions, include a <code>memoryConfiguration</code> object. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-configure-memory.html\">Configure memory</a>.</p> </li> <li> <p>To override the default prompt behavior for agent orchestration and to use advanced prompts, include a <code>promptOverrideConfiguration</code> object. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html\">Advanced prompts</a>.</p> </li> <li> <p>If your agent fails to be created, the response returns a list of <code>failureReasons</code> alongside a list of <code>recommendedActions</code> for you to troubleshoot.</p> </li> <li> <p>The agent instructions will not be honored if your agent has only one knowledge base, uses default prompts, has no action group, and user input is disabled.</p> </li> </ul>

        Args:
            agent_name: <p>A name for the agent that you create.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            instruction: <p>Instructions that tell the agent what it should do and how it should interact with users.</p>
            foundation_model: <p>The identifier for the model that you want to be used for orchestration by the agent you create.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns\">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html\">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html\">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html\">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html\">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html\">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            description: <p>A description of the agent.</p>
            orchestration_type: <p> Specifies the type of orchestration strategy for the agent. This is set to <code>DEFAULT</code> orchestration type, by default. </p>
            custom_orchestration: <p> Contains details of the custom orchestration configured for the agent. </p>
            idle_session_ttl_in_seconds: <p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>
            agent_resource_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key with which to encrypt the agent.</p>
            tags: <p>Any tags that you want to attach to the agent.</p>
            prompt_override_configuration: <p>Contains configurations to override prompts in different parts of an agent sequence. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html\">Advanced prompts</a>.</p>
            guardrail_configuration: <p>The unique Guardrail configuration assigned to the agent when it is created.</p>
            memory_configuration: <p> Contains the details of the memory configured for the agent.</p>
            agent_collaboration: <p>The agent's collaboration role.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.create_agent_request.CreateAgentRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.create_agent_response.CreateAgentResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent.create_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.create_agent_request.CreateAgentRequest = {}  # type: ignore[typeddict-item]
        input_["agent_name"] = agent_name
        if client_token is not None:
            input_["client_token"] = client_token
        if instruction is not None:
            input_["instruction"] = instruction
        if foundation_model is not None:
            input_["foundation_model"] = foundation_model
        if description is not None:
            input_["description"] = description
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if agent_resource_role_arn is not None:
            input_["agent_resource_role_arn"] = agent_resource_role_arn
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if tags is not None:
            input_["tags"] = tags
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_agent(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "aws_sdk_bedrock_agent.types.delete_agent_response.DeleteAgentResponse":
        """<p>Deletes an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.delete_agent_request.DeleteAgentRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.delete_agent_response.DeleteAgentResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent.delete_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.delete_agent_request.DeleteAgentRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_agent(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.get_agent_response.GetAgentResponse":
        """<p>Gets information about an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.get_agent_request.GetAgentRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.get_agent_response.GetAgentResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent.get_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.get_agent_request.GetAgentRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_agents(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_agents_response.ListAgentsResponse":
        """<p>Lists the agents belonging to an account and information about each agent.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.list_agents_request.ListAgentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.list_agents_response.ListAgentsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agents

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agents.list_agents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.list_agents_request.ListAgentsRequest = {}  # type: ignore[typeddict-item]
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

    def prepare_agent(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.prepare_agent_response.PrepareAgentResponse":
        """<p>Creates a <code>DRAFT</code> version of the agent that can be used for internal testing.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to create a <code>DRAFT</code> version.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.prepare_agent_request.PrepareAgentRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.prepare_agent_response.PrepareAgentResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_agent

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_agent.prepare_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.prepare_agent_request.PrepareAgentRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_agent(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_name: "aws_sdk_bedrock_agent.types.name.Name",
        foundation_model: "aws_sdk_bedrock_agent.types.model_identifier.ModelIdentifier",
        agent_resource_role_arn: "aws_sdk_bedrock_agent.types.agent_role_arn.AgentRoleArn",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        instruction: Optional[
            "aws_sdk_bedrock_agent.types.instruction.Instruction"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.description.Description"
        ] = None,
        orchestration_type: Optional[
            "aws_sdk_bedrock_agent.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "aws_sdk_bedrock_agent.types.custom_orchestration.CustomOrchestration"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "aws_sdk_bedrock_agent.types.session_ttl.SessionTTL"
        ] = None,
        customer_encryption_key_arn: Optional[
            "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        prompt_override_configuration: Optional[
            "aws_sdk_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "aws_sdk_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        memory_configuration: Optional[
            "aws_sdk_bedrock_agent.types.memory_configuration.MemoryConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "aws_sdk_bedrock_agent.types.agent_collaboration.AgentCollaboration"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.update_agent_response.UpdateAgentResponse":
        """<p>Updates the configuration of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_name: <p>Specifies a new name for the agent.</p>
            instruction: <p>Specifies new instructions that tell the agent what it should do and how it should interact with users.</p>
            foundation_model: <p>The identifier for the model that you want to be used for orchestration by the agent you create.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns\">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html\">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html\">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html\">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html\">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html\">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            description: <p>Specifies a new description of the agent.</p>
            orchestration_type: <p> Specifies the type of orchestration strategy for the agent. This is set to <code>DEFAULT</code> orchestration type, by default. </p>
            custom_orchestration: <p> Contains details of the custom orchestration configured for the agent. </p>
            idle_session_ttl_in_seconds: <p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>
            agent_resource_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key with which to encrypt the agent.</p>
            prompt_override_configuration: <p>Contains configurations to override prompts in different parts of an agent sequence. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html\">Advanced prompts</a>.</p>
            guardrail_configuration: <p>The unique Guardrail configuration assigned to the agent when it is updated.</p>
            memory_configuration: <p>Specifies the new memory configuration for the agent. </p>
            agent_collaboration: <p>The agent's collaboration role.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.update_agent_request.UpdateAgentRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.update_agent_response.UpdateAgentResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent.update_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.update_agent_request.UpdateAgentRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_name"] = agent_name
        if instruction is not None:
            input_["instruction"] = instruction
        input_["foundation_model"] = foundation_model
        if description is not None:
            input_["description"] = description
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        input_["agent_resource_role_arn"] = agent_resource_role_arn
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAgentResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def create_agent(
        self,
        agent_name: "aws_sdk_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        instruction: Optional[
            "aws_sdk_bedrock_agent.types.instruction.Instruction"
        ] = None,
        foundation_model: Optional[
            "aws_sdk_bedrock_agent.types.model_identifier.ModelIdentifier"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.description.Description"
        ] = None,
        orchestration_type: Optional[
            "aws_sdk_bedrock_agent.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "aws_sdk_bedrock_agent.types.custom_orchestration.CustomOrchestration"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "aws_sdk_bedrock_agent.types.session_ttl.SessionTTL"
        ] = None,
        agent_resource_role_arn: Optional[
            "aws_sdk_bedrock_agent.types.agent_role_arn.AgentRoleArn"
        ] = None,
        customer_encryption_key_arn: Optional[
            "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_bedrock_agent.types.tags_map.TagsMap"] = None,
        prompt_override_configuration: Optional[
            "aws_sdk_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "aws_sdk_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        memory_configuration: Optional[
            "aws_sdk_bedrock_agent.types.memory_configuration.MemoryConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "aws_sdk_bedrock_agent.types.agent_collaboration.AgentCollaboration"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.create_agent_response.CreateAgentResponse":
        """<p>Creates an agent that orchestrates interactions between foundation models, data sources, software applications, user conversations, and APIs to carry out tasks to help customers.</p> <ul> <li> <p>Specify the following fields for security purposes.</p> <ul> <li> <p> <code>agentResourceRoleArn</code> – The Amazon Resource Name (ARN) of the role with permissions to invoke API operations on an agent.</p> </li> <li> <p>(Optional) <code>customerEncryptionKeyArn</code> – The Amazon Resource Name (ARN) of a KMS key to encrypt the creation of the agent.</p> </li> <li> <p>(Optional) <code>idleSessionTTLinSeconds</code> – Specify the number of seconds for which the agent should maintain session information. After this time expires, the subsequent <code>InvokeAgent</code> request begins a new session.</p> </li> </ul> </li> <li> <p>To enable your agent to retain conversational context across multiple sessions, include a <code>memoryConfiguration</code> object. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-configure-memory.html\">Configure memory</a>.</p> </li> <li> <p>To override the default prompt behavior for agent orchestration and to use advanced prompts, include a <code>promptOverrideConfiguration</code> object. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html\">Advanced prompts</a>.</p> </li> <li> <p>If your agent fails to be created, the response returns a list of <code>failureReasons</code> alongside a list of <code>recommendedActions</code> for you to troubleshoot.</p> </li> <li> <p>The agent instructions will not be honored if your agent has only one knowledge base, uses default prompts, has no action group, and user input is disabled.</p> </li> </ul>

        Args:
            agent_name: <p>A name for the agent that you create.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            instruction: <p>Instructions that tell the agent what it should do and how it should interact with users.</p>
            foundation_model: <p>The identifier for the model that you want to be used for orchestration by the agent you create.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns\">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html\">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html\">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html\">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html\">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html\">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            description: <p>A description of the agent.</p>
            orchestration_type: <p> Specifies the type of orchestration strategy for the agent. This is set to <code>DEFAULT</code> orchestration type, by default. </p>
            custom_orchestration: <p> Contains details of the custom orchestration configured for the agent. </p>
            idle_session_ttl_in_seconds: <p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>
            agent_resource_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key with which to encrypt the agent.</p>
            tags: <p>Any tags that you want to attach to the agent.</p>
            prompt_override_configuration: <p>Contains configurations to override prompts in different parts of an agent sequence. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html\">Advanced prompts</a>.</p>
            guardrail_configuration: <p>The unique Guardrail configuration assigned to the agent when it is created.</p>
            memory_configuration: <p> Contains the details of the memory configured for the agent.</p>
            agent_collaboration: <p>The agent's collaboration role.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.create_agent_request.CreateAgentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.create_agent_response.CreateAgentResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent.async_create_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.create_agent_request.CreateAgentRequest = {}  # type: ignore[typeddict-item]
        input_["agent_name"] = agent_name
        if client_token is not None:
            input_["client_token"] = client_token
        if instruction is not None:
            input_["instruction"] = instruction
        if foundation_model is not None:
            input_["foundation_model"] = foundation_model
        if description is not None:
            input_["description"] = description
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if agent_resource_role_arn is not None:
            input_["agent_resource_role_arn"] = agent_resource_role_arn
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if tags is not None:
            input_["tags"] = tags
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_agent(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "aws_sdk_bedrock_agent.types.delete_agent_response.DeleteAgentResponse":
        """<p>Deletes an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.delete_agent_request.DeleteAgentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.delete_agent_response.DeleteAgentResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent.async_delete_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.delete_agent_request.DeleteAgentRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_agent(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.get_agent_response.GetAgentResponse":
        """<p>Gets information about an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.get_agent_request.GetAgentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.get_agent_response.GetAgentResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent.async_get_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.get_agent_request.GetAgentRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_agents(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_agents_response.ListAgentsResponse":
        """<p>Lists the agents belonging to an account and information about each agent.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.list_agents_request.ListAgentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.list_agents_response.ListAgentsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agents

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agents.async_list_agents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.list_agents_request.ListAgentsRequest = {}  # type: ignore[typeddict-item]
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

    async def prepare_agent(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.prepare_agent_response.PrepareAgentResponse":
        """<p>Creates a <code>DRAFT</code> version of the agent that can be used for internal testing.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to create a <code>DRAFT</code> version.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.prepare_agent_request.PrepareAgentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.prepare_agent_response.PrepareAgentResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_agent

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_agent.async_prepare_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.prepare_agent_request.PrepareAgentRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_agent(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_name: "aws_sdk_bedrock_agent.types.name.Name",
        foundation_model: "aws_sdk_bedrock_agent.types.model_identifier.ModelIdentifier",
        agent_resource_role_arn: "aws_sdk_bedrock_agent.types.agent_role_arn.AgentRoleArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        instruction: Optional[
            "aws_sdk_bedrock_agent.types.instruction.Instruction"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.description.Description"
        ] = None,
        orchestration_type: Optional[
            "aws_sdk_bedrock_agent.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "aws_sdk_bedrock_agent.types.custom_orchestration.CustomOrchestration"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "aws_sdk_bedrock_agent.types.session_ttl.SessionTTL"
        ] = None,
        customer_encryption_key_arn: Optional[
            "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        prompt_override_configuration: Optional[
            "aws_sdk_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "aws_sdk_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        memory_configuration: Optional[
            "aws_sdk_bedrock_agent.types.memory_configuration.MemoryConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "aws_sdk_bedrock_agent.types.agent_collaboration.AgentCollaboration"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.update_agent_response.UpdateAgentResponse":
        """<p>Updates the configuration of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_name: <p>Specifies a new name for the agent.</p>
            instruction: <p>Specifies new instructions that tell the agent what it should do and how it should interact with users.</p>
            foundation_model: <p>The identifier for the model that you want to be used for orchestration by the agent you create.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns\">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html\">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html\">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html\">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html\">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html\">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            description: <p>Specifies a new description of the agent.</p>
            orchestration_type: <p> Specifies the type of orchestration strategy for the agent. This is set to <code>DEFAULT</code> orchestration type, by default. </p>
            custom_orchestration: <p> Contains details of the custom orchestration configured for the agent. </p>
            idle_session_ttl_in_seconds: <p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>
            agent_resource_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key with which to encrypt the agent.</p>
            prompt_override_configuration: <p>Contains configurations to override prompts in different parts of an agent sequence. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html\">Advanced prompts</a>.</p>
            guardrail_configuration: <p>The unique Guardrail configuration assigned to the agent when it is updated.</p>
            memory_configuration: <p>Specifies the new memory configuration for the agent. </p>
            agent_collaboration: <p>The agent's collaboration role.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.update_agent_request.UpdateAgentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.update_agent_response.UpdateAgentResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent.async_update_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.update_agent_request.UpdateAgentRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["agent_name"] = agent_name
        if instruction is not None:
            input_["instruction"] = instruction
        input_["foundation_model"] = foundation_model
        if description is not None:
            input_["description"] = description
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        input_["agent_resource_role_arn"] = agent_resource_role_arn
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
