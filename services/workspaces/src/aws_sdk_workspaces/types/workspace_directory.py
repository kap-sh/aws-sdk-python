"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceDirectory``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.active_directory_config
    import aws_sdk_workspaces.types.alias
    import aws_sdk_workspaces.types.arn
    import aws_sdk_workspaces.types.certificate_based_auth_properties
    import aws_sdk_workspaces.types.default_workspace_creation_properties
    import aws_sdk_workspaces.types.description
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.directory_name
    import aws_sdk_workspaces.types.dns_ip_addresses
    import aws_sdk_workspaces.types.dns_ipv6_addresses
    import aws_sdk_workspaces.types.endpoint_encryption_mode
    import aws_sdk_workspaces.types.idc_config
    import aws_sdk_workspaces.types.ip_group_id_list
    import aws_sdk_workspaces.types.microsoft_entra_config
    import aws_sdk_workspaces.types.registration_code
    import aws_sdk_workspaces.types.saml_properties
    import aws_sdk_workspaces.types.security_group_id
    import aws_sdk_workspaces.types.selfservice_permissions
    import aws_sdk_workspaces.types.streaming_properties
    import aws_sdk_workspaces.types.subnet_ids
    import aws_sdk_workspaces.types.tenancy
    import aws_sdk_workspaces.types.user_identity_type
    import aws_sdk_workspaces.types.user_name
    import aws_sdk_workspaces.types.workspace_access_properties
    import aws_sdk_workspaces.types.workspace_directory_description
    import aws_sdk_workspaces.types.workspace_directory_name
    import aws_sdk_workspaces.types.workspace_directory_state
    import aws_sdk_workspaces.types.workspace_directory_type
    import aws_sdk_workspaces.types.workspace_type


