from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import ensure_async_iterator
from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import ensure_sync_iterator
from aws_sdk_bedrock_agentcore_control._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import BedrockAgentCoreControlClient, BedrockAgentCoreControlClientConfig
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import AsyncBedrockAgentCoreControlClient, AsyncBedrockAgentCoreControlClientConfig
    import aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_response
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type
    import aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response
    import aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_response
    import aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_request
    import aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_response
    import aws_sdk_bedrock_agentcore_control.types.oauth2_credential_provider_item
    import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_response

class Oauth2CredentialProvider:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service
    def put(self, name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName", credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType", oauth2_provider_config_input: "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, tags: Optional["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse":
        """<p>Creates a new OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider. The name must be unique within your account.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider. This specifies which OAuth2 implementation to use.</p>
            oauth2_provider_config_input: <p>The configuration settings for the OAuth2 provider, including client ID, client secret, and other vendor-specific settings.</p>
            tags: <p>A map of tag keys and values to assign to the OAuth2 credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider.create_oauth2_credential_provider(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["credential_provider_vendor"] = credential_provider_vendor
        input["oauth2_provider_config_input"] = oauth2_provider_config_input
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse":
        """<p>Retrieves information about an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider.get_oauth2_credential_provider(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName", credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType", oauth2_provider_config_input: "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse":
        """<p>Updates an existing OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to update.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider.</p>
            oauth2_provider_config_input: <p>The configuration input for the OAuth2 provider.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider.update_oauth2_credential_provider(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["credential_provider_vendor"] = credential_provider_vendor
        input["oauth2_provider_config_input"] = oauth2_provider_config_input

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName", *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse":
        """<p>Deletes an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider.delete_oauth2_credential_provider(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_oauth2_credential_providers(self, *, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None, next_token: Optional[str] = None, max_results: Optional[int] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse":
        """<p>Lists all OAuth2 credential providers in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers
            output, http_response = aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers.list_oauth2_credential_providers(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncOauth2CredentialProvider:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service
    async def put(self, name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName", credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType", oauth2_provider_config_input: "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, tags: Optional["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"] = None) -> "aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse":
        """<p>Creates a new OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider. The name must be unique within your account.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider. This specifies which OAuth2 implementation to use.</p>
            oauth2_provider_config_input: <p>The configuration settings for the OAuth2 provider, including client ID, client secret, and other vendor-specific settings.</p>
            tags: <p>A map of tag keys and values to assign to the OAuth2 credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider.async_create_oauth2_credential_provider(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["credential_provider_vendor"] = credential_provider_vendor
        input["oauth2_provider_config_input"] = oauth2_provider_config_input
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse":
        """<p>Retrieves information about an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider.async_get_oauth2_credential_provider(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName", credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType", oauth2_provider_config_input: "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse":
        """<p>Updates an existing OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to update.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider.</p>
            oauth2_provider_config_input: <p>The configuration input for the OAuth2 provider.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider.async_update_oauth2_credential_provider(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["credential_provider_vendor"] = credential_provider_vendor
        input["oauth2_provider_config_input"] = oauth2_provider_config_input

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName", *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None) -> "aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse":
        """<p>Deletes an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider.async_delete_oauth2_credential_provider(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_oauth2_credential_providers(self, *, config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None, next_token: Optional[str] = None, max_results: Optional[int] = None) -> "aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse":
        """<p>Lists all OAuth2 credential providers in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse"]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers
            output, http_response = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers.async_list_oauth2_credential_providers(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output