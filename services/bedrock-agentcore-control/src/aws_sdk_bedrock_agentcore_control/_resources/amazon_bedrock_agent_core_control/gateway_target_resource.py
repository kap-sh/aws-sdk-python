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
    import aws_sdk_bedrock_agentcore_control.types.create_gateway_target_request
    import aws_sdk_bedrock_agentcore_control.types.create_gateway_target_response
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations
    import aws_sdk_bedrock_agentcore_control.types.delete_gateway_target_request
    import aws_sdk_bedrock_agentcore_control.types.delete_gateway_target_response
    import aws_sdk_bedrock_agentcore_control.types.gateway_identifier
    import aws_sdk_bedrock_agentcore_control.types.get_gateway_target_request
    import aws_sdk_bedrock_agentcore_control.types.get_gateway_target_response
    import aws_sdk_bedrock_agentcore_control.types.list_gateway_targets_request
    import aws_sdk_bedrock_agentcore_control.types.list_gateway_targets_response
    import aws_sdk_bedrock_agentcore_control.types.metadata_configuration
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint
    import aws_sdk_bedrock_agentcore_control.types.synchronize_gateway_targets_request
    import aws_sdk_bedrock_agentcore_control.types.synchronize_gateway_targets_response
    import aws_sdk_bedrock_agentcore_control.types.target_configuration
    import aws_sdk_bedrock_agentcore_control.types.target_description
    import aws_sdk_bedrock_agentcore_control.types.target_id
    import aws_sdk_bedrock_agentcore_control.types.target_id_list
    import aws_sdk_bedrock_agentcore_control.types.target_max_results
    import aws_sdk_bedrock_agentcore_control.types.target_name
    import aws_sdk_bedrock_agentcore_control.types.target_next_token
    import aws_sdk_bedrock_agentcore_control.types.target_summary
    import aws_sdk_bedrock_agentcore_control.types.update_gateway_target_request
    import aws_sdk_bedrock_agentcore_control.types.update_gateway_target_response

class GatewayTargetResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service
    def create_gateway_target(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", name: "aws_sdk_bedrock_agentcore_control.types.target_name.TargetName", target_configuration: "aws_sdk_bedrock_agentcore_control.types.target_configuration.TargetConfiguration", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.target_description.TargetDescription"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None, credential_provider_configurations: Optional["aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations.CredentialProviderConfigurations"] = None, metadata_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.metadata_configuration.MetadataConfiguration"] = None, private_endpoint: Optional["aws_sdk_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_gateway_target_response.CreateGatewayTargetResponse":
        """<p>Creates a target for a gateway. A target defines an endpoint that the gateway can connect to.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to create a target for.</p>
            name: <p>The name of the gateway target. The name must be unique within the gateway.</p>
            description: <p>The description of the gateway target.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            target_configuration: <p>The configuration settings for the target, including endpoint information and schema definitions.</p>
            credential_provider_configurations: <p>The credential provider configurations for the target. These configurations specify how the gateway authenticates with the target endpoint.</p>
            metadata_configuration: <p>Optional configuration for HTTP header and query parameter propagation to and from the gateway target.</p>
            private_endpoint: <p>The private endpoint configuration for the gateway target. Use this to connect the gateway to private resources in your VPC.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_gateway_target_request.CreateGatewayTargetRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.create_gateway_target_response.CreateGatewayTargetResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_target
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_target.create_gateway_target(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_gateway_target_request.CreateGatewayTargetRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        input["name"] = name
        if description is not None:
            input["description"] = description
        if client_token is not None:
            input["client_token"] = client_token
        input["target_configuration"] = target_configuration
        if credential_provider_configurations is not None:
            input["credential_provider_configurations"] = credential_provider_configurations
        if metadata_configuration is not None:
            input["metadata_configuration"] = metadata_configuration
        if private_endpoint is not None:
            input["private_endpoint"] = private_endpoint

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete_gateway_target(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", target_id: "aws_sdk_bedrock_agentcore_control.types.target_id.TargetId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_gateway_target_response.DeleteGatewayTargetResponse":
        """<p>Deletes a gateway target.</p> <p>You cannot delete a target that is in a pending authorization state (<code>CREATE_PENDING_AUTH</code>, <code>UPDATE_PENDING_AUTH</code>, or <code>SYNCHRONIZE_PENDING_AUTH</code>). Wait for the authorization to complete or fail before deleting the target.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway associated with the target.</p>
            target_id: <p>The unique identifier of the gateway target to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_gateway_target_request.DeleteGatewayTargetRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_gateway_target_response.DeleteGatewayTargetResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_target
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_target.delete_gateway_target(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_gateway_target_request.DeleteGatewayTargetRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        input["target_id"] = target_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_gateway_target(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", target_id: "aws_sdk_bedrock_agentcore_control.types.target_id.TargetId", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_gateway_target_response.GetGatewayTargetResponse":
        """<p>Retrieves information about a specific gateway target.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway that contains the target.</p>
            target_id: <p>The unique identifier of the target to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_gateway_target_request.GetGatewayTargetRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.get_gateway_target_response.GetGatewayTargetResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_target
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_target.get_gateway_target(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_gateway_target_request.GetGatewayTargetRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        input["target_id"] = target_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_gateway_targets(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.target_max_results.TargetMaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.target_next_token.TargetNextToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_gateway_targets_response.ListGatewayTargetsResponse":
        """<p>Lists all targets for a specific gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to list targets for.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_gateway_targets_request.ListGatewayTargetsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_gateway_targets_response.ListGatewayTargetsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_targets
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_targets.list_gateway_targets(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_gateway_targets_request.ListGatewayTargetsRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def synchronize_gateway_targets(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", target_id_list: "aws_sdk_bedrock_agentcore_control.types.target_id_list.TargetIdList", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.synchronize_gateway_targets_response.SynchronizeGatewayTargetsResponse":
        """<p>Synchronizes the gateway targets by fetching the latest tool definitions from the target endpoints.</p> <p>You cannot synchronize a target that is in a pending authorization state (<code>CREATE_PENDING_AUTH</code>, <code>UPDATE_PENDING_AUTH</code>, or <code>SYNCHRONIZE_PENDING_AUTH</code>). Wait for the authorization to complete or fail before synchronizing.</p> <p>You cannot synchronize a target that has a static tool schema (<code>mcpToolSchema</code>) configured. Remove the static schema through an <code>UpdateGatewayTarget</code> call to enable dynamic tool synchronization.</p>

        Args:
            gateway_identifier: <p>The gateway Identifier.</p>
            target_id_list: <p>The target ID list.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.synchronize_gateway_targets_request.SynchronizeGatewayTargetsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.synchronize_gateway_targets_response.SynchronizeGatewayTargetsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.synchronize_gateway_targets
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.synchronize_gateway_targets.synchronize_gateway_targets(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.synchronize_gateway_targets_request.SynchronizeGatewayTargetsRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        input["target_id_list"] = target_id_list

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update_gateway_target(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", target_id: "aws_sdk_bedrock_agentcore_control.types.target_id.TargetId", name: "aws_sdk_bedrock_agentcore_control.types.target_name.TargetName", target_configuration: "aws_sdk_bedrock_agentcore_control.types.target_configuration.TargetConfiguration", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.target_description.TargetDescription"] = None, credential_provider_configurations: Optional["aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations.CredentialProviderConfigurations"] = None, metadata_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.metadata_configuration.MetadataConfiguration"] = None, private_endpoint: Optional["aws_sdk_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_gateway_target_response.UpdateGatewayTargetResponse":
        """<p>Updates an existing gateway target.</p> <p>You cannot update a target that is in a pending authorization state (<code>CREATE_PENDING_AUTH</code>, <code>UPDATE_PENDING_AUTH</code>, or <code>SYNCHRONIZE_PENDING_AUTH</code>). Wait for the authorization to complete or fail before updating the target.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway associated with the target.</p>
            target_id: <p>The unique identifier of the gateway target to update.</p>
            name: <p>The updated name for the gateway target.</p>
            description: <p>The updated description for the gateway target.</p>
            credential_provider_configurations: <p>The updated credential provider configurations for the gateway target.</p>
            metadata_configuration: <p>Configuration for HTTP header and query parameter propagation to the gateway target.</p>
            private_endpoint: <p>The private endpoint configuration for the gateway target. Use this to connect the gateway to private resources in your VPC.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_gateway_target_request.UpdateGatewayTargetRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.update_gateway_target_response.UpdateGatewayTargetResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_target
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_target.update_gateway_target(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_gateway_target_request.UpdateGatewayTargetRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        input["target_id"] = target_id
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["target_configuration"] = target_configuration
        if credential_provider_configurations is not None:
            input["credential_provider_configurations"] = credential_provider_configurations
        if metadata_configuration is not None:
            input["metadata_configuration"] = metadata_configuration
        if private_endpoint is not None:
            input["private_endpoint"] = private_endpoint

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncGatewayTargetResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service
    async def create_gateway_target(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", name: "aws_sdk_bedrock_agentcore_control.types.target_name.TargetName", target_configuration: "aws_sdk_bedrock_agentcore_control.types.target_configuration.TargetConfiguration", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.target_description.TargetDescription"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None, credential_provider_configurations: Optional["aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations.CredentialProviderConfigurations"] = None, metadata_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.metadata_configuration.MetadataConfiguration"] = None, private_endpoint: Optional["aws_sdk_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_gateway_target_response.CreateGatewayTargetResponse":
        """<p>Creates a target for a gateway. A target defines an endpoint that the gateway can connect to.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to create a target for.</p>
            name: <p>The name of the gateway target. The name must be unique within the gateway.</p>
            description: <p>The description of the gateway target.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            target_configuration: <p>The configuration settings for the target, including endpoint information and schema definitions.</p>
            credential_provider_configurations: <p>The credential provider configurations for the target. These configurations specify how the gateway authenticates with the target endpoint.</p>
            metadata_configuration: <p>Optional configuration for HTTP header and query parameter propagation to and from the gateway target.</p>
            private_endpoint: <p>The private endpoint configuration for the gateway target. Use this to connect the gateway to private resources in your VPC.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_gateway_target_request.CreateGatewayTargetRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.create_gateway_target_response.CreateGatewayTargetResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_target
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_target.async_create_gateway_target(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_gateway_target_request.CreateGatewayTargetRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        input["name"] = name
        if description is not None:
            input["description"] = description
        if client_token is not None:
            input["client_token"] = client_token
        input["target_configuration"] = target_configuration
        if credential_provider_configurations is not None:
            input["credential_provider_configurations"] = credential_provider_configurations
        if metadata_configuration is not None:
            input["metadata_configuration"] = metadata_configuration
        if private_endpoint is not None:
            input["private_endpoint"] = private_endpoint

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete_gateway_target(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", target_id: "aws_sdk_bedrock_agentcore_control.types.target_id.TargetId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_gateway_target_response.DeleteGatewayTargetResponse":
        """<p>Deletes a gateway target.</p> <p>You cannot delete a target that is in a pending authorization state (<code>CREATE_PENDING_AUTH</code>, <code>UPDATE_PENDING_AUTH</code>, or <code>SYNCHRONIZE_PENDING_AUTH</code>). Wait for the authorization to complete or fail before deleting the target.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway associated with the target.</p>
            target_id: <p>The unique identifier of the gateway target to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_gateway_target_request.DeleteGatewayTargetRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_gateway_target_response.DeleteGatewayTargetResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_target
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_target.async_delete_gateway_target(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_gateway_target_request.DeleteGatewayTargetRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        input["target_id"] = target_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_gateway_target(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", target_id: "aws_sdk_bedrock_agentcore_control.types.target_id.TargetId", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_gateway_target_response.GetGatewayTargetResponse":
        """<p>Retrieves information about a specific gateway target.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway that contains the target.</p>
            target_id: <p>The unique identifier of the target to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_gateway_target_request.GetGatewayTargetRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.get_gateway_target_response.GetGatewayTargetResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_target
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_target.async_get_gateway_target(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_gateway_target_request.GetGatewayTargetRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        input["target_id"] = target_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_gateway_targets(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.target_max_results.TargetMaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.target_next_token.TargetNextToken"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_gateway_targets_response.ListGatewayTargetsResponse":
        """<p>Lists all targets for a specific gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to list targets for.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_gateway_targets_request.ListGatewayTargetsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_gateway_targets_response.ListGatewayTargetsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_targets
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_targets.async_list_gateway_targets(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_gateway_targets_request.ListGatewayTargetsRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def synchronize_gateway_targets(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", target_id_list: "aws_sdk_bedrock_agentcore_control.types.target_id_list.TargetIdList", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.synchronize_gateway_targets_response.SynchronizeGatewayTargetsResponse":
        """<p>Synchronizes the gateway targets by fetching the latest tool definitions from the target endpoints.</p> <p>You cannot synchronize a target that is in a pending authorization state (<code>CREATE_PENDING_AUTH</code>, <code>UPDATE_PENDING_AUTH</code>, or <code>SYNCHRONIZE_PENDING_AUTH</code>). Wait for the authorization to complete or fail before synchronizing.</p> <p>You cannot synchronize a target that has a static tool schema (<code>mcpToolSchema</code>) configured. Remove the static schema through an <code>UpdateGatewayTarget</code> call to enable dynamic tool synchronization.</p>

        Args:
            gateway_identifier: <p>The gateway Identifier.</p>
            target_id_list: <p>The target ID list.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.synchronize_gateway_targets_request.SynchronizeGatewayTargetsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.synchronize_gateway_targets_response.SynchronizeGatewayTargetsResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.synchronize_gateway_targets
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.synchronize_gateway_targets.async_synchronize_gateway_targets(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.synchronize_gateway_targets_request.SynchronizeGatewayTargetsRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        input["target_id_list"] = target_id_list

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update_gateway_target(self, gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier", target_id: "aws_sdk_bedrock_agentcore_control.types.target_id.TargetId", name: "aws_sdk_bedrock_agentcore_control.types.target_name.TargetName", target_configuration: "aws_sdk_bedrock_agentcore_control.types.target_configuration.TargetConfiguration", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.target_description.TargetDescription"] = None, credential_provider_configurations: Optional["aws_sdk_bedrock_agentcore_control.types.credential_provider_configurations.CredentialProviderConfigurations"] = None, metadata_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.metadata_configuration.MetadataConfiguration"] = None, private_endpoint: Optional["aws_sdk_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_gateway_target_response.UpdateGatewayTargetResponse":
        """<p>Updates an existing gateway target.</p> <p>You cannot update a target that is in a pending authorization state (<code>CREATE_PENDING_AUTH</code>, <code>UPDATE_PENDING_AUTH</code>, or <code>SYNCHRONIZE_PENDING_AUTH</code>). Wait for the authorization to complete or fail before updating the target.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway associated with the target.</p>
            target_id: <p>The unique identifier of the gateway target to update.</p>
            name: <p>The updated name for the gateway target.</p>
            description: <p>The updated description for the gateway target.</p>
            credential_provider_configurations: <p>The updated credential provider configurations for the gateway target.</p>
            metadata_configuration: <p>Configuration for HTTP header and query parameter propagation to the gateway target.</p>
            private_endpoint: <p>The private endpoint configuration for the gateway target. Use this to connect the gateway to private resources in your VPC.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_gateway_target_request.UpdateGatewayTargetRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.update_gateway_target_response.UpdateGatewayTargetResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_target
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_target.async_update_gateway_target(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_gateway_target_request.UpdateGatewayTargetRequest = {}  # type: ignore[typeddict-item]
        input["gateway_identifier"] = gateway_identifier
        input["target_id"] = target_id
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["target_configuration"] = target_configuration
        if credential_provider_configurations is not None:
            input["credential_provider_configurations"] = credential_provider_configurations
        if metadata_configuration is not None:
            input["metadata_configuration"] = metadata_configuration
        if private_endpoint is not None:
            input["private_endpoint"] = private_endpoint

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output