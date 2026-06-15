"""Generated from Smithy shape ``com.amazonaws.ecs#EFSVolumeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.efs_authorization_config
    import aws_sdk_ecs.types.efs_transit_encryption
    import aws_sdk_ecs.types.string


class EFSVolumeConfiguration(TypedDict):
    file_system_id: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon EFS file system ID to use.</p>"""
    root_directory: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume will be used. Specifying <code>/</code> will have the same effect as omitting this parameter.</p> <important> <p>If an EFS access point is specified in the <code>authorizationConfig</code>, the root directory parameter must either be omitted or set to <code>/</code> which will enforce the path set on the EFS access point.</p> </important>"""
    transit_encryption: NotRequired[
        "aws_sdk_ecs.types.efs_transit_encryption.EFSTransitEncryption"
    ]
    r"""<p>Determines whether to use encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be turned on if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of <code>DISABLED</code> is used. For more information, see <a href=\"https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html\">Encrypting data in transit</a> in the <i>Amazon Elastic File System User Guide</i>.</p>"""
    transit_encryption_port: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    r"""<p>The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you do not specify a transit encryption port, it will use the port selection strategy that the Amazon EFS mount helper uses. For more information, see <a href=\"https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html\">EFS mount helper</a> in the <i>Amazon Elastic File System User Guide</i>.</p>"""
    authorization_config: NotRequired[
        "aws_sdk_ecs.types.efs_authorization_config.EFSAuthorizationConfig"
    ]
    """<p>The authorization configuration details for the Amazon EFS file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EFSVolumeConfiguration) -> dict:
    out: dict = {}
    out["fileSystemId"] = value["file_system_id"]
    if "root_directory" in value:
        out["rootDirectory"] = value["root_directory"]
    if "transit_encryption" in value:
        import aws_sdk_ecs.types.efs_transit_encryption

        out["transitEncryption"] = (
            aws_sdk_ecs.types.efs_transit_encryption.serialize_aws_json_1_1(
                value["transit_encryption"]
            )
        )
    if "transit_encryption_port" in value:
        out["transitEncryptionPort"] = value["transit_encryption_port"]
    if "authorization_config" in value:
        import aws_sdk_ecs.types.efs_authorization_config

        out["authorizationConfig"] = (
            aws_sdk_ecs.types.efs_authorization_config.serialize_aws_json_1_1(
                value["authorization_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EFSVolumeConfiguration:
    out: EFSVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if "fileSystemId" in data:
        out["file_system_id"] = data["fileSystemId"]
    else:
        raise DeserializationError("EFSVolumeConfiguration.file_system_id required")
    if "rootDirectory" in data:
        out["root_directory"] = data["rootDirectory"]
    if "transitEncryption" in data:
        import aws_sdk_ecs.types.efs_transit_encryption

        out["transit_encryption"] = (
            aws_sdk_ecs.types.efs_transit_encryption.deserialize_aws_json_1_1(
                data["transitEncryption"]
            )
        )
    if "transitEncryptionPort" in data:
        out["transit_encryption_port"] = data["transitEncryptionPort"]
    if "authorizationConfig" in data:
        import aws_sdk_ecs.types.efs_authorization_config

        out["authorization_config"] = (
            aws_sdk_ecs.types.efs_authorization_config.deserialize_aws_json_1_1(
                data["authorizationConfig"]
            )
        )
    return out
