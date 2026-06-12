"""Generated from Smithy shape ``com.amazonaws.fsx#SelfManagedActiveDirectoryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.active_directory_fully_qualified_name
    import aws_sdk_fsx.types.customer_secrets_manager_arn
    import aws_sdk_fsx.types.directory_password
    import aws_sdk_fsx.types.directory_user_name
    import aws_sdk_fsx.types.dns_ips
    import aws_sdk_fsx.types.file_system_administrators_group_name
    import aws_sdk_fsx.types.organizational_unit_distinguished_name


class SelfManagedActiveDirectoryConfiguration(TypedDict):
    domain_name: NotRequired[
        "aws_sdk_fsx.types.active_directory_fully_qualified_name.ActiveDirectoryFullyQualifiedName"
    ]
    """<p>The fully qualified domain name of the self-managed AD directory, such as <code>corp.example.com</code>.</p>"""
    organizational_unit_distinguished_name: NotRequired[
        "aws_sdk_fsx.types.organizational_unit_distinguished_name.OrganizationalUnitDistinguishedName"
    ]
    """<p>(Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory. Amazon FSx only accepts OU as the direct parent of the file system. An example is <code>OU=FSx,DC=yourdomain,DC=corp,DC=com</code>. To learn more, see <a href=\"https://tools.ietf.org/html/rfc2253\">RFC 2253</a>. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. </p> <important> <p>Only Organizational Unit (OU) objects can be the direct parent of the file system that you're creating.</p> </important>"""
    file_system_administrators_group: NotRequired[
        "aws_sdk_fsx.types.file_system_administrators_group_name.FileSystemAdministratorsGroupName"
    ]
    """<p>(Optional) The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don't provide one, your AD domain's Domain Admins group is used.</p>"""
    user_name: NotRequired["aws_sdk_fsx.types.directory_user_name.DirectoryUserName"]
    """<p>The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain. This account must have the permission to join computers to the domain in the organizational unit provided in <code>OrganizationalUnitDistinguishedName</code>, or in the default location of your AD domain.</p>"""
    password: NotRequired["aws_sdk_fsx.types.directory_password.DirectoryPassword"]
    """<p>The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.</p>"""
    dns_ips: NotRequired["aws_sdk_fsx.types.dns_ips.DnsIps"]
    """<p>A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory. </p>"""
    domain_join_service_account_secret: NotRequired[
        "aws_sdk_fsx.types.customer_secrets_manager_arn.CustomerSecretsManagerARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret containing the self-managed Active Directory domain join service account credentials. When provided, Amazon FSx uses the credentials stored in this secret to join the file system to your self-managed Active Directory domain.</p> <p>The secret must contain two key-value pairs:</p> <ul> <li> <p> <code>CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME</code> - The username for the service account</p> </li> <li> <p> <code>CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD</code> - The password for the service account</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-manage-prereqs.html\"> Using Amazon FSx for Windows with your self-managed Microsoft Active Directory</a> or <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/self-manage-prereqs.html\"> Using Amazon FSx for ONTAP with your self-managed Microsoft Active Directory</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelfManagedActiveDirectoryConfiguration) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "organizational_unit_distinguished_name" in value:
        out["OrganizationalUnitDistinguishedName"] = value[
            "organizational_unit_distinguished_name"
        ]
    if "file_system_administrators_group" in value:
        out["FileSystemAdministratorsGroup"] = value["file_system_administrators_group"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "password" in value:
        out["Password"] = value["password"]
    if "dns_ips" in value:
        import aws_sdk_fsx.types.dns_ips

        out["DnsIps"] = aws_sdk_fsx.types.dns_ips.serialize_aws_json_1_1(
            value["dns_ips"]
        )
    if "domain_join_service_account_secret" in value:
        out["DomainJoinServiceAccountSecret"] = value[
            "domain_join_service_account_secret"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> SelfManagedActiveDirectoryConfiguration:
    out: SelfManagedActiveDirectoryConfiguration = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "OrganizationalUnitDistinguishedName" in data:
        out["organizational_unit_distinguished_name"] = data[
            "OrganizationalUnitDistinguishedName"
        ]
    if "FileSystemAdministratorsGroup" in data:
        out["file_system_administrators_group"] = data["FileSystemAdministratorsGroup"]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "Password" in data:
        out["password"] = data["Password"]
    if "DnsIps" in data:
        import aws_sdk_fsx.types.dns_ips

        out["dns_ips"] = aws_sdk_fsx.types.dns_ips.deserialize_aws_json_1_1(
            data["DnsIps"]
        )
    if "DomainJoinServiceAccountSecret" in data:
        out["domain_join_service_account_secret"] = data[
            "DomainJoinServiceAccountSecret"
        ]
    return out
