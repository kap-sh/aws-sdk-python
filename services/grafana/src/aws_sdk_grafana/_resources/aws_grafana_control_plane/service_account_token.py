from typing import Optional, TYPE_CHECKING
from aws_sdk_grafana._services.async_grafana import ensure_async_iterator
from aws_sdk_grafana._services.grafana import ensure_sync_iterator
from aws_sdk_grafana._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_grafana._auth._signers
import aws_sdk_grafana._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_grafana._services.grafana import grafanaClient, grafanaClientConfig
    from aws_sdk_grafana._services.async_grafana import AsyncgrafanaClient, AsyncgrafanaClientConfig
    import aws_sdk_grafana.types.create_workspace_service_account_token_request
    import aws_sdk_grafana.types.create_workspace_service_account_token_response
    import aws_sdk_grafana.types.delete_workspace_service_account_token_request
    import aws_sdk_grafana.types.delete_workspace_service_account_token_response
    import aws_sdk_grafana.types.list_workspace_service_account_tokens_request
    import aws_sdk_grafana.types.list_workspace_service_account_tokens_response
    import aws_sdk_grafana.types.pagination_token
    import aws_sdk_grafana.types.service_account_token_name
    import aws_sdk_grafana.types.service_account_token_summary
    import aws_sdk_grafana.types.workspace_id

