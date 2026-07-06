"""Generated from Smithy shape ``com.amazonaws.fsx#SelfManagedActiveDirectoryConfigurationUpdates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.active_directory_fully_qualified_name
    import aws_sdk_fsx.types.customer_secrets_manager_arn
    import aws_sdk_fsx.types.directory_password
    import aws_sdk_fsx.types.directory_user_name
    import aws_sdk_fsx.types.dns_ips
    import aws_sdk_fsx.types.file_system_administrators_group_name
    import aws_sdk_fsx.types.organizational_unit_distinguished_name


class SelfManagedActiveDirectoryConfigurationUpdates(TypedDict, closed=True):
    user_name: NotRequired["aws_sdk_fsx.types.directory_user_name.DirectoryUserName"]
    """<p>Specifies the updated user name for the service account on your self-managed Active Directory domain. Amazon FSx uses this account to join to your self-managed Active Directory domain.</p> <p>This account must have the permissions required to join computers to the domain in the organizational unit provided in <code>OrganizationalUnitDistinguishedName</code>.</p>"""
    password: NotRequired["aws_sdk_fsx.types.directory_password.DirectoryPassword"]
    """<p>Specifies the updated password for the service account on your self-managed Active Directory domain. Amazon FSx uses this account to join to your self-managed Active Directory domain.</p>"""
    dns_ips: NotRequired["aws_sdk_fsx.types.dns_ips.DnsIps"]
    """<p>A list of up to three DNS server or domain controller IP addresses in your self-managed Active Directory domain.</p>"""
    domain_name: NotRequired[
        "aws_sdk_fsx.types.active_directory_fully_qualified_name.ActiveDirectoryFullyQualifiedName"
    ]
    """<p>Specifies an updated fully qualified domain name of your self-managed Active Directory configuration.</p>"""
    organizational_unit_distinguished_name: NotRequired[
        "aws_sdk_fsx.types.organizational_unit_distinguished_name.OrganizationalUnitDistinguishedName"
    ]
    """<p>Specifies an updated fully qualified distinguished name of the organization unit within your self-managed Active Directory.</p>"""
    file_system_administrators_group: NotRequired[
        "aws_sdk_fsx.types.file_system_administrators_group_name.FileSystemAdministratorsGroupName"
    ]
    """<p>For FSx for ONTAP file systems only - Specifies the updated name of the self-managed Active Directory domain group whose members are granted administrative privileges for the Amazon FSx resource.</p>"""
    domain_join_service_account_secret: NotRequired[
        "aws_sdk_fsx.types.customer_secrets_manager_arn.CustomerSecretsManagerARN"
    ]
    """<p>Specifies the updated Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret containing the self-managed Active Directory domain join service account credentials. Amazon FSx uses this account to join to your self-managed Active Directory domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: SelfManagedActiveDirectoryConfigurationUpdates,
) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "password" in value:
        out["Password"] = value["password"]
    if "dns_ips" in value:
        import aws_sdk_fsx.types.dns_ips

        out["DnsIps"] = aws_sdk_fsx.types.dns_ips.serialize_aws_json_1_1(
            value["dns_ips"]
        )
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "organizational_unit_distinguished_name" in value:
        out["OrganizationalUnitDistinguishedName"] = value[
            "organizational_unit_distinguished_name"
        ]
    if "file_system_administrators_group" in value:
        out["FileSystemAdministratorsGroup"] = value["file_system_administrators_group"]
    if "domain_join_service_account_secret" in value:
        out["DomainJoinServiceAccountSecret"] = value[
            "domain_join_service_account_secret"
        ]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> SelfManagedActiveDirectoryConfigurationUpdates:
    out: SelfManagedActiveDirectoryConfigurationUpdates = {}  # type: ignore[typeddict-item]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "Password" in data:
        out["password"] = data["Password"]
    if "DnsIps" in data:
        import aws_sdk_fsx.types.dns_ips

        out["dns_ips"] = aws_sdk_fsx.types.dns_ips.deserialize_aws_json_1_1(
            data["DnsIps"]
        )
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "OrganizationalUnitDistinguishedName" in data:
        out["organizational_unit_distinguished_name"] = data[
            "OrganizationalUnitDistinguishedName"
        ]
    if "FileSystemAdministratorsGroup" in data:
        out["file_system_administrators_group"] = data["FileSystemAdministratorsGroup"]
    if "DomainJoinServiceAccountSecret" in data:
        out["domain_join_service_account_secret"] = data[
            "DomainJoinServiceAccountSecret"
        ]
    return out
