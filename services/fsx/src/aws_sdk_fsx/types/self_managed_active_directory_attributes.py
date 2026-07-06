"""Generated from Smithy shape ``com.amazonaws.fsx#SelfManagedActiveDirectoryAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.active_directory_fully_qualified_name
    import aws_sdk_fsx.types.customer_secrets_manager_arn
    import aws_sdk_fsx.types.directory_user_name
    import aws_sdk_fsx.types.dns_ips
    import aws_sdk_fsx.types.file_system_administrators_group_name
    import aws_sdk_fsx.types.organizational_unit_distinguished_name


class SelfManagedActiveDirectoryAttributes(TypedDict, closed=True):
    domain_name: NotRequired[
        "aws_sdk_fsx.types.active_directory_fully_qualified_name.ActiveDirectoryFullyQualifiedName"
    ]
    """<p>The fully qualified domain name of the self-managed AD directory.</p>"""
    organizational_unit_distinguished_name: NotRequired[
        "aws_sdk_fsx.types.organizational_unit_distinguished_name.OrganizationalUnitDistinguishedName"
    ]
    """<p>The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.</p>"""
    file_system_administrators_group: NotRequired[
        "aws_sdk_fsx.types.file_system_administrators_group_name.FileSystemAdministratorsGroupName"
    ]
    """<p>The name of the domain group whose members have administrative privileges for the FSx file system.</p>"""
    user_name: NotRequired["aws_sdk_fsx.types.directory_user_name.DirectoryUserName"]
    """<p>The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.</p>"""
    dns_ips: NotRequired["aws_sdk_fsx.types.dns_ips.DnsIps"]
    """<p>A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory.</p>"""
    domain_join_service_account_secret: NotRequired[
        "aws_sdk_fsx.types.customer_secrets_manager_arn.CustomerSecretsManagerARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret containing the service account credentials used to join the file system to your self-managed Active Directory domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelfManagedActiveDirectoryAttributes) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> SelfManagedActiveDirectoryAttributes:
    out: SelfManagedActiveDirectoryAttributes = {}  # type: ignore[typeddict-item]
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
