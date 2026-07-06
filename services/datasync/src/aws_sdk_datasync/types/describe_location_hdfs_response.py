"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationHdfsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datasync.types.agent_arn_list
    import aws_sdk_datasync.types.cmk_secret_config
    import aws_sdk_datasync.types.custom_secret_config
    import aws_sdk_datasync.types.hdfs_authentication_type
    import aws_sdk_datasync.types.hdfs_block_size
    import aws_sdk_datasync.types.hdfs_name_node_list
    import aws_sdk_datasync.types.hdfs_replication_factor
    import aws_sdk_datasync.types.hdfs_user
    import aws_sdk_datasync.types.kerberos_principal
    import aws_sdk_datasync.types.kms_key_provider_uri
    import aws_sdk_datasync.types.location_arn
    import aws_sdk_datasync.types.location_uri
    import aws_sdk_datasync.types.managed_secret_config
    import aws_sdk_datasync.types.qop_configuration
    import aws_sdk_datasync.types.time


class DescribeLocationHdfsResponse(TypedDict, closed=True):
    location_arn: NotRequired["aws_sdk_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the HDFS location.</p>"""
    location_uri: NotRequired["aws_sdk_datasync.types.location_uri.LocationUri"]
    """<p>The URI of the HDFS location.</p>"""
    name_nodes: NotRequired[
        "aws_sdk_datasync.types.hdfs_name_node_list.HdfsNameNodeList"
    ]
    """<p>The NameNode that manages the HDFS namespace. </p>"""
    block_size: NotRequired["aws_sdk_datasync.types.hdfs_block_size.HdfsBlockSize"]
    """<p>The size of the data blocks to write into the HDFS cluster. </p>"""
    replication_factor: NotRequired[
        "aws_sdk_datasync.types.hdfs_replication_factor.HdfsReplicationFactor"
    ]
    """<p>The number of DataNodes to replicate the data to when writing to the HDFS cluster. </p>"""
    kms_key_provider_uri: NotRequired[
        "aws_sdk_datasync.types.kms_key_provider_uri.KmsKeyProviderUri"
    ]
    """<p> The URI of the HDFS cluster's Key Management Server (KMS). </p>"""
    qop_configuration: NotRequired[
        "aws_sdk_datasync.types.qop_configuration.QopConfiguration"
    ]
    """<p>The Quality of Protection (QOP) configuration, which specifies the Remote Procedure Call (RPC) and data transfer protection settings configured on the HDFS cluster. </p>"""
    authentication_type: NotRequired[
        "aws_sdk_datasync.types.hdfs_authentication_type.HdfsAuthenticationType"
    ]
    """<p>The type of authentication used to determine the identity of the user. </p>"""
    simple_user: NotRequired["aws_sdk_datasync.types.hdfs_user.HdfsUser"]
    """<p>The user name to identify the client on the host operating system. This parameter is used if the <code>AuthenticationType</code> is defined as <code>SIMPLE</code>.</p>"""
    kerberos_principal: NotRequired[
        "aws_sdk_datasync.types.kerberos_principal.KerberosPrincipal"
    ]
    """<p>The Kerberos principal with access to the files and folders on the HDFS cluster. This parameter is used if the <code>AuthenticationType</code> is defined as <code>KERBEROS</code>.</p>"""
    agent_arns: NotRequired["aws_sdk_datasync.types.agent_arn_list.AgentArnList"]
    """<p>The ARNs of the DataSync agents that can connect with your HDFS cluster.</p>"""
    creation_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>The time that the HDFS location was created.</p>"""
    managed_secret_config: NotRequired[
        "aws_sdk_datasync.types.managed_secret_config.ManagedSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as a <code>KerberosKeytab</code> that DataSync uses to access a specific storage location. DataSync uses the default Amazon Web Services-managed KMS key to encrypt this secret in Secrets Manager.</p>"""
    cmk_secret_config: NotRequired[
        "aws_sdk_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as a <code>KerberosKeytab</code> that DataSync uses to access a specific storage location, with a customer-managed KMS key.</p>"""
    custom_secret_config: NotRequired[
        "aws_sdk_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Describes configuration information for a customer-managed secret, such as a <code>KerberosKeytab</code> that DataSync uses to access a specific storage location, with a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationHdfsResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "name_nodes" in value:
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
    if "authentication_type" in value:
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
    if "agent_arns" in value:
        import aws_sdk_datasync.types.agent_arn_list

        out["AgentArns"] = aws_sdk_datasync.types.agent_arn_list.serialize_aws_json_1_1(
            value["agent_arns"]
        )
    if "creation_time" in value:
        import aws_sdk_datasync.types.time

        out["CreationTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "managed_secret_config" in value:
        import aws_sdk_datasync.types.managed_secret_config

        out["ManagedSecretConfig"] = (
            aws_sdk_datasync.types.managed_secret_config.serialize_aws_json_1_1(
                value["managed_secret_config"]
            )
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


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationHdfsResponse:
    out: DescribeLocationHdfsResponse = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    if "LocationUri" in data:
        out["location_uri"] = data["LocationUri"]
    if "NameNodes" in data:
        import aws_sdk_datasync.types.hdfs_name_node_list

        out["name_nodes"] = (
            aws_sdk_datasync.types.hdfs_name_node_list.deserialize_aws_json_1_1(
                data["NameNodes"]
            )
        )
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
    if "SimpleUser" in data:
        out["simple_user"] = data["SimpleUser"]
    if "KerberosPrincipal" in data:
        out["kerberos_principal"] = data["KerberosPrincipal"]
    if "AgentArns" in data:
        import aws_sdk_datasync.types.agent_arn_list

        out["agent_arns"] = (
            aws_sdk_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
                data["AgentArns"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_datasync.types.time

        out["creation_time"] = aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "ManagedSecretConfig" in data:
        import aws_sdk_datasync.types.managed_secret_config

        out["managed_secret_config"] = (
            aws_sdk_datasync.types.managed_secret_config.deserialize_aws_json_1_1(
                data["ManagedSecretConfig"]
            )
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
