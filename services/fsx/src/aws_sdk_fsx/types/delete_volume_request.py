"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.delete_volume_ontap_configuration
    import aws_sdk_fsx.types.delete_volume_open_zfs_configuration
    import aws_sdk_fsx.types.volume_id


class DeleteVolumeRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    volume_id: NotRequired["aws_sdk_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the volume that you are deleting.</p>"""
    ontap_configuration: NotRequired[
        "aws_sdk_fsx.types.delete_volume_ontap_configuration.DeleteVolumeOntapConfiguration"
    ]
    """<p>For Amazon FSx for ONTAP volumes, specify whether to take a final backup of the volume and apply tags to the backup. To apply tags to the backup, you must have the <code>fsx:TagResource</code> permission.</p>"""
    open_zfs_configuration: NotRequired[
        "aws_sdk_fsx.types.delete_volume_open_zfs_configuration.DeleteVolumeOpenZFSConfiguration"
    ]
    """<p>For Amazon FSx for OpenZFS volumes, specify whether to delete all child volumes and snapshots.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVolumeRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "ontap_configuration" in value:
        import aws_sdk_fsx.types.delete_volume_ontap_configuration

        out["OntapConfiguration"] = (
            aws_sdk_fsx.types.delete_volume_ontap_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "open_zfs_configuration" in value:
        import aws_sdk_fsx.types.delete_volume_open_zfs_configuration

        out["OpenZFSConfiguration"] = (
            aws_sdk_fsx.types.delete_volume_open_zfs_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVolumeRequest:
    out: DeleteVolumeRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "OntapConfiguration" in data:
        import aws_sdk_fsx.types.delete_volume_ontap_configuration

        out["ontap_configuration"] = (
            aws_sdk_fsx.types.delete_volume_ontap_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if "OpenZFSConfiguration" in data:
        import aws_sdk_fsx.types.delete_volume_open_zfs_configuration

        out["open_zfs_configuration"] = (
            aws_sdk_fsx.types.delete_volume_open_zfs_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    return out
