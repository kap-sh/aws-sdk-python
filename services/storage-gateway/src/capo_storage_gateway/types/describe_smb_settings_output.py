"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeSMBSettingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.active_directory_status
    import capo_storage_gateway.types.boolean
    import capo_storage_gateway.types.domain_name
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.smb_local_groups
    import capo_storage_gateway.types.smb_security_strategy


class DescribeSMBSettingsOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    domain_name: NotRequired["capo_storage_gateway.types.domain_name.DomainName"]
    """<p>The name of the domain that the gateway is joined to.</p>"""
    active_directory_status: NotRequired[
        "capo_storage_gateway.types.active_directory_status.ActiveDirectoryStatus"
    ]
    """<p>Indicates the status of a gateway that is a member of the Active Directory domain.</p> <note> <p>This field is only used as part of a <code>JoinDomain</code> request. It is not affected by Active Directory connectivity changes that occur after the <code>JoinDomain</code> request succeeds.</p> </note> <ul> <li> <p> <code>ACCESS_DENIED</code>: Indicates that the <code>JoinDomain</code> operation failed due to an authentication error.</p> </li> <li> <p> <code>DETACHED</code>: Indicates that gateway is not joined to a domain.</p> </li> <li> <p> <code>JOINED</code>: Indicates that the gateway has successfully joined a domain.</p> </li> <li> <p> <code>JOINING</code>: Indicates that a <code>JoinDomain</code> operation is in progress.</p> </li> <li> <p> <code>NETWORK_ERROR</code>: Indicates that <code>JoinDomain</code> operation failed due to a network or connectivity error.</p> </li> <li> <p> <code>TIMEOUT</code>: Indicates that the <code>JoinDomain</code> operation failed because the operation didn't complete within the allotted time.</p> </li> <li> <p> <code>UNKNOWN_ERROR</code>: Indicates that the <code>JoinDomain</code> operation failed due to another type of error.</p> </li> </ul>"""
    smb_guest_password_set: NotRequired["capo_storage_gateway.types.boolean.Boolean"]
    """<p>This value is <code>true</code> if a password for the guest user <code>smbguest</code> is set, otherwise <code>false</code>. Only supported for S3 File Gateways.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""
    smb_security_strategy: NotRequired[
        "capo_storage_gateway.types.smb_security_strategy.SMBSecurityStrategy"
    ]
    """<p>The type of security strategy that was specified for file gateway.</p> <ul> <li> <p> <code>ClientSpecified</code>: If you choose this option, requests are established based on what is negotiated by the client. This option is recommended when you want to maximize compatibility across different clients in your environment. Supported only for S3 File Gateway.</p> </li> <li> <p> <code>MandatorySigning</code>: If you choose this option, File Gateway only allows connections from SMBv2 or SMBv3 clients that have signing turned on. This option works with SMB clients on Microsoft Windows Vista, Windows Server 2008, or later. </p> </li> <li> <p> <code>MandatoryEncryption</code>: If you choose this option, File Gateway only allows connections from SMBv3 clients that have encryption turned on. Both 256-bit and 128-bit algorithms are allowed. This option is recommended for environments that handle sensitive data. It works with SMB clients on Microsoft Windows 8, Windows Server 2012, or later.</p> </li> <li> <p> <code>MandatoryEncryptionNoAes128</code>: If you choose this option, File Gateway only allows connections from SMBv3 clients that use 256-bit AES encryption algorithms. 128-bit algorithms are not allowed. This option is recommended for environments that handle sensitive data. It works with SMB clients on Microsoft Windows 8, Windows Server 2012, or later.</p> </li> </ul>"""
    file_shares_visible: NotRequired["capo_storage_gateway.types.boolean.Boolean"]
    """<p>The shares on this gateway appear when listing shares. Only supported for S3 File Gateways. </p>"""
    smb_local_groups: NotRequired[
        "capo_storage_gateway.types.smb_local_groups.SMBLocalGroups"
    ]
    """<p>A list of Active Directory users and groups that have special permissions for SMB file shares on the gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSMBSettingsOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "active_directory_status" in value:
        import capo_storage_gateway.types.active_directory_status

        out["ActiveDirectoryStatus"] = (
            capo_storage_gateway.types.active_directory_status.serialize_aws_json_1_1(
                value["active_directory_status"]
            )
        )
    if "smb_guest_password_set" in value:
        out["SMBGuestPasswordSet"] = value["smb_guest_password_set"]
    if "smb_security_strategy" in value:
        import capo_storage_gateway.types.smb_security_strategy

        out["SMBSecurityStrategy"] = (
            capo_storage_gateway.types.smb_security_strategy.serialize_aws_json_1_1(
                value["smb_security_strategy"]
            )
        )
    if "file_shares_visible" in value:
        out["FileSharesVisible"] = value["file_shares_visible"]
    if "smb_local_groups" in value:
        import capo_storage_gateway.types.smb_local_groups

        out["SMBLocalGroups"] = (
            capo_storage_gateway.types.smb_local_groups.serialize_aws_json_1_1(
                value["smb_local_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSMBSettingsOutput:
    out: DescribeSMBSettingsOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "ActiveDirectoryStatus" in data:
        import capo_storage_gateway.types.active_directory_status

        out["active_directory_status"] = (
            capo_storage_gateway.types.active_directory_status.deserialize_aws_json_1_1(
                data["ActiveDirectoryStatus"]
            )
        )
    if "SMBGuestPasswordSet" in data:
        out["smb_guest_password_set"] = data["SMBGuestPasswordSet"]
    if "SMBSecurityStrategy" in data:
        import capo_storage_gateway.types.smb_security_strategy

        out["smb_security_strategy"] = (
            capo_storage_gateway.types.smb_security_strategy.deserialize_aws_json_1_1(
                data["SMBSecurityStrategy"]
            )
        )
    if "FileSharesVisible" in data:
        out["file_shares_visible"] = data["FileSharesVisible"]
    if "SMBLocalGroups" in data:
        import capo_storage_gateway.types.smb_local_groups

        out["smb_local_groups"] = (
            capo_storage_gateway.types.smb_local_groups.deserialize_aws_json_1_1(
                data["SMBLocalGroups"]
            )
        )
    return out
