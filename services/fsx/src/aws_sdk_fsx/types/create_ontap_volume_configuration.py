"""Generated from Smithy shape ``com.amazonaws.fsx#CreateOntapVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.create_aggregate_configuration
    import aws_sdk_fsx.types.create_snaplock_configuration
    import aws_sdk_fsx.types.flag
    import aws_sdk_fsx.types.input_ontap_volume_type
    import aws_sdk_fsx.types.junction_path
    import aws_sdk_fsx.types.security_style
    import aws_sdk_fsx.types.snapshot_policy
    import aws_sdk_fsx.types.storage_virtual_machine_id
    import aws_sdk_fsx.types.tiering_policy
    import aws_sdk_fsx.types.volume_capacity
    import aws_sdk_fsx.types.volume_capacity_bytes
    import aws_sdk_fsx.types.volume_style


class CreateOntapVolumeConfiguration(TypedDict, closed=True):
    junction_path: NotRequired["aws_sdk_fsx.types.junction_path.JunctionPath"]
    """<p>Specifies the location in the SVM's namespace where the volume is mounted. This parameter is required. The <code>JunctionPath</code> must have a leading forward slash, such as <code>/vol3</code>.</p>"""
    security_style: NotRequired["aws_sdk_fsx.types.security_style.SecurityStyle"]
    r"""<p>Specifies the security style for the volume. If a volume's security style is not specified, it is automatically set to the root volume's security style. The security style determines the type of permissions that FSx for ONTAP uses to control data access. Specify one of the following values:</p> <ul> <li> <p> <code>UNIX</code> if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account. </p> </li> <li> <p> <code>NTFS</code> if the file system is managed by a Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Windows user as the service account.</p> </li> <li> <p> <code>MIXED</code> This is an advanced setting. For more information, see the topic <a href=\"https://docs.netapp.com/us-en/ontap/nfs-admin/security-styles-their-effects-concept.html\">What the security styles and their effects are</a> in the NetApp Documentation Center.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-security-style\">Volume security style</a> in the FSx for ONTAP User Guide.</p>"""
    size_in_megabytes: NotRequired["aws_sdk_fsx.types.volume_capacity.VolumeCapacity"]
    """<p>Use <code>SizeInBytes</code> instead. Specifies the size of the volume, in megabytes (MB), that you are creating.</p>"""
    storage_efficiency_enabled: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>Set to true to enable deduplication, compression, and compaction storage efficiency features on the volume, or set to false to disable them.</p> <p> <code>StorageEfficiencyEnabled</code> is required when creating a <code>RW</code> volume (<code>OntapVolumeType</code> set to <code>RW</code>).</p>"""
    storage_virtual_machine_id: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_id.StorageVirtualMachineId"
    ]
    """<p>Specifies the ONTAP SVM in which to create the volume.</p>"""
    tiering_policy: NotRequired["aws_sdk_fsx.types.tiering_policy.TieringPolicy"]
    ontap_volume_type: NotRequired[
        "aws_sdk_fsx.types.input_ontap_volume_type.InputOntapVolumeType"
    ]
    r"""<p>Specifies the type of volume you are creating. Valid values are the following:</p> <ul> <li> <p> <code>RW</code> specifies a read/write volume. <code>RW</code> is the default.</p> </li> <li> <p> <code>DP</code> specifies a data-protection volume. A <code>DP</code> volume is read-only and can be used as the destination of a NetApp SnapMirror relationship.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-types\">Volume types</a> in the Amazon FSx for NetApp ONTAP User Guide.</p>"""
    snapshot_policy: NotRequired["aws_sdk_fsx.types.snapshot_policy.SnapshotPolicy"]
    r"""<p>Specifies the snapshot policy for the volume. There are three built-in snapshot policies:</p> <ul> <li> <p> <code>default</code>: This is the default policy. A maximum of six hourly snapshots taken five minutes past the hour. A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after midnight. A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.</p> </li> <li> <p> <code>default-1weekly</code>: This policy is the same as the <code>default</code> policy except that it only retains one snapshot from the weekly schedule.</p> </li> <li> <p> <code>none</code>: This policy does not take any snapshots. This policy can be assigned to volumes to prevent automatic snapshots from being taken.</p> </li> </ul> <p>You can also provide the name of a custom policy that you created with the ONTAP CLI or REST API.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html#snapshot-policies\">Snapshot policies</a> in the Amazon FSx for NetApp ONTAP User Guide.</p>"""
    copy_tags_to_backups: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>A boolean flag indicating whether tags for the volume should be copied to backups. This value defaults to false. If it's set to true, all tags for the volume are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the volume, regardless of this value.</p>"""
    snaplock_configuration: NotRequired[
        "aws_sdk_fsx.types.create_snaplock_configuration.CreateSnaplockConfiguration"
    ]
    """<p>Specifies the SnapLock configuration for an FSx for ONTAP volume. </p>"""
    volume_style: NotRequired["aws_sdk_fsx.types.volume_style.VolumeStyle"]
    r"""<p>Use to specify the style of an ONTAP volume. FSx for ONTAP offers two styles of volumes that you can use for different purposes, FlexVol and FlexGroup volumes. For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-styles\">Volume styles</a> in the Amazon FSx for NetApp ONTAP User Guide.</p>"""
    aggregate_configuration: NotRequired[
        "aws_sdk_fsx.types.create_aggregate_configuration.CreateAggregateConfiguration"
    ]
    """<p>Use to specify configuration options for a volume’s storage aggregate or aggregates.</p>"""
    size_in_bytes: NotRequired[
        "aws_sdk_fsx.types.volume_capacity_bytes.VolumeCapacityBytes"
    ]
    """<p>Specifies the configured size of the volume, in bytes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOntapVolumeConfiguration) -> dict:
    out: dict = {}
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
    if "tiering_policy" in value:
        import aws_sdk_fsx.types.tiering_policy

        out["TieringPolicy"] = aws_sdk_fsx.types.tiering_policy.serialize_aws_json_1_1(
            value["tiering_policy"]
        )
    if "ontap_volume_type" in value:
        import aws_sdk_fsx.types.input_ontap_volume_type

        out["OntapVolumeType"] = (
            aws_sdk_fsx.types.input_ontap_volume_type.serialize_aws_json_1_1(
                value["ontap_volume_type"]
            )
        )
    if "snapshot_policy" in value:
        out["SnapshotPolicy"] = value["snapshot_policy"]
    if "copy_tags_to_backups" in value:
        out["CopyTagsToBackups"] = value["copy_tags_to_backups"]
    if "snaplock_configuration" in value:
        import aws_sdk_fsx.types.create_snaplock_configuration

        out["SnaplockConfiguration"] = (
            aws_sdk_fsx.types.create_snaplock_configuration.serialize_aws_json_1_1(
                value["snaplock_configuration"]
            )
        )
    if "volume_style" in value:
        import aws_sdk_fsx.types.volume_style

        out["VolumeStyle"] = aws_sdk_fsx.types.volume_style.serialize_aws_json_1_1(
            value["volume_style"]
        )
    if "aggregate_configuration" in value:
        import aws_sdk_fsx.types.create_aggregate_configuration

        out["AggregateConfiguration"] = (
            aws_sdk_fsx.types.create_aggregate_configuration.serialize_aws_json_1_1(
                value["aggregate_configuration"]
            )
        )
    if "size_in_bytes" in value:
        out["SizeInBytes"] = value["size_in_bytes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOntapVolumeConfiguration:
    out: CreateOntapVolumeConfiguration = {}  # type: ignore[typeddict-item]
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
    if "TieringPolicy" in data:
        import aws_sdk_fsx.types.tiering_policy

        out["tiering_policy"] = (
            aws_sdk_fsx.types.tiering_policy.deserialize_aws_json_1_1(
                data["TieringPolicy"]
            )
        )
    if "OntapVolumeType" in data:
        import aws_sdk_fsx.types.input_ontap_volume_type

        out["ontap_volume_type"] = (
            aws_sdk_fsx.types.input_ontap_volume_type.deserialize_aws_json_1_1(
                data["OntapVolumeType"]
            )
        )
    if "SnapshotPolicy" in data:
        out["snapshot_policy"] = data["SnapshotPolicy"]
    if "CopyTagsToBackups" in data:
        out["copy_tags_to_backups"] = data["CopyTagsToBackups"]
    if "SnaplockConfiguration" in data:
        import aws_sdk_fsx.types.create_snaplock_configuration

        out["snaplock_configuration"] = (
            aws_sdk_fsx.types.create_snaplock_configuration.deserialize_aws_json_1_1(
                data["SnaplockConfiguration"]
            )
        )
    if "VolumeStyle" in data:
        import aws_sdk_fsx.types.volume_style

        out["volume_style"] = aws_sdk_fsx.types.volume_style.deserialize_aws_json_1_1(
            data["VolumeStyle"]
        )
    if "AggregateConfiguration" in data:
        import aws_sdk_fsx.types.create_aggregate_configuration

        out["aggregate_configuration"] = (
            aws_sdk_fsx.types.create_aggregate_configuration.deserialize_aws_json_1_1(
                data["AggregateConfiguration"]
            )
        )
    if "SizeInBytes" in data:
        out["size_in_bytes"] = data["SizeInBytes"]
    return out
