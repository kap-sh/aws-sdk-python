"""Generated from Smithy shape ``com.amazonaws.fsx#CreateVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.create_ontap_volume_configuration
    import aws_sdk_fsx.types.create_open_zfs_volume_configuration
    import aws_sdk_fsx.types.tags
    import aws_sdk_fsx.types.volume_name
    import aws_sdk_fsx.types.volume_type


class CreateVolumeRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    volume_type: NotRequired["aws_sdk_fsx.types.volume_type.VolumeType"]
    """<p>Specifies the type of volume to create; <code>ONTAP</code> and <code>OPENZFS</code> are the only valid volume types.</p>"""
    name: NotRequired["aws_sdk_fsx.types.volume_name.VolumeName"]
    """<p>Specifies the name of the volume that you're creating.</p>"""
    ontap_configuration: NotRequired[
        "aws_sdk_fsx.types.create_ontap_volume_configuration.CreateOntapVolumeConfiguration"
    ]
    """<p>Specifies the configuration to use when creating the ONTAP volume.</p>"""
    tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]
    open_zfs_configuration: NotRequired[
        "aws_sdk_fsx.types.create_open_zfs_volume_configuration.CreateOpenZFSVolumeConfiguration"
    ]
    """<p>Specifies the configuration to use when creating the OpenZFS volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVolumeRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "volume_type" in value:
        import aws_sdk_fsx.types.volume_type

        out["VolumeType"] = aws_sdk_fsx.types.volume_type.serialize_aws_json_1_1(
            value["volume_type"]
        )
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
    if "open_zfs_configuration" in value:
        import aws_sdk_fsx.types.create_open_zfs_volume_configuration

        out["OpenZFSConfiguration"] = (
            aws_sdk_fsx.types.create_open_zfs_volume_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVolumeRequest:
    out: CreateVolumeRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "VolumeType" in data:
        import aws_sdk_fsx.types.volume_type

        out["volume_type"] = aws_sdk_fsx.types.volume_type.deserialize_aws_json_1_1(
            data["VolumeType"]
        )
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
    if "OpenZFSConfiguration" in data:
        import aws_sdk_fsx.types.create_open_zfs_volume_configuration

        out["open_zfs_configuration"] = (
            aws_sdk_fsx.types.create_open_zfs_volume_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    return out
