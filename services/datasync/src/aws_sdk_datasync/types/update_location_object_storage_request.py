"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationObjectStorageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.agent_arn_list
    import aws_sdk_datasync.types.cmk_secret_config
    import aws_sdk_datasync.types.custom_secret_config
    import aws_sdk_datasync.types.location_arn
    import aws_sdk_datasync.types.object_storage_access_key
    import aws_sdk_datasync.types.object_storage_certificate
    import aws_sdk_datasync.types.object_storage_secret_key
    import aws_sdk_datasync.types.object_storage_server_port
    import aws_sdk_datasync.types.object_storage_server_protocol
    import aws_sdk_datasync.types.s3_subdirectory
    import aws_sdk_datasync.types.server_hostname


class UpdateLocationObjectStorageRequest(TypedDict):
    location_arn: "aws_sdk_datasync.types.location_arn.LocationArn"
    """<p>Specifies the ARN of the object storage system location that you're updating.</p>"""
    server_port: NotRequired[
        "aws_sdk_datasync.types.object_storage_server_port.ObjectStorageServerPort"
    ]
    """<p>Specifies the port that your object storage server accepts inbound network traffic on (for example, port 443).</p>"""
    server_protocol: NotRequired[
        "aws_sdk_datasync.types.object_storage_server_protocol.ObjectStorageServerProtocol"
    ]
    """<p>Specifies the protocol that your object storage server uses to communicate.</p>"""
    subdirectory: NotRequired["aws_sdk_datasync.types.s3_subdirectory.S3Subdirectory"]
    """<p>Specifies the object prefix for your object storage server. If this is a source location, DataSync only copies objects with this prefix. If this is a destination location, DataSync writes all objects with this prefix.</p>"""
    server_hostname: NotRequired[
        "aws_sdk_datasync.types.server_hostname.ServerHostname"
    ]
    """<p>Specifies the domain name or IP address (IPv4 or IPv6) of the object storage server that your DataSync agent connects to.</p>"""
    access_key: NotRequired[
        "aws_sdk_datasync.types.object_storage_access_key.ObjectStorageAccessKey"
    ]
    """<p>Specifies the access key (for example, a user name) if credentials are required to authenticate with the object storage server.</p>"""
    secret_key: NotRequired[
        "aws_sdk_datasync.types.object_storage_secret_key.ObjectStorageSecretKey"
    ]
    """<p>Specifies the secret key (for example, a password) if credentials are required to authenticate with the object storage server.</p> <note> <p>If you provide a secret using <code>SecretKey</code>, but do not provide secret configuration details using <code>CmkSecretConfig</code> or <code>CustomSecretConfig</code>, then DataSync stores the token using your Amazon Web Services account's Secrets Manager secret.</p> </note>"""
    agent_arns: NotRequired["aws_sdk_datasync.types.agent_arn_list.AgentArnList"]
    """<p>(Optional) Specifies the Amazon Resource Names (ARNs) of the DataSync agents that can connect with your object storage system. If you are setting up an agentless cross-cloud transfer, you do not need to specify a value for this parameter.</p> <note> <p>You cannot add or remove agents from a storage location after you initially create it.</p> </note>"""
    server_certificate: NotRequired[
        "aws_sdk_datasync.types.object_storage_certificate.ObjectStorageCertificate"
    ]
    """<p>Specifies a certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA). You must specify a single <code>.pem</code> file with a full certificate chain (for example, <code>file:///home/user/.ssh/object_storage_certificates.pem</code>).</p> <p>The certificate chain might include:</p> <ul> <li> <p>The object storage system's certificate</p> </li> <li> <p>All intermediate certificates (if there are any)</p> </li> <li> <p>The root certificate of the signing CA</p> </li> </ul> <p>You can concatenate your certificates into a <code>.pem</code> file (which can be up to 32768 bytes before base64 encoding). The following example <code>cat</code> command creates an <code>object_storage_certificates.pem</code> file that includes three certificates:</p> <p> <code>cat object_server_certificate.pem intermediate_certificate.pem ca_root_certificate.pem > object_storage_certificates.pem</code> </p> <p>To use this parameter, configure <code>ServerProtocol</code> to <code>HTTPS</code>.</p> <p>Updating this parameter doesn't interfere with tasks that you have in progress.</p>"""
    cmk_secret_config: NotRequired[
        "aws_sdk_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Specifies configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.</p>"""
    custom_secret_config: NotRequired[
        "aws_sdk_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Specifies configuration information for a customer-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationObjectStorageRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    if "server_port" in value:
        out["ServerPort"] = value["server_port"]
    if "server_protocol" in value:
        import aws_sdk_datasync.types.object_storage_server_protocol

        out["ServerProtocol"] = (
            aws_sdk_datasync.types.object_storage_server_protocol.serialize_aws_json_1_1(
                value["server_protocol"]
            )
        )
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    if "server_hostname" in value:
        out["ServerHostname"] = value["server_hostname"]
    if "access_key" in value:
        out["AccessKey"] = value["access_key"]
    if "secret_key" in value:
        out["SecretKey"] = value["secret_key"]
    if "agent_arns" in value:
        import aws_sdk_datasync.types.agent_arn_list

        out["AgentArns"] = aws_sdk_datasync.types.agent_arn_list.serialize_aws_json_1_1(
            value["agent_arns"]
        )
    if "server_certificate" in value:
        import aws_sdk_datasync.types.object_storage_certificate

        out["ServerCertificate"] = (
            aws_sdk_datasync.types.object_storage_certificate.serialize_aws_json_1_1(
                value["server_certificate"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationObjectStorageRequest:
    out: UpdateLocationObjectStorageRequest = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError(
            "UpdateLocationObjectStorageRequest.location_arn required"
        )
    if "ServerPort" in data:
        out["server_port"] = data["ServerPort"]
    if "ServerProtocol" in data:
        import aws_sdk_datasync.types.object_storage_server_protocol

        out["server_protocol"] = (
            aws_sdk_datasync.types.object_storage_server_protocol.deserialize_aws_json_1_1(
                data["ServerProtocol"]
            )
        )
    if "Subdirectory" in data:
        out["subdirectory"] = data["Subdirectory"]
    if "ServerHostname" in data:
        out["server_hostname"] = data["ServerHostname"]
    if "AccessKey" in data:
        out["access_key"] = data["AccessKey"]
    if "SecretKey" in data:
        out["secret_key"] = data["SecretKey"]
    if "AgentArns" in data:
        import aws_sdk_datasync.types.agent_arn_list

        out["agent_arns"] = (
            aws_sdk_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
                data["AgentArns"]
            )
        )
    if "ServerCertificate" in data:
        import aws_sdk_datasync.types.object_storage_certificate

        out["server_certificate"] = (
            aws_sdk_datasync.types.object_storage_certificate.deserialize_aws_json_1_1(
                data["ServerCertificate"]
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
