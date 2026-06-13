from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import ensure_async_iterator
from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import ensure_sync_iterator
from aws_sdk_bedrock_agentcore_control._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import BedrockAgentCoreControlClient, BedrockAgentCoreControlClientConfig
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import AsyncBedrockAgentCoreControlClient, AsyncBedrockAgentCoreControlClientConfig
    import aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.create_policy_request
    import aws_sdk_bedrock_agentcore_control.types.create_policy_response
    import aws_sdk_bedrock_agentcore_control.types.delete_policy_request
    import aws_sdk_bedrock_agentcore_control.types.delete_policy_response
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.get_policy_request
    import aws_sdk_bedrock_agentcore_control.types.get_policy_response
    import aws_sdk_bedrock_agentcore_control.types.get_policy_summary_request
    import aws_sdk_bedrock_agentcore_control.types.get_policy_summary_response
    import aws_sdk_bedrock_agentcore_control.types.list_policies_request
    import aws_sdk_bedrock_agentcore_control.types.list_policies_response
    import aws_sdk_bedrock_agentcore_control.types.list_policy_summaries_request
    import aws_sdk_bedrock_agentcore_control.types.list_policy_summaries_response
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.policy
    import aws_sdk_bedrock_agentcore_control.types.policy_definition
    import aws_sdk_bedrock_agentcore_control.types.policy_name
    import aws_sdk_bedrock_agentcore_control.types.policy_summary
    import aws_sdk_bedrock_agentcore_control.types.policy_validation_mode
    import aws_sdk_bedrock_agentcore_control.types.resource_id
    import aws_sdk_bedrock_agentcore_control.types.update_policy_request
    import aws_sdk_bedrock_agentcore_control.types.update_policy_response
    import aws_sdk_bedrock_agentcore_control.types.updated_description

class PolicyResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service
    def create(self, name: "aws_sdk_bedrock_agentcore_control.types.policy_name.PolicyName", definition: "aws_sdk_bedrock_agentcore_control.types.policy_definition.PolicyDefinition", policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.description.Description"] = None, validation_mode: Optional["aws_sdk_bedrock_agentcore_control.types.policy_validation_mode.PolicyValidationMode"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_policy_response.CreatePolicyResponse":
        """<p>Creates a policy within the AgentCore Policy system. Policies provide real-time, deterministic control over agentic interactions with AgentCore Gateway. Using the Cedar policy language, you can define fine-grained policies that specify which interactions with Gateway tools are permitted based on input parameters and OAuth claims, ensuring agents operate within defined boundaries and business rules. The policy is validated during creation against the Cedar schema generated from the Gateway's tools' input schemas, which defines the available tools, their parameters, and expected data types. This is an asynchronous operation. Use the <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicy.html\">GetPolicy</a> operation to poll the <code>status</code> field to track completion.</p>

        Args:
            name: <p>The customer-assigned immutable name for the policy. Must be unique within the account. This name is used for policy identification and cannot be changed after creation.</p>
            definition: <p>The Cedar policy statement that defines the access control rules. This contains the actual policy logic written in Cedar policy language, specifying effect (permit or forbid), principals, actions, resources, and conditions for agent behavior control.</p>
            description: <p>A human-readable description of the policy's purpose and functionality (1-4,096 characters). This helps policy administrators understand the policy's intent, business rules, and operational scope. Use this field to document why the policy exists, what business requirement it addresses, and any special considerations for maintenance. Clear descriptions are essential for policy governance, auditing, and troubleshooting.</p>
            validation_mode: <p>The validation mode for the policy creation. Determines how Cedar analyzer validation results are handled during policy creation. FAIL_ON_ANY_FINDINGS (default) runs the Cedar analyzer to validate the policy against the Cedar schema and tool context, failing creation if the analyzer detects any validation issues to ensure strict conformance. IGNORE_ALL_FINDINGS runs the Cedar analyzer but allows policy creation even if validation issues are detected, useful for testing or when the policy schema is evolving. Use FAIL_ON_ANY_FINDINGS for production policies to ensure correctness, and IGNORE_ALL_FINDINGS only when you understand and accept the analyzer findings.</p>
            policy_engine_id: <p>The identifier of the policy engine which contains this policy. Policy engines group related policies and provide the execution context for policy evaluation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don't need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without creating a duplicate policy.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_policy_request.CreatePolicyRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.create_policy_response.CreatePolicyResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_policy
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_policy.create_policy(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_policy_request.CreatePolicyRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["definition"] = definition
        if description is not None:
            input["description"] = description
        if validation_mode is not None:
            input["validation_mode"] = validation_mode
        input["policy_engine_id"] = policy_engine_id
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_policy_response.GetPolicyResponse":
        """<p>Retrieves detailed information about a specific policy within the AgentCore Policy system. This operation returns the complete policy definition, metadata, and current status, allowing administrators to review and manage policy configurations.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to be retrieved.</p>
            policy_id: <p>The unique identifier of the policy to be retrieved. This must be a valid policy ID that exists within the specified policy engine.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_policy_request.GetPolicyRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.get_policy_response.GetPolicyResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy.get_policy(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_policy_request.GetPolicyRequest = {}  # type: ignore[typeddict-item]
        input["policy_engine_id"] = policy_engine_id
        input["policy_id"] = policy_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.updated_description.UpdatedDescription"] = None, definition: Optional["aws_sdk_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"] = None, validation_mode: Optional["aws_sdk_bedrock_agentcore_control.types.policy_validation_mode.PolicyValidationMode"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_policy_response.UpdatePolicyResponse":
        """<p>Updates an existing policy within the AgentCore Policy system. This operation allows modification of the policy description and definition while maintaining the policy's identity. The updated policy is validated against the Cedar schema before being applied. This is an asynchronous operation. Use the <code>GetPolicy</code> operation to poll the <code>status</code> field to track completion.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to be updated. This ensures the policy is updated within the correct policy engine context.</p>
            policy_id: <p>The unique identifier of the policy to be updated. This must be a valid policy ID that exists within the specified policy engine.</p>
            description: <p>The new human-readable description for the policy. This optional field allows updating the policy's documentation while keeping the same policy logic.</p>
            definition: <p>The new Cedar policy statement that defines the access control rules. This replaces the existing policy definition with new logic while maintaining the policy's identity.</p>
            validation_mode: <p>The validation mode for the policy update. Determines how Cedar analyzer validation results are handled during policy updates. FAIL_ON_ANY_FINDINGS runs the Cedar analyzer and fails the update if validation issues are detected, ensuring the policy conforms to the Cedar schema and tool context. IGNORE_ALL_FINDINGS runs the Cedar analyzer but allows updates despite validation warnings. Use FAIL_ON_ANY_FINDINGS to ensure policy correctness during updates, especially when modifying policy logic or conditions.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_policy_request.UpdatePolicyRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.update_policy_response.UpdatePolicyResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_policy
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_policy.update_policy(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_policy_request.UpdatePolicyRequest = {}  # type: ignore[typeddict-item]
        input["policy_engine_id"] = policy_engine_id
        input["policy_id"] = policy_id
        if description is not None:
            input["description"] = description
        if definition is not None:
            input["definition"] = definition
        if validation_mode is not None:
            input["validation_mode"] = validation_mode

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_policy_response.DeletePolicyResponse":
        """<p>Deletes an existing policy from the AgentCore Policy system. Once deleted, the policy can no longer be used for agent behavior control and all references to it become invalid. This is an asynchronous operation. Use the <code>GetPolicy</code> operation to poll the <code>status</code> field to track completion.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to be deleted. This ensures the policy is deleted from the correct policy engine context.</p>
            policy_id: <p>The unique identifier of the policy to be deleted. This must be a valid policy ID that exists within the specified policy engine.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_policy_request.DeletePolicyRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_policy_response.DeletePolicyResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_policy
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_policy.delete_policy(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_policy_request.DeletePolicyRequest = {}  # type: ignore[typeddict-item]
        input["policy_engine_id"] = policy_engine_id
        input["policy_id"] = policy_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, target_resource_scope: Optional["aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_policies_response.ListPoliciesResponse":
        """<p>Retrieves a list of policies within the AgentCore Policy engine. This operation supports pagination and filtering to help administrators manage and discover policies across policy engines. Results can be filtered by policy engine or resource associations.</p>

        Args:
            next_token: <p>A pagination token returned from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicies.html\">ListPolicies</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>
            max_results: <p>The maximum number of policies to return in a single response. If not specified, the default is 10 policies per page, with a maximum of 100 per page.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policies to retrieve.</p>
            target_resource_scope: <p>Optional filter to list policies that apply to a specific resource scope or resource type. This helps narrow down policy results to those relevant for particular Amazon Web Services resources, agent tools, or operational contexts within the policy engine ecosystem.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_policies_request.ListPoliciesRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_policies_response.ListPoliciesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policies
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policies.list_policies(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_policies_request.ListPoliciesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["policy_engine_id"] = policy_engine_id
        if target_resource_scope is not None:
            input["target_resource_scope"] = target_resource_scope

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_policy_summary(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_policy_summary_response.GetPolicySummaryResponse":
        """<p>Retrieves a metadata-only summary of a specific policy without decrypting customer content. This lightweight read operation returns resource identifiers, status, and timestamps, but does not include the policy definition, description, or status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to retrieve the summary for.</p>
            policy_id: <p>The unique identifier of the policy to retrieve the summary for. This must be a valid policy ID that exists within the specified policy engine.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_policy_summary_request.GetPolicySummaryRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.get_policy_summary_response.GetPolicySummaryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_summary
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_summary.get_policy_summary(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_policy_summary_request.GetPolicySummaryRequest = {}  # type: ignore[typeddict-item]
        input["policy_engine_id"] = policy_engine_id
        input["policy_id"] = policy_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_policy_summaries(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, target_resource_scope: Optional["aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_policy_summaries_response.ListPolicySummariesResponse":
        """<p>Retrieves a paginated list of metadata-only policy summaries within a policy engine without decrypting customer content. This lightweight read operation returns resource identifiers, status, and timestamps for each policy, but does not include policy definitions, descriptions, or status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            next_token: <p>A pagination token returned from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicySummaries.html\">ListPolicySummaries</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>
            max_results: <p>The maximum number of policy summaries to return in a single response.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policy summaries to retrieve.</p>
            target_resource_scope: <p>Optional filter to list policy summaries that apply to a specific resource scope or resource type. This helps narrow down results to those relevant for particular Amazon Web Services resources, agent tools, or operational contexts within the policy engine ecosystem.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_policy_summaries_request.ListPolicySummariesRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_policy_summaries_response.ListPolicySummariesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_summaries
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_summaries.list_policy_summaries(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_policy_summaries_request.ListPolicySummariesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["policy_engine_id"] = policy_engine_id
        if target_resource_scope is not None:
            input["target_resource_scope"] = target_resource_scope

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncPolicyResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service
    async def create(self, name: "aws_sdk_bedrock_agentcore_control.types.policy_name.PolicyName", definition: "aws_sdk_bedrock_agentcore_control.types.policy_definition.PolicyDefinition", policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.description.Description"] = None, validation_mode: Optional["aws_sdk_bedrock_agentcore_control.types.policy_validation_mode.PolicyValidationMode"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_policy_response.CreatePolicyResponse":
        """<p>Creates a policy within the AgentCore Policy system. Policies provide real-time, deterministic control over agentic interactions with AgentCore Gateway. Using the Cedar policy language, you can define fine-grained policies that specify which interactions with Gateway tools are permitted based on input parameters and OAuth claims, ensuring agents operate within defined boundaries and business rules. The policy is validated during creation against the Cedar schema generated from the Gateway's tools' input schemas, which defines the available tools, their parameters, and expected data types. This is an asynchronous operation. Use the <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicy.html\">GetPolicy</a> operation to poll the <code>status</code> field to track completion.</p>

        Args:
            name: <p>The customer-assigned immutable name for the policy. Must be unique within the account. This name is used for policy identification and cannot be changed after creation.</p>
            definition: <p>The Cedar policy statement that defines the access control rules. This contains the actual policy logic written in Cedar policy language, specifying effect (permit or forbid), principals, actions, resources, and conditions for agent behavior control.</p>
            description: <p>A human-readable description of the policy's purpose and functionality (1-4,096 characters). This helps policy administrators understand the policy's intent, business rules, and operational scope. Use this field to document why the policy exists, what business requirement it addresses, and any special considerations for maintenance. Clear descriptions are essential for policy governance, auditing, and troubleshooting.</p>
            validation_mode: <p>The validation mode for the policy creation. Determines how Cedar analyzer validation results are handled during policy creation. FAIL_ON_ANY_FINDINGS (default) runs the Cedar analyzer to validate the policy against the Cedar schema and tool context, failing creation if the analyzer detects any validation issues to ensure strict conformance. IGNORE_ALL_FINDINGS runs the Cedar analyzer but allows policy creation even if validation issues are detected, useful for testing or when the policy schema is evolving. Use FAIL_ON_ANY_FINDINGS for production policies to ensure correctness, and IGNORE_ALL_FINDINGS only when you understand and accept the analyzer findings.</p>
            policy_engine_id: <p>The identifier of the policy engine which contains this policy. Policy engines group related policies and provide the execution context for policy evaluation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don't need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without creating a duplicate policy.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_policy_request.CreatePolicyRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.create_policy_response.CreatePolicyResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_policy
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_policy.async_create_policy(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_policy_request.CreatePolicyRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["definition"] = definition
        if description is not None:
            input["description"] = description
        if validation_mode is not None:
            input["validation_mode"] = validation_mode
        input["policy_engine_id"] = policy_engine_id
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_policy_response.GetPolicyResponse":
        """<p>Retrieves detailed information about a specific policy within the AgentCore Policy system. This operation returns the complete policy definition, metadata, and current status, allowing administrators to review and manage policy configurations.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to be retrieved.</p>
            policy_id: <p>The unique identifier of the policy to be retrieved. This must be a valid policy ID that exists within the specified policy engine.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_policy_request.GetPolicyRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.get_policy_response.GetPolicyResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy.async_get_policy(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_policy_request.GetPolicyRequest = {}  # type: ignore[typeddict-item]
        input["policy_engine_id"] = policy_engine_id
        input["policy_id"] = policy_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.updated_description.UpdatedDescription"] = None, definition: Optional["aws_sdk_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"] = None, validation_mode: Optional["aws_sdk_bedrock_agentcore_control.types.policy_validation_mode.PolicyValidationMode"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_policy_response.UpdatePolicyResponse":
        """<p>Updates an existing policy within the AgentCore Policy system. This operation allows modification of the policy description and definition while maintaining the policy's identity. The updated policy is validated against the Cedar schema before being applied. This is an asynchronous operation. Use the <code>GetPolicy</code> operation to poll the <code>status</code> field to track completion.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to be updated. This ensures the policy is updated within the correct policy engine context.</p>
            policy_id: <p>The unique identifier of the policy to be updated. This must be a valid policy ID that exists within the specified policy engine.</p>
            description: <p>The new human-readable description for the policy. This optional field allows updating the policy's documentation while keeping the same policy logic.</p>
            definition: <p>The new Cedar policy statement that defines the access control rules. This replaces the existing policy definition with new logic while maintaining the policy's identity.</p>
            validation_mode: <p>The validation mode for the policy update. Determines how Cedar analyzer validation results are handled during policy updates. FAIL_ON_ANY_FINDINGS runs the Cedar analyzer and fails the update if validation issues are detected, ensuring the policy conforms to the Cedar schema and tool context. IGNORE_ALL_FINDINGS runs the Cedar analyzer but allows updates despite validation warnings. Use FAIL_ON_ANY_FINDINGS to ensure policy correctness during updates, especially when modifying policy logic or conditions.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_policy_request.UpdatePolicyRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.update_policy_response.UpdatePolicyResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_policy
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_policy.async_update_policy(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_policy_request.UpdatePolicyRequest = {}  # type: ignore[typeddict-item]
        input["policy_engine_id"] = policy_engine_id
        input["policy_id"] = policy_id
        if description is not None:
            input["description"] = description
        if definition is not None:
            input["definition"] = definition
        if validation_mode is not None:
            input["validation_mode"] = validation_mode

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_policy_response.DeletePolicyResponse":
        """<p>Deletes an existing policy from the AgentCore Policy system. Once deleted, the policy can no longer be used for agent behavior control and all references to it become invalid. This is an asynchronous operation. Use the <code>GetPolicy</code> operation to poll the <code>status</code> field to track completion.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to be deleted. This ensures the policy is deleted from the correct policy engine context.</p>
            policy_id: <p>The unique identifier of the policy to be deleted. This must be a valid policy ID that exists within the specified policy engine.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_policy_request.DeletePolicyRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_policy_response.DeletePolicyResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_policy
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_policy.async_delete_policy(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_policy_request.DeletePolicyRequest = {}  # type: ignore[typeddict-item]
        input["policy_engine_id"] = policy_engine_id
        input["policy_id"] = policy_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, target_resource_scope: Optional["aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_policies_response.ListPoliciesResponse":
        """<p>Retrieves a list of policies within the AgentCore Policy engine. This operation supports pagination and filtering to help administrators manage and discover policies across policy engines. Results can be filtered by policy engine or resource associations.</p>

        Args:
            next_token: <p>A pagination token returned from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicies.html\">ListPolicies</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>
            max_results: <p>The maximum number of policies to return in a single response. If not specified, the default is 10 policies per page, with a maximum of 100 per page.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policies to retrieve.</p>
            target_resource_scope: <p>Optional filter to list policies that apply to a specific resource scope or resource type. This helps narrow down policy results to those relevant for particular Amazon Web Services resources, agent tools, or operational contexts within the policy engine ecosystem.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_policies_request.ListPoliciesRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_policies_response.ListPoliciesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policies
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policies.async_list_policies(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_policies_request.ListPoliciesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["policy_engine_id"] = policy_engine_id
        if target_resource_scope is not None:
            input["target_resource_scope"] = target_resource_scope

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_policy_summary(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_policy_summary_response.GetPolicySummaryResponse":
        """<p>Retrieves a metadata-only summary of a specific policy without decrypting customer content. This lightweight read operation returns resource identifiers, status, and timestamps, but does not include the policy definition, description, or status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to retrieve the summary for.</p>
            policy_id: <p>The unique identifier of the policy to retrieve the summary for. This must be a valid policy ID that exists within the specified policy engine.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_policy_summary_request.GetPolicySummaryRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.get_policy_summary_response.GetPolicySummaryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_summary
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_summary.async_get_policy_summary(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_policy_summary_request.GetPolicySummaryRequest = {}  # type: ignore[typeddict-item]
        input["policy_engine_id"] = policy_engine_id
        input["policy_id"] = policy_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_policy_summaries(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, target_resource_scope: Optional["aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_policy_summaries_response.ListPolicySummariesResponse":
        """<p>Retrieves a paginated list of metadata-only policy summaries within a policy engine without decrypting customer content. This lightweight read operation returns resource identifiers, status, and timestamps for each policy, but does not include policy definitions, descriptions, or status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            next_token: <p>A pagination token returned from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicySummaries.html\">ListPolicySummaries</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>
            max_results: <p>The maximum number of policy summaries to return in a single response.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policy summaries to retrieve.</p>
            target_resource_scope: <p>Optional filter to list policy summaries that apply to a specific resource scope or resource type. This helps narrow down results to those relevant for particular Amazon Web Services resources, agent tools, or operational contexts within the policy engine ecosystem.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_policy_summaries_request.ListPolicySummariesRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_policy_summaries_response.ListPolicySummariesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_summaries
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_summaries.async_list_policy_summaries(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_policy_summaries_request.ListPolicySummariesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["policy_engine_id"] = policy_engine_id
        if target_resource_scope is not None:
            input["target_resource_scope"] = target_resource_scope

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output