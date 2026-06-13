from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import ensure_async_iterator
from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import ensure_sync_iterator
from aws_sdk_bedrock_agentcore_control._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import BedrockAgentCoreControlClient, BedrockAgentCoreControlClientConfig
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import AsyncBedrockAgentCoreControlClient, AsyncBedrockAgentCoreControlClientConfig
    import aws_sdk_bedrock_agentcore_control.types.agent_endpoint_description
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_id
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_version
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request
    import aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response
    import aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request
    import aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response
    import aws_sdk_bedrock_agentcore_control.types.endpoint_name
    import aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request
    import aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response
    import aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request
    import aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request
    import aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response

class AgentEndpointResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service
    def create(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, agent_runtime_version: Optional["aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None, tags: Optional["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse":
        """<p>Creates an AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to create an endpoint for.</p>
            name: <p>The name of the AgentCore Runtime endpoint.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to use for the endpoint.</p>
            description: <p>The description of the AgentCore Runtime endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>A map of tag keys and values to assign to the agent runtime endpoint. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime_endpoint
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime_endpoint.create_agent_runtime_endpoint(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        input["name"] = name
        if agent_runtime_version is not None:
            input["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            input["description"] = description
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", endpoint_name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse":
        """<p>Gets information about an Amazon Secure AgentEndpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime_endpoint
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime_endpoint.get_agent_runtime_endpoint(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        input["endpoint_name"] = endpoint_name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", endpoint_name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, agent_runtime_version: Optional["aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response.UpdateAgentRuntimeEndpointResponse":
        """<p>Updates an existing Amazon Bedrock AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to update.</p>
            agent_runtime_version: <p>The updated version of the AgentCore Runtime for the endpoint.</p>
            description: <p>The updated description of the AgentCore Runtime endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response.UpdateAgentRuntimeEndpointResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime_endpoint
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime_endpoint.update_agent_runtime_endpoint(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        input["endpoint_name"] = endpoint_name
        if agent_runtime_version is not None:
            input["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            input["description"] = description
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", endpoint_name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse":
        """<p>Deletes an AAgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime_endpoint
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime_endpoint.delete_agent_runtime_endpoint(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        input["endpoint_name"] = endpoint_name
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse":
        """<p>Lists all endpoints for a specific Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to list endpoints for.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request.ListAgentRuntimeEndpointsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_endpoints
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_endpoints.list_agent_runtime_endpoints(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request.ListAgentRuntimeEndpointsRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncAgentEndpointResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service
    async def create(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, agent_runtime_version: Optional["aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None, tags: Optional["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse":
        """<p>Creates an AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to create an endpoint for.</p>
            name: <p>The name of the AgentCore Runtime endpoint.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to use for the endpoint.</p>
            description: <p>The description of the AgentCore Runtime endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>A map of tag keys and values to assign to the agent runtime endpoint. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime_endpoint
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime_endpoint.async_create_agent_runtime_endpoint(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        input["name"] = name
        if agent_runtime_version is not None:
            input["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            input["description"] = description
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", endpoint_name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse":
        """<p>Gets information about an Amazon Secure AgentEndpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime_endpoint
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime_endpoint.async_get_agent_runtime_endpoint(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        input["endpoint_name"] = endpoint_name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", endpoint_name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, agent_runtime_version: Optional["aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response.UpdateAgentRuntimeEndpointResponse":
        """<p>Updates an existing Amazon Bedrock AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to update.</p>
            agent_runtime_version: <p>The updated version of the AgentCore Runtime for the endpoint.</p>
            description: <p>The updated description of the AgentCore Runtime endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response.UpdateAgentRuntimeEndpointResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime_endpoint
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime_endpoint.async_update_agent_runtime_endpoint(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        input["endpoint_name"] = endpoint_name
        if agent_runtime_version is not None:
            input["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            input["description"] = description
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", endpoint_name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse":
        """<p>Deletes an AAgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime_endpoint
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime_endpoint.async_delete_agent_runtime_endpoint(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        input["endpoint_name"] = endpoint_name
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse":
        """<p>Lists all endpoints for a specific Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to list endpoints for.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request.ListAgentRuntimeEndpointsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_endpoints
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_endpoints.async_list_agent_runtime_endpoints(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request.ListAgentRuntimeEndpointsRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output