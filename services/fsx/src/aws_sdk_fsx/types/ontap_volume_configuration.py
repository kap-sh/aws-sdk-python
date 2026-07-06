"""Generated from Smithy shape ``com.amazonaws.fsx#OntapVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.aggregate_configuration
    import aws_sdk_fsx.types.flag
    import aws_sdk_fsx.types.flex_cache_endpoint_type
    import aws_sdk_fsx.types.junction_path
    import aws_sdk_fsx.types.ontap_volume_type
    import aws_sdk_fsx.types.security_style
    import aws_sdk_fsx.types.snaplock_configuration
    import aws_sdk_fsx.types.snapshot_policy
    import aws_sdk_fsx.types.storage_virtual_machine_id
    import aws_sdk_fsx.types.tiering_policy
    import aws_sdk_fsx.types.uuid
    import aws_sdk_fsx.types.volume_capacity
    import aws_sdk_fsx.types.volume_capacity_bytes
    import aws_sdk_fsx.types.volume_style


class OntapVolumeConfiguration(TypedDict, closed=True):
    flex_cache_endpoint_type: NotRequired[
        "aws_sdk_fsx.types.flex_cache_endpoint_type.FlexCacheEndpointType"
    ]
    """<p>Specifies the FlexCache endpoint type of the volume. Valid values are the following:</p> <ul> <li> <p> <code>NONE</code> specifies that the volume doesn't have a FlexCache configuration. <code>NONE</code> is the default.</p> </li> <li> <p> <code>ORIGIN</code> specifies that the volume is the origin volume for a FlexCache volume.</p> </li> <li> <p> <code>CACHE</code> specifies that the volume is a FlexCache volume.</p> </li> </ul>"""
    junction_path: NotRequired["aws_sdk_fsx.types.junction_path.JunctionPath"]
    """<p>Specifies the directory that network-attached storage (NAS) clients use to mount the volume, along with the storage virtual machine (SVM) Domain Name System (DNS) name or IP address. You can create a <code>JunctionPath</code> directly below a parent volume junction or on a directory within a volume. A <code>JunctionPath</code> for a volume named <code>vol3</code> might be <code>/vol1/vol2/vol3</code>, or <code>/vol1/dir2/vol3</code>, or even <code>/dir1/dir2/vol3</code>.</p>"""
    security_style: NotRequired["aws_sdk_fsx.types.security_style.SecurityStyle"]
    """<p>The security style for the volume, which can be <code>UNIX</code>, <code>NTFS</code>, or <code>MIXED</code>.</p>"""
    size_in_megabytes: NotRequired["aws_sdk_fsx.types.volume_capacity.VolumeCapacity"]
    """<p>The configured size of the volume, in megabytes (MBs).</p>"""
    storage_efficiency_enabled: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>The volume's storage efficiency setting.</p>"""
    storage_virtual_machine_id: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_id.StorageVirtualMachineId"
    ]
    """<p>The ID of the volume's storage virtual machine.</p>"""
    storage_virtual_machine_root: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>A Boolean flag indicating whether this volume is the root volume for its storage virtual machine (SVM). Only one volume on an SVM can be the root volume. This value defaults to <code>false</code>. If this value is <code>true</code>, then this is the SVM root volume.</p> <p>This flag is useful when you're deleting an SVM, because you must first delete all non-root volumes. This flag, when set to <code>false</code>, helps you identify which volumes to delete before you can delete the SVM.</p>"""
    tiering_policy: NotRequired["aws_sdk_fsx.types.tiering_policy.TieringPolicy"]
    """<p>The volume's <code>TieringPolicy</code> setting.</p>"""
    uuid: NotRequired["aws_sdk_fsx.types.uuid.UUID"]
    """<p>The volume's universally unique identifier (UUID).</p>"""
    ontap_volume_type: NotRequired[
        "aws_sdk_fsx.types.ontap_volume_type.OntapVolumeType"
    ]
    """<p>Specifies the type of volume. Valid values are the following:</p> <ul> <li> <p> <code>RW</code> specifies a read/write volume. <code>RW</code> is the default.</p> </li> <li> <p> <code>DP</code> specifies a data-protection volume. You can protect data by replicating it to data-protection mirror copies. If a disaster occurs, you can use these data-protection mirror copies to recover data.</p> </li> <li> <p> <code>LS</code> specifies a load-sharing mirror volume. A load-sharing mirror reduces the network traffic to a FlexVol volume by providing additional read-only access to clients.</p> </li> </ul>"""
    snapshot_policy: NotRequired["aws_sdk_fsx.types.snapshot_policy.SnapshotPolicy"]
    r"""<p>Specifies the snapshot policy for the volume. There are three built-in snapshot policies:</p> <ul> <li> <p> <code>default</code>: This is the default policy. A maximum of six hourly snapshots taken five minutes past the hour. A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after midnight. A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.</p> </li> <li> <p> <code>default-1weekly</code>: This policy is the same as the <code>default</code> policy except that it only retains one snapshot from the weekly schedule.</p> </li> <li> <p> <code>none</code>: This policy does not take any snapshots. This policy can be assigned to volumes to prevent automatic snapshots from being taken.</p> </li> </ul> <p>You can also provide the name of a custom policy that you created with the ONTAP CLI or REST API.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html#snapshot-policies\">Snapshot policies</a> in the Amazon FSx for NetApp ONTAP User Guide.</p>"""
    copy_tags_to_backups: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>A boolean flag indicating whether tags for the volume should be copied to backups. This value defaults to false. If it's set to true, all tags for the volume are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the volume, regardless of this value.</p>"""
    snaplock_configuration: NotRequired[
        "aws_sdk_fsx.types.snaplock_configuration.SnaplockConfiguration"
    ]
    """<p>The SnapLock configuration object for an FSx for ONTAP SnapLock volume. </p>"""
    volume_style: NotRequired["aws_sdk_fsx.types.volume_style.VolumeStyle"]
    r"""<p>Use to specify the style of an ONTAP volume. For more information about FlexVols and FlexGroups, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-types.html\">Volume types</a> in Amazon FSx for NetApp ONTAP User Guide.</p>"""
    aggregate_configuration: NotRequired[
        "aws_sdk_fsx.types.aggregate_configuration.AggregateConfiguration"
    ]
    """<p>This structure specifies configuration options for a volume’s storage aggregate or aggregates.</p>"""
    size_in_bytes: NotRequired[
        "aws_sdk_fsx.types.volume_capacity_bytes.VolumeCapacityBytes"
    ]
    """<p>The configured size of the volume, in bytes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OntapVolumeConfiguration) -> dict:
    out: dict = {}
    if "flex_cache_endpoint_type" in value:
        import aws_sdk_fsx.types.flex_cache_endpoint_type

        out["FlexCacheEndpointType"] = (
            aws_sdk_fsx.types.flex_cache_endpoint_type.serialize_aws_json_1_1(
                value["flex_cache_endpoint_type"]
            )
        )
    if "junction_path" in value:
        out["JunctionPath"] = value["junction_path"]
    if "security_style" in value:
        import aws_sdk_fsx.types.security_style

        out["SecurityStyle"] = aws_sdk_fsx.types.security_style.serialize_aws_json_1_1(
            value["security_style"]
        )
    if "size_in_megabytes" in value:
        out["SizeInMegabytes"] = value["size_in_megabytes"]
    if "storage_efficiency_enabled" in value:
        out["StorageEfficiencyEnabled"] = value["storage_efficiency_enabled"]
    if "storage_virtual_machine_id" in value:
        out["StorageVirtualMachineId"] = value["storage_virtual_machine_id"]
    if "storage_virtual_machine_root" in value:
        out["StorageVirtualMachineRoot"] = value["storage_virtual_machine_root"]
    if "tiering_policy" in value:
        import aws_sdk_fsx.types.tiering_policy

        out["TieringPolicy"] = aws_sdk_fsx.types.tiering_policy.serialize_aws_json_1_1(
            value["tiering_policy"]
        )
    if "uuid" in value:
        out["UUID"] = value["uuid"]
    if "ontap_volume_type" in value:
        import aws_sdk_fsx.types.ontap_volume_type

        out["OntapVolumeType"] = (
            aws_sdk_fsx.types.ontap_volume_type.serialize_aws_json_1_1(
                value["ontap_volume_type"]
            )
        )
    if "snapshot_policy" in value:
        out["SnapshotPolicy"] = value["snapshot_policy"]
    if "copy_tags_to_backups" in value:
        out["CopyTagsToBackups"] = value["copy_tags_to_backups"]
    if "snaplock_configuration" in value:
        import aws_sdk_fsx.types.snaplock_configuration

        out["SnaplockConfiguration"] = (
            aws_sdk_fsx.types.snaplock_configuration.serialize_aws_json_1_1(
                value["snaplock_configuration"]
            )
        )
    if "volume_style" in value:
        import aws_sdk_fsx.types.volume_style

        out["VolumeStyle"] = aws_sdk_fsx.types.volume_style.serialize_aws_json_1_1(
            value["volume_style"]
        )
    if "aggregate_configuration" in value:
        import aws_sdk_fsx.types.aggregate_configuration

        out["AggregateConfiguration"] = (
            aws_sdk_fsx.types.aggregate_configuration.serialize_aws_json_1_1(
                value["aggregate_configuration"]
            )
        )
    if "size_in_bytes" in value:
        out["SizeInBytes"] = value["size_in_bytes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OntapVolumeConfiguration:
    out: OntapVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if "FlexCacheEndpointType" in data:
        import aws_sdk_fsx.types.flex_cache_endpoint_type

        out["flex_cache_endpoint_type"] = (
            aws_sdk_fsx.types.flex_cache_endpoint_type.deserialize_aws_json_1_1(
                data["FlexCacheEndpointType"]
            )
        )
    if "JunctionPath" in data:
        out["junction_path"] = data["JunctionPath"]
    if "SecurityStyle" in data:
        import aws_sdk_fsx.types.security_style

        out["security_style"] = (
            aws_sdk_fsx.types.security_style.deserialize_aws_json_1_1(
                data["SecurityStyle"]
            )
        )
    if "SizeInMegabytes" in data:
        out["size_in_megabytes"] = data["SizeInMegabytes"]
    if "StorageEfficiencyEnabled" in data:
        out["storage_efficiency_enabled"] = data["StorageEfficiencyEnabled"]
    if "StorageVirtualMachineId" in data:
        out["storage_virtual_machine_id"] = data["StorageVirtualMachineId"]
    if "StorageVirtualMachineRoot" in data:
        out["storage_virtual_machine_root"] = data["StorageVirtualMachineRoot"]
    if "TieringPolicy" in data:
        import aws_sdk_fsx.types.tiering_policy

        out["tiering_policy"] = (
            aws_sdk_fsx.types.tiering_policy.deserialize_aws_json_1_1(
                data["TieringPolicy"]
            )
        )
    if "UUID" in data:
        out["uuid"] = data["UUID"]
    if "OntapVolumeType" in data:
        import aws_sdk_fsx.types.ontap_volume_type

        out["ontap_volume_type"] = (
            aws_sdk_fsx.types.ontap_volume_type.deserialize_aws_json_1_1(
                data["OntapVolumeType"]
            )
        )
    if "SnapshotPolicy" in data:
        out["snapshot_policy"] = data["SnapshotPolicy"]
    if "CopyTagsToBackups" in data:
        out["copy_tags_to_backups"] = data["CopyTagsToBackups"]
    if "SnaplockConfiguration" in data:
        import aws_sdk_fsx.types.snaplock_configuration

        out["snaplock_configuration"] = (
            aws_sdk_fsx.types.snaplock_configuration.deserialize_aws_json_1_1(
                data["SnaplockConfiguration"]
            )
        )
    if "VolumeStyle" in data:
        import aws_sdk_fsx.types.volume_style

        out["volume_style"] = aws_sdk_fsx.types.volume_style.deserialize_aws_json_1_1(
            data["VolumeStyle"]
        )
    if "AggregateConfiguration" in data:
        import aws_sdk_fsx.types.aggregate_configuration

        out["aggregate_configuration"] = (
            aws_sdk_fsx.types.aggregate_configuration.deserialize_aws_json_1_1(
                data["AggregateConfiguration"]
            )
        )
    if "SizeInBytes" in data:
        out["size_in_bytes"] = data["SizeInBytes"]
    return out
