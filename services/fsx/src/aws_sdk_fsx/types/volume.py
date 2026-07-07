"""Generated from Smithy shape ``com.amazonaws.fsx#Volume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.administrative_actions
    import aws_sdk_fsx.types.creation_time
    import aws_sdk_fsx.types.file_system_id
    import aws_sdk_fsx.types.lifecycle_transition_reason
    import aws_sdk_fsx.types.ontap_volume_configuration
    import aws_sdk_fsx.types.open_zfs_volume_configuration
    import aws_sdk_fsx.types.resource_arn
    import aws_sdk_fsx.types.tags
    import aws_sdk_fsx.types.volume_id
    import aws_sdk_fsx.types.volume_lifecycle
    import aws_sdk_fsx.types.volume_name
    import aws_sdk_fsx.types.volume_type


class Volume(TypedDict, closed=True):
    creation_time: NotRequired["aws_sdk_fsx.types.creation_time.CreationTime"]
    file_system_id: NotRequired["aws_sdk_fsx.types.file_system_id.FileSystemId"]
    lifecycle: NotRequired["aws_sdk_fsx.types.volume_lifecycle.VolumeLifecycle"]
    """<p>The lifecycle status of the volume.</p> <ul> <li> <p> <code>AVAILABLE</code> - The volume is fully available for use.</p> </li> <li> <p> <code>CREATED</code> - The volume has been created.</p> </li> <li> <p> <code>CREATING</code> - Amazon FSx is creating the new volume.</p> </li> <li> <p> <code>DELETING</code> - Amazon FSx is deleting an existing volume.</p> </li> <li> <p> <code>FAILED</code> - Amazon FSx was unable to create the volume.</p> </li> <li> <p> <code>MISCONFIGURED</code> - The volume is in a failed but recoverable state.</p> </li> <li> <p> <code>PENDING</code> - Amazon FSx hasn't started creating the volume.</p> </li> </ul>"""
    name: NotRequired["aws_sdk_fsx.types.volume_name.VolumeName"]
    """<p>The name of the volume.</p>"""
    ontap_configuration: NotRequired[
        "aws_sdk_fsx.types.ontap_volume_configuration.OntapVolumeConfiguration"
    ]
    resource_arn: NotRequired["aws_sdk_fsx.types.resource_arn.ResourceARN"]
    tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]
    volume_id: NotRequired["aws_sdk_fsx.types.volume_id.VolumeId"]
    """<p>The system-generated, unique ID of the volume.</p>"""
    volume_type: NotRequired["aws_sdk_fsx.types.volume_type.VolumeType"]
    """<p>The type of the volume.</p>"""
    lifecycle_transition_reason: NotRequired[
        "aws_sdk_fsx.types.lifecycle_transition_reason.LifecycleTransitionReason"
    ]
    """<p>The reason why the volume lifecycle status changed.</p>"""
    administrative_actions: NotRequired[
        "aws_sdk_fsx.types.administrative_actions.AdministrativeActions"
    ]
    """<p>A list of administrative actions for the volume that are in process or waiting to be processed. Administrative actions describe changes to the volume that you have initiated using the <code>UpdateVolume</code> action.</p>"""
    open_zfs_configuration: NotRequired[
        "aws_sdk_fsx.types.open_zfs_volume_configuration.OpenZFSVolumeConfiguration"
    ]
    """<p>The configuration of an Amazon FSx for OpenZFS volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Volume) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import aws_sdk_fsx.types.creation_time

        out["CreationTime"] = aws_sdk_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "lifecycle" in value:
        import aws_sdk_fsx.types.volume_lifecycle

        out["Lifecycle"] = aws_sdk_fsx.types.volume_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "ontap_configuration" in value:
        import aws_sdk_fsx.types.ontap_volume_configuration

        out["OntapConfiguration"] = (
            aws_sdk_fsx.types.ontap_volume_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tags" in value:
        import aws_sdk_fsx.types.tags

        out["Tags"] = aws_sdk_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "volume_type" in value:
        import aws_sdk_fsx.types.volume_type

        out["VolumeType"] = aws_sdk_fsx.types.volume_type.serialize_aws_json_1_1(
            value["volume_type"]
        )
    if "lifecycle_transition_reason" in value:
        import aws_sdk_fsx.types.lifecycle_transition_reason

        out["LifecycleTransitionReason"] = (
            aws_sdk_fsx.types.lifecycle_transition_reason.serialize_aws_json_1_1(
                value["lifecycle_transition_reason"]
            )
        )
    if "administrative_actions" in value:
        import aws_sdk_fsx.types.administrative_actions

        out["AdministrativeActions"] = (
            aws_sdk_fsx.types.administrative_actions.serialize_aws_json_1_1(
                value["administrative_actions"]
            )
        )
    if "open_zfs_configuration" in value:
        import aws_sdk_fsx.types.open_zfs_volume_configuration

        out["OpenZFSConfiguration"] = (
            aws_sdk_fsx.types.open_zfs_volume_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Volume:
    out: Volume = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        import aws_sdk_fsx.types.creation_time

        out["creation_time"] = aws_sdk_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.volume_lifecycle

        out["lifecycle"] = aws_sdk_fsx.types.volume_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "OntapConfiguration" in data:
        import aws_sdk_fsx.types.ontap_volume_configuration

        out["ontap_configuration"] = (
            aws_sdk_fsx.types.ontap_volume_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "Tags" in data:
        import aws_sdk_fsx.types.tags

        out["tags"] = aws_sdk_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "VolumeType" in data:
        import aws_sdk_fsx.types.volume_type

        out["volume_type"] = aws_sdk_fsx.types.volume_type.deserialize_aws_json_1_1(
            data["VolumeType"]
        )
    if "LifecycleTransitionReason" in data:
        import aws_sdk_fsx.types.lifecycle_transition_reason

        out["lifecycle_transition_reason"] = (
            aws_sdk_fsx.types.lifecycle_transition_reason.deserialize_aws_json_1_1(
                data["LifecycleTransitionReason"]
            )
        )
    if "AdministrativeActions" in data:
        import aws_sdk_fsx.types.administrative_actions

        out["administrative_actions"] = (
            aws_sdk_fsx.types.administrative_actions.deserialize_aws_json_1_1(
                data["AdministrativeActions"]
            )
        )
    if "OpenZFSConfiguration" in data:
        import aws_sdk_fsx.types.open_zfs_volume_configuration

        out["open_zfs_configuration"] = (
            aws_sdk_fsx.types.open_zfs_volume_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    return out
