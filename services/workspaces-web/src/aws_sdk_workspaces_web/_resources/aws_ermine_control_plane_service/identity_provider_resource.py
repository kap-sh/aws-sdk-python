from typing import Optional, TYPE_CHECKING
from aws_sdk_workspaces_web._services.async_work_spaces_web import ensure_async_iterator
from aws_sdk_workspaces_web._services.work_spaces_web import ensure_sync_iterator
from aws_sdk_workspaces_web._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_workspaces_web._auth._signers
import aws_sdk_workspaces_web._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_workspaces_web._services.work_spaces_web import WorkSpacesWebClient, WorkSpacesWebClientConfig
    from aws_sdk_workspaces_web._services.async_work_spaces_web import AsyncWorkSpacesWebClient, AsyncWorkSpacesWebClientConfig
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.client_token
    import aws_sdk_workspaces_web.types.create_identity_provider_request
    import aws_sdk_workspaces_web.types.create_identity_provider_response
    import aws_sdk_workspaces_web.types.delete_identity_provider_request
    import aws_sdk_workspaces_web.types.delete_identity_provider_response
    import aws_sdk_workspaces_web.types.get_identity_provider_request
    import aws_sdk_workspaces_web.types.get_identity_provider_response
    import aws_sdk_workspaces_web.types.identity_provider_details
    import aws_sdk_workspaces_web.types.identity_provider_name
    import aws_sdk_workspaces_web.types.identity_provider_type
    import aws_sdk_workspaces_web.types.list_identity_providers_request
    import aws_sdk_workspaces_web.types.list_identity_providers_response
    import aws_sdk_workspaces_web.types.max_results
    import aws_sdk_workspaces_web.types.pagination_token
    import aws_sdk_workspaces_web.types.subresource_arn
    import aws_sdk_workspaces_web.types.tag_list
    import aws_sdk_workspaces_web.types.update_identity_provider_request
    import aws_sdk_workspaces_web.types.update_identity_provider_response

