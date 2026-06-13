from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import ensure_async_iterator
from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import ensure_sync_iterator
from aws_sdk_bedrock_agentcore_control._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import BedrockAgentCoreControlClient, BedrockAgentCoreControlClientConfig
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import AsyncBedrockAgentCoreControlClient, AsyncBedrockAgentCoreControlClientConfig
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.content
    import aws_sdk_bedrock_agentcore_control.types.get_policy_generation_request
    import aws_sdk_bedrock_agentcore_control.types.get_policy_generation_response
    import aws_sdk_bedrock_agentcore_control.types.get_policy_generation_summary_request
    import aws_sdk_bedrock_agentcore_control.types.get_policy_generation_summary_response
    import aws_sdk_bedrock_agentcore_control.types.list_policy_generation_assets_request
    import aws_sdk_bedrock_agentcore_control.types.list_policy_generation_assets_response
    import aws_sdk_bedrock_agentcore_control.types.list_policy_generation_summaries_request
    import aws_sdk_bedrock_agentcore_control.types.list_policy_generation_summaries_response
    import aws_sdk_bedrock_agentcore_control.types.list_policy_generations_request
    import aws_sdk_bedrock_agentcore_control.types.list_policy_generations_response
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.policy_generation
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_asset
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_name
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_summary
    import aws_sdk_bedrock_agentcore_control.types.resource
    import aws_sdk_bedrock_agentcore_control.types.resource_id
    import aws_sdk_bedrock_agentcore_control.types.start_policy_generation_request
    import aws_sdk_bedrock_agentcore_control.types.start_policy_generation_response

class PolicyGenerationResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service
    def create(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", resource: "aws_sdk_bedrock_agentcore_control.types.resource.Resource", content: "aws_sdk_bedrock_agentcore_control.types.content.Content", name: "aws_sdk_bedrock_agentcore_control.types.policy_generation_name.PolicyGenerationName", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.start_policy_generation_response.StartPolicyGenerationResponse":
        """<p>Initiates the AI-powered generation of Cedar policies from natural language descriptions within the AgentCore Policy system. This feature enables both technical and non-technical users to create policies by describing their authorization requirements in plain English, which is then automatically translated into formal Cedar policy statements. The generation process analyzes the natural language input along with the Gateway's tool context to produce validated policy options. Generated policy assets are automatically deleted after 7 days, so you should review and create policies from the generated assets within this timeframe. Once created, policies are permanent and not subject to this expiration. Generated policies should be reviewed and tested in log-only mode before deploying to production. Use this when you want to describe policy intent naturally rather than learning Cedar syntax, though generated policies may require refinement for complex scenarios.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that provides the context for policy generation. This engine's schema and tool context are used to ensure generated policies are valid and applicable.</p>
            resource: <p>The resource information that provides context for policy generation. This helps the AI understand the target resources and generate appropriate access control rules.</p>
            content: <p>The natural language description of the desired policy behavior. This content is processed by AI to generate corresponding Cedar policy statements that match the described intent.</p>
            name: <p>A customer-assigned name for the policy generation request. This helps track and identify generation operations, especially when running multiple generations simultaneously.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don't need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without starting a duplicate generation.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.start_policy_generation_request.StartPolicyGenerationRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.start_policy_generation_response.StartPolicyGenerationResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.start_policy_generation
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.start_policy_generation.start_policy_generation(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.start_policy_generation_request.StartPolicyGenerationRequest = {}  # type: ignore[typeddict-item]
        input["policy_engine_id"] = policy_engine_id
        input["resource"] = resource
        input["content"] = content
        input["name"] = name
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, policy_generation_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_policy_generation_response.GetPolicyGenerationResponse":
        """<p>Retrieves information about a policy generation request within the AgentCore Policy system. Policy generation converts natural language descriptions into Cedar policy statements using AI-powered translation, enabling non-technical users to create policies.</p>

        Args:
            policy_generation_id: <p>The unique identifier of the policy generation request to be retrieved. This must be a valid generation ID from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html\">StartPolicyGeneration</a> call.</p>
            policy_engine_id: <p>The identifier of the policy engine associated with the policy generation request. This provides the context for the generation operation and schema validation.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_policy_generation_request.GetPolicyGenerationRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.get_policy_generation_response.GetPolicyGenerationResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation.get_policy_generation(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_policy_generation_request.GetPolicyGenerationRequest = {}  # type: ignore[typeddict-item]
        input["policy_generation_id"] = policy_generation_id
        input["policy_engine_id"] = policy_engine_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_policy_generations_response.ListPolicyGenerationsResponse":
        """<p>Retrieves a list of policy generation requests within the AgentCore Policy system. This operation supports pagination and filtering to help track and manage AI-powered policy generation operations.</p>

        Args:
            next_token: <p>A pagination token for retrieving additional policy generations when results are paginated.</p>
            max_results: <p>The maximum number of policy generations to return in a single response.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policy generations to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_policy_generations_request.ListPolicyGenerationsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_policy_generations_response.ListPolicyGenerationsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generations
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generations.list_policy_generations(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_policy_generations_request.ListPolicyGenerationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["policy_engine_id"] = policy_engine_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_policy_generation_summary(self, policy_generation_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_policy_generation_summary_response.GetPolicyGenerationSummaryResponse":
        """<p>Retrieves a metadata-only summary of a specific policy generation request without decrypting customer content. This lightweight read operation returns resource identifiers, status, timestamps, and findings, but does not include status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            policy_generation_id: <p>The unique identifier of the policy generation request to retrieve the summary for.</p>
            policy_engine_id: <p>The identifier of the policy engine associated with the policy generation request.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_policy_generation_summary_request.GetPolicyGenerationSummaryRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.get_policy_generation_summary_response.GetPolicyGenerationSummaryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation_summary
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation_summary.get_policy_generation_summary(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_policy_generation_summary_request.GetPolicyGenerationSummaryRequest = {}  # type: ignore[typeddict-item]
        input["policy_generation_id"] = policy_generation_id
        input["policy_engine_id"] = policy_engine_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_policy_generation_assets(self, policy_generation_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_policy_generation_assets_response.ListPolicyGenerationAssetsResponse":
        """<p>Retrieves a list of generated policy assets from a policy generation request within the AgentCore Policy system. This operation returns the actual Cedar policies and related artifacts produced by the AI-powered policy generation process, allowing users to review and select from multiple generated policy options.</p>

        Args:
            policy_generation_id: <p>The unique identifier of the policy generation request whose assets are to be retrieved. This must be a valid generation ID from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html\">StartPolicyGeneration</a> call that has completed processing.</p>
            policy_engine_id: <p>The unique identifier of the policy engine associated with the policy generation request. This provides the context for the generation operation and ensures assets are retrieved from the correct policy engine.</p>
            next_token: <p>A pagination token returned from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationAssets.html\">ListPolicyGenerationAssets</a> call. Use this token to retrieve the next page of assets when the response is paginated due to large numbers of generated policy options.</p>
            max_results: <p>The maximum number of policy generation assets to return in a single response. If not specified, the default is 10 assets per page, with a maximum of 100 per page. This helps control response size when dealing with policy generations that produce many alternative policy options.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_policy_generation_assets_request.ListPolicyGenerationAssetsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_policy_generation_assets_response.ListPolicyGenerationAssetsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_assets
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_assets.list_policy_generation_assets(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_policy_generation_assets_request.ListPolicyGenerationAssetsRequest = {}  # type: ignore[typeddict-item]
        input["policy_generation_id"] = policy_generation_id
        input["policy_engine_id"] = policy_engine_id
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_policy_generation_summaries(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_policy_generation_summaries_response.ListPolicyGenerationSummariesResponse":
        """<p>Retrieves a paginated list of metadata-only policy generation summaries within a policy engine without decrypting customer content. This lightweight read operation returns resource identifiers, status, timestamps, and findings for each policy generation, but does not include status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            next_token: <p>A pagination token returned from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationSummaries.html\">ListPolicyGenerationSummaries</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>
            max_results: <p>The maximum number of policy generation summaries to return in a single response.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policy generation summaries to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_policy_generation_summaries_request.ListPolicyGenerationSummariesRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_policy_generation_summaries_response.ListPolicyGenerationSummariesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_summaries
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_summaries.list_policy_generation_summaries(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_policy_generation_summaries_request.ListPolicyGenerationSummariesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["policy_engine_id"] = policy_engine_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncPolicyGenerationResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service
    async def create(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", resource: "aws_sdk_bedrock_agentcore_control.types.resource.Resource", content: "aws_sdk_bedrock_agentcore_control.types.content.Content", name: "aws_sdk_bedrock_agentcore_control.types.policy_generation_name.PolicyGenerationName", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.start_policy_generation_response.StartPolicyGenerationResponse":
        """<p>Initiates the AI-powered generation of Cedar policies from natural language descriptions within the AgentCore Policy system. This feature enables both technical and non-technical users to create policies by describing their authorization requirements in plain English, which is then automatically translated into formal Cedar policy statements. The generation process analyzes the natural language input along with the Gateway's tool context to produce validated policy options. Generated policy assets are automatically deleted after 7 days, so you should review and create policies from the generated assets within this timeframe. Once created, policies are permanent and not subject to this expiration. Generated policies should be reviewed and tested in log-only mode before deploying to production. Use this when you want to describe policy intent naturally rather than learning Cedar syntax, though generated policies may require refinement for complex scenarios.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that provides the context for policy generation. This engine's schema and tool context are used to ensure generated policies are valid and applicable.</p>
            resource: <p>The resource information that provides context for policy generation. This helps the AI understand the target resources and generate appropriate access control rules.</p>
            content: <p>The natural language description of the desired policy behavior. This content is processed by AI to generate corresponding Cedar policy statements that match the described intent.</p>
            name: <p>A customer-assigned name for the policy generation request. This helps track and identify generation operations, especially when running multiple generations simultaneously.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don't need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without starting a duplicate generation.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.start_policy_generation_request.StartPolicyGenerationRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.start_policy_generation_response.StartPolicyGenerationResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.start_policy_generation
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.start_policy_generation.async_start_policy_generation(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.start_policy_generation_request.StartPolicyGenerationRequest = {}  # type: ignore[typeddict-item]
        input["policy_engine_id"] = policy_engine_id
        input["resource"] = resource
        input["content"] = content
        input["name"] = name
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, policy_generation_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_policy_generation_response.GetPolicyGenerationResponse":
        """<p>Retrieves information about a policy generation request within the AgentCore Policy system. Policy generation converts natural language descriptions into Cedar policy statements using AI-powered translation, enabling non-technical users to create policies.</p>

        Args:
            policy_generation_id: <p>The unique identifier of the policy generation request to be retrieved. This must be a valid generation ID from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html\">StartPolicyGeneration</a> call.</p>
            policy_engine_id: <p>The identifier of the policy engine associated with the policy generation request. This provides the context for the generation operation and schema validation.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_policy_generation_request.GetPolicyGenerationRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.get_policy_generation_response.GetPolicyGenerationResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation.async_get_policy_generation(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_policy_generation_request.GetPolicyGenerationRequest = {}  # type: ignore[typeddict-item]
        input["policy_generation_id"] = policy_generation_id
        input["policy_engine_id"] = policy_engine_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_policy_generations_response.ListPolicyGenerationsResponse":
        """<p>Retrieves a list of policy generation requests within the AgentCore Policy system. This operation supports pagination and filtering to help track and manage AI-powered policy generation operations.</p>

        Args:
            next_token: <p>A pagination token for retrieving additional policy generations when results are paginated.</p>
            max_results: <p>The maximum number of policy generations to return in a single response.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policy generations to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_policy_generations_request.ListPolicyGenerationsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_policy_generations_response.ListPolicyGenerationsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generations
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generations.async_list_policy_generations(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_policy_generations_request.ListPolicyGenerationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["policy_engine_id"] = policy_engine_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_policy_generation_summary(self, policy_generation_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_policy_generation_summary_response.GetPolicyGenerationSummaryResponse":
        """<p>Retrieves a metadata-only summary of a specific policy generation request without decrypting customer content. This lightweight read operation returns resource identifiers, status, timestamps, and findings, but does not include status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            policy_generation_id: <p>The unique identifier of the policy generation request to retrieve the summary for.</p>
            policy_engine_id: <p>The identifier of the policy engine associated with the policy generation request.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_policy_generation_summary_request.GetPolicyGenerationSummaryRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.get_policy_generation_summary_response.GetPolicyGenerationSummaryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation_summary
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation_summary.async_get_policy_generation_summary(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_policy_generation_summary_request.GetPolicyGenerationSummaryRequest = {}  # type: ignore[typeddict-item]
        input["policy_generation_id"] = policy_generation_id
        input["policy_engine_id"] = policy_engine_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_policy_generation_assets(self, policy_generation_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_policy_generation_assets_response.ListPolicyGenerationAssetsResponse":
        """<p>Retrieves a list of generated policy assets from a policy generation request within the AgentCore Policy system. This operation returns the actual Cedar policies and related artifacts produced by the AI-powered policy generation process, allowing users to review and select from multiple generated policy options.</p>

        Args:
            policy_generation_id: <p>The unique identifier of the policy generation request whose assets are to be retrieved. This must be a valid generation ID from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html\">StartPolicyGeneration</a> call that has completed processing.</p>
            policy_engine_id: <p>The unique identifier of the policy engine associated with the policy generation request. This provides the context for the generation operation and ensures assets are retrieved from the correct policy engine.</p>
            next_token: <p>A pagination token returned from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationAssets.html\">ListPolicyGenerationAssets</a> call. Use this token to retrieve the next page of assets when the response is paginated due to large numbers of generated policy options.</p>
            max_results: <p>The maximum number of policy generation assets to return in a single response. If not specified, the default is 10 assets per page, with a maximum of 100 per page. This helps control response size when dealing with policy generations that produce many alternative policy options.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_policy_generation_assets_request.ListPolicyGenerationAssetsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_policy_generation_assets_response.ListPolicyGenerationAssetsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_assets
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_assets.async_list_policy_generation_assets(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_policy_generation_assets_request.ListPolicyGenerationAssetsRequest = {}  # type: ignore[typeddict-item]
        input["policy_generation_id"] = policy_generation_id
        input["policy_engine_id"] = policy_engine_id
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_policy_generation_summaries(self, policy_engine_id: "aws_sdk_bedrock_agentcore_control.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_policy_generation_summaries_response.ListPolicyGenerationSummariesResponse":
        """<p>Retrieves a paginated list of metadata-only policy generation summaries within a policy engine without decrypting customer content. This lightweight read operation returns resource identifiers, status, timestamps, and findings for each policy generation, but does not include status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            next_token: <p>A pagination token returned from a previous <a href=\"https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationSummaries.html\">ListPolicyGenerationSummaries</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>
            max_results: <p>The maximum number of policy generation summaries to return in a single response.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policy generation summaries to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_policy_generation_summaries_request.ListPolicyGenerationSummariesRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_policy_generation_summaries_response.ListPolicyGenerationSummariesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_summaries
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_summaries.async_list_policy_generation_summaries(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_policy_generation_summaries_request.ListPolicyGenerationSummariesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["policy_engine_id"] = policy_engine_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output