from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import ensure_async_iterator
from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import ensure_sync_iterator
from aws_sdk_bedrock_agentcore_control._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import BedrockAgentCoreControlClient, BedrockAgentCoreControlClientConfig
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import AsyncBedrockAgentCoreControlClient, AsyncBedrockAgentCoreControlClientConfig
    import aws_sdk_bedrock_agentcore_control.types.approval_configuration
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.create_registry_request
    import aws_sdk_bedrock_agentcore_control.types.create_registry_response
    import aws_sdk_bedrock_agentcore_control.types.delete_registry_request
    import aws_sdk_bedrock_agentcore_control.types.delete_registry_response
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.get_registry_request
    import aws_sdk_bedrock_agentcore_control.types.get_registry_response
    import aws_sdk_bedrock_agentcore_control.types.list_registries_request
    import aws_sdk_bedrock_agentcore_control.types.list_registries_response
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.registry_authorizer_type
    import aws_sdk_bedrock_agentcore_control.types.registry_identifier
    import aws_sdk_bedrock_agentcore_control.types.registry_name
    import aws_sdk_bedrock_agentcore_control.types.registry_status
    import aws_sdk_bedrock_agentcore_control.types.registry_summary
    import aws_sdk_bedrock_agentcore_control.types.update_registry_request
    import aws_sdk_bedrock_agentcore_control.types.update_registry_response
    import aws_sdk_bedrock_agentcore_control.types.updated_approval_configuration
    import aws_sdk_bedrock_agentcore_control.types.updated_authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.updated_description

class RegistryResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service
    def create(self, name: "aws_sdk_bedrock_agentcore_control.types.registry_name.RegistryName", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.description.Description"] = None, authorizer_type: Optional["aws_sdk_bedrock_agentcore_control.types.registry_authorizer_type.RegistryAuthorizerType"] = None, authorizer_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None, approval_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.approval_configuration.ApprovalConfiguration"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_registry_response.CreateRegistryResponse":
        """<p>Creates a new registry in your Amazon Web Services account. A registry serves as a centralized catalog for organizing and managing registry records, including MCP servers, A2A agents, agent skills, and custom resource types.</p> <p>If you specify <code>CUSTOM_JWT</code> as the <code>authorizerType</code>, you must provide an <code>authorizerConfiguration</code>.</p>

        Args:
            name: <p>The name of the registry. The name must be unique within your account and can contain alphanumeric characters and underscores.</p>
            description: <p>A description of the registry.</p>
            authorizer_type: <p>The type of authorizer to use for the registry. This controls the authorization method for the Search and Invoke APIs used by consumers, and does not affect the standard CRUDL APIs for registry and registry record management used by administrators.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>
            authorizer_configuration: <p>The authorizer configuration for the registry. Required if <code>authorizerType</code> is <code>CUSTOM_JWT</code>. For details, see the <code>AuthorizerConfiguration</code> data type.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            approval_configuration: <p>The approval configuration for registry records. Controls whether records require explicit approval before becoming active. See the <code>ApprovalConfiguration</code> data type for supported configuration options.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_registry_request.CreateRegistryRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.create_registry_response.CreateRegistryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry.create_registry(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_registry_request.CreateRegistryRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if authorizer_type is not None:
            input["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input["authorizer_configuration"] = authorizer_configuration
        if client_token is not None:
            input["client_token"] = client_token
        if approval_configuration is not None:
            input["approval_configuration"] = approval_configuration

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, registry_id: "aws_sdk_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_registry_response.GetRegistryResponse":
        """<p>Retrieves information about a specific registry.</p>

        Args:
            registry_id: <p>The identifier of the registry to retrieve. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_registry_request.GetRegistryRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.get_registry_response.GetRegistryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry.get_registry(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_registry_request.GetRegistryRequest = {}  # type: ignore[typeddict-item]
        input["registry_id"] = registry_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, registry_id: "aws_sdk_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, name: Optional["aws_sdk_bedrock_agentcore_control.types.registry_name.RegistryName"] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.updated_description.UpdatedDescription"] = None, authorizer_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.updated_authorizer_configuration.UpdatedAuthorizerConfiguration"] = None, approval_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.updated_approval_configuration.UpdatedApprovalConfiguration"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_registry_response.UpdateRegistryResponse":
        """<p>Updates an existing registry. This operation uses PATCH semantics, so you only need to specify the fields you want to change.</p>

        Args:
            registry_id: <p>The identifier of the registry to update. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            name: <p>The updated name of the registry.</p>
            description: <p>The updated description of the registry. To clear the description, include the <code>UpdatedDescription</code> wrapper with <code>optionalValue</code> not specified.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the registry. Changing the authorizer configuration can break existing consumers of the registry who are using the authorization type prior to the update.</p>
            approval_configuration: <p>The updated approval configuration for registry records. The updated configuration only affects new records that move to <code>PENDING_APPROVAL</code> status after the change. Existing records already in <code>PENDING_APPROVAL</code> status are not affected.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_registry_request.UpdateRegistryRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.update_registry_response.UpdateRegistryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry.update_registry(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_registry_request.UpdateRegistryRequest = {}  # type: ignore[typeddict-item]
        input["registry_id"] = registry_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if authorizer_configuration is not None:
            input["authorizer_configuration"] = authorizer_configuration
        if approval_configuration is not None:
            input["approval_configuration"] = approval_configuration

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, registry_id: "aws_sdk_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_registry_response.DeleteRegistryResponse":
        """<p>Deletes a registry. The registry must contain zero records before it can be deleted. This operation initiates the deletion process asynchronously.</p>

        Args:
            registry_id: <p>The identifier of the registry to delete. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_registry_request.DeleteRegistryRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_registry_response.DeleteRegistryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry.delete_registry(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_registry_request.DeleteRegistryRequest = {}  # type: ignore[typeddict-item]
        input["registry_id"] = registry_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, status: Optional["aws_sdk_bedrock_agentcore_control.types.registry_status.RegistryStatus"] = None, authorizer_type: Optional["aws_sdk_bedrock_agentcore_control.types.registry_authorizer_type.RegistryAuthorizerType"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_registries_response.ListRegistriesResponse":
        """<p>Lists all registries in the account. You can optionally filter results by status using the <code>status</code> parameter, or by authorizer type using the <code>authorizerType</code> parameter.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            status: <p>Filter registries by their current status. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, <code>DELETING</code>, and <code>DELETE_FAILED</code>.</p>
            authorizer_type: <p>Filter registries by their authorizer type. Possible values are <code>CUSTOM_JWT</code> and <code>AWS_IAM</code>. For more information about authorizer types, see the <code>RegistryAuthorizerType</code> enum.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_registries_request.ListRegistriesRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_registries_response.ListRegistriesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registries
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registries.list_registries(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_registries_request.ListRegistriesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if status is not None:
            input["status"] = status
        if authorizer_type is not None:
            input["authorizer_type"] = authorizer_type

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncRegistryResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service
    async def create(self, name: "aws_sdk_bedrock_agentcore_control.types.registry_name.RegistryName", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.description.Description"] = None, authorizer_type: Optional["aws_sdk_bedrock_agentcore_control.types.registry_authorizer_type.RegistryAuthorizerType"] = None, authorizer_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"] = None, client_token: Optional["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"] = None, approval_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.approval_configuration.ApprovalConfiguration"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_registry_response.CreateRegistryResponse":
        """<p>Creates a new registry in your Amazon Web Services account. A registry serves as a centralized catalog for organizing and managing registry records, including MCP servers, A2A agents, agent skills, and custom resource types.</p> <p>If you specify <code>CUSTOM_JWT</code> as the <code>authorizerType</code>, you must provide an <code>authorizerConfiguration</code>.</p>

        Args:
            name: <p>The name of the registry. The name must be unique within your account and can contain alphanumeric characters and underscores.</p>
            description: <p>A description of the registry.</p>
            authorizer_type: <p>The type of authorizer to use for the registry. This controls the authorization method for the Search and Invoke APIs used by consumers, and does not affect the standard CRUDL APIs for registry and registry record management used by administrators.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>
            authorizer_configuration: <p>The authorizer configuration for the registry. Required if <code>authorizerType</code> is <code>CUSTOM_JWT</code>. For details, see the <code>AuthorizerConfiguration</code> data type.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            approval_configuration: <p>The approval configuration for registry records. Controls whether records require explicit approval before becoming active. See the <code>ApprovalConfiguration</code> data type for supported configuration options.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_registry_request.CreateRegistryRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.create_registry_response.CreateRegistryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry.async_create_registry(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_registry_request.CreateRegistryRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if authorizer_type is not None:
            input["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input["authorizer_configuration"] = authorizer_configuration
        if client_token is not None:
            input["client_token"] = client_token
        if approval_configuration is not None:
            input["approval_configuration"] = approval_configuration

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, registry_id: "aws_sdk_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_registry_response.GetRegistryResponse":
        """<p>Retrieves information about a specific registry.</p>

        Args:
            registry_id: <p>The identifier of the registry to retrieve. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_registry_request.GetRegistryRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.get_registry_response.GetRegistryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry.async_get_registry(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_registry_request.GetRegistryRequest = {}  # type: ignore[typeddict-item]
        input["registry_id"] = registry_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, registry_id: "aws_sdk_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, name: Optional["aws_sdk_bedrock_agentcore_control.types.registry_name.RegistryName"] = None, description: Optional["aws_sdk_bedrock_agentcore_control.types.updated_description.UpdatedDescription"] = None, authorizer_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.updated_authorizer_configuration.UpdatedAuthorizerConfiguration"] = None, approval_configuration: Optional["aws_sdk_bedrock_agentcore_control.types.updated_approval_configuration.UpdatedApprovalConfiguration"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_registry_response.UpdateRegistryResponse":
        """<p>Updates an existing registry. This operation uses PATCH semantics, so you only need to specify the fields you want to change.</p>

        Args:
            registry_id: <p>The identifier of the registry to update. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            name: <p>The updated name of the registry.</p>
            description: <p>The updated description of the registry. To clear the description, include the <code>UpdatedDescription</code> wrapper with <code>optionalValue</code> not specified.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the registry. Changing the authorizer configuration can break existing consumers of the registry who are using the authorization type prior to the update.</p>
            approval_configuration: <p>The updated approval configuration for registry records. The updated configuration only affects new records that move to <code>PENDING_APPROVAL</code> status after the change. Existing records already in <code>PENDING_APPROVAL</code> status are not affected.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_registry_request.UpdateRegistryRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.update_registry_response.UpdateRegistryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry.async_update_registry(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_registry_request.UpdateRegistryRequest = {}  # type: ignore[typeddict-item]
        input["registry_id"] = registry_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if authorizer_configuration is not None:
            input["authorizer_configuration"] = authorizer_configuration
        if approval_configuration is not None:
            input["approval_configuration"] = approval_configuration

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, registry_id: "aws_sdk_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_registry_response.DeleteRegistryResponse":
        """<p>Deletes a registry. The registry must contain zero records before it can be deleted. This operation initiates the deletion process asynchronously.</p>

        Args:
            registry_id: <p>The identifier of the registry to delete. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_registry_request.DeleteRegistryRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_registry_response.DeleteRegistryResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry.async_delete_registry(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_registry_request.DeleteRegistryRequest = {}  # type: ignore[typeddict-item]
        input["registry_id"] = registry_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"] = None, status: Optional["aws_sdk_bedrock_agentcore_control.types.registry_status.RegistryStatus"] = None, authorizer_type: Optional["aws_sdk_bedrock_agentcore_control.types.registry_authorizer_type.RegistryAuthorizerType"] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_registries_response.ListRegistriesResponse":
        """<p>Lists all registries in the account. You can optionally filter results by status using the <code>status</code> parameter, or by authorizer type using the <code>authorizerType</code> parameter.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            status: <p>Filter registries by their current status. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, <code>DELETING</code>, and <code>DELETE_FAILED</code>.</p>
            authorizer_type: <p>Filter registries by their authorizer type. Possible values are <code>CUSTOM_JWT</code> and <code>AWS_IAM</code>. For more information about authorizer types, see the <code>RegistryAuthorizerType</code> enum.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_registries_request.ListRegistriesRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_registries_response.ListRegistriesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registries
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registries.async_list_registries(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_registries_request.ListRegistriesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if status is not None:
            input["status"] = status
        if authorizer_type is not None:
            input["authorizer_type"] = authorizer_type

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output