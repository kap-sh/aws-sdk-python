from typing import Optional, TYPE_CHECKING
from aws_sdk_grafana._services.async_grafana import ensure_async_iterator
from aws_sdk_grafana._services.grafana import ensure_sync_iterator
from aws_sdk_grafana._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_grafana._auth._signers
import aws_sdk_grafana._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_grafana._services.grafana import grafanaClient, grafanaClientConfig
    from aws_sdk_grafana._services.async_grafana import AsyncgrafanaClient, AsyncgrafanaClientConfig
    import aws_sdk_grafana.types.api_key_name
    import aws_sdk_grafana.types.create_workspace_api_key_request
    import aws_sdk_grafana.types.create_workspace_api_key_response
    import aws_sdk_grafana.types.delete_workspace_api_key_request
    import aws_sdk_grafana.types.delete_workspace_api_key_response
    import aws_sdk_grafana.types.workspace_id

class ApiKey:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service
    def create_workspace_api_key(self, key_name: "aws_sdk_grafana.types.api_key_name.ApiKeyName", key_role: str, seconds_to_live: int, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[grafanaClientConfig] = None) -> "aws_sdk_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse":
        """<p>Creates a Grafana API key for the workspace. This key can be used to authenticate requests sent to the workspace's HTTP API. See <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html\">https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html</a> for available APIs and example requests.</p> <note> <p>In workspaces compatible with Grafana version 9 or above, use workspace service accounts instead of API keys. API keys will be removed in a future release.</p> </note>

        Args:
            key_name: <p>Specifies the name of the key. Keynames must be unique to the workspace.</p>
            key_role: <p>Specifies the permission level of the key.</p> <p> Valid values: <code>ADMIN</code>|<code>EDITOR</code>|<code>VIEWER</code> </p>
            seconds_to_live: <p>Specifies the time in seconds until the key expires. Keys can be valid for up to 30 days.</p>
            workspace_id: <p>The ID of the workspace to create an API key.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_grafana.types.create_workspace_api_key_request.CreateWorkspaceApiKeyRequest]') -> OperationResponse["aws_sdk_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_api_key
            output, http_response = aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_api_key.create_workspace_api_key(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.create_workspace_api_key_request.CreateWorkspaceApiKeyRequest = {}  # type: ignore[typeddict-item]
        input["key_name"] = key_name
        input["key_role"] = key_role
        input["seconds_to_live"] = seconds_to_live
        input["workspace_id"] = workspace_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete_workspace_api_key(self, key_name: "aws_sdk_grafana.types.api_key_name.ApiKeyName", workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[grafanaClientConfig] = None) -> "aws_sdk_grafana.types.delete_workspace_api_key_response.DeleteWorkspaceApiKeyResponse":
        """<p>Deletes a Grafana API key for the workspace.</p> <note> <p>In workspaces compatible with Grafana version 9 or above, use workspace service accounts instead of API keys. API keys will be removed in a future release.</p> </note>

        Args:
            key_name: <p>The name of the API key to delete.</p>
            workspace_id: <p>The ID of the workspace to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_grafana.types.delete_workspace_api_key_request.DeleteWorkspaceApiKeyRequest]') -> OperationResponse["aws_sdk_grafana.types.delete_workspace_api_key_response.DeleteWorkspaceApiKeyResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_api_key
            output, http_response = aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_api_key.delete_workspace_api_key(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.delete_workspace_api_key_request.DeleteWorkspaceApiKeyRequest = {}  # type: ignore[typeddict-item]
        input["key_name"] = key_name
        input["workspace_id"] = workspace_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncApiKey:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service
    async def create_workspace_api_key(self, key_name: "aws_sdk_grafana.types.api_key_name.ApiKeyName", key_role: str, seconds_to_live: int, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[AsyncgrafanaClientConfig] = None) -> "aws_sdk_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse":
        """<p>Creates a Grafana API key for the workspace. This key can be used to authenticate requests sent to the workspace's HTTP API. See <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html\">https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html</a> for available APIs and example requests.</p> <note> <p>In workspaces compatible with Grafana version 9 or above, use workspace service accounts instead of API keys. API keys will be removed in a future release.</p> </note>

        Args:
            key_name: <p>Specifies the name of the key. Keynames must be unique to the workspace.</p>
            key_role: <p>Specifies the permission level of the key.</p> <p> Valid values: <code>ADMIN</code>|<code>EDITOR</code>|<code>VIEWER</code> </p>
            seconds_to_live: <p>Specifies the time in seconds until the key expires. Keys can be valid for up to 30 days.</p>
            workspace_id: <p>The ID of the workspace to create an API key.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_grafana.types.create_workspace_api_key_request.CreateWorkspaceApiKeyRequest]') -> AsyncOperationResponse["aws_sdk_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_api_key
            output, http_response = await aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_api_key.async_create_workspace_api_key(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.create_workspace_api_key_request.CreateWorkspaceApiKeyRequest = {}  # type: ignore[typeddict-item]
        input["key_name"] = key_name
        input["key_role"] = key_role
        input["seconds_to_live"] = seconds_to_live
        input["workspace_id"] = workspace_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete_workspace_api_key(self, key_name: "aws_sdk_grafana.types.api_key_name.ApiKeyName", workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[AsyncgrafanaClientConfig] = None) -> "aws_sdk_grafana.types.delete_workspace_api_key_response.DeleteWorkspaceApiKeyResponse":
        """<p>Deletes a Grafana API key for the workspace.</p> <note> <p>In workspaces compatible with Grafana version 9 or above, use workspace service accounts instead of API keys. API keys will be removed in a future release.</p> </note>

        Args:
            key_name: <p>The name of the API key to delete.</p>
            workspace_id: <p>The ID of the workspace to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_grafana.types.delete_workspace_api_key_request.DeleteWorkspaceApiKeyRequest]') -> AsyncOperationResponse["aws_sdk_grafana.types.delete_workspace_api_key_response.DeleteWorkspaceApiKeyResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_api_key
            output, http_response = await aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_api_key.async_delete_workspace_api_key(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.delete_workspace_api_key_request.DeleteWorkspaceApiKeyRequest = {}  # type: ignore[typeddict-item]
        input["key_name"] = key_name
        input["workspace_id"] = workspace_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output