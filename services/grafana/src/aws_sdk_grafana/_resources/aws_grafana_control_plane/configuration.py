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
    import aws_sdk_grafana.types.describe_workspace_configuration_request
    import aws_sdk_grafana.types.describe_workspace_configuration_response
    import aws_sdk_grafana.types.grafana_version
    import aws_sdk_grafana.types.overridable_configuration_json
    import aws_sdk_grafana.types.update_workspace_configuration_request
    import aws_sdk_grafana.types.update_workspace_configuration_response
    import aws_sdk_grafana.types.workspace_id
    from aws_sdk_grafana._services.async_grafana import (
        AsyncgrafanaClient,
        AsyncgrafanaClientConfig,
    )
    from aws_sdk_grafana._services.grafana import grafanaClient, grafanaClientConfig


class Configuration:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service

    def describe_workspace_configuration(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse":
        """<p>Gets the current configuration string for the given workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to get configuration information for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.describe_workspace_configuration

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.describe_workspace_configuration.describe_workspace_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["workspace_id"] = workspace_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_workspace_configuration(
        self,
        configuration: "aws_sdk_grafana.types.overridable_configuration_json.OverridableConfigurationJson",
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        grafana_version: Optional[
            "aws_sdk_grafana.types.grafana_version.GrafanaVersion"
        ] = None,
    ) -> "aws_sdk_grafana.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse":
        """<p>Updates the configuration string for the given workspace</p>

        Args:
            configuration: <p>The new configuration string for the workspace. For more information about the format and configuration options available, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html\">Working in your Grafana workspace</a>.</p>
            workspace_id: <p>The ID of the workspace to update.</p>
            grafana_version: <p>Specifies the version of Grafana to support in the workspace. If not specified, keeps the current version of the workspace.</p> <p>Can only be used to upgrade (for example, from 8.4 to 9.4), not downgrade (for example, from 9.4 to 8.4).</p> <p>To know what versions are available to upgrade to for a specific workspace, see the <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListVersions.html\">ListVersions</a> operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.update_workspace_configuration

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.update_workspace_configuration.update_workspace_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["configuration"] = configuration
        input["workspace_id"] = workspace_id
        if grafana_version is not None:
            input["grafana_version"] = grafana_version

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncConfiguration:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service

    async def describe_workspace_configuration(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse":
        """<p>Gets the current configuration string for the given workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to get configuration information for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.describe_workspace_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.describe_workspace_configuration.async_describe_workspace_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["workspace_id"] = workspace_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_workspace_configuration(
        self,
        configuration: "aws_sdk_grafana.types.overridable_configuration_json.OverridableConfigurationJson",
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        grafana_version: Optional[
            "aws_sdk_grafana.types.grafana_version.GrafanaVersion"
        ] = None,
    ) -> "aws_sdk_grafana.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse":
        """<p>Updates the configuration string for the given workspace</p>

        Args:
            configuration: <p>The new configuration string for the workspace. For more information about the format and configuration options available, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html\">Working in your Grafana workspace</a>.</p>
            workspace_id: <p>The ID of the workspace to update.</p>
            grafana_version: <p>Specifies the version of Grafana to support in the workspace. If not specified, keeps the current version of the workspace.</p> <p>Can only be used to upgrade (for example, from 8.4 to 9.4), not downgrade (for example, from 9.4 to 8.4).</p> <p>To know what versions are available to upgrade to for a specific workspace, see the <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListVersions.html\">ListVersions</a> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.update_workspace_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.update_workspace_configuration.async_update_workspace_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_grafana.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["configuration"] = configuration
        input["workspace_id"] = workspace_id
        if grafana_version is not None:
            input["grafana_version"] = grafana_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
