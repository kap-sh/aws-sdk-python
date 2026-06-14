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
    import aws_sdk_grafana.types.account_access_type
    import aws_sdk_grafana.types.authentication_providers
    import aws_sdk_grafana.types.client_token
    import aws_sdk_grafana.types.create_workspace_request
    import aws_sdk_grafana.types.create_workspace_response
    import aws_sdk_grafana.types.data_source_types_list
    import aws_sdk_grafana.types.delete_workspace_request
    import aws_sdk_grafana.types.delete_workspace_response
    import aws_sdk_grafana.types.describe_workspace_request
    import aws_sdk_grafana.types.describe_workspace_response
    import aws_sdk_grafana.types.description
    import aws_sdk_grafana.types.grafana_version
    import aws_sdk_grafana.types.iam_role_arn
    import aws_sdk_grafana.types.ip_address_type
    import aws_sdk_grafana.types.kms_key_id
    import aws_sdk_grafana.types.list_workspaces_request
    import aws_sdk_grafana.types.list_workspaces_response
    import aws_sdk_grafana.types.network_access_configuration
    import aws_sdk_grafana.types.notification_destinations_list
    import aws_sdk_grafana.types.organization_role_name
    import aws_sdk_grafana.types.organizational_unit_list
    import aws_sdk_grafana.types.overridable_configuration_json
    import aws_sdk_grafana.types.pagination_token
    import aws_sdk_grafana.types.permission_type
    import aws_sdk_grafana.types.stack_set_name
    import aws_sdk_grafana.types.tag_map
    import aws_sdk_grafana.types.update_workspace_request
    import aws_sdk_grafana.types.update_workspace_response
    import aws_sdk_grafana.types.vpc_configuration
    import aws_sdk_grafana.types.workspace_id
    import aws_sdk_grafana.types.workspace_name
    import aws_sdk_grafana.types.workspace_summary
    from aws_sdk_grafana._services.async_grafana import (
        AsyncgrafanaClient,
        AsyncgrafanaClientConfig,
    )
    from aws_sdk_grafana._services.grafana import grafanaClient, grafanaClientConfig


