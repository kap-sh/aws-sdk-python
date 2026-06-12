"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_authorization_config_details
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails(TypedDict):
    authorization_config: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_authorization_config_details.AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails"
    ]
    """<p>The authorization configuration details for the Amazon EFS file system.</p>"""
    filesystem_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon EFS file system identifier to use.</p>"""
    root_directory: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The directory within the Amazon EFS file system to mount as the root directory inside the host.</p>"""
    transit_encryption: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. </p>"""
    transit_encryption_port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails,
) -> dict:
    out: dict = {}
    if "authorization_config" in value:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_authorization_config_details

        out["AuthorizationConfig"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_authorization_config_details.serialize_json(
                value["authorization_config"]
            )
        )
    if "filesystem_id" in value:
        out["FilesystemId"] = value["filesystem_id"]
    if "root_directory" in value:
        out["RootDirectory"] = value["root_directory"]
    if "transit_encryption" in value:
        out["TransitEncryption"] = value["transit_encryption"]
    if "transit_encryption_port" in value:
        out["TransitEncryptionPort"] = value["transit_encryption_port"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails:
    out: AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "AuthorizationConfig" in data:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_authorization_config_details

        out["authorization_config"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_volumes_efs_volume_configuration_authorization_config_details.deserialize_json(
                data["AuthorizationConfig"]
            )
        )
    if "FilesystemId" in data:
        out["filesystem_id"] = data["FilesystemId"]
    if "RootDirectory" in data:
        out["root_directory"] = data["RootDirectory"]
    if "TransitEncryption" in data:
        out["transit_encryption"] = data["TransitEncryption"]
    if "TransitEncryptionPort" in data:
        out["transit_encryption_port"] = data["TransitEncryptionPort"]
    return out