class WorkspaceDirectory(TypedDict):
    directory_id: NotRequired["aws_sdk_workspaces.types.directory_id.DirectoryId"]
    """<p>The directory identifier.</p>"""
    alias: NotRequired["aws_sdk_workspaces.types.alias.Alias"]
    """<p>The directory alias.</p>"""
    directory_name: NotRequired["aws_sdk_workspaces.types.directory_name.DirectoryName"]
    """<p>The name of the directory.</p>"""
    registration_code: NotRequired[
        "aws_sdk_workspaces.types.registration_code.RegistrationCode"
    ]
    """<p>The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.</p>"""
    subnet_ids: NotRequired["aws_sdk_workspaces.types.subnet_ids.SubnetIds"]
    """<p>The identifiers of the subnets used with the directory.</p>"""
    dns_ip_addresses: NotRequired[
        "aws_sdk_workspaces.types.dns_ip_addresses.DnsIpAddresses"
    ]
    """<p>The IP addresses of the DNS servers for the directory.</p>"""
    dns_ipv6_addresses: NotRequired[
        "aws_sdk_workspaces.types.dns_ipv6_addresses.DnsIpv6Addresses"
    ]
    """<p>The IPv6 addresses of the DNS servers for the directory.</p>"""
    customer_user_name: NotRequired["aws_sdk_workspaces.types.user_name.UserName"]
    """<p>The user name for the service account.</p>"""
    iam_role_id: NotRequired["aws_sdk_workspaces.types.arn.ARN"]
    """<p>The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.</p>"""
    directory_type: NotRequired[
        "aws_sdk_workspaces.types.workspace_directory_type.WorkspaceDirectoryType"
    ]
    """<p>The directory type.</p>"""
    workspace_security_group_id: NotRequired[
        "aws_sdk_workspaces.types.security_group_id.SecurityGroupId"
    ]
    """<p>The identifier of the security group that is assigned to new WorkSpaces.</p>"""
    state: NotRequired[
        "aws_sdk_workspaces.types.workspace_directory_state.WorkspaceDirectoryState"
    ]
    r"""<p>The state of the directory's registration with Amazon WorkSpaces. After a directory is deregistered, the <code>DEREGISTERED</code> state is returned very briefly before the directory metadata is cleaned up, so this state is rarely returned. To confirm that a directory is deregistered, check for the directory ID by using <a href=\"https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectories.html\"> DescribeWorkspaceDirectories</a>. If the directory ID isn't returned, then the directory has been successfully deregistered.</p>"""
    workspace_creation_properties: NotRequired[
        "aws_sdk_workspaces.types.default_workspace_creation_properties.DefaultWorkspaceCreationProperties"
    ]
    """<p>The default creation properties for all WorkSpaces in the directory.</p>"""
    ip_group_ids: NotRequired["aws_sdk_workspaces.types.ip_group_id_list.IpGroupIdList"]
    """<p>The identifiers of the IP access control groups associated with the directory.</p>"""
    workspace_access_properties: NotRequired[
        "aws_sdk_workspaces.types.workspace_access_properties.WorkspaceAccessProperties"
    ]
    """<p>The devices and operating systems that users can use to access WorkSpaces.</p>"""
    tenancy: NotRequired["aws_sdk_workspaces.types.tenancy.Tenancy"]
    r"""<p>Specifies whether the directory is dedicated or shared. To use Bring Your Own License (BYOL), this value must be set to <code>DEDICATED</code>. For more information, see <a href=\"https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html\">Bring Your Own Windows Desktop Images</a>.</p>"""
    selfservice_permissions: NotRequired[
        "aws_sdk_workspaces.types.selfservice_permissions.SelfservicePermissions"
    ]
    """<p>The default self-service permissions for WorkSpaces in the directory.</p>"""
    saml_properties: NotRequired[
        "aws_sdk_workspaces.types.saml_properties.SamlProperties"
    ]
    """<p>Describes the enablement status, user access URL, and relay state parameter name that are used for configuring federation with an SAML 2.0 identity provider.</p>"""
    certificate_based_auth_properties: NotRequired[
        "aws_sdk_workspaces.types.certificate_based_auth_properties.CertificateBasedAuthProperties"
    ]
    """<p>The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory for WorkSpaces login.</p>"""
    endpoint_encryption_mode: NotRequired[
        "aws_sdk_workspaces.types.endpoint_encryption_mode.EndpointEncryptionMode"
    ]
    """<p>Endpoint encryption mode that allows you to configure the specified directory between Standard TLS and FIPS 140-2 validated mode.</p>"""
    microsoft_entra_config: NotRequired[
        "aws_sdk_workspaces.types.microsoft_entra_config.MicrosoftEntraConfig"
    ]
    """<p>Specifies details about Microsoft Entra configurations.</p>"""
    workspace_directory_name: NotRequired[
        "aws_sdk_workspaces.types.workspace_directory_name.WorkspaceDirectoryName"
    ]
    """<p>The name fo the WorkSpace directory.</p>"""
    workspace_directory_description: NotRequired[
        "aws_sdk_workspaces.types.workspace_directory_description.WorkspaceDirectoryDescription"
    ]
    """<p>The description of the WorkSpace directory</p>"""
    user_identity_type: NotRequired[
        "aws_sdk_workspaces.types.user_identity_type.UserIdentityType"
    ]
    """<p>Indicates the identity type of the specifired user.</p>"""
    workspace_type: NotRequired["aws_sdk_workspaces.types.workspace_type.WorkspaceType"]
    """<p>Indicates whether the directory's WorkSpace type is personal or pools.</p>"""
    idc_config: NotRequired["aws_sdk_workspaces.types.idc_config.IDCConfig"]
    """<p>Specifies details about identity center configurations.</p>"""
    active_directory_config: NotRequired[
        "aws_sdk_workspaces.types.active_directory_config.ActiveDirectoryConfig"
    ]
    """<p>Information about the Active Directory config.</p>"""
    streaming_properties: NotRequired[
        "aws_sdk_workspaces.types.streaming_properties.StreamingProperties"
    ]
    """<p>The streaming properties to configure.</p>"""
    error_message: NotRequired["aws_sdk_workspaces.types.description.Description"]
    """<p>The error message returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceDirectory) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "directory_name" in value:
        out["DirectoryName"] = value["directory_name"]
    if "registration_code" in value:
        out["RegistrationCode"] = value["registration_code"]
    if "subnet_ids" in value:
        import aws_sdk_workspaces.types.subnet_ids

        out["SubnetIds"] = aws_sdk_workspaces.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "dns_ip_addresses" in value:
        import aws_sdk_workspaces.types.dns_ip_addresses

        out["DnsIpAddresses"] = (
            aws_sdk_workspaces.types.dns_ip_addresses.serialize_aws_json_1_1(
                value["dns_ip_addresses"]
            )
        )
    if "dns_ipv6_addresses" in value:
        import aws_sdk_workspaces.types.dns_ipv6_addresses

        out["DnsIpv6Addresses"] = (
            aws_sdk_workspaces.types.dns_ipv6_addresses.serialize_aws_json_1_1(
                value["dns_ipv6_addresses"]
            )
        )
    if "customer_user_name" in value:
        out["CustomerUserName"] = value["customer_user_name"]
    if "iam_role_id" in value:
        out["IamRoleId"] = value["iam_role_id"]
    if "directory_type" in value:
        import aws_sdk_workspaces.types.workspace_directory_type

        out["DirectoryType"] = (
            aws_sdk_workspaces.types.workspace_directory_type.serialize_aws_json_1_1(
                value["directory_type"]
            )
        )
    if "workspace_security_group_id" in value:
        out["WorkspaceSecurityGroupId"] = value["workspace_security_group_id"]
    if "state" in value:
        import aws_sdk_workspaces.types.workspace_directory_state

        out["State"] = (
            aws_sdk_workspaces.types.workspace_directory_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "workspace_creation_properties" in value:
        import aws_sdk_workspaces.types.default_workspace_creation_properties

        out["WorkspaceCreationProperties"] = (
            aws_sdk_workspaces.types.default_workspace_creation_properties.serialize_aws_json_1_1(
                value["workspace_creation_properties"]
            )
        )
    if "ip_group_ids" in value:
        import aws_sdk_workspaces.types.ip_group_id_list

        out["ipGroupIds"] = (
            aws_sdk_workspaces.types.ip_group_id_list.serialize_aws_json_1_1(
                value["ip_group_ids"]
            )
        )
    if "workspace_access_properties" in value:
        import aws_sdk_workspaces.types.workspace_access_properties

        out["WorkspaceAccessProperties"] = (
            aws_sdk_workspaces.types.workspace_access_properties.serialize_aws_json_1_1(
                value["workspace_access_properties"]
            )
        )
    if "tenancy" in value:
        import aws_sdk_workspaces.types.tenancy

        out["Tenancy"] = aws_sdk_workspaces.types.tenancy.serialize_aws_json_1_1(
            value["tenancy"]
        )
    if "selfservice_permissions" in value:
        import aws_sdk_workspaces.types.selfservice_permissions

        out["SelfservicePermissions"] = (
            aws_sdk_workspaces.types.selfservice_permissions.serialize_aws_json_1_1(
                value["selfservice_permissions"]
            )
        )
    if "saml_properties" in value:
        import aws_sdk_workspaces.types.saml_properties

        out["SamlProperties"] = (
            aws_sdk_workspaces.types.saml_properties.serialize_aws_json_1_1(
                value["saml_properties"]
            )
        )
    if "certificate_based_auth_properties" in value:
        import aws_sdk_workspaces.types.certificate_based_auth_properties

        out["CertificateBasedAuthProperties"] = (
            aws_sdk_workspaces.types.certificate_based_auth_properties.serialize_aws_json_1_1(
                value["certificate_based_auth_properties"]
            )
        )
    if "endpoint_encryption_mode" in value:
        import aws_sdk_workspaces.types.endpoint_encryption_mode

        out["EndpointEncryptionMode"] = (
            aws_sdk_workspaces.types.endpoint_encryption_mode.serialize_aws_json_1_1(
                value["endpoint_encryption_mode"]
            )
        )
    if "microsoft_entra_config" in value:
        import aws_sdk_workspaces.types.microsoft_entra_config

        out["MicrosoftEntraConfig"] = (
            aws_sdk_workspaces.types.microsoft_entra_config.serialize_aws_json_1_1(
                value["microsoft_entra_config"]
            )
        )
    if "workspace_directory_name" in value:
        out["WorkspaceDirectoryName"] = value["workspace_directory_name"]
    if "workspace_directory_description" in value:
        out["WorkspaceDirectoryDescription"] = value["workspace_directory_description"]
    if "user_identity_type" in value:
        import aws_sdk_workspaces.types.user_identity_type

        out["UserIdentityType"] = (
            aws_sdk_workspaces.types.user_identity_type.serialize_aws_json_1_1(
                value["user_identity_type"]
            )
        )
    if "workspace_type" in value:
        import aws_sdk_workspaces.types.workspace_type

        out["WorkspaceType"] = (
            aws_sdk_workspaces.types.workspace_type.serialize_aws_json_1_1(
                value["workspace_type"]
            )
        )
    if "idc_config" in value:
        import aws_sdk_workspaces.types.idc_config

        out["IDCConfig"] = aws_sdk_workspaces.types.idc_config.serialize_aws_json_1_1(
            value["idc_config"]
        )
    if "active_directory_config" in value:
        import aws_sdk_workspaces.types.active_directory_config

        out["ActiveDirectoryConfig"] = (
            aws_sdk_workspaces.types.active_directory_config.serialize_aws_json_1_1(
                value["active_directory_config"]
            )
        )
    if "streaming_properties" in value:
        import aws_sdk_workspaces.types.streaming_properties

        out["StreamingProperties"] = (
            aws_sdk_workspaces.types.streaming_properties.serialize_aws_json_1_1(
                value["streaming_properties"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspaceDirectory:
    out: WorkspaceDirectory = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    if "DirectoryName" in data:
        out["directory_name"] = data["DirectoryName"]
    if "RegistrationCode" in data:
        out["registration_code"] = data["RegistrationCode"]
    if "SubnetIds" in data:
        import aws_sdk_workspaces.types.subnet_ids

        out["subnet_ids"] = (
            aws_sdk_workspaces.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    if "DnsIpAddresses" in data:
        import aws_sdk_workspaces.types.dns_ip_addresses

        out["dns_ip_addresses"] = (
            aws_sdk_workspaces.types.dns_ip_addresses.deserialize_aws_json_1_1(
                data["DnsIpAddresses"]
            )
        )
    if "DnsIpv6Addresses" in data:
        import aws_sdk_workspaces.types.dns_ipv6_addresses

        out["dns_ipv6_addresses"] = (
            aws_sdk_workspaces.types.dns_ipv6_addresses.deserialize_aws_json_1_1(
                data["DnsIpv6Addresses"]
            )
        )
    if "CustomerUserName" in data:
        out["customer_user_name"] = data["CustomerUserName"]
    if "IamRoleId" in data:
        out["iam_role_id"] = data["IamRoleId"]
    if "DirectoryType" in data:
        import aws_sdk_workspaces.types.workspace_directory_type

        out["directory_type"] = (
            aws_sdk_workspaces.types.workspace_directory_type.deserialize_aws_json_1_1(
                data["DirectoryType"]
            )
        )
    if "WorkspaceSecurityGroupId" in data:
        out["workspace_security_group_id"] = data["WorkspaceSecurityGroupId"]
    if "State" in data:
        import aws_sdk_workspaces.types.workspace_directory_state

        out["state"] = (
            aws_sdk_workspaces.types.workspace_directory_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "WorkspaceCreationProperties" in data:
        import aws_sdk_workspaces.types.default_workspace_creation_properties

        out["workspace_creation_properties"] = (
            aws_sdk_workspaces.types.default_workspace_creation_properties.deserialize_aws_json_1_1(
                data["WorkspaceCreationProperties"]
            )
        )
    if "ipGroupIds" in data:
        import aws_sdk_workspaces.types.ip_group_id_list

        out["ip_group_ids"] = (
            aws_sdk_workspaces.types.ip_group_id_list.deserialize_aws_json_1_1(
                data["ipGroupIds"]
            )
        )
    if "WorkspaceAccessProperties" in data:
        import aws_sdk_workspaces.types.workspace_access_properties

        out["workspace_access_properties"] = (
            aws_sdk_workspaces.types.workspace_access_properties.deserialize_aws_json_1_1(
                data["WorkspaceAccessProperties"]
            )
        )
    if "Tenancy" in data:
        import aws_sdk_workspaces.types.tenancy

        out["tenancy"] = aws_sdk_workspaces.types.tenancy.deserialize_aws_json_1_1(
            data["Tenancy"]
        )
    if "SelfservicePermissions" in data:
        import aws_sdk_workspaces.types.selfservice_permissions

        out["selfservice_permissions"] = (
            aws_sdk_workspaces.types.selfservice_permissions.deserialize_aws_json_1_1(
                data["SelfservicePermissions"]
            )
        )
    if "SamlProperties" in data:
        import aws_sdk_workspaces.types.saml_properties

        out["saml_properties"] = (
            aws_sdk_workspaces.types.saml_properties.deserialize_aws_json_1_1(
                data["SamlProperties"]
            )
        )
    if "CertificateBasedAuthProperties" in data:
        import aws_sdk_workspaces.types.certificate_based_auth_properties

        out["certificate_based_auth_properties"] = (
            aws_sdk_workspaces.types.certificate_based_auth_properties.deserialize_aws_json_1_1(
                data["CertificateBasedAuthProperties"]
            )
        )
    if "EndpointEncryptionMode" in data:
        import aws_sdk_workspaces.types.endpoint_encryption_mode

        out["endpoint_encryption_mode"] = (
            aws_sdk_workspaces.types.endpoint_encryption_mode.deserialize_aws_json_1_1(
                data["EndpointEncryptionMode"]
            )
        )
    if "MicrosoftEntraConfig" in data:
        import aws_sdk_workspaces.types.microsoft_entra_config

        out["microsoft_entra_config"] = (
            aws_sdk_workspaces.types.microsoft_entra_config.deserialize_aws_json_1_1(
                data["MicrosoftEntraConfig"]
            )
        )
    if "WorkspaceDirectoryName" in data:
        out["workspace_directory_name"] = data["WorkspaceDirectoryName"]
    if "WorkspaceDirectoryDescription" in data:
        out["workspace_directory_description"] = data["WorkspaceDirectoryDescription"]
    if "UserIdentityType" in data:
        import aws_sdk_workspaces.types.user_identity_type

        out["user_identity_type"] = (
            aws_sdk_workspaces.types.user_identity_type.deserialize_aws_json_1_1(
                data["UserIdentityType"]
            )
        )
    if "WorkspaceType" in data:
        import aws_sdk_workspaces.types.workspace_type

        out["workspace_type"] = (
            aws_sdk_workspaces.types.workspace_type.deserialize_aws_json_1_1(
                data["WorkspaceType"]
            )
        )
    if "IDCConfig" in data:
        import aws_sdk_workspaces.types.idc_config

        out["idc_config"] = (
            aws_sdk_workspaces.types.idc_config.deserialize_aws_json_1_1(
                data["IDCConfig"]
            )
        )
    if "ActiveDirectoryConfig" in data:
        import aws_sdk_workspaces.types.active_directory_config

        out["active_directory_config"] = (
            aws_sdk_workspaces.types.active_directory_config.deserialize_aws_json_1_1(
                data["ActiveDirectoryConfig"]
            )
        )
    if "StreamingProperties" in data:
        import aws_sdk_workspaces.types.streaming_properties

        out["streaming_properties"] = (
            aws_sdk_workspaces.types.streaming_properties.deserialize_aws_json_1_1(
                data["StreamingProperties"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