class Workspace:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service

    def create(
        self,
        account_access_type: "aws_sdk_grafana.types.account_access_type.AccountAccessType",
        permission_type: "aws_sdk_grafana.types.permission_type.PermissionType",
        authentication_providers: "aws_sdk_grafana.types.authentication_providers.AuthenticationProviders",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        client_token: Optional["aws_sdk_grafana.types.client_token.ClientToken"] = None,
        organization_role_name: Optional[
            "aws_sdk_grafana.types.organization_role_name.OrganizationRoleName"
        ] = None,
        stack_set_name: Optional[
            "aws_sdk_grafana.types.stack_set_name.StackSetName"
        ] = None,
        workspace_data_sources: Optional[
            "aws_sdk_grafana.types.data_source_types_list.DataSourceTypesList"
        ] = None,
        workspace_description: Optional[
            "aws_sdk_grafana.types.description.Description"
        ] = None,
        workspace_name: Optional[
            "aws_sdk_grafana.types.workspace_name.WorkspaceName"
        ] = None,
        workspace_notification_destinations: Optional[
            "aws_sdk_grafana.types.notification_destinations_list.NotificationDestinationsList"
        ] = None,
        workspace_organizational_units: Optional[
            "aws_sdk_grafana.types.organizational_unit_list.OrganizationalUnitList"
        ] = None,
        workspace_role_arn: Optional[
            "aws_sdk_grafana.types.iam_role_arn.IamRoleArn"
        ] = None,
        tags: Optional["aws_sdk_grafana.types.tag_map.TagMap"] = None,
        vpc_configuration: Optional[
            "aws_sdk_grafana.types.vpc_configuration.VpcConfiguration"
        ] = None,
        configuration: Optional[
            "aws_sdk_grafana.types.overridable_configuration_json.OverridableConfigurationJson"
        ] = None,
        network_access_control: Optional[
            "aws_sdk_grafana.types.network_access_configuration.NetworkAccessConfiguration"
        ] = None,
        grafana_version: Optional[
            "aws_sdk_grafana.types.grafana_version.GrafanaVersion"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_grafana.types.ip_address_type.IPAddressType"
        ] = None,
        kms_key_id: Optional["aws_sdk_grafana.types.kms_key_id.KmsKeyId"] = None,
    ) -> "aws_sdk_grafana.types.create_workspace_response.CreateWorkspaceResponse":
        """<p>Creates a <i>workspace</i>. In a workspace, you can create Grafana dashboards and visualizations to analyze your metrics, logs, and traces. You don't have to build, package, or deploy any hardware to run the Grafana server.</p> <p>Don't use <code>CreateWorkspace</code> to modify an existing workspace. Instead, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspace.html\">UpdateWorkspace</a>.</p>

        Args:
            account_access_type: <p>Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If you specify <code>ORGANIZATION</code>, you must specify which organizational units the workspace can access in the <code>workspaceOrganizationalUnits</code> parameter.</p>
            client_token: <p>A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.</p>
            organization_role_name: <p>The name of an IAM role that already exists to use with Organizations to access Amazon Web Services data sources and notification channels in other accounts in an organization.</p>
            permission_type: <p>When creating a workspace through the Amazon Web Services API, CLI or Amazon Web Services CloudFormation, you must manage IAM roles and provision the permissions that the workspace needs to use Amazon Web Services data sources and notification channels.</p> <p>You must also specify a <code>workspaceRoleArn</code> for a role that you will manage for the workspace to use when accessing those datasources and notification channels.</p> <p>The ability for Amazon Managed Grafana to create and update IAM roles on behalf of the user is supported only in the Amazon Managed Grafana console, where this value may be set to <code>SERVICE_MANAGED</code>.</p> <note> <p>Use only the <code>CUSTOMER_MANAGED</code> permission type when creating a workspace with the API, CLI or Amazon Web Services CloudFormation. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html\">Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels</a>.</p>
            stack_set_name: <p>The name of the CloudFormation stack set to use to generate IAM roles to be used for this workspace.</p>
            workspace_data_sources: <p>This parameter is for internal use only, and should not be used.</p>
            workspace_description: <p>A description for the workspace. This is used only to help you identify this workspace.</p> <p>Pattern: <code>^[\\p{L}\\p{Z}\\p{N}\\p{P}]{0,2048}$</code> </p>
            workspace_name: <p>The name for the workspace. It does not have to be unique.</p>
            workspace_notification_destinations: <p>Specify the Amazon Web Services notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels.</p>
            workspace_organizational_units: <p>Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.</p>
            workspace_role_arn: <p>Specified the IAM role that grants permissions to the Amazon Web Services resources that the workspace will view data from, including both data sources and notification channels. You are responsible for managing the permissions for this role as new data sources or notification channels are added. </p>
            authentication_providers: <p>Specifies whether this workspace uses SAML 2.0, IAM Identity Center, or both to authenticate users for using the Grafana console within a workspace. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html\">User authentication in Amazon Managed Grafana</a>.</p>
            tags: <p>The list of tags associated with the workspace.</p>
            vpc_configuration: <p>The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.</p> <note> <p>Connecting to a private VPC is not yet available in the Asia Pacific (Seoul) Region (ap-northeast-2).</p> </note>
            configuration: <p>The configuration string for the workspace that you create. For more information about the format and configuration options available, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html\">Working in your Grafana workspace</a>.</p>
            network_access_control: <p>Configuration for network access to your workspace.</p> <p>When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization will still be required.</p> <p>If this is not configured, or is removed, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>
            grafana_version: <p>Specifies the version of Grafana to support in the new workspace. If not specified, defaults to the latest version (for example, 10.4).</p> <p>To get a list of supported versions, use the <code>ListVersions</code> operation.</p>
            ip_address_type: <p>Specifies whether the workspace supports IPv4 only, or IPv4 and IPv6. Valid values are <code>IPv4</code> and <code>DualStack</code>. For more information about IP address types, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-nac.html\">Network access control</a>.</p>
            kms_key_id: <p>The ID or ARN of the Key Management Service key to use for encrypting workspace data.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.create_workspace_request.CreateWorkspaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.create_workspace_response.CreateWorkspaceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace.create_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.create_workspace_request.CreateWorkspaceRequest = {}  # type: ignore[typeddict-item]
        input_["account_access_type"] = account_access_type
        if client_token is not None:
            input_["client_token"] = client_token
        if organization_role_name is not None:
            input_["organization_role_name"] = organization_role_name
        input_["permission_type"] = permission_type
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if workspace_data_sources is not None:
            input_["workspace_data_sources"] = workspace_data_sources
        if workspace_description is not None:
            input_["workspace_description"] = workspace_description
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name
        if workspace_notification_destinations is not None:
            input_["workspace_notification_destinations"] = (
                workspace_notification_destinations
            )
        if workspace_organizational_units is not None:
            input_["workspace_organizational_units"] = workspace_organizational_units
        if workspace_role_arn is not None:
            input_["workspace_role_arn"] = workspace_role_arn
        input_["authentication_providers"] = authentication_providers
        if tags is not None:
            input_["tags"] = tags
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if configuration is not None:
            input_["configuration"] = configuration
        if network_access_control is not None:
            input_["network_access_control"] = network_access_control
        if grafana_version is not None:
            input_["grafana_version"] = grafana_version
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.describe_workspace_response.DescribeWorkspaceResponse":
        """<p>Displays information about one Amazon Managed Grafana workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to display information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.describe_workspace_request.DescribeWorkspaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.describe_workspace_response.DescribeWorkspaceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.describe_workspace

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.describe_workspace.describe_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.describe_workspace_request.DescribeWorkspaceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        account_access_type: Optional[
            "aws_sdk_grafana.types.account_access_type.AccountAccessType"
        ] = None,
        organization_role_name: Optional[
            "aws_sdk_grafana.types.organization_role_name.OrganizationRoleName"
        ] = None,
        permission_type: Optional[
            "aws_sdk_grafana.types.permission_type.PermissionType"
        ] = None,
        stack_set_name: Optional[
            "aws_sdk_grafana.types.stack_set_name.StackSetName"
        ] = None,
        workspace_data_sources: Optional[
            "aws_sdk_grafana.types.data_source_types_list.DataSourceTypesList"
        ] = None,
        workspace_description: Optional[
            "aws_sdk_grafana.types.description.Description"
        ] = None,
        workspace_name: Optional[
            "aws_sdk_grafana.types.workspace_name.WorkspaceName"
        ] = None,
        workspace_notification_destinations: Optional[
            "aws_sdk_grafana.types.notification_destinations_list.NotificationDestinationsList"
        ] = None,
        workspace_organizational_units: Optional[
            "aws_sdk_grafana.types.organizational_unit_list.OrganizationalUnitList"
        ] = None,
        workspace_role_arn: Optional[
            "aws_sdk_grafana.types.iam_role_arn.IamRoleArn"
        ] = None,
        vpc_configuration: Optional[
            "aws_sdk_grafana.types.vpc_configuration.VpcConfiguration"
        ] = None,
        remove_vpc_configuration: Optional[bool] = None,
        network_access_control: Optional[
            "aws_sdk_grafana.types.network_access_configuration.NetworkAccessConfiguration"
        ] = None,
        remove_network_access_configuration: Optional[bool] = None,
        ip_address_type: Optional[
            "aws_sdk_grafana.types.ip_address_type.IPAddressType"
        ] = None,
    ) -> "aws_sdk_grafana.types.update_workspace_response.UpdateWorkspaceResponse":
        """<p>Modifies an existing Amazon Managed Grafana workspace. If you use this operation and omit any optional parameters, the existing values of those parameters are not changed.</p> <p>To modify the user authentication methods that the workspace uses, such as SAML or IAM Identity Center, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspaceAuthentication.html\">UpdateWorkspaceAuthentication</a>.</p> <p>To modify which users in the workspace have the <code>Admin</code> and <code>Editor</code> Grafana roles, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdatePermissions.html\">UpdatePermissions</a>.</p>

        Args:
            account_access_type: <p>Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If you specify <code>ORGANIZATION</code>, you must specify which organizational units the workspace can access in the <code>workspaceOrganizationalUnits</code> parameter.</p>
            organization_role_name: <p>The name of an IAM role that already exists to use to access resources through Organizations. This can only be used with a workspace that has the <code>permissionType</code> set to <code>CUSTOMER_MANAGED</code>.</p>
            permission_type: <p>Use this parameter if you want to change a workspace from <code>SERVICE_MANAGED</code> to <code>CUSTOMER_MANAGED</code>. This allows you to manage the permissions that the workspace uses to access datasources and notification channels. If the workspace is in a member Amazon Web Services account of an organization, and that account is not a delegated administrator account, and you want the workspace to access data sources in other Amazon Web Services accounts in the organization, you must choose <code>CUSTOMER_MANAGED</code>.</p> <p>If you specify this as <code>CUSTOMER_MANAGED</code>, you must also specify a <code>workspaceRoleArn</code> that the workspace will use for accessing Amazon Web Services resources.</p> <p>For more information on the role and permissions needed, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html\">Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels</a> </p> <note> <p>Do not use this to convert a <code>CUSTOMER_MANAGED</code> workspace to <code>SERVICE_MANAGED</code>. Do not include this parameter if you want to leave the workspace as <code>SERVICE_MANAGED</code>.</p> <p>You can convert a <code>CUSTOMER_MANAGED</code> workspace to <code>SERVICE_MANAGED</code> using the Amazon Managed Grafana console. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-and-notification.html\">Managing permissions for data sources and notification channels</a>.</p> </note>
            stack_set_name: <p>The name of the CloudFormation stack set to use to generate IAM roles to be used for this workspace.</p>
            workspace_data_sources: <p>This parameter is for internal use only, and should not be used.</p>
            workspace_description: <p>A description for the workspace. This is used only to help you identify this workspace.</p>
            workspace_id: <p>The ID of the workspace to update.</p>
            workspace_name: <p>A new name for the workspace to update.</p>
            workspace_notification_destinations: <p>Specify the Amazon Web Services notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels.</p>
            workspace_organizational_units: <p>Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.</p>
            workspace_role_arn: <p>Specifies an IAM role that grants permissions to Amazon Web Services resources that the workspace accesses, such as data sources and notification channels. If this workspace has <code>permissionType</code> <code>CUSTOMER_MANAGED</code>, then this role is required.</p>
            vpc_configuration: <p>The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.</p>
            remove_vpc_configuration: <p>Whether to remove the VPC configuration from the workspace.</p> <p>Setting this to <code>true</code> and providing a <code>vpcConfiguration</code> to set will return an error.</p>
            network_access_control: <p>The configuration settings for network access to your workspace.</p> <p>When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization will still be required.</p> <p>If this is not configured, or is removed, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>
            remove_network_access_configuration: <p>Whether to remove the network access configuration from the workspace.</p> <p>Setting this to <code>true</code> and providing a <code>networkAccessControl</code> to set will return an error.</p> <p>If you remove this configuration by setting this to <code>true</code>, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>
            ip_address_type: <p>Specifies whether the workspace supports IPv4 only, or IPv4 and IPv6. Valid values are <code>IPv4</code> and <code>DualStack</code>. For more information about IP address types, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-nac.html\">Network access control</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.update_workspace_request.UpdateWorkspaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.update_workspace_response.UpdateWorkspaceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.update_workspace

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.update_workspace.update_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.update_workspace_request.UpdateWorkspaceRequest = {}  # type: ignore[typeddict-item]
        if account_access_type is not None:
            input_["account_access_type"] = account_access_type
        if organization_role_name is not None:
            input_["organization_role_name"] = organization_role_name
        if permission_type is not None:
            input_["permission_type"] = permission_type
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if workspace_data_sources is not None:
            input_["workspace_data_sources"] = workspace_data_sources
        if workspace_description is not None:
            input_["workspace_description"] = workspace_description
        input_["workspace_id"] = workspace_id
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name
        if workspace_notification_destinations is not None:
            input_["workspace_notification_destinations"] = (
                workspace_notification_destinations
            )
        if workspace_organizational_units is not None:
            input_["workspace_organizational_units"] = workspace_organizational_units
        if workspace_role_arn is not None:
            input_["workspace_role_arn"] = workspace_role_arn
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if remove_vpc_configuration is not None:
            input_["remove_vpc_configuration"] = remove_vpc_configuration
        if network_access_control is not None:
            input_["network_access_control"] = network_access_control
        if remove_network_access_configuration is not None:
            input_["remove_network_access_configuration"] = (
                remove_network_access_configuration
            )
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.delete_workspace_response.DeleteWorkspaceResponse":
        """<p>Deletes an Amazon Managed Grafana workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.delete_workspace_request.DeleteWorkspaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.delete_workspace_response.DeleteWorkspaceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace.delete_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.delete_workspace_request.DeleteWorkspaceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_grafana.types.list_workspaces_response.ListWorkspacesResponse":
        """<p>Returns a list of Amazon Managed Grafana workspaces in the account, with some information about each workspace. For more complete information about one workspace, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_DescribeWorkspace.html\">DescribeWorkspace</a>.</p>

        Args:
            max_results: <p>The maximum number of workspaces to include in the results.</p>
            next_token: <p>The token for the next set of workspaces to return. (You receive this token from a previous <code>ListWorkspaces</code> operation.)</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_grafana.types.list_workspaces_request.ListWorkspacesRequest]",
        ) -> OperationResponse[
            "aws_sdk_grafana.types.list_workspaces_response.ListWorkspacesResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspaces

            output, http_response = (
                aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspaces.list_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.list_workspaces_request.ListWorkspacesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncWorkspace:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service

    async def create(
        self,
        account_access_type: "aws_sdk_grafana.types.account_access_type.AccountAccessType",
        permission_type: "aws_sdk_grafana.types.permission_type.PermissionType",
        authentication_providers: "aws_sdk_grafana.types.authentication_providers.AuthenticationProviders",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        client_token: Optional["aws_sdk_grafana.types.client_token.ClientToken"] = None,
        organization_role_name: Optional[
            "aws_sdk_grafana.types.organization_role_name.OrganizationRoleName"
        ] = None,
        stack_set_name: Optional[
            "aws_sdk_grafana.types.stack_set_name.StackSetName"
        ] = None,
        workspace_data_sources: Optional[
            "aws_sdk_grafana.types.data_source_types_list.DataSourceTypesList"
        ] = None,
        workspace_description: Optional[
            "aws_sdk_grafana.types.description.Description"
        ] = None,
        workspace_name: Optional[
            "aws_sdk_grafana.types.workspace_name.WorkspaceName"
        ] = None,
        workspace_notification_destinations: Optional[
            "aws_sdk_grafana.types.notification_destinations_list.NotificationDestinationsList"
        ] = None,
        workspace_organizational_units: Optional[
            "aws_sdk_grafana.types.organizational_unit_list.OrganizationalUnitList"
        ] = None,
        workspace_role_arn: Optional[
            "aws_sdk_grafana.types.iam_role_arn.IamRoleArn"
        ] = None,
        tags: Optional["aws_sdk_grafana.types.tag_map.TagMap"] = None,
        vpc_configuration: Optional[
            "aws_sdk_grafana.types.vpc_configuration.VpcConfiguration"
        ] = None,
        configuration: Optional[
            "aws_sdk_grafana.types.overridable_configuration_json.OverridableConfigurationJson"
        ] = None,
        network_access_control: Optional[
            "aws_sdk_grafana.types.network_access_configuration.NetworkAccessConfiguration"
        ] = None,
        grafana_version: Optional[
            "aws_sdk_grafana.types.grafana_version.GrafanaVersion"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_grafana.types.ip_address_type.IPAddressType"
        ] = None,
        kms_key_id: Optional["aws_sdk_grafana.types.kms_key_id.KmsKeyId"] = None,
    ) -> "aws_sdk_grafana.types.create_workspace_response.CreateWorkspaceResponse":
        """<p>Creates a <i>workspace</i>. In a workspace, you can create Grafana dashboards and visualizations to analyze your metrics, logs, and traces. You don't have to build, package, or deploy any hardware to run the Grafana server.</p> <p>Don't use <code>CreateWorkspace</code> to modify an existing workspace. Instead, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspace.html\">UpdateWorkspace</a>.</p>

        Args:
            account_access_type: <p>Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If you specify <code>ORGANIZATION</code>, you must specify which organizational units the workspace can access in the <code>workspaceOrganizationalUnits</code> parameter.</p>
            client_token: <p>A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.</p>
            organization_role_name: <p>The name of an IAM role that already exists to use with Organizations to access Amazon Web Services data sources and notification channels in other accounts in an organization.</p>
            permission_type: <p>When creating a workspace through the Amazon Web Services API, CLI or Amazon Web Services CloudFormation, you must manage IAM roles and provision the permissions that the workspace needs to use Amazon Web Services data sources and notification channels.</p> <p>You must also specify a <code>workspaceRoleArn</code> for a role that you will manage for the workspace to use when accessing those datasources and notification channels.</p> <p>The ability for Amazon Managed Grafana to create and update IAM roles on behalf of the user is supported only in the Amazon Managed Grafana console, where this value may be set to <code>SERVICE_MANAGED</code>.</p> <note> <p>Use only the <code>CUSTOMER_MANAGED</code> permission type when creating a workspace with the API, CLI or Amazon Web Services CloudFormation. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html\">Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels</a>.</p>
            stack_set_name: <p>The name of the CloudFormation stack set to use to generate IAM roles to be used for this workspace.</p>
            workspace_data_sources: <p>This parameter is for internal use only, and should not be used.</p>
            workspace_description: <p>A description for the workspace. This is used only to help you identify this workspace.</p> <p>Pattern: <code>^[\\p{L}\\p{Z}\\p{N}\\p{P}]{0,2048}$</code> </p>
            workspace_name: <p>The name for the workspace. It does not have to be unique.</p>
            workspace_notification_destinations: <p>Specify the Amazon Web Services notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels.</p>
            workspace_organizational_units: <p>Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.</p>
            workspace_role_arn: <p>Specified the IAM role that grants permissions to the Amazon Web Services resources that the workspace will view data from, including both data sources and notification channels. You are responsible for managing the permissions for this role as new data sources or notification channels are added. </p>
            authentication_providers: <p>Specifies whether this workspace uses SAML 2.0, IAM Identity Center, or both to authenticate users for using the Grafana console within a workspace. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html\">User authentication in Amazon Managed Grafana</a>.</p>
            tags: <p>The list of tags associated with the workspace.</p>
            vpc_configuration: <p>The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.</p> <note> <p>Connecting to a private VPC is not yet available in the Asia Pacific (Seoul) Region (ap-northeast-2).</p> </note>
            configuration: <p>The configuration string for the workspace that you create. For more information about the format and configuration options available, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html\">Working in your Grafana workspace</a>.</p>
            network_access_control: <p>Configuration for network access to your workspace.</p> <p>When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization will still be required.</p> <p>If this is not configured, or is removed, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>
            grafana_version: <p>Specifies the version of Grafana to support in the new workspace. If not specified, defaults to the latest version (for example, 10.4).</p> <p>To get a list of supported versions, use the <code>ListVersions</code> operation.</p>
            ip_address_type: <p>Specifies whether the workspace supports IPv4 only, or IPv4 and IPv6. Valid values are <code>IPv4</code> and <code>DualStack</code>. For more information about IP address types, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-nac.html\">Network access control</a>.</p>
            kms_key_id: <p>The ID or ARN of the Key Management Service key to use for encrypting workspace data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.create_workspace_request.CreateWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.create_workspace_response.CreateWorkspaceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.create_workspace.async_create_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.create_workspace_request.CreateWorkspaceRequest = {}  # type: ignore[typeddict-item]
        input_["account_access_type"] = account_access_type
        if client_token is not None:
            input_["client_token"] = client_token
        if organization_role_name is not None:
            input_["organization_role_name"] = organization_role_name
        input_["permission_type"] = permission_type
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if workspace_data_sources is not None:
            input_["workspace_data_sources"] = workspace_data_sources
        if workspace_description is not None:
            input_["workspace_description"] = workspace_description
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name
        if workspace_notification_destinations is not None:
            input_["workspace_notification_destinations"] = (
                workspace_notification_destinations
            )
        if workspace_organizational_units is not None:
            input_["workspace_organizational_units"] = workspace_organizational_units
        if workspace_role_arn is not None:
            input_["workspace_role_arn"] = workspace_role_arn
        input_["authentication_providers"] = authentication_providers
        if tags is not None:
            input_["tags"] = tags
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if configuration is not None:
            input_["configuration"] = configuration
        if network_access_control is not None:
            input_["network_access_control"] = network_access_control
        if grafana_version is not None:
            input_["grafana_version"] = grafana_version
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.describe_workspace_response.DescribeWorkspaceResponse":
        """<p>Displays information about one Amazon Managed Grafana workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to display information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.describe_workspace_request.DescribeWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.describe_workspace_response.DescribeWorkspaceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.describe_workspace

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.describe_workspace.async_describe_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.describe_workspace_request.DescribeWorkspaceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        account_access_type: Optional[
            "aws_sdk_grafana.types.account_access_type.AccountAccessType"
        ] = None,
        organization_role_name: Optional[
            "aws_sdk_grafana.types.organization_role_name.OrganizationRoleName"
        ] = None,
        permission_type: Optional[
            "aws_sdk_grafana.types.permission_type.PermissionType"
        ] = None,
        stack_set_name: Optional[
            "aws_sdk_grafana.types.stack_set_name.StackSetName"
        ] = None,
        workspace_data_sources: Optional[
            "aws_sdk_grafana.types.data_source_types_list.DataSourceTypesList"
        ] = None,
        workspace_description: Optional[
            "aws_sdk_grafana.types.description.Description"
        ] = None,
        workspace_name: Optional[
            "aws_sdk_grafana.types.workspace_name.WorkspaceName"
        ] = None,
        workspace_notification_destinations: Optional[
            "aws_sdk_grafana.types.notification_destinations_list.NotificationDestinationsList"
        ] = None,
        workspace_organizational_units: Optional[
            "aws_sdk_grafana.types.organizational_unit_list.OrganizationalUnitList"
        ] = None,
        workspace_role_arn: Optional[
            "aws_sdk_grafana.types.iam_role_arn.IamRoleArn"
        ] = None,
        vpc_configuration: Optional[
            "aws_sdk_grafana.types.vpc_configuration.VpcConfiguration"
        ] = None,
        remove_vpc_configuration: Optional[bool] = None,
        network_access_control: Optional[
            "aws_sdk_grafana.types.network_access_configuration.NetworkAccessConfiguration"
        ] = None,
        remove_network_access_configuration: Optional[bool] = None,
        ip_address_type: Optional[
            "aws_sdk_grafana.types.ip_address_type.IPAddressType"
        ] = None,
    ) -> "aws_sdk_grafana.types.update_workspace_response.UpdateWorkspaceResponse":
        """<p>Modifies an existing Amazon Managed Grafana workspace. If you use this operation and omit any optional parameters, the existing values of those parameters are not changed.</p> <p>To modify the user authentication methods that the workspace uses, such as SAML or IAM Identity Center, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspaceAuthentication.html\">UpdateWorkspaceAuthentication</a>.</p> <p>To modify which users in the workspace have the <code>Admin</code> and <code>Editor</code> Grafana roles, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdatePermissions.html\">UpdatePermissions</a>.</p>

        Args:
            account_access_type: <p>Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If you specify <code>ORGANIZATION</code>, you must specify which organizational units the workspace can access in the <code>workspaceOrganizationalUnits</code> parameter.</p>
            organization_role_name: <p>The name of an IAM role that already exists to use to access resources through Organizations. This can only be used with a workspace that has the <code>permissionType</code> set to <code>CUSTOMER_MANAGED</code>.</p>
            permission_type: <p>Use this parameter if you want to change a workspace from <code>SERVICE_MANAGED</code> to <code>CUSTOMER_MANAGED</code>. This allows you to manage the permissions that the workspace uses to access datasources and notification channels. If the workspace is in a member Amazon Web Services account of an organization, and that account is not a delegated administrator account, and you want the workspace to access data sources in other Amazon Web Services accounts in the organization, you must choose <code>CUSTOMER_MANAGED</code>.</p> <p>If you specify this as <code>CUSTOMER_MANAGED</code>, you must also specify a <code>workspaceRoleArn</code> that the workspace will use for accessing Amazon Web Services resources.</p> <p>For more information on the role and permissions needed, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html\">Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels</a> </p> <note> <p>Do not use this to convert a <code>CUSTOMER_MANAGED</code> workspace to <code>SERVICE_MANAGED</code>. Do not include this parameter if you want to leave the workspace as <code>SERVICE_MANAGED</code>.</p> <p>You can convert a <code>CUSTOMER_MANAGED</code> workspace to <code>SERVICE_MANAGED</code> using the Amazon Managed Grafana console. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-and-notification.html\">Managing permissions for data sources and notification channels</a>.</p> </note>
            stack_set_name: <p>The name of the CloudFormation stack set to use to generate IAM roles to be used for this workspace.</p>
            workspace_data_sources: <p>This parameter is for internal use only, and should not be used.</p>
            workspace_description: <p>A description for the workspace. This is used only to help you identify this workspace.</p>
            workspace_id: <p>The ID of the workspace to update.</p>
            workspace_name: <p>A new name for the workspace to update.</p>
            workspace_notification_destinations: <p>Specify the Amazon Web Services notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels.</p>
            workspace_organizational_units: <p>Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.</p>
            workspace_role_arn: <p>Specifies an IAM role that grants permissions to Amazon Web Services resources that the workspace accesses, such as data sources and notification channels. If this workspace has <code>permissionType</code> <code>CUSTOMER_MANAGED</code>, then this role is required.</p>
            vpc_configuration: <p>The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.</p>
            remove_vpc_configuration: <p>Whether to remove the VPC configuration from the workspace.</p> <p>Setting this to <code>true</code> and providing a <code>vpcConfiguration</code> to set will return an error.</p>
            network_access_control: <p>The configuration settings for network access to your workspace.</p> <p>When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization will still be required.</p> <p>If this is not configured, or is removed, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>
            remove_network_access_configuration: <p>Whether to remove the network access configuration from the workspace.</p> <p>Setting this to <code>true</code> and providing a <code>networkAccessControl</code> to set will return an error.</p> <p>If you remove this configuration by setting this to <code>true</code>, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>
            ip_address_type: <p>Specifies whether the workspace supports IPv4 only, or IPv4 and IPv6. Valid values are <code>IPv4</code> and <code>DualStack</code>. For more information about IP address types, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-nac.html\">Network access control</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.update_workspace_request.UpdateWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.update_workspace_response.UpdateWorkspaceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.update_workspace

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.update_workspace.async_update_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.update_workspace_request.UpdateWorkspaceRequest = {}  # type: ignore[typeddict-item]
        if account_access_type is not None:
            input_["account_access_type"] = account_access_type
        if organization_role_name is not None:
            input_["organization_role_name"] = organization_role_name
        if permission_type is not None:
            input_["permission_type"] = permission_type
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if workspace_data_sources is not None:
            input_["workspace_data_sources"] = workspace_data_sources
        if workspace_description is not None:
            input_["workspace_description"] = workspace_description
        input_["workspace_id"] = workspace_id
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name
        if workspace_notification_destinations is not None:
            input_["workspace_notification_destinations"] = (
                workspace_notification_destinations
            )
        if workspace_organizational_units is not None:
            input_["workspace_organizational_units"] = workspace_organizational_units
        if workspace_role_arn is not None:
            input_["workspace_role_arn"] = workspace_role_arn
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if remove_vpc_configuration is not None:
            input_["remove_vpc_configuration"] = remove_vpc_configuration
        if network_access_control is not None:
            input_["network_access_control"] = network_access_control
        if remove_network_access_configuration is not None:
            input_["remove_network_access_configuration"] = (
                remove_network_access_configuration
            )
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "aws_sdk_grafana.types.delete_workspace_response.DeleteWorkspaceResponse":
        """<p>Deletes an Amazon Managed Grafana workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.delete_workspace_request.DeleteWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.delete_workspace_response.DeleteWorkspaceResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.delete_workspace.async_delete_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.delete_workspace_request.DeleteWorkspaceRequest = {}  # type: ignore[typeddict-item]
        input_["workspace_id"] = workspace_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_grafana.types.list_workspaces_response.ListWorkspacesResponse":
        """<p>Returns a list of Amazon Managed Grafana workspaces in the account, with some information about each workspace. For more complete information about one workspace, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_DescribeWorkspace.html\">DescribeWorkspace</a>.</p>

        Args:
            max_results: <p>The maximum number of workspaces to include in the results.</p>
            next_token: <p>The token for the next set of workspaces to return. (You receive this token from a previous <code>ListWorkspaces</code> operation.)</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_grafana.types.list_workspaces_request.ListWorkspacesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_grafana.types.list_workspaces_response.ListWorkspacesResponse"
        ]:
            import aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspaces

            (
                output,
                http_response,
            ) = await aws_sdk_grafana._operations.aws_grafana_control_plane.list_workspaces.async_list_workspaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_grafana.types.list_workspaces_request.ListWorkspacesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
