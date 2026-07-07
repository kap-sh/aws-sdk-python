"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationSmbRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.agent_arn_list
    import aws_sdk_datasync.types.cmk_secret_config
    import aws_sdk_datasync.types.custom_secret_config
    import aws_sdk_datasync.types.dns_ip_list
    import aws_sdk_datasync.types.input_tag_list
    import aws_sdk_datasync.types.kerberos_keytab_file
    import aws_sdk_datasync.types.kerberos_krb5_conf_file
    import aws_sdk_datasync.types.kerberos_principal
    import aws_sdk_datasync.types.server_hostname
    import aws_sdk_datasync.types.smb_authentication_type
    import aws_sdk_datasync.types.smb_domain
    import aws_sdk_datasync.types.smb_mount_options
    import aws_sdk_datasync.types.smb_password
    import aws_sdk_datasync.types.smb_subdirectory
    import aws_sdk_datasync.types.smb_user


class CreateLocationSmbRequest(TypedDict, closed=True):
    subdirectory: "aws_sdk_datasync.types.smb_subdirectory.SmbSubdirectory"
    r"""<p>Specifies the name of the share exported by your SMB file server where DataSync will read or write data. You can include a subdirectory in the share path (for example, <code>/path/to/subdirectory</code>). Make sure that other SMB clients in your network can also mount this path.</p> <p>To copy all data in the subdirectory, DataSync must be able to mount the SMB share and access all of its data. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions\">Providing DataSync access to SMB file servers</a>.</p>"""
    server_hostname: "aws_sdk_datasync.types.server_hostname.ServerHostname"
    """<p>Specifies the domain name or IP address (IPv4 or IPv6) of the SMB file server that your DataSync agent connects to.</p> <note> <p>If you're using Kerberos authentication, you must specify a domain name.</p> </note>"""
    user: NotRequired["aws_sdk_datasync.types.smb_user.SmbUser"]
    r"""<p>Specifies the user that can mount and access the files, folders, and file metadata in your SMB file server. This parameter applies only if <code>AuthenticationType</code> is set to <code>NTLM</code>.</p> <p>For information about choosing a user with the right level of access for your transfer, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions\">Providing DataSync access to SMB file servers</a>.</p>"""
    domain: NotRequired["aws_sdk_datasync.types.smb_domain.SmbDomain"]
    """<p>Specifies the Windows domain name that your SMB file server belongs to. This parameter applies only if <code>AuthenticationType</code> is set to <code>NTLM</code>.</p> <p>If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right file server.</p>"""
    password: NotRequired["aws_sdk_datasync.types.smb_password.SmbPassword"]
    """<p>Specifies the password of the user who can mount your SMB file server and has permission to access the files and folders involved in your transfer. This parameter applies only if <code>AuthenticationType</code> is set to <code>NTLM</code>.</p>"""
    cmk_secret_config: NotRequired[
        "aws_sdk_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    r"""<p>Specifies configuration information for a DataSync-managed secret, either a <code>Password</code> or <code>KerberosKeytab</code> (for <code>NTLM</code> (default) and <code>KERBEROS</code> authentication types, respectively) that DataSync uses to access a specific SMB storage location, with a customer-managed KMS key.</p> <p>When you include this parameter as part of a <code>CreateLocationSmbRequest</code> request, you provide only the KMS key ARN. DataSync uses this KMS key together with either the <code>Password</code> or <code>KerberosKeytab</code> you specify to create a DataSync-managed secret to store the location access credentials.</p> <p>Make sure that DataSync has permission to access the KMS key that you specify. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key\"> Using a service-managed secret encrypted with a custom KMS key</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with either <code>Password</code> or <code>KerberosKeytab</code>) or <code>CustomSecretConfig</code> (without any <code>Password</code> and <code>KerberosKeytab</code>) to provide credentials for a <code>CreateLocationSmbRequest</code> request. Do not provide both <code>CmkSecretConfig</code> and <code>CustomSecretConfig</code> parameters for the same request.</p> </note>"""
    custom_secret_config: NotRequired[
        "aws_sdk_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    r"""<p>Specifies configuration information for a customer-managed Secrets Manager secret where the SMB storage location credentials is stored in Secrets Manager as plain text (for <code>Password</code>) or binary (for <code>KerberosKeytab</code>). This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key\"> Using a secret that you manage</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>SasConfiguration</code>) or <code>CustomSecretConfig</code> (without <code>SasConfiguration</code>) to provide credentials for a <code>CreateLocationSmbRequest</code> request. Do not provide both parameters for the same request.</p> </note>"""
    agent_arns: "aws_sdk_datasync.types.agent_arn_list.AgentArnList"
    """<p>Specifies the DataSync agent (or agents) that can connect to your SMB file server. You specify an agent by using its Amazon Resource Name (ARN).</p>"""
    mount_options: NotRequired[
        "aws_sdk_datasync.types.smb_mount_options.SmbMountOptions"
    ]
    """<p>Specifies the version of the SMB protocol that DataSync uses to access your SMB file server.</p>"""
    tags: NotRequired["aws_sdk_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your location.</p>"""
    authentication_type: NotRequired[
        "aws_sdk_datasync.types.smb_authentication_type.SmbAuthenticationType"
    ]
    r"""<p>Specifies the authentication protocol that DataSync uses to connect to your SMB file server. DataSync supports <code>NTLM</code> (default) and <code>KERBEROS</code> authentication.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions\">Providing DataSync access to SMB file servers</a>.</p>"""
    dns_ip_addresses: NotRequired["aws_sdk_datasync.types.dns_ip_list.DnsIpList"]
    """<p>Specifies the IPv4 or IPv6 addresses for the DNS servers that your SMB file server belongs to. This parameter applies only if <code>AuthenticationType</code> is set to <code>KERBEROS</code>.</p> <p>If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right SMB file server.</p>"""
    kerberos_principal: NotRequired[
        "aws_sdk_datasync.types.kerberos_principal.KerberosPrincipal"
    ]
    """<p>Specifies a Kerberos principal, which is an identity in your Kerberos realm that has permission to access the files, folders, and file metadata in your SMB file server.</p> <p>A Kerberos principal might look like <code>HOST/kerberosuser@MYDOMAIN.ORG</code>.</p> <p>Principal names are case sensitive. Your DataSync task execution will fail if the principal that you specify for this parameter doesn’t exactly match the principal that you use to create the keytab file.</p>"""
    kerberos_keytab: NotRequired[
        "aws_sdk_datasync.types.kerberos_keytab_file.KerberosKeytabFile"
    ]
    """<p>Specifies your Kerberos key table (keytab) file, which includes mappings between your Kerberos principal and encryption keys.</p> <p>To avoid task execution errors, make sure that the Kerberos principal that you use to create the keytab file matches exactly what you specify for <code>KerberosPrincipal</code>. </p>"""
    kerberos_krb5_conf: NotRequired[
        "aws_sdk_datasync.types.kerberos_krb5_conf_file.KerberosKrb5ConfFile"
    ]
    """<p>Specifies a Kerberos configuration file (<code>krb5.conf</code>) that defines your Kerberos realm configuration.</p> <p>The file must be base64 encoded. If you're using the CLI, the encoding is done for you.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationSmbRequest) -> dict:
    out: dict = {}
    out["Subdirectory"] = value["subdirectory"]
    out["ServerHostname"] = value["server_hostname"]
    if "user" in value:
        out["User"] = value["user"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "password" in value:
        out["Password"] = value["password"]
    if "cmk_secret_config" in value:
        import aws_sdk_datasync.types.cmk_secret_config

        out["CmkSecretConfig"] = (
            aws_sdk_datasync.types.cmk_secret_config.serialize_aws_json_1_1(
                value["cmk_secret_config"]
            )
        )
    if "custom_secret_config" in value:
        import aws_sdk_datasync.types.custom_secret_config

        out["CustomSecretConfig"] = (
            aws_sdk_datasync.types.custom_secret_config.serialize_aws_json_1_1(
                value["custom_secret_config"]
            )
        )
    import aws_sdk_datasync.types.agent_arn_list

    out["AgentArns"] = aws_sdk_datasync.types.agent_arn_list.serialize_aws_json_1_1(
        value["agent_arns"]
    )
    if "mount_options" in value:
        import aws_sdk_datasync.types.smb_mount_options

        out["MountOptions"] = (
            aws_sdk_datasync.types.smb_mount_options.serialize_aws_json_1_1(
                value["mount_options"]
            )
        )
    if "tags" in value:
        import aws_sdk_datasync.types.input_tag_list

        out["Tags"] = aws_sdk_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "authentication_type" in value:
        import aws_sdk_datasync.types.smb_authentication_type

        out["AuthenticationType"] = (
            aws_sdk_datasync.types.smb_authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "dns_ip_addresses" in value:
        import aws_sdk_datasync.types.dns_ip_list

        out["DnsIpAddresses"] = (
            aws_sdk_datasync.types.dns_ip_list.serialize_aws_json_1_1(
                value["dns_ip_addresses"]
            )
        )
    if "kerberos_principal" in value:
        out["KerberosPrincipal"] = value["kerberos_principal"]
    if "kerberos_keytab" in value:
        import aws_sdk_datasync.types.kerberos_keytab_file

        out["KerberosKeytab"] = (
            aws_sdk_datasync.types.kerberos_keytab_file.serialize_aws_json_1_1(
                value["kerberos_keytab"]
            )
        )
    if "kerberos_krb5_conf" in value:
        import aws_sdk_datasync.types.kerberos_krb5_conf_file

        out["KerberosKrb5Conf"] = (
            aws_sdk_datasync.types.kerberos_krb5_conf_file.serialize_aws_json_1_1(
                value["kerberos_krb5_conf"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationSmbRequest:
    out: CreateLocationSmbRequest = {}  # type: ignore[typeddict-item]
    if "Subdirectory" in data:
        out["subdirectory"] = data["Subdirectory"]
    else:
        raise DeserializationError("CreateLocationSmbRequest.subdirectory required")
    if "ServerHostname" in data:
        out["server_hostname"] = data["ServerHostname"]
    else:
        raise DeserializationError("CreateLocationSmbRequest.server_hostname required")
    if "User" in data:
        out["user"] = data["User"]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "Password" in data:
        out["password"] = data["Password"]
    if "CmkSecretConfig" in data:
        import aws_sdk_datasync.types.cmk_secret_config

        out["cmk_secret_config"] = (
            aws_sdk_datasync.types.cmk_secret_config.deserialize_aws_json_1_1(
                data["CmkSecretConfig"]
            )
        )
    if "CustomSecretConfig" in data:
        import aws_sdk_datasync.types.custom_secret_config

        out["custom_secret_config"] = (
            aws_sdk_datasync.types.custom_secret_config.deserialize_aws_json_1_1(
                data["CustomSecretConfig"]
            )
        )
    if "AgentArns" in data:
        import aws_sdk_datasync.types.agent_arn_list

        out["agent_arns"] = (
            aws_sdk_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
                data["AgentArns"]
            )
        )
    else:
        raise DeserializationError("CreateLocationSmbRequest.agent_arns required")
    if "MountOptions" in data:
        import aws_sdk_datasync.types.smb_mount_options

        out["mount_options"] = (
            aws_sdk_datasync.types.smb_mount_options.deserialize_aws_json_1_1(
                data["MountOptions"]
            )
        )
    if "Tags" in data:
        import aws_sdk_datasync.types.input_tag_list

        out["tags"] = aws_sdk_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "AuthenticationType" in data:
        import aws_sdk_datasync.types.smb_authentication_type

        out["authentication_type"] = (
            aws_sdk_datasync.types.smb_authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if "DnsIpAddresses" in data:
        import aws_sdk_datasync.types.dns_ip_list

        out["dns_ip_addresses"] = (
            aws_sdk_datasync.types.dns_ip_list.deserialize_aws_json_1_1(
                data["DnsIpAddresses"]
            )
        )
    if "KerberosPrincipal" in data:
        out["kerberos_principal"] = data["KerberosPrincipal"]
    if "KerberosKeytab" in data:
        import aws_sdk_datasync.types.kerberos_keytab_file

        out["kerberos_keytab"] = (
            aws_sdk_datasync.types.kerberos_keytab_file.deserialize_aws_json_1_1(
                data["KerberosKeytab"]
            )
        )
    if "KerberosKrb5Conf" in data:
        import aws_sdk_datasync.types.kerberos_krb5_conf_file

        out["kerberos_krb5_conf"] = (
            aws_sdk_datasync.types.kerberos_krb5_conf_file.deserialize_aws_json_1_1(
                data["KerberosKrb5Conf"]
            )
        )
    return out
