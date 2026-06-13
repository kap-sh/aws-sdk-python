from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import ensure_async_iterator
from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import ensure_sync_iterator
from aws_sdk_bedrock_agentcore_control._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import BedrockAgentCoreControlClient, BedrockAgentCoreControlClientConfig
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import AsyncBedrockAgentCoreControlClient, AsyncBedrockAgentCoreControlClientConfig
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_artifact
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_id
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_name
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_version
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_request
    import aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_response
    import aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_request
    import aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_response
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.environment_variables_map
    import aws_sdk_bedrock_agentcore_control.types.filesystem_configurations
    import aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_request
    import aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_response
    import aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration
    import aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_versions_request
    import aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_versions_response
    import aws_sdk_bedrock_agentcore_control.types.list_agent_runtimes_request
    import aws_sdk_bedrock_agentcore_control.types.list_agent_runtimes_response
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.network_configuration
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.protocol_configuration
    import aws_sdk_bedrock_agentcore_control.types.request_header_configuration
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.runtime_metadata_configuration
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_request
    import aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_response

class AgentResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service
    def create(self, agent_runtime_name: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_name.AgentRuntimeName", agent_runtime_artifact: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact", role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn", network_configuration: "aws_sdk_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.description.Description"] = None, authorizer_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"] = None, request_header_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"] = None, protocol_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"] = None, lifecycle_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"] = None, environment_variables: Optional["aws_sdk_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"] = None, filesystem_configurations: Optional["aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"] = None, tags: Optional["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_response.CreateAgentRuntimeResponse":
        """<p>Creates an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_name: <p>The name of the AgentCore Runtime.</p>
            agent_runtime_artifact: <p>The artifact of the AgentCore Runtime.</p>
            role_arn: <p>The IAM role ARN that provides permissions for the AgentCore Runtime.</p>
            network_configuration: <p>The network configuration for the AgentCore Runtime.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            description: <p>The description of the AgentCore Runtime.</p>
            authorizer_configuration: <p>The authorizer configuration for the AgentCore Runtime.</p>
            request_header_configuration: <p>Configuration for HTTP request headers that will be passed through to the runtime.</p>
            lifecycle_configuration: <p>The life cycle configuration for the AgentCore Runtime.</p>
            environment_variables: <p>Environment variables to set in the AgentCore Runtime environment.</p>
            filesystem_configurations: <p>The filesystem configurations to mount into the AgentCore Runtime. Use filesystem configurations to provide persistent storage to your AgentCore Runtime sessions.</p>
            tags: <p>A map of tag keys and values to assign to the agent runtime. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_response.CreateAgentRuntimeResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime.create_agent_runtime(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_name"] = agent_runtime_name
        input["agent_runtime_artifact"] = agent_runtime_artifact
        input["role_arn"] = role_arn
        input["network_configuration"] = network_configuration
        if client_token is not None:
            input["client_token"] = client_token
        if description is not None:
            input["description"] = description
        if authorizer_configuration is not None:
            input["authorizer_configuration"] = authorizer_configuration
        if request_header_configuration is not None:
            input["request_header_configuration"] = request_header_configuration
        if protocol_configuration is not None:
            input["protocol_configuration"] = protocol_configuration
        if lifecycle_configuration is not None:
            input["lifecycle_configuration"] = lifecycle_configuration
        if environment_variables is not None:
            input["environment_variables"] = environment_variables
        if filesystem_configurations is not None:
            input["filesystem_configurations"] = filesystem_configurations
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, agent_runtime_version: Optional["aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse":
        """<p>Gets an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to retrieve.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_request.GetAgentRuntimeRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime.get_agent_runtime(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_request.GetAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        if agent_runtime_version is not None:
            input["agent_runtime_version"] = agent_runtime_version

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", agent_runtime_artifact: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact", role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn", network_configuration: "aws_sdk_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.description.Description"] = None, authorizer_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"] = None, request_header_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"] = None, protocol_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"] = None, lifecycle_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"] = None, metadata_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.runtime_metadata_configuration.RuntimeMetadataConfiguration"] = None, environment_variables: Optional["aws_sdk_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"] = None, filesystem_configurations: Optional["aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_response.UpdateAgentRuntimeResponse":
        """<p>Updates an existing Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to update.</p>
            agent_runtime_artifact: <p>The updated artifact of the AgentCore Runtime.</p>
            role_arn: <p>The updated IAM role ARN that provides permissions for the AgentCore Runtime.</p>
            network_configuration: <p>The updated network configuration for the AgentCore Runtime.</p>
            description: <p>The updated description of the AgentCore Runtime.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the AgentCore Runtime.</p>
            request_header_configuration: <p>The updated configuration for HTTP request headers that will be passed through to the runtime.</p>
            lifecycle_configuration: <p>The updated life cycle configuration for the AgentCore Runtime.</p>
            metadata_configuration: <p>The updated configuration for microVM Metadata Service (MMDS) settings for the AgentCore Runtime.</p>
            environment_variables: <p>Updated environment variables to set in the AgentCore Runtime environment.</p>
            filesystem_configurations: <p>The updated filesystem configurations to mount into the AgentCore Runtime.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_response.UpdateAgentRuntimeResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime.update_agent_runtime(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        input["agent_runtime_artifact"] = agent_runtime_artifact
        input["role_arn"] = role_arn
        input["network_configuration"] = network_configuration
        if description is not None:
            input["description"] = description
        if authorizer_configuration is not None:
            input["authorizer_configuration"] = authorizer_configuration
        if request_header_configuration is not None:
            input["request_header_configuration"] = request_header_configuration
        if protocol_configuration is not None:
            input["protocol_configuration"] = protocol_configuration
        if lifecycle_configuration is not None:
            input["lifecycle_configuration"] = lifecycle_configuration
        if metadata_configuration is not None:
            input["metadata_configuration"] = metadata_configuration
        if environment_variables is not None:
            input["environment_variables"] = environment_variables
        if filesystem_configurations is not None:
            input["filesystem_configurations"] = filesystem_configurations
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_response.DeleteAgentRuntimeResponse":
        """<p>Deletes an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_request.DeleteAgentRuntimeRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_response.DeleteAgentRuntimeResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime.delete_agent_runtime(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_request.DeleteAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse":
        """<p>Lists all Amazon Secure Agents in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_agent_runtimes_request.ListAgentRuntimesRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtimes
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtimes.list_agent_runtimes(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_agent_runtimes_request.ListAgentRuntimesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_agent_runtime_versions(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse":
        """<p>Lists all versions of a specific Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to list versions for.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_versions_request.ListAgentRuntimeVersionsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions.list_agent_runtime_versions(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_versions_request.ListAgentRuntimeVersionsRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncAgentResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service
    async def create(self, agent_runtime_name: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_name.AgentRuntimeName", agent_runtime_artifact: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact", role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn", network_configuration: "aws_sdk_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.description.Description"] = None, authorizer_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"] = None, request_header_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"] = None, protocol_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"] = None, lifecycle_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"] = None, environment_variables: Optional["aws_sdk_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"] = None, filesystem_configurations: Optional["aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"] = None, tags: Optional["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_response.CreateAgentRuntimeResponse":
        """<p>Creates an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_name: <p>The name of the AgentCore Runtime.</p>
            agent_runtime_artifact: <p>The artifact of the AgentCore Runtime.</p>
            role_arn: <p>The IAM role ARN that provides permissions for the AgentCore Runtime.</p>
            network_configuration: <p>The network configuration for the AgentCore Runtime.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            description: <p>The description of the AgentCore Runtime.</p>
            authorizer_configuration: <p>The authorizer configuration for the AgentCore Runtime.</p>
            request_header_configuration: <p>Configuration for HTTP request headers that will be passed through to the runtime.</p>
            lifecycle_configuration: <p>The life cycle configuration for the AgentCore Runtime.</p>
            environment_variables: <p>Environment variables to set in the AgentCore Runtime environment.</p>
            filesystem_configurations: <p>The filesystem configurations to mount into the AgentCore Runtime. Use filesystem configurations to provide persistent storage to your AgentCore Runtime sessions.</p>
            tags: <p>A map of tag keys and values to assign to the agent runtime. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_response.CreateAgentRuntimeResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime.async_create_agent_runtime(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_name"] = agent_runtime_name
        input["agent_runtime_artifact"] = agent_runtime_artifact
        input["role_arn"] = role_arn
        input["network_configuration"] = network_configuration
        if client_token is not None:
            input["client_token"] = client_token
        if description is not None:
            input["description"] = description
        if authorizer_configuration is not None:
            input["authorizer_configuration"] = authorizer_configuration
        if request_header_configuration is not None:
            input["request_header_configuration"] = request_header_configuration
        if protocol_configuration is not None:
            input["protocol_configuration"] = protocol_configuration
        if lifecycle_configuration is not None:
            input["lifecycle_configuration"] = lifecycle_configuration
        if environment_variables is not None:
            input["environment_variables"] = environment_variables
        if filesystem_configurations is not None:
            input["filesystem_configurations"] = filesystem_configurations
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, agent_runtime_version: Optional["aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse":
        """<p>Gets an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to retrieve.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_request.GetAgentRuntimeRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime.async_get_agent_runtime(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_agent_runtime_request.GetAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        if agent_runtime_version is not None:
            input["agent_runtime_version"] = agent_runtime_version

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", agent_runtime_artifact: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact", role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn", network_configuration: "aws_sdk_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.description.Description"] = None, authorizer_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"] = None, request_header_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"] = None, protocol_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"] = None, lifecycle_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"] = None, metadata_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.runtime_metadata_configuration.RuntimeMetadataConfiguration"] = None, environment_variables: Optional["aws_sdk_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"] = None, filesystem_configurations: Optional["aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_response.UpdateAgentRuntimeResponse":
        """<p>Updates an existing Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to update.</p>
            agent_runtime_artifact: <p>The updated artifact of the AgentCore Runtime.</p>
            role_arn: <p>The updated IAM role ARN that provides permissions for the AgentCore Runtime.</p>
            network_configuration: <p>The updated network configuration for the AgentCore Runtime.</p>
            description: <p>The updated description of the AgentCore Runtime.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the AgentCore Runtime.</p>
            request_header_configuration: <p>The updated configuration for HTTP request headers that will be passed through to the runtime.</p>
            lifecycle_configuration: <p>The updated life cycle configuration for the AgentCore Runtime.</p>
            metadata_configuration: <p>The updated configuration for microVM Metadata Service (MMDS) settings for the AgentCore Runtime.</p>
            environment_variables: <p>Updated environment variables to set in the AgentCore Runtime environment.</p>
            filesystem_configurations: <p>The updated filesystem configurations to mount into the AgentCore Runtime.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_response.UpdateAgentRuntimeResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime.async_update_agent_runtime(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        input["agent_runtime_artifact"] = agent_runtime_artifact
        input["role_arn"] = role_arn
        input["network_configuration"] = network_configuration
        if description is not None:
            input["description"] = description
        if authorizer_configuration is not None:
            input["authorizer_configuration"] = authorizer_configuration
        if request_header_configuration is not None:
            input["request_header_configuration"] = request_header_configuration
        if protocol_configuration is not None:
            input["protocol_configuration"] = protocol_configuration
        if lifecycle_configuration is not None:
            input["lifecycle_configuration"] = lifecycle_configuration
        if metadata_configuration is not None:
            input["metadata_configuration"] = metadata_configuration
        if environment_variables is not None:
            input["environment_variables"] = environment_variables
        if filesystem_configurations is not None:
            input["filesystem_configurations"] = filesystem_configurations
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_response.DeleteAgentRuntimeResponse":
        """<p>Deletes an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_request.DeleteAgentRuntimeRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_response.DeleteAgentRuntimeResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime.async_delete_agent_runtime(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_agent_runtime_request.DeleteAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse":
        """<p>Lists all Amazon Secure Agents in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_agent_runtimes_request.ListAgentRuntimesRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtimes
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtimes.async_list_agent_runtimes(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_agent_runtimes_request.ListAgentRuntimesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_agent_runtime_versions(self, agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse":
        """<p>Lists all versions of a specific Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to list versions for.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_versions_request.ListAgentRuntimeVersionsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions.async_list_agent_runtime_versions(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_agent_runtime_versions_request.ListAgentRuntimeVersionsRequest = {}  # type: ignore[typeddict-item]
        input["agent_runtime_id"] = agent_runtime_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output