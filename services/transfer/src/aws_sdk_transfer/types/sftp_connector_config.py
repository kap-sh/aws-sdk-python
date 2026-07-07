"""Generated from Smithy shape ``com.amazonaws.transfer#SftpConnectorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.max_concurrent_connections
    import aws_sdk_transfer.types.secret_id
    import aws_sdk_transfer.types.sftp_connector_trusted_host_key_list


class SftpConnectorConfig(TypedDict, closed=True):
    user_secret_id: NotRequired["aws_sdk_transfer.types.secret_id.SecretId"]
    """<p>The identifier for the secret (in Amazon Web Services Secrets Manager) that contains the SFTP user's private key, password, or both. The identifier must be the Amazon Resource Name (ARN) of the secret.</p> <note> <ul> <li> <p>Required when creating an SFTP connector</p> </li> <li> <p>Optional when updating an existing SFTP connector</p> </li> </ul> </note>"""
    trusted_host_keys: NotRequired[
        "aws_sdk_transfer.types.sftp_connector_trusted_host_key_list.SftpConnectorTrustedHostKeyList"
    ]
    """<p>The public portion of the host key, or keys, that are used to identify the external server to which you are connecting. You can use the <code>ssh-keyscan</code> command against the SFTP server to retrieve the necessary key.</p> <note> <p> <code>TrustedHostKeys</code> is optional for <code>CreateConnector</code>. If not provided, you can use <code>TestConnection</code> to retrieve the server host key during the initial connection attempt, and subsequently update the connector with the observed host key.</p> </note> <p>When creating connectors with egress config (VPC_LATTICE type connectors), since host name is not something we can verify, the only accepted trusted host key format is <code>key-type key-body</code> without the host name. For example: <code>ssh-rsa AAAAB3Nza...&lt;long-string-for-public-key&gt;</code> </p> <p>The three standard SSH public key format elements are <code>&lt;key type&gt;</code>, <code>&lt;body base64&gt;</code>, and an optional <code>&lt;comment&gt;</code>, with spaces between each element. Specify only the <code>&lt;key type&gt;</code> and <code>&lt;body base64&gt;</code>: do not enter the <code>&lt;comment&gt;</code> portion of the key.</p> <p>For the trusted host key, Transfer Family accepts RSA and ECDSA keys.</p> <ul> <li> <p>For RSA keys, the <code>&lt;key type&gt;</code> string is <code>ssh-rsa</code>.</p> </li> <li> <p>For ECDSA keys, the <code>&lt;key type&gt;</code> string is either <code>ecdsa-sha2-nistp256</code>, <code>ecdsa-sha2-nistp384</code>, or <code>ecdsa-sha2-nistp521</code>, depending on the size of the key you generated.</p> </li> </ul> <p>Run this command to retrieve the SFTP server host key, where your SFTP server name is <code>ftp.host.com</code>.</p> <p> <code>ssh-keyscan ftp.host.com</code> </p> <p>This prints the public host key to standard output.</p> <p> <code>ftp.host.com ssh-rsa AAAAB3Nza...&lt;long-string-for-public-key&gt;</code> </p> <p>Copy and paste this string into the <code>TrustedHostKeys</code> field for the <code>create-connector</code> command or into the <b>Trusted host keys</b> field in the console.</p> <p>For VPC Lattice type connectors (VPC_LATTICE), remove the hostname from the key and use only the <code>key-type key-body</code> format. In this example, it should be: <code>ssh-rsa AAAAB3Nza...&lt;long-string-for-public-key&gt;</code> </p>"""
    max_concurrent_connections: (
        "aws_sdk_transfer.types.max_concurrent_connections.MaxConcurrentConnections"
    )
    """<p>Specify the number of concurrent connections that your connector creates to the remote server. The default value is <code>1</code>. The maximum values is <code>5</code>.</p> <note> <p>If you are using the Amazon Web Services Management Console, the default value is <code>5</code>.</p> </note> <p>This parameter specifies the number of active connections that your connector can establish with the remote server at the same time. Increasing this value can enhance connector performance when transferring large file batches by enabling parallel operations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SftpConnectorConfig) -> dict:
    out: dict = {}
    if "user_secret_id" in value:
        out["UserSecretId"] = value["user_secret_id"]
    if "trusted_host_keys" in value:
        import aws_sdk_transfer.types.sftp_connector_trusted_host_key_list

        out["TrustedHostKeys"] = (
            aws_sdk_transfer.types.sftp_connector_trusted_host_key_list.serialize_aws_json_1_1(
                value["trusted_host_keys"]
            )
        )
    out["MaxConcurrentConnections"] = value.get("max_concurrent_connections", 1)
    return out


def deserialize_aws_json_1_1(data: dict) -> SftpConnectorConfig:
    out: SftpConnectorConfig = {}  # type: ignore[typeddict-item]
    if "UserSecretId" in data:
        out["user_secret_id"] = data["UserSecretId"]
    if "TrustedHostKeys" in data:
        import aws_sdk_transfer.types.sftp_connector_trusted_host_key_list

        out["trusted_host_keys"] = (
            aws_sdk_transfer.types.sftp_connector_trusted_host_key_list.deserialize_aws_json_1_1(
                data["TrustedHostKeys"]
            )
        )
    if "MaxConcurrentConnections" in data:
        out["max_concurrent_connections"] = data["MaxConcurrentConnections"]
    else:
        out["max_concurrent_connections"] = 1
    return out
