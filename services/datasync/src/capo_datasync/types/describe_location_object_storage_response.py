"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationObjectStorageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn_list
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.location_arn
    import capo_datasync.types.location_uri
    import capo_datasync.types.managed_secret_config
    import capo_datasync.types.object_storage_access_key
    import capo_datasync.types.object_storage_certificate
    import capo_datasync.types.object_storage_server_port
    import capo_datasync.types.object_storage_server_protocol
    import capo_datasync.types.time


class DescribeLocationObjectStorageResponse(TypedDict, closed=True):
    location_arn: NotRequired["capo_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the object storage system location.</p>"""
    location_uri: NotRequired["capo_datasync.types.location_uri.LocationUri"]
    """<p>The URI of the object storage system location.</p>"""
    access_key: NotRequired[
        "capo_datasync.types.object_storage_access_key.ObjectStorageAccessKey"
    ]
    """<p>The access key (for example, a user name) required to authenticate with the object storage system.</p>"""
    server_port: NotRequired[
        "capo_datasync.types.object_storage_server_port.ObjectStorageServerPort"
    ]
    """<p>The port that your object storage server accepts inbound network traffic on (for example, port 443).</p>"""
    server_protocol: NotRequired[
        "capo_datasync.types.object_storage_server_protocol.ObjectStorageServerProtocol"
    ]
    """<p>The protocol that your object storage system uses to communicate.</p>"""
    agent_arns: NotRequired["capo_datasync.types.agent_arn_list.AgentArnList"]
    """<p>The ARNs of the DataSync agents that can connect with your object storage system.</p>"""
    creation_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that the location was created.</p>"""
    server_certificate: NotRequired[
        "capo_datasync.types.object_storage_certificate.ObjectStorageCertificate"
    ]
    """<p>The certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA).</p>"""
    managed_secret_config: NotRequired[
        "capo_datasync.types.managed_secret_config.ManagedSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location. DataSync uses the default Amazon Web Services-managed KMS key to encrypt this secret in Secrets Manager.</p>"""
    cmk_secret_config: NotRequired[
        "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.</p>"""
    custom_secret_config: NotRequired[
        "capo_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Describes configuration information for a customer-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationObjectStorageResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "access_key" in value:
        out["AccessKey"] = value["access_key"]
    if "server_port" in value:
        out["ServerPort"] = value["server_port"]
    if "server_protocol" in value:
        import capo_datasync.types.object_storage_server_protocol

        out["ServerProtocol"] = (
            capo_datasync.types.object_storage_server_protocol.serialize_aws_json_1_1(
                value["server_protocol"]
            )
        )
    if "agent_arns" in value:
        import capo_datasync.types.agent_arn_list

        out["AgentArns"] = capo_datasync.types.agent_arn_list.serialize_aws_json_1_1(
            value["agent_arns"]
        )
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "server_certificate" in value:
        import capo_datasync.types.object_storage_certificate

        out["ServerCertificate"] = (
            capo_datasync.types.object_storage_certificate.serialize_aws_json_1_1(
                value["server_certificate"]
            )
        )
    if "managed_secret_config" in value:
        import capo_datasync.types.managed_secret_config

        out["ManagedSecretConfig"] = (
            capo_datasync.types.managed_secret_config.serialize_aws_json_1_1(
                value["managed_secret_config"]
            )
        )
    if "cmk_secret_config" in value:
        import capo_datasync.types.cmk_secret_config

        out["CmkSecretConfig"] = (
            capo_datasync.types.cmk_secret_config.serialize_aws_json_1_1(
                value["cmk_secret_config"]
            )
        )
    if "custom_secret_config" in value:
        import capo_datasync.types.custom_secret_config

        out["CustomSecretConfig"] = (
            capo_datasync.types.custom_secret_config.serialize_aws_json_1_1(
                value["custom_secret_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationObjectStorageResponse:
    out: DescribeLocationObjectStorageResponse = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    if "LocationUri" in data:
        out["location_uri"] = data["LocationUri"]
    if "AccessKey" in data:
        out["access_key"] = data["AccessKey"]
    if "ServerPort" in data:
        out["server_port"] = data["ServerPort"]
    if "ServerProtocol" in data:
        import capo_datasync.types.object_storage_server_protocol

        out["server_protocol"] = (
            capo_datasync.types.object_storage_server_protocol.deserialize_aws_json_1_1(
                data["ServerProtocol"]
            )
        )
    if "AgentArns" in data:
        import capo_datasync.types.agent_arn_list

        out["agent_arns"] = capo_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
            data["AgentArns"]
        )
    if "CreationTime" in data:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "ServerCertificate" in data:
        import capo_datasync.types.object_storage_certificate

        out["server_certificate"] = (
            capo_datasync.types.object_storage_certificate.deserialize_aws_json_1_1(
                data["ServerCertificate"]
            )
        )
    if "ManagedSecretConfig" in data:
        import capo_datasync.types.managed_secret_config

        out["managed_secret_config"] = (
            capo_datasync.types.managed_secret_config.deserialize_aws_json_1_1(
                data["ManagedSecretConfig"]
            )
        )
    if "CmkSecretConfig" in data:
        import capo_datasync.types.cmk_secret_config

        out["cmk_secret_config"] = (
            capo_datasync.types.cmk_secret_config.deserialize_aws_json_1_1(
                data["CmkSecretConfig"]
            )
        )
    if "CustomSecretConfig" in data:
        import capo_datasync.types.custom_secret_config

        out["custom_secret_config"] = (
            capo_datasync.types.custom_secret_config.deserialize_aws_json_1_1(
                data["CustomSecretConfig"]
            )
        )
    return out