class IdentityProviderResource:
    def __init__(self, service: WorkSpacesWebClient) -> None:
        self._service = service
    def create(self, portal_arn: "aws_sdk_workspaces_web.types.arn.ARN", identity_provider_name: "aws_sdk_workspaces_web.types.identity_provider_name.IdentityProviderName", identity_provider_type: "aws_sdk_workspaces_web.types.identity_provider_type.IdentityProviderType", identity_provider_details: "aws_sdk_workspaces_web.types.identity_provider_details.IdentityProviderDetails", *, config_overrides: Optional[WorkSpacesWebClientConfig] = None, client_token: Optional["aws_sdk_workspaces_web.types.client_token.ClientToken"] = None, tags: Optional["aws_sdk_workspaces_web.types.tag_list.TagList"] = None) -> "aws_sdk_workspaces_web.types.create_identity_provider_response.CreateIdentityProviderResponse":
        """<p>Creates an identity provider resource that is then associated with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            identity_provider_name: <p>The identity provider name.</p>
            identity_provider_type: <p>The identity provider type.</p>
            identity_provider_details: <p>The identity provider details. The following list describes the provider detail keys for each identity provider type. </p> <ul> <li> <p>For Google and Login with Amazon:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For Facebook:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>api_version</code> </p> </li> </ul> </li> <li> <p>For Sign in with Apple:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>team_id</code> </p> </li> <li> <p> <code>key_id</code> </p> </li> <li> <p> <code>private_key</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For OIDC providers:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>attributes_request_method</code> </p> </li> <li> <p> <code>oidc_issuer</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>authorize_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>token_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>attributes_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>jwks_uri</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> </ul> </li> <li> <p>For SAML providers:</p> <ul> <li> <p> <code>MetadataFile</code> OR <code>MetadataURL</code> </p> </li> <li> <p> <code>IDPSignout</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>IDPInit</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>RequestSigningAlgorithm</code> (string) <i>optional</i> - Only accepts <code>rsa-sha256</code> </p> </li> <li> <p> <code>EncryptedResponses</code> (boolean) <i>optional</i> </p> </li> </ul> </li> </ul>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request.</p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            tags: <p>The tags to add to the identity provider resource. A tag is a key-value pair.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_workspaces_web.types.create_identity_provider_request.CreateIdentityProviderRequest]') -> OperationResponse["aws_sdk_workspaces_web.types.create_identity_provider_response.CreateIdentityProviderResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.create_identity_provider
            output, http_response = aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.create_identity_provider.create_identity_provider(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.create_identity_provider_request.CreateIdentityProviderRequest = {}  # type: ignore[typeddict-item]
        input["portal_arn"] = portal_arn
        input["identity_provider_name"] = identity_provider_name
        input["identity_provider_type"] = identity_provider_type
        input["identity_provider_details"] = identity_provider_details
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, identity_provider_arn: "aws_sdk_workspaces_web.types.subresource_arn.SubresourceARN", *, config_overrides: Optional[WorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.get_identity_provider_response.GetIdentityProviderResponse":
        """<p>Gets the identity provider.</p>

        Args:
            identity_provider_arn: <p>The ARN of the identity provider.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_workspaces_web.types.get_identity_provider_request.GetIdentityProviderRequest]') -> OperationResponse["aws_sdk_workspaces_web.types.get_identity_provider_response.GetIdentityProviderResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_identity_provider
            output, http_response = aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_identity_provider.get_identity_provider(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.get_identity_provider_request.GetIdentityProviderRequest = {}  # type: ignore[typeddict-item]
        input["identity_provider_arn"] = identity_provider_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, identity_provider_arn: "aws_sdk_workspaces_web.types.subresource_arn.SubresourceARN", *, config_overrides: Optional[WorkSpacesWebClientConfig] = None, identity_provider_name: Optional["aws_sdk_workspaces_web.types.identity_provider_name.IdentityProviderName"] = None, identity_provider_type: Optional["aws_sdk_workspaces_web.types.identity_provider_type.IdentityProviderType"] = None, identity_provider_details: Optional["aws_sdk_workspaces_web.types.identity_provider_details.IdentityProviderDetails"] = None, client_token: Optional["aws_sdk_workspaces_web.types.client_token.ClientToken"] = None) -> "aws_sdk_workspaces_web.types.update_identity_provider_response.UpdateIdentityProviderResponse":
        """<p>Updates the identity provider. </p>

        Args:
            identity_provider_arn: <p>The ARN of the identity provider.</p>
            identity_provider_name: <p>The name of the identity provider.</p>
            identity_provider_type: <p>The type of the identity provider.</p>
            identity_provider_details: <p>The details of the identity provider. The following list describes the provider detail keys for each identity provider type. </p> <ul> <li> <p>For Google and Login with Amazon:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For Facebook:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>api_version</code> </p> </li> </ul> </li> <li> <p>For Sign in with Apple:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>team_id</code> </p> </li> <li> <p> <code>key_id</code> </p> </li> <li> <p> <code>private_key</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For OIDC providers:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>attributes_request_method</code> </p> </li> <li> <p> <code>oidc_issuer</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>authorize_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>token_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>attributes_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>jwks_uri</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> </ul> </li> <li> <p>For SAML providers:</p> <ul> <li> <p> <code>MetadataFile</code> OR <code>MetadataURL</code> </p> </li> <li> <p> <code>IDPSignout</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>IDPInit</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>RequestSigningAlgorithm</code> (string) <i>optional</i> - Only accepts <code>rsa-sha256</code> </p> </li> <li> <p> <code>EncryptedResponses</code> (boolean) <i>optional</i> </p> </li> </ul> </li> </ul>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_workspaces_web.types.update_identity_provider_request.UpdateIdentityProviderRequest]') -> OperationResponse["aws_sdk_workspaces_web.types.update_identity_provider_response.UpdateIdentityProviderResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.update_identity_provider
            output, http_response = aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.update_identity_provider.update_identity_provider(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.update_identity_provider_request.UpdateIdentityProviderRequest = {}  # type: ignore[typeddict-item]
        input["identity_provider_arn"] = identity_provider_arn
        if identity_provider_name is not None:
            input["identity_provider_name"] = identity_provider_name
        if identity_provider_type is not None:
            input["identity_provider_type"] = identity_provider_type
        if identity_provider_details is not None:
            input["identity_provider_details"] = identity_provider_details
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, identity_provider_arn: "aws_sdk_workspaces_web.types.subresource_arn.SubresourceARN", *, config_overrides: Optional[WorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.delete_identity_provider_response.DeleteIdentityProviderResponse":
        """<p>Deletes the identity provider.</p>

        Args:
            identity_provider_arn: <p>The ARN of the identity provider.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_workspaces_web.types.delete_identity_provider_request.DeleteIdentityProviderRequest]') -> OperationResponse["aws_sdk_workspaces_web.types.delete_identity_provider_response.DeleteIdentityProviderResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.delete_identity_provider
            output, http_response = aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.delete_identity_provider.delete_identity_provider(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.delete_identity_provider_request.DeleteIdentityProviderRequest = {}  # type: ignore[typeddict-item]
        input["identity_provider_arn"] = identity_provider_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, portal_arn: "aws_sdk_workspaces_web.types.arn.ARN", *, config_overrides: Optional[WorkSpacesWebClientConfig] = None, next_token: Optional["aws_sdk_workspaces_web.types.pagination_token.PaginationToken"] = None, max_results: Optional["aws_sdk_workspaces_web.types.max_results.MaxResults"] = None) -> "aws_sdk_workspaces_web.types.list_identity_providers_response.ListIdentityProvidersResponse":
        """<p>Retrieves a list of identity providers for a specific web portal.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>
            portal_arn: <p>The ARN of the web portal.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_workspaces_web.types.list_identity_providers_request.ListIdentityProvidersRequest]') -> OperationResponse["aws_sdk_workspaces_web.types.list_identity_providers_response.ListIdentityProvidersResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_identity_providers
            output, http_response = aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_identity_providers.list_identity_providers(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.list_identity_providers_request.ListIdentityProvidersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["portal_arn"] = portal_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncIdentityProviderResource:
    def __init__(self, service: AsyncWorkSpacesWebClient) -> None:
        self._service = service
    async def create(self, portal_arn: "aws_sdk_workspaces_web.types.arn.ARN", identity_provider_name: "aws_sdk_workspaces_web.types.identity_provider_name.IdentityProviderName", identity_provider_type: "aws_sdk_workspaces_web.types.identity_provider_type.IdentityProviderType", identity_provider_details: "aws_sdk_workspaces_web.types.identity_provider_details.IdentityProviderDetails", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None, client_token: Optional["aws_sdk_workspaces_web.types.client_token.ClientToken"] = None, tags: Optional["aws_sdk_workspaces_web.types.tag_list.TagList"] = None) -> "aws_sdk_workspaces_web.types.create_identity_provider_response.CreateIdentityProviderResponse":
        """<p>Creates an identity provider resource that is then associated with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            identity_provider_name: <p>The identity provider name.</p>
            identity_provider_type: <p>The identity provider type.</p>
            identity_provider_details: <p>The identity provider details. The following list describes the provider detail keys for each identity provider type. </p> <ul> <li> <p>For Google and Login with Amazon:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For Facebook:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>api_version</code> </p> </li> </ul> </li> <li> <p>For Sign in with Apple:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>team_id</code> </p> </li> <li> <p> <code>key_id</code> </p> </li> <li> <p> <code>private_key</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For OIDC providers:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>attributes_request_method</code> </p> </li> <li> <p> <code>oidc_issuer</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>authorize_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>token_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>attributes_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>jwks_uri</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> </ul> </li> <li> <p>For SAML providers:</p> <ul> <li> <p> <code>MetadataFile</code> OR <code>MetadataURL</code> </p> </li> <li> <p> <code>IDPSignout</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>IDPInit</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>RequestSigningAlgorithm</code> (string) <i>optional</i> - Only accepts <code>rsa-sha256</code> </p> </li> <li> <p> <code>EncryptedResponses</code> (boolean) <i>optional</i> </p> </li> </ul> </li> </ul>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request.</p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            tags: <p>The tags to add to the identity provider resource. A tag is a key-value pair.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.create_identity_provider_request.CreateIdentityProviderRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.create_identity_provider_response.CreateIdentityProviderResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.create_identity_provider
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.create_identity_provider.async_create_identity_provider(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.create_identity_provider_request.CreateIdentityProviderRequest = {}  # type: ignore[typeddict-item]
        input["portal_arn"] = portal_arn
        input["identity_provider_name"] = identity_provider_name
        input["identity_provider_type"] = identity_provider_type
        input["identity_provider_details"] = identity_provider_details
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, identity_provider_arn: "aws_sdk_workspaces_web.types.subresource_arn.SubresourceARN", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.get_identity_provider_response.GetIdentityProviderResponse":
        """<p>Gets the identity provider.</p>

        Args:
            identity_provider_arn: <p>The ARN of the identity provider.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.get_identity_provider_request.GetIdentityProviderRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.get_identity_provider_response.GetIdentityProviderResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_identity_provider
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_identity_provider.async_get_identity_provider(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.get_identity_provider_request.GetIdentityProviderRequest = {}  # type: ignore[typeddict-item]
        input["identity_provider_arn"] = identity_provider_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, identity_provider_arn: "aws_sdk_workspaces_web.types.subresource_arn.SubresourceARN", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None, identity_provider_name: Optional["aws_sdk_workspaces_web.types.identity_provider_name.IdentityProviderName"] = None, identity_provider_type: Optional["aws_sdk_workspaces_web.types.identity_provider_type.IdentityProviderType"] = None, identity_provider_details: Optional["aws_sdk_workspaces_web.types.identity_provider_details.IdentityProviderDetails"] = None, client_token: Optional["aws_sdk_workspaces_web.types.client_token.ClientToken"] = None) -> "aws_sdk_workspaces_web.types.update_identity_provider_response.UpdateIdentityProviderResponse":
        """<p>Updates the identity provider. </p>

        Args:
            identity_provider_arn: <p>The ARN of the identity provider.</p>
            identity_provider_name: <p>The name of the identity provider.</p>
            identity_provider_type: <p>The type of the identity provider.</p>
            identity_provider_details: <p>The details of the identity provider. The following list describes the provider detail keys for each identity provider type. </p> <ul> <li> <p>For Google and Login with Amazon:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For Facebook:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>api_version</code> </p> </li> </ul> </li> <li> <p>For Sign in with Apple:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>team_id</code> </p> </li> <li> <p> <code>key_id</code> </p> </li> <li> <p> <code>private_key</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For OIDC providers:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>attributes_request_method</code> </p> </li> <li> <p> <code>oidc_issuer</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>authorize_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>token_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>attributes_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>jwks_uri</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> </ul> </li> <li> <p>For SAML providers:</p> <ul> <li> <p> <code>MetadataFile</code> OR <code>MetadataURL</code> </p> </li> <li> <p> <code>IDPSignout</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>IDPInit</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>RequestSigningAlgorithm</code> (string) <i>optional</i> - Only accepts <code>rsa-sha256</code> </p> </li> <li> <p> <code>EncryptedResponses</code> (boolean) <i>optional</i> </p> </li> </ul> </li> </ul>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.update_identity_provider_request.UpdateIdentityProviderRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.update_identity_provider_response.UpdateIdentityProviderResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.update_identity_provider
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.update_identity_provider.async_update_identity_provider(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.update_identity_provider_request.UpdateIdentityProviderRequest = {}  # type: ignore[typeddict-item]
        input["identity_provider_arn"] = identity_provider_arn
        if identity_provider_name is not None:
            input["identity_provider_name"] = identity_provider_name
        if identity_provider_type is not None:
            input["identity_provider_type"] = identity_provider_type
        if identity_provider_details is not None:
            input["identity_provider_details"] = identity_provider_details
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, identity_provider_arn: "aws_sdk_workspaces_web.types.subresource_arn.SubresourceARN", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.delete_identity_provider_response.DeleteIdentityProviderResponse":
        """<p>Deletes the identity provider.</p>

        Args:
            identity_provider_arn: <p>The ARN of the identity provider.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.delete_identity_provider_request.DeleteIdentityProviderRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.delete_identity_provider_response.DeleteIdentityProviderResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.delete_identity_provider
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.delete_identity_provider.async_delete_identity_provider(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.delete_identity_provider_request.DeleteIdentityProviderRequest = {}  # type: ignore[typeddict-item]
        input["identity_provider_arn"] = identity_provider_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, portal_arn: "aws_sdk_workspaces_web.types.arn.ARN", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None, next_token: Optional["aws_sdk_workspaces_web.types.pagination_token.PaginationToken"] = None, max_results: Optional["aws_sdk_workspaces_web.types.max_results.MaxResults"] = None) -> "aws_sdk_workspaces_web.types.list_identity_providers_response.ListIdentityProvidersResponse":
        """<p>Retrieves a list of identity providers for a specific web portal.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>
            portal_arn: <p>The ARN of the web portal.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.list_identity_providers_request.ListIdentityProvidersRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.list_identity_providers_response.ListIdentityProvidersResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_identity_providers
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_identity_providers.async_list_identity_providers(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.list_identity_providers_request.ListIdentityProvidersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["portal_arn"] = portal_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output