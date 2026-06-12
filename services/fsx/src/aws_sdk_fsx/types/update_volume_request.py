"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.update_ontap_volume_configuration
    import aws_sdk_fsx.types.update_open_zfs_volume_configuration
    import aws_sdk_fsx.types.volume_id
    import aws_sdk_fsx.types.volume_name


class UpdateVolumeRequest(TypedDict):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    volume_id: NotRequired["aws_sdk_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the volume that you want to update, in the format <code>fsvol-0123456789abcdef0</code>.</p>"""
    ontap_configuration: NotRequired[
        "aws_sdk_fsx.types.update_ontap_volume_configuration.UpdateOntapVolumeConfiguration"
    ]
    """<p>The configuration of the ONTAP volume that you are updating.</p>"""
    name: NotRequired["aws_sdk_fsx.types.volume_name.VolumeName"]
    """<p>The name of the OpenZFS volume. OpenZFS root volumes are automatically named <code>FSX</code>. Child volume names must be unique among their parent volume's children. The name of the volume is part of the mount string for the OpenZFS volume. </p>"""
    open_zfs_configuration: NotRequired[
        "aws_sdk_fsx.types.update_open_zfs_volume_configuration.UpdateOpenZFSVolumeConfiguration"
    ]
    """<p>The configuration of the OpenZFS volume that you are updating.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVolumeRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "ontap_configuration" in value:
        import aws_sdk_fsx.types.update_ontap_volume_configuration

        out["OntapConfiguration"] = (
            aws_sdk_fsx.types.update_ontap_volume_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "open_zfs_configuration" in value:
        import aws_sdk_fsx.types.update_open_zfs_volume_configuration

        out["OpenZFSConfiguration"] = (
            aws_sdk_fsx.types.update_open_zfs_volume_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVolumeRequest:
    out: UpdateVolumeRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "OntapConfiguration" in data:
        import aws_sdk_fsx.types.update_ontap_volume_configuration

        out["ontap_configuration"] = (
            aws_sdk_fsx.types.update_ontap_volume_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "OpenZFSConfiguration" in data:
        import aws_sdk_fsx.types.update_open_zfs_volume_configuration

        out["open_zfs_configuration"] = (
            aws_sdk_fsx.types.update_open_zfs_volume_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    return out
