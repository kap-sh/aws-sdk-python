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
    import aws_sdk_grafana.types.associate_license_request
    import aws_sdk_grafana.types.associate_license_response
    import aws_sdk_grafana.types.disassociate_license_request
    import aws_sdk_grafana.types.disassociate_license_response
    import aws_sdk_grafana.types.grafana_token
    import aws_sdk_grafana.types.license_type
    import aws_sdk_grafana.types.workspace_id
    from aws_sdk_grafana._services.async_grafana import (
        AsyncgrafanaClient,
        AsyncgrafanaClientConfig,
    )
    from aws_sdk_grafana._services.grafana import grafanaClient, grafanaClientConfig


class License:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service

    def associate_license(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        license_type: "aws_sdk_grafana.types.license_type.LicenseType",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        grafana_token: Optional[
            "aws_sdk_grafana.types.grafana_token.GrafanaToken"
        ] = None,
    ) -> "aws_sdk_grafana.types.associate_license_response.AssociateLicenseResponse":
        """<p>Assigns a Grafana Enterprise license to a workspace. To upgrade, you must use <code>ENTERPRISE</code> for the <code>licenseType</code>, and pass in a valid Grafana Labs token for the <code>grafanaToken</code>. Upgrading to Grafana Enterprise incurs additional fees. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html\">Upgrade a workspace to Grafana Enterprise</a>.</p>

        Args:
            workspace_id: <p>The ID of the workspace to associate the license with.</p>
            license_type: <p>The type of license to associate with the workspace.</p> <note> <p>Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.</p> </note>
            grafana_token: <p>A token from Grafana Labs that ties your Amazon Web Services account with a Grafana Labs account. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise\">Link your account with Grafana Labs</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.associate_license_request.AssociateLicenseRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.associate_license_response.AssociateLicenseResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.associate_license

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.associate_license.associate_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.associate_license_request.AssociateLicenseRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["license_type"] = license_type
        if grafana_token is not None:
            input_["grafana_token"] = grafana_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_license(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        license_type: "aws_sdk_grafana.types.license_type.LicenseType",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.disassociate_license_response.DisassociateLicenseResponse":
        """<p>Removes the Grafana Enterprise license from a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to remove the Grafana Enterprise license from.</p>
            license_type: <p>The type of license to remove from the workspace.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.disassociate_license_request.DisassociateLicenseRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.disassociate_license_response.DisassociateLicenseResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.disassociate_license

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.disassociate_license.disassociate_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.disassociate_license_request.DisassociateLicenseRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["license_type"] = license_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncLicense:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service

    async def associate_license(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        license_type: "aws_sdk_grafana.types.license_type.LicenseType",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        grafana_token: Optional[
            "aws_sdk_grafana.types.grafana_token.GrafanaToken"
        ] = None,
    ) -> "aws_sdk_grafana.types.associate_license_response.AssociateLicenseResponse":
        """<p>Assigns a Grafana Enterprise license to a workspace. To upgrade, you must use <code>ENTERPRISE</code> for the <code>licenseType</code>, and pass in a valid Grafana Labs token for the <code>grafanaToken</code>. Upgrading to Grafana Enterprise incurs additional fees. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html\">Upgrade a workspace to Grafana Enterprise</a>.</p>

        Args:
            workspace_id: <p>The ID of the workspace to associate the license with.</p>
            license_type: <p>The type of license to associate with the workspace.</p> <note> <p>Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.</p> </note>
            grafana_token: <p>A token from Grafana Labs that ties your Amazon Web Services account with a Grafana Labs account. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise\">Link your account with Grafana Labs</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.associate_license_request.AssociateLicenseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.associate_license_response.AssociateLicenseResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.associate_license

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.associate_license.async_associate_license(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.associate_license_request.AssociateLicenseRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["license_type"] = license_type
        if grafana_token is not None:
            input_["grafana_token"] = grafana_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_license(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        license_type: "aws_sdk_grafana.types.license_type.LicenseType",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.disassociate_license_response.DisassociateLicenseResponse":
        """<p>Removes the Grafana Enterprise license from a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to remove the Grafana Enterprise license from.</p>
            license_type: <p>The type of license to remove from the workspace.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.disassociate_license_request.DisassociateLicenseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.disassociate_license_response.DisassociateLicenseResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.disassociate_license

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.disassociate_license.async_disassociate_license(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.disassociate_license_request.DisassociateLicenseRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id
        input_["license_type"] = license_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