class ServiceAccountToken:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service
    def create_workspace_service_account_token(self, name: "aws_sdk_grafana.types.service_account_token_name.ServiceAccountTokenName", seconds_to_live: int, service_account_id: str, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[grafanaClientConfig] = None) -> "aws_sdk_grafana.types.create_workspace_service_account_token_response.CreateWorkspaceServiceAccountTokenResponse":
        """<p>Creates a token that can be used to authenticate and authorize Grafana HTTP API operations for the given <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html\">workspace service account</a>. The service account acts as a user for the API operations, and defines the permissions that are used by the API.</p> <important> <p>When you create the service account token, you will receive a key that is used when calling Grafana APIs. Do not lose this key, as it will not be retrievable again.</p> <p>If you do lose the key, you can delete the token and recreate it to receive a new key. This will disable the initial key.</p> </important> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            name: <p>A name for the token to create.</p>
            seconds_to_live: <p>Sets how long the token will be valid, in seconds. You can set the time up to 30 days in the future.</p>
            service_account_id: <p>The ID of the service account for which to create a token.</p>
            workspace_id: <p>The ID of the workspace the service account resides within.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_grafana.types.create_workspace_service_account_token_request.CreateWorkspaceServiceAccountTokenRequest]') -> OperationResponse["aws_sdk_grafana.types.create_workspace_service_account_token_response.CreateWorkspaceServiceAccountTokenResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_service_account_token
            output, http_response = aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_service_account_token.create_workspace_service_account_token(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.create_workspace_service_account_token_request.CreateWorkspaceServiceAccountTokenRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["seconds_to_live"] = seconds_to_live
        input["service_account_id"] = service_account_id
        input["workspace_id"] = workspace_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete_workspace_service_account_token(self, token_id: str, service_account_id: str, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[grafanaClientConfig] = None) -> "aws_sdk_grafana.types.delete_workspace_service_account_token_response.DeleteWorkspaceServiceAccountTokenResponse":
        """<p>Deletes a token for the workspace service account.</p> <p>This will disable the key associated with the token. If any automation is currently using the key, it will no longer be authenticated or authorized to perform actions with the Grafana HTTP APIs.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            token_id: <p>The ID of the token to delete.</p>
            service_account_id: <p>The ID of the service account from which to delete the token.</p>
            workspace_id: <p>The ID of the workspace from which to delete the token.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_grafana.types.delete_workspace_service_account_token_request.DeleteWorkspaceServiceAccountTokenRequest]') -> OperationResponse["aws_sdk_grafana.types.delete_workspace_service_account_token_response.DeleteWorkspaceServiceAccountTokenResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account_token
            output, http_response = aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account_token.delete_workspace_service_account_token(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.delete_workspace_service_account_token_request.DeleteWorkspaceServiceAccountTokenRequest = {}  # type: ignore[typeddict-item]
        input["token_id"] = token_id
        input["service_account_id"] = service_account_id
        input["workspace_id"] = workspace_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_workspace_service_account_tokens(self, service_account_id: str, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[grafanaClientConfig] = None, max_results: Optional[int] = None, next_token: Optional["aws_sdk_grafana.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_grafana.types.list_workspace_service_account_tokens_response.ListWorkspaceServiceAccountTokensResponse":
        """<p>Returns a list of tokens for a workspace service account.</p> <note> <p>This does not return the key for each token. You cannot access keys after they are created. To create a new key, delete the token and recreate it.</p> </note> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            max_results: <p>The maximum number of tokens to include in the results.</p>
            next_token: <p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccountTokens</code> operation.)</p>
            service_account_id: <p>The ID of the service account for which to return tokens.</p>
            workspace_id: <p>The ID of the workspace for which to return tokens.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_grafana.types.list_workspace_service_account_tokens_request.ListWorkspaceServiceAccountTokensRequest]') -> OperationResponse["aws_sdk_grafana.types.list_workspace_service_account_tokens_response.ListWorkspaceServiceAccountTokensResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspace_service_account_tokens
            output, http_response = aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspace_service_account_tokens.list_workspace_service_account_tokens(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.list_workspace_service_account_tokens_request.ListWorkspaceServiceAccountTokensRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["service_account_id"] = service_account_id
        input["workspace_id"] = workspace_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncServiceAccountToken:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service
    async def create_workspace_service_account_token(self, name: "aws_sdk_grafana.types.service_account_token_name.ServiceAccountTokenName", seconds_to_live: int, service_account_id: str, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[AsyncgrafanaClientConfig] = None) -> "aws_sdk_grafana.types.create_workspace_service_account_token_response.CreateWorkspaceServiceAccountTokenResponse":
        """<p>Creates a token that can be used to authenticate and authorize Grafana HTTP API operations for the given <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html\">workspace service account</a>. The service account acts as a user for the API operations, and defines the permissions that are used by the API.</p> <important> <p>When you create the service account token, you will receive a key that is used when calling Grafana APIs. Do not lose this key, as it will not be retrievable again.</p> <p>If you do lose the key, you can delete the token and recreate it to receive a new key. This will disable the initial key.</p> </important> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            name: <p>A name for the token to create.</p>
            seconds_to_live: <p>Sets how long the token will be valid, in seconds. You can set the time up to 30 days in the future.</p>
            service_account_id: <p>The ID of the service account for which to create a token.</p>
            workspace_id: <p>The ID of the workspace the service account resides within.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_grafana.types.create_workspace_service_account_token_request.CreateWorkspaceServiceAccountTokenRequest]') -> AsyncOperationResponse["aws_sdk_grafana.types.create_workspace_service_account_token_response.CreateWorkspaceServiceAccountTokenResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_service_account_token
            output, http_response = await aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_service_account_token.async_create_workspace_service_account_token(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.create_workspace_service_account_token_request.CreateWorkspaceServiceAccountTokenRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["seconds_to_live"] = seconds_to_live
        input["service_account_id"] = service_account_id
        input["workspace_id"] = workspace_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete_workspace_service_account_token(self, token_id: str, service_account_id: str, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[AsyncgrafanaClientConfig] = None) -> "aws_sdk_grafana.types.delete_workspace_service_account_token_response.DeleteWorkspaceServiceAccountTokenResponse":
        """<p>Deletes a token for the workspace service account.</p> <p>This will disable the key associated with the token. If any automation is currently using the key, it will no longer be authenticated or authorized to perform actions with the Grafana HTTP APIs.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            token_id: <p>The ID of the token to delete.</p>
            service_account_id: <p>The ID of the service account from which to delete the token.</p>
            workspace_id: <p>The ID of the workspace from which to delete the token.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_grafana.types.delete_workspace_service_account_token_request.DeleteWorkspaceServiceAccountTokenRequest]') -> AsyncOperationResponse["aws_sdk_grafana.types.delete_workspace_service_account_token_response.DeleteWorkspaceServiceAccountTokenResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account_token
            output, http_response = await aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account_token.async_delete_workspace_service_account_token(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.delete_workspace_service_account_token_request.DeleteWorkspaceServiceAccountTokenRequest = {}  # type: ignore[typeddict-item]
        input["token_id"] = token_id
        input["service_account_id"] = service_account_id
        input["workspace_id"] = workspace_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_workspace_service_account_tokens(self, service_account_id: str, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[AsyncgrafanaClientConfig] = None, max_results: Optional[int] = None, next_token: Optional["aws_sdk_grafana.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_grafana.types.list_workspace_service_account_tokens_response.ListWorkspaceServiceAccountTokensResponse":
        """<p>Returns a list of tokens for a workspace service account.</p> <note> <p>This does not return the key for each token. You cannot access keys after they are created. To create a new key, delete the token and recreate it.</p> </note> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            max_results: <p>The maximum number of tokens to include in the results.</p>
            next_token: <p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccountTokens</code> operation.)</p>
            service_account_id: <p>The ID of the service account for which to return tokens.</p>
            workspace_id: <p>The ID of the workspace for which to return tokens.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_grafana.types.list_workspace_service_account_tokens_request.ListWorkspaceServiceAccountTokensRequest]') -> AsyncOperationResponse["aws_sdk_grafana.types.list_workspace_service_account_tokens_response.ListWorkspaceServiceAccountTokensResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspace_service_account_tokens
            output, http_response = await aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspace_service_account_tokens.async_list_workspace_service_account_tokens(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.list_workspace_service_account_tokens_request.ListWorkspaceServiceAccountTokensRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["service_account_id"] = service_account_id
        input["workspace_id"] = workspace_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output