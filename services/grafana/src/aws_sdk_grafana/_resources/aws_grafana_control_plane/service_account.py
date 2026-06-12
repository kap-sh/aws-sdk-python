from typing import Optional, TYPE_CHECKING
from aws_sdk_grafana._services.async_grafana import ensure_async_iterator
from aws_sdk_grafana._services.grafana import ensure_sync_iterator
from aws_sdk_grafana._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_grafana._auth._signers
import aws_sdk_grafana._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_grafana._services.grafana import grafanaClient, grafanaClientConfig
    from aws_sdk_grafana._services.async_grafana import AsyncgrafanaClient, AsyncgrafanaClientConfig
    import aws_sdk_grafana.types.create_workspace_service_account_request
    import aws_sdk_grafana.types.create_workspace_service_account_response
    import aws_sdk_grafana.types.delete_workspace_service_account_request
    import aws_sdk_grafana.types.delete_workspace_service_account_response
    import aws_sdk_grafana.types.list_workspace_service_accounts_request
    import aws_sdk_grafana.types.list_workspace_service_accounts_response
    import aws_sdk_grafana.types.pagination_token
    import aws_sdk_grafana.types.role
    import aws_sdk_grafana.types.service_account_name
    import aws_sdk_grafana.types.service_account_summary
    import aws_sdk_grafana.types.workspace_id

class ServiceAccount:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service
    def create_workspace_service_account(self, name: "aws_sdk_grafana.types.service_account_name.ServiceAccountName", grafana_role: "aws_sdk_grafana.types.role.Role", workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[grafanaClientConfig] = None) -> "aws_sdk_grafana.types.create_workspace_service_account_response.CreateWorkspaceServiceAccountResponse":
        """<p>Creates a service account for the workspace. A service account can be used to call Grafana HTTP APIs, and run automated workloads. After creating the service account with the correct <code>GrafanaRole</code> for your use case, use <code>CreateWorkspaceServiceAccountToken</code> to create a token that can be used to authenticate and authorize Grafana HTTP API calls.</p> <p>You can only create service accounts for workspaces that are compatible with Grafana version 9 and above.</p> <note> <p>For more information about service accounts, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html\">Service accounts</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> <p>For more information about the Grafana HTTP APIs, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html\">Using Grafana HTTP APIs</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> </note>

        Args:
            name: <p>A name for the service account. The name must be unique within the workspace, as it determines the ID associated with the service account.</p>
            grafana_role: <p>The permission level to use for this service account.</p> <note> <p>For more information about the roles and the permissions each has, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-user-roles.html\">User roles</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> </note>
            workspace_id: <p>The ID of the workspace within which to create the service account.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_grafana.types.create_workspace_service_account_request.CreateWorkspaceServiceAccountRequest]') -> OperationResponse["aws_sdk_grafana.types.create_workspace_service_account_response.CreateWorkspaceServiceAccountResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_service_account
            output, http_response = aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_service_account.create_workspace_service_account(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.create_workspace_service_account_request.CreateWorkspaceServiceAccountRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["grafana_role"] = grafana_role
        input["workspace_id"] = workspace_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete_workspace_service_account(self, service_account_id: str, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[grafanaClientConfig] = None) -> "aws_sdk_grafana.types.delete_workspace_service_account_response.DeleteWorkspaceServiceAccountResponse":
        """<p>Deletes a workspace service account from the workspace.</p> <p>This will delete any tokens created for the service account, as well. If the tokens are currently in use, the will fail to authenticate / authorize after they are deleted.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            service_account_id: <p>The ID of the service account to delete.</p>
            workspace_id: <p>The ID of the workspace where the service account resides.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_grafana.types.delete_workspace_service_account_request.DeleteWorkspaceServiceAccountRequest]') -> OperationResponse["aws_sdk_grafana.types.delete_workspace_service_account_response.DeleteWorkspaceServiceAccountResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account
            output, http_response = aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account.delete_workspace_service_account(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.delete_workspace_service_account_request.DeleteWorkspaceServiceAccountRequest = {}  # type: ignore[typeddict-item]
        input["service_account_id"] = service_account_id
        input["workspace_id"] = workspace_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_workspace_service_accounts(self, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[grafanaClientConfig] = None, max_results: Optional[int] = None, next_token: Optional["aws_sdk_grafana.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_grafana.types.list_workspace_service_accounts_response.ListWorkspaceServiceAccountsResponse":
        """<p>Returns a list of service accounts for a workspace.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            max_results: <p>The maximum number of service accounts to include in the results.</p>
            next_token: <p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccounts</code> operation.)</p>
            workspace_id: <p>The workspace for which to list service accounts.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_grafana.types.list_workspace_service_accounts_request.ListWorkspaceServiceAccountsRequest]') -> OperationResponse["aws_sdk_grafana.types.list_workspace_service_accounts_response.ListWorkspaceServiceAccountsResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspace_service_accounts
            output, http_response = aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspace_service_accounts.list_workspace_service_accounts(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.list_workspace_service_accounts_request.ListWorkspaceServiceAccountsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["workspace_id"] = workspace_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncServiceAccount:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service
    async def create_workspace_service_account(self, name: "aws_sdk_grafana.types.service_account_name.ServiceAccountName", grafana_role: "aws_sdk_grafana.types.role.Role", workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[AsyncgrafanaClientConfig] = None) -> "aws_sdk_grafana.types.create_workspace_service_account_response.CreateWorkspaceServiceAccountResponse":
        """<p>Creates a service account for the workspace. A service account can be used to call Grafana HTTP APIs, and run automated workloads. After creating the service account with the correct <code>GrafanaRole</code> for your use case, use <code>CreateWorkspaceServiceAccountToken</code> to create a token that can be used to authenticate and authorize Grafana HTTP API calls.</p> <p>You can only create service accounts for workspaces that are compatible with Grafana version 9 and above.</p> <note> <p>For more information about service accounts, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html\">Service accounts</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> <p>For more information about the Grafana HTTP APIs, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html\">Using Grafana HTTP APIs</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> </note>

        Args:
            name: <p>A name for the service account. The name must be unique within the workspace, as it determines the ID associated with the service account.</p>
            grafana_role: <p>The permission level to use for this service account.</p> <note> <p>For more information about the roles and the permissions each has, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-user-roles.html\">User roles</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> </note>
            workspace_id: <p>The ID of the workspace within which to create the service account.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_grafana.types.create_workspace_service_account_request.CreateWorkspaceServiceAccountRequest]') -> AsyncOperationResponse["aws_sdk_grafana.types.create_workspace_service_account_response.CreateWorkspaceServiceAccountResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_service_account
            output, http_response = await aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace_service_account.async_create_workspace_service_account(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.create_workspace_service_account_request.CreateWorkspaceServiceAccountRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["grafana_role"] = grafana_role
        input["workspace_id"] = workspace_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete_workspace_service_account(self, service_account_id: str, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[AsyncgrafanaClientConfig] = None) -> "aws_sdk_grafana.types.delete_workspace_service_account_response.DeleteWorkspaceServiceAccountResponse":
        """<p>Deletes a workspace service account from the workspace.</p> <p>This will delete any tokens created for the service account, as well. If the tokens are currently in use, the will fail to authenticate / authorize after they are deleted.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            service_account_id: <p>The ID of the service account to delete.</p>
            workspace_id: <p>The ID of the workspace where the service account resides.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_grafana.types.delete_workspace_service_account_request.DeleteWorkspaceServiceAccountRequest]') -> AsyncOperationResponse["aws_sdk_grafana.types.delete_workspace_service_account_response.DeleteWorkspaceServiceAccountResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account
            output, http_response = await aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account.async_delete_workspace_service_account(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.delete_workspace_service_account_request.DeleteWorkspaceServiceAccountRequest = {}  # type: ignore[typeddict-item]
        input["service_account_id"] = service_account_id
        input["workspace_id"] = workspace_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_workspace_service_accounts(self, workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId", *, config_overrides: Optional[AsyncgrafanaClientConfig] = None, max_results: Optional[int] = None, next_token: Optional["aws_sdk_grafana.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_grafana.types.list_workspace_service_accounts_response.ListWorkspaceServiceAccountsResponse":
        """<p>Returns a list of service accounts for a workspace.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            max_results: <p>The maximum number of service accounts to include in the results.</p>
            next_token: <p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccounts</code> operation.)</p>
            workspace_id: <p>The workspace for which to list service accounts.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_grafana.types.list_workspace_service_accounts_request.ListWorkspaceServiceAccountsRequest]') -> AsyncOperationResponse["aws_sdk_grafana.types.list_workspace_service_accounts_response.ListWorkspaceServiceAccountsResponse"]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspace_service_accounts
            output, http_response = await aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspace_service_accounts.async_list_workspace_service_accounts(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.list_workspace_service_accounts_request.ListWorkspaceServiceAccountsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["workspace_id"] = workspace_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output