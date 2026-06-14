from typing import TYPE_CHECKING, Optional

import aws_sdk_grafana._auth._signers
import aws_sdk_grafana._auth._sigv4
from aws_sdk_grafana._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_grafana.types.list_permissions_request
    import aws_sdk_grafana.types.list_permissions_response
    import aws_sdk_grafana.types.pagination_token
    import aws_sdk_grafana.types.permission_entry
    import aws_sdk_grafana.types.sso_id
    import aws_sdk_grafana.types.update_instruction_batch
    import aws_sdk_grafana.types.update_permissions_request
    import aws_sdk_grafana.types.update_permissions_response
    import aws_sdk_grafana.types.user_type
    import aws_sdk_grafana.types.workspace_id
    from aws_sdk_grafana._services.async_grafana import (
        AsyncgrafanaClient,
        AsyncgrafanaClientConfig,
    )
    from aws_sdk_grafana._services.grafana import grafanaClient, grafanaClientConfig


class Permission:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service

    def read(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_grafana.types.pagination_token.PaginationToken"
        ] = None,
        user_type: Optional["aws_sdk_grafana.types.user_type.UserType"] = None,
        user_id: Optional["aws_sdk_grafana.types.sso_id.SsoId"] = None,
        group_id: Optional["aws_sdk_grafana.types.sso_id.SsoId"] = None,
    ) -> "aws_sdk_grafana.types.list_permissions_response.ListPermissionsResponse":
        """<p>Lists the users and groups who have the Grafana <code>Admin</code> and <code>Editor</code> roles in this workspace. If you use this operation without specifying <code>userId</code> or <code>groupId</code>, the operation returns the roles of all users and groups. If you specify a <code>userId</code> or a <code>groupId</code>, only the roles for that user or group are returned. If you do this, you can specify only one <code>userId</code> or one <code>groupId</code>.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token to use when requesting the next set of results. You received this token from a previous <code>ListPermissions</code> operation.</p>
            user_type: <p>(Optional) If you specify <code>SSO_USER</code>, then only the permissions of IAM Identity Center users are returned. If you specify <code>SSO_GROUP</code>, only the permissions of IAM Identity Center groups are returned.</p>
            user_id: <p>(Optional) Limits the results to only the user that matches this ID.</p>
            group_id: <p>(Optional) Limits the results to only the group that matches this ID.</p>
            workspace_id: <p>The ID of the workspace to list permissions for. This parameter is required.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.list_permissions_request.ListPermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.list_permissions_response.ListPermissionsResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_permissions

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.list_permissions.list_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.list_permissions_request.ListPermissionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if user_type is not None:
            input_["user_type"] = user_type
        if user_id is not None:
            input_["user_id"] = user_id
        if group_id is not None:
            input_["group_id"] = group_id
        input_["workspace_id"] = workspace_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        update_instruction_batch: "aws_sdk_grafana.types.update_instruction_batch.UpdateInstructionBatch",
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.update_permissions_response.UpdatePermissionsResponse":
        """<p>Updates which users in a workspace have the Grafana <code>Admin</code> or <code>Editor</code> roles.</p>

        Args:
            update_instruction_batch: <p>An array of structures that contain the permission updates to make.</p>
            workspace_id: <p>The ID of the workspace to update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.update_permissions_request.UpdatePermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.update_permissions_response.UpdatePermissionsResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.update_permissions

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.update_permissions.update_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.update_permissions_request.UpdatePermissionsRequest = {}  # type: ignore[typeddict-item]
        input_["update_instruction_batch"] = update_instruction_batch
        input_["workspace_id"] = workspace_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncPermission:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service

    async def read(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_grafana.types.pagination_token.PaginationToken"
        ] = None,
        user_type: Optional["aws_sdk_grafana.types.user_type.UserType"] = None,
        user_id: Optional["aws_sdk_grafana.types.sso_id.SsoId"] = None,
        group_id: Optional["aws_sdk_grafana.types.sso_id.SsoId"] = None,
    ) -> "aws_sdk_grafana.types.list_permissions_response.ListPermissionsResponse":
        """<p>Lists the users and groups who have the Grafana <code>Admin</code> and <code>Editor</code> roles in this workspace. If you use this operation without specifying <code>userId</code> or <code>groupId</code>, the operation returns the roles of all users and groups. If you specify a <code>userId</code> or a <code>groupId</code>, only the roles for that user or group are returned. If you do this, you can specify only one <code>userId</code> or one <code>groupId</code>.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token to use when requesting the next set of results. You received this token from a previous <code>ListPermissions</code> operation.</p>
            user_type: <p>(Optional) If you specify <code>SSO_USER</code>, then only the permissions of IAM Identity Center users are returned. If you specify <code>SSO_GROUP</code>, only the permissions of IAM Identity Center groups are returned.</p>
            user_id: <p>(Optional) Limits the results to only the user that matches this ID.</p>
            group_id: <p>(Optional) Limits the results to only the group that matches this ID.</p>
            workspace_id: <p>The ID of the workspace to list permissions for. This parameter is required.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.list_permissions_request.ListPermissionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.list_permissions_response.ListPermissionsResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_permissions

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.list_permissions.async_list_permissions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.list_permissions_request.ListPermissionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if user_type is not None:
            input_["user_type"] = user_type
        if user_id is not None:
            input_["user_id"] = user_id
        if group_id is not None:
            input_["group_id"] = group_id
        input_["workspace_id"] = workspace_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        update_instruction_batch: "aws_sdk_grafana.types.update_instruction_batch.UpdateInstructionBatch",
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.update_permissions_response.UpdatePermissionsResponse":
        """<p>Updates which users in a workspace have the Grafana <code>Admin</code> or <code>Editor</code> roles.</p>

        Args:
            update_instruction_batch: <p>An array of structures that contain the permission updates to make.</p>
            workspace_id: <p>The ID of the workspace to update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.update_permissions_request.UpdatePermissionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.update_permissions_response.UpdatePermissionsResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.update_permissions

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.update_permissions.async_update_permissions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.update_permissions_request.UpdatePermissionsRequest = {}  # type: ignore[typeddict-item]
        input_["update_instruction_batch"] = update_instruction_batch
        input_["workspace_id"] = workspace_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
