"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationHdfsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.agent_arn_list
    import aws_sdk_datasync.types.cmk_secret_config
    import aws_sdk_datasync.types.custom_secret_config
    import aws_sdk_datasync.types.hdfs_authentication_type
    import aws_sdk_datasync.types.hdfs_block_size
    import aws_sdk_datasync.types.hdfs_name_node_list
    import aws_sdk_datasync.types.hdfs_replication_factor
    import aws_sdk_datasync.types.hdfs_subdirectory
    import aws_sdk_datasync.types.hdfs_user
    import aws_sdk_datasync.types.input_tag_list
    import aws_sdk_datasync.types.kerberos_keytab_file
    import aws_sdk_datasync.types.kerberos_krb5_conf_file
    import aws_sdk_datasync.types.kerberos_principal
    import aws_sdk_datasync.types.kms_key_provider_uri
    import aws_sdk_datasync.types.qop_configuration


class CreateLocationHdfsRequest(TypedDict, closed=True):
    subdirectory: NotRequired[
        "aws_sdk_datasync.types.hdfs_subdirectory.HdfsSubdirectory"
    ]
    """<p>A subdirectory in the HDFS cluster. This subdirectory is used to read data from or write data to the HDFS cluster. If the subdirectory isn't specified, it will default to <code>/</code>.</p>"""
    name_nodes: "aws_sdk_datasync.types.hdfs_name_node_list.HdfsNameNodeList"
    """<p>The NameNode that manages the HDFS namespace. The NameNode performs operations such as opening, closing, and renaming files and directories. The NameNode contains the information to map blocks of data to the DataNodes. You can use only one NameNode.</p>"""
    block_size: NotRequired["aws_sdk_datasync.types.hdfs_block_size.HdfsBlockSize"]
    """<p>The size of data blocks to write into the HDFS cluster. The block size must be a multiple of 512 bytes. The default block size is 128 mebibytes (MiB).</p>"""
    replication_factor: NotRequired[
        "aws_sdk_datasync.types.hdfs_replication_factor.HdfsReplicationFactor"
    ]
    """<p>The number of DataNodes to replicate the data to when writing to the HDFS cluster. By default, data is replicated to three DataNodes.</p>"""
    kms_key_provider_uri: NotRequired[
        "aws_sdk_datasync.types.kms_key_provider_uri.KmsKeyProviderUri"
    ]
    """<p>The URI of the HDFS cluster's Key Management Server (KMS). </p>"""
    qop_configuration: NotRequired[
        "aws_sdk_datasync.types.qop_configuration.QopConfiguration"
    ]
    """<p>The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer protection settings configured on the Hadoop Distributed File System (HDFS) cluster. If <code>QopConfiguration</code> isn't specified, <code>RpcProtection</code> and <code>DataTransferProtection</code> default to <code>PRIVACY</code>. If you set <code>RpcProtection</code> or <code>DataTransferProtection</code>, the other parameter assumes the same value. </p>"""
    authentication_type: (
        "aws_sdk_datasync.types.hdfs_authentication_type.HdfsAuthenticationType"
    )
    """<p>The type of authentication used to determine the identity of the user. </p>"""
    simple_user: NotRequired["aws_sdk_datasync.types.hdfs_user.HdfsUser"]
    """<p>The user name used to identify the client on the host operating system. </p> <note> <p>If <code>SIMPLE</code> is specified for <code>AuthenticationType</code>, this parameter is required. </p> </note>"""
    kerberos_principal: NotRequired[
        "aws_sdk_datasync.types.kerberos_principal.KerberosPrincipal"
    ]
    """<p>The Kerberos principal with access to the files and folders on the HDFS cluster. </p> <note> <p>If <code>KERBEROS</code> is specified for <code>AuthenticationType</code>, this parameter is required.</p> </note>"""
    kerberos_keytab: NotRequired[
        "aws_sdk_datasync.types.kerberos_keytab_file.KerberosKeytabFile"
    ]
    """<p>The Kerberos key table (keytab) that contains mappings between the defined Kerberos principal and the encrypted keys. You can load the keytab from a file by providing the file's address.</p> <note> <p>If <code>KERBEROS</code> is specified for <code>AuthenticationType</code>, this parameter is required. </p> </note>"""
    kerberos_krb5_conf: NotRequired[
        "aws_sdk_datasync.types.kerberos_krb5_conf_file.KerberosKrb5ConfFile"
    ]
    """<p>The <code>krb5.conf</code> file that contains the Kerberos configuration information. You can load the <code>krb5.conf</code> file by providing the file's address. If you're using the CLI, it performs the base64 encoding for you. Otherwise, provide the base64-encoded text. </p> <note> <p>If <code>KERBEROS</code> is specified for <code>AuthenticationType</code>, this parameter is required.</p> </note>"""
    agent_arns: "aws_sdk_datasync.types.agent_arn_list.AgentArnList"
    """<p>The Amazon Resource Names (ARNs) of the DataSync agents that can connect to your HDFS cluster.</p>"""
    tags: NotRequired["aws_sdk_datasync.types.input_tag_list.InputTagList"]
    """<p>The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources. </p>"""
    cmk_secret_config: NotRequired[
        "aws_sdk_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    r"""<p>Specifies configuration information for a DataSync-managed secret, which includes the Kerberos keytab that DataSync uses to access a specific Hadoop Distributed File System (HDFS) storage location, with a customer-managed KMS key.</p> <p>When you include this parameter as part of a <code>CreateLocationHdfs</code> request, you provide only the KMS key ARN. DataSync uses this KMS key together with the <code>KerberosKeytab</code> you specify for to create a DataSync-managed secret to store the location access credentials.</p> <p>Make sure that DataSync has permission to access the KMS key that you specify. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key\"> Using a service-managed secret encrypted with a custom KMS key</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>KerberosKeytab</code>) or <code>CustomSecretConfig</code> (without <code>KerberosKeytab</code>) to provide credentials for a <code>CreateLocationHdfs</code> request. Do not provide both parameters for the same request.</p> </note>"""
    custom_secret_config: NotRequired[
        "aws_sdk_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    r"""<p>Specifies configuration information for a customer-managed Secrets Manager secret where the Kerberos keytab for the HDFS storage location is stored in binary, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key\"> Using a secret that you manage</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>KerberosKeytab</code>) or <code>CustomSecretConfig</code> (without <code>KerberosKeytab</code>) to provide credentials for a <code>CreateLocationHdfs</code> request. Do not provide both parameters for the same request.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationHdfsRequest) -> dict:
    out: dict = {}
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    import aws_sdk_datasync.types.hdfs_name_node_list

    out["NameNodes"] = (
        aws_sdk_datasync.types.hdfs_name_node_list.serialize_aws_json_1_1(
            value["name_nodes"]
        )
    )
    if "block_size" in value:
        out["BlockSize"] = value["block_size"]
    if "replication_factor" in value:
        out["ReplicationFactor"] = value["replication_factor"]
    if "kms_key_provider_uri" in value:
        out["KmsKeyProviderUri"] = value["kms_key_provider_uri"]
    if "qop_configuration" in value:
        import aws_sdk_datasync.types.qop_configuration

        out["QopConfiguration"] = (
            aws_sdk_datasync.types.qop_configuration.serialize_aws_json_1_1(
                value["qop_configuration"]
            )
        )
    import aws_sdk_datasync.types.hdfs_authentication_type

    out["AuthenticationType"] = (
        aws_sdk_datasync.types.hdfs_authentication_type.serialize_aws_json_1_1(
            value["authentication_type"]
        )
    )
    if "simple_user" in value:
        out["SimpleUser"] = value["simple_user"]
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
    import aws_sdk_datasync.types.agent_arn_list

    out["AgentArns"] = aws_sdk_datasync.types.agent_arn_list.serialize_aws_json_1_1(
        value["agent_arns"]
    )
    if "tags" in value:
        import aws_sdk_datasync.types.input_tag_list

        out["Tags"] = aws_sdk_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationHdfsRequest:
    out: CreateLocationHdfsRequest = {}  # type: ignore[typeddict-item]
    if "Subdirectory" in data:
        out["subdirectory"] = data["Subdirectory"]
    if "NameNodes" in data:
        import aws_sdk_datasync.types.hdfs_name_node_list

        out["name_nodes"] = (
            aws_sdk_datasync.types.hdfs_name_node_list.deserialize_aws_json_1_1(
                data["NameNodes"]
            )
        )
    else:
        raise DeserializationError("CreateLocationHdfsRequest.name_nodes required")
    if "BlockSize" in data:
        out["block_size"] = data["BlockSize"]
    if "ReplicationFactor" in data:
        out["replication_factor"] = data["ReplicationFactor"]
    if "KmsKeyProviderUri" in data:
        out["kms_key_provider_uri"] = data["KmsKeyProviderUri"]
    if "QopConfiguration" in data:
        import aws_sdk_datasync.types.qop_configuration

        out["qop_configuration"] = (
            aws_sdk_datasync.types.qop_configuration.deserialize_aws_json_1_1(
                data["QopConfiguration"]
            )
        )
    if "AuthenticationType" in data:
        import aws_sdk_datasync.types.hdfs_authentication_type

        out["authentication_type"] = (
            aws_sdk_datasync.types.hdfs_authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLocationHdfsRequest.authentication_type required"
        )
    if "SimpleUser" in data:
        out["simple_user"] = data["SimpleUser"]
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
    if "AgentArns" in data:
        import aws_sdk_datasync.types.agent_arn_list

        out["agent_arns"] = (
            aws_sdk_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
                data["AgentArns"]
            )
        )
    else:
        raise DeserializationError("CreateLocationHdfsRequest.agent_arns required")
    if "Tags" in data:
        import aws_sdk_datasync.types.input_tag_list

        out["tags"] = aws_sdk_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
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
    return out
