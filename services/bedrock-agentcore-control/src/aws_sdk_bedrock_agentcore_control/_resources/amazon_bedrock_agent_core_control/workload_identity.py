from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import ensure_async_iterator
from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import ensure_sync_iterator
from aws_sdk_bedrock_agentcore_control._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import BedrockAgentCoreControlClient, BedrockAgentCoreControlClientConfig
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import AsyncBedrockAgentCoreControlClient, AsyncBedrockAgentCoreControlClientConfig
    import aws_sdk_bedrock_agentcore_control.types.create_workload_identity_request
    import aws_sdk_bedrock_agentcore_control.types.create_workload_identity_response
    import aws_sdk_bedrock_agentcore_control.types.delete_workload_identity_request
    import aws_sdk_bedrock_agentcore_control.types.delete_workload_identity_response
    import aws_sdk_bedrock_agentcore_control.types.get_workload_identity_request
    import aws_sdk_bedrock_agentcore_control.types.get_workload_identity_response
    import aws_sdk_bedrock_agentcore_control.types.list_workload_identities_request
    import aws_sdk_bedrock_agentcore_control.types.list_workload_identities_response
    import aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.update_workload_identity_request
    import aws_sdk_bedrock_agentcore_control.types.update_workload_identity_response
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_type

class WorkloadIdentity:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service
    def put(self, name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, allowed_resource_oauth2_return_urls: Optional["aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.ResourceOauth2ReturnUrlListType"] = None, tags: Optional["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_workload_identity_response.CreateWorkloadIdentityResponse":
        """<p>Creates a new workload identity.</p>

        Args:
            name: <p>The name of the workload identity. The name must be unique within your account.</p>
            allowed_resource_oauth2_return_urls: <p>The list of allowed OAuth2 return URLs for resources associated with this workload identity.</p>
            tags: <p>A map of tag keys and values to assign to the workload identity. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_workload_identity_request.CreateWorkloadIdentityRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.create_workload_identity_response.CreateWorkloadIdentityResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_workload_identity
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_workload_identity.create_workload_identity(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_workload_identity_request.CreateWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if allowed_resource_oauth2_return_urls is not None:
            input["allowed_resource_oauth2_return_urls"] = allowed_resource_oauth2_return_urls
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_workload_identity_response.GetWorkloadIdentityResponse":
        """<p>Retrieves information about a workload identity.</p>

        Args:
            name: <p>The name of the workload identity to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_workload_identity_request.GetWorkloadIdentityRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.get_workload_identity_response.GetWorkloadIdentityResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_workload_identity
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_workload_identity.get_workload_identity(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_workload_identity_request.GetWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, allowed_resource_oauth2_return_urls: Optional["aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.ResourceOauth2ReturnUrlListType"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_workload_identity_response.UpdateWorkloadIdentityResponse":
        """<p>Updates an existing workload identity.</p>

        Args:
            name: <p>The name of the workload identity to update.</p>
            allowed_resource_oauth2_return_urls: <p>The new list of allowed OAuth2 return URLs for resources associated with this workload identity. This list replaces the existing list.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_workload_identity_request.UpdateWorkloadIdentityRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.update_workload_identity_response.UpdateWorkloadIdentityResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_workload_identity
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_workload_identity.update_workload_identity(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_workload_identity_request.UpdateWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if allowed_resource_oauth2_return_urls is not None:
            input["allowed_resource_oauth2_return_urls"] = allowed_resource_oauth2_return_urls

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_workload_identity_response.DeleteWorkloadIdentityResponse":
        """<p>Deletes a workload identity.</p>

        Args:
            name: <p>The name of the workload identity to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_workload_identity_request.DeleteWorkloadIdentityRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_workload_identity_response.DeleteWorkloadIdentityResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_workload_identity
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_workload_identity.delete_workload_identity(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_workload_identity_request.DeleteWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_workload_identities(self, *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, next_token: Optional[str] = None, max_results: Optional[int] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_workload_identities_response.ListWorkloadIdentitiesResponse":
        """<p>Lists all workload identities in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_workload_identities_request.ListWorkloadIdentitiesRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_workload_identities_response.ListWorkloadIdentitiesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_workload_identities
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_workload_identities.list_workload_identities(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_workload_identities_request.ListWorkloadIdentitiesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncWorkloadIdentity:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service
    async def put(self, name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, allowed_resource_oauth2_return_urls: Optional["aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.ResourceOauth2ReturnUrlListType"] = None, tags: Optional["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_workload_identity_response.CreateWorkloadIdentityResponse":
        """<p>Creates a new workload identity.</p>

        Args:
            name: <p>The name of the workload identity. The name must be unique within your account.</p>
            allowed_resource_oauth2_return_urls: <p>The list of allowed OAuth2 return URLs for resources associated with this workload identity.</p>
            tags: <p>A map of tag keys and values to assign to the workload identity. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_workload_identity_request.CreateWorkloadIdentityRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.create_workload_identity_response.CreateWorkloadIdentityResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_workload_identity
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_workload_identity.async_create_workload_identity(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_workload_identity_request.CreateWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if allowed_resource_oauth2_return_urls is not None:
            input["allowed_resource_oauth2_return_urls"] = allowed_resource_oauth2_return_urls
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_workload_identity_response.GetWorkloadIdentityResponse":
        """<p>Retrieves information about a workload identity.</p>

        Args:
            name: <p>The name of the workload identity to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_workload_identity_request.GetWorkloadIdentityRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.get_workload_identity_response.GetWorkloadIdentityResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_workload_identity
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_workload_identity.async_get_workload_identity(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_workload_identity_request.GetWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, allowed_resource_oauth2_return_urls: Optional["aws_sdk_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.ResourceOauth2ReturnUrlListType"] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_workload_identity_response.UpdateWorkloadIdentityResponse":
        """<p>Updates an existing workload identity.</p>

        Args:
            name: <p>The name of the workload identity to update.</p>
            allowed_resource_oauth2_return_urls: <p>The new list of allowed OAuth2 return URLs for resources associated with this workload identity. This list replaces the existing list.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_workload_identity_request.UpdateWorkloadIdentityRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.update_workload_identity_response.UpdateWorkloadIdentityResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_workload_identity
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_workload_identity.async_update_workload_identity(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_workload_identity_request.UpdateWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if allowed_resource_oauth2_return_urls is not None:
            input["allowed_resource_oauth2_return_urls"] = allowed_resource_oauth2_return_urls

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, name: "aws_sdk_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_workload_identity_response.DeleteWorkloadIdentityResponse":
        """<p>Deletes a workload identity.</p>

        Args:
            name: <p>The name of the workload identity to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_workload_identity_request.DeleteWorkloadIdentityRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_workload_identity_response.DeleteWorkloadIdentityResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_workload_identity
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_workload_identity.async_delete_workload_identity(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_workload_identity_request.DeleteWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_workload_identities(self, *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, next_token: Optional[str] = None, max_results: Optional[int] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_workload_identities_response.ListWorkloadIdentitiesResponse":
        """<p>Lists all workload identities in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_workload_identities_request.ListWorkloadIdentitiesRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_workload_identities_response.ListWorkloadIdentitiesResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_workload_identities
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_workload_identities.async_list_workload_identities(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_workload_identities_request.ListWorkloadIdentitiesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output