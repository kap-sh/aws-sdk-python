"""Generated from Smithy shape ``com.amazonaws.fsx#CreateVolumeFromBackupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.backup_id
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.create_ontap_volume_configuration
    import aws_sdk_fsx.types.tags
    import aws_sdk_fsx.types.volume_name


class CreateVolumeFromBackupRequest(TypedDict):
    backup_id: NotRequired["aws_sdk_fsx.types.backup_id.BackupId"]
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    name: NotRequired["aws_sdk_fsx.types.volume_name.VolumeName"]
    """<p>The name of the new volume you're creating.</p>"""
    ontap_configuration: NotRequired[
        "aws_sdk_fsx.types.create_ontap_volume_configuration.CreateOntapVolumeConfiguration"
    ]
    """<p>Specifies the configuration of the ONTAP volume that you are creating.</p>"""
    tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVolumeFromBackupRequest) -> dict:
    out: dict = {}
    if "backup_id" in value:
        out["BackupId"] = value["backup_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "name" in value:
        out["Name"] = value["name"]
    if "ontap_configuration" in value:
        import aws_sdk_fsx.types.create_ontap_volume_configuration

        out["OntapConfiguration"] = (
            aws_sdk_fsx.types.create_ontap_volume_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_fsx.types.tags

        out["Tags"] = aws_sdk_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVolumeFromBackupRequest:
    out: CreateVolumeFromBackupRequest = {}  # type: ignore[typeddict-item]
    if "BackupId" in data:
        out["backup_id"] = data["BackupId"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "OntapConfiguration" in data:
        import aws_sdk_fsx.types.create_ontap_volume_configuration

        out["ontap_configuration"] = (
            aws_sdk_fsx.types.create_ontap_volume_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if "Tags" in data:
        import aws_sdk_fsx.types.tags

        out["tags"] = aws_sdk_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
