"""Generated from Smithy shape ``com.amazonaws.docdb#DBClusterSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.availability_zones
    import capo_docdb.types.boolean
    import capo_docdb.types.integer
    import capo_docdb.types.string
    import capo_docdb.types.t_stamp


class DBClusterSnapshot(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_docdb.types.availability_zones.AvailabilityZones"
    ]
    """<p>Provides the list of Amazon EC2 Availability Zones that instances in the cluster snapshot can be restored in.</p>"""
    db_cluster_snapshot_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>Specifies the identifier for the cluster snapshot.</p>"""
    db_cluster_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>Specifies the cluster identifier of the cluster that this cluster snapshot was created from.</p>"""
    snapshot_create_time: NotRequired["capo_docdb.types.t_stamp.TStamp"]
    """<p>Provides the time when the snapshot was taken, in UTC.</p>"""
    engine: NotRequired["capo_docdb.types.string.String"]
    """<p>Specifies the name of the database engine.</p>"""
    status: NotRequired["capo_docdb.types.string.String"]
    """<p>Specifies the status of this cluster snapshot.</p>"""
    port: NotRequired["capo_docdb.types.integer.Integer"]
    """<p>Specifies the port that the cluster was listening on at the time of the snapshot.</p>"""
    vpc_id: NotRequired["capo_docdb.types.string.String"]
    """<p>Provides the virtual private cloud (VPC) ID that is associated with the cluster snapshot.</p>"""
    cluster_create_time: NotRequired["capo_docdb.types.t_stamp.TStamp"]
    """<p>Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).</p>"""
    master_username: NotRequired["capo_docdb.types.string.String"]
    """<p>Provides the master user name for the cluster snapshot.</p>"""
    engine_version: NotRequired["capo_docdb.types.string.String"]
    """<p>Provides the version of the database engine for this cluster snapshot.</p>"""
    snapshot_type: NotRequired["capo_docdb.types.string.String"]
    """<p>Provides the type of the cluster snapshot.</p>"""
    percent_progress: NotRequired["capo_docdb.types.integer.Integer"]
    """<p>Specifies the percentage of the estimated data that has been transferred.</p>"""
    storage_encrypted: NotRequired["capo_docdb.types.boolean.Boolean"]
    """<p>Specifies whether the cluster snapshot is encrypted.</p>"""
    kms_key_id: NotRequired["capo_docdb.types.string.String"]
    """<p>If <code>StorageEncrypted</code> is <code>true</code>, the KMS key identifier for the encrypted cluster snapshot.</p>"""
    db_cluster_snapshot_arn: NotRequired["capo_docdb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the cluster snapshot.</p>"""
    source_db_cluster_snapshot_arn: NotRequired["capo_docdb.types.string.String"]
    """<p>If the cluster snapshot was copied from a source cluster snapshot, the ARN for the source cluster snapshot; otherwise, a null value.</p>"""
    storage_type: NotRequired["capo_docdb.types.string.String"]
    """<p>Storage type associated with your cluster snapshot</p> <p>For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the <i>Amazon DocumentDB Developer Guide</i>.</p> <p>Valid values for storage type - <code>standard | iopt1</code> </p> <p>Default value is <code>standard </code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterSnapshot, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zones" in value:
        import capo_docdb.types.availability_zones

        capo_docdb.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterSnapshotIdentifier",
                str(value["db_cluster_snapshot_identifier"]),
            )
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "snapshot_create_time" in value:
        import capo_docdb.types.t_stamp

        capo_docdb.types.t_stamp.serialize_query(
            value["snapshot_create_time"], pairs, f"{key_prefix}SnapshotCreateTime"
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "cluster_create_time" in value:
        import capo_docdb.types.t_stamp

        capo_docdb.types.t_stamp.serialize_query(
            value["cluster_create_time"], pairs, f"{key_prefix}ClusterCreateTime"
        )
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "snapshot_type" in value:
        pairs.append((f"{key_prefix}SnapshotType", str(value["snapshot_type"])))
    if "percent_progress" in value:
        pairs.append((f"{key_prefix}PercentProgress", str(value["percent_progress"])))
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{key_prefix}StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "db_cluster_snapshot_arn" in value:
        pairs.append(
            (f"{key_prefix}DBClusterSnapshotArn", str(value["db_cluster_snapshot_arn"]))
        )
    if "source_db_cluster_snapshot_arn" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBClusterSnapshotArn",
                str(value["source_db_cluster_snapshot_arn"]),
            )
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))


def deserialize_query(el: Element) -> DBClusterSnapshot:
    out: DBClusterSnapshot = {}  # type: ignore[typeddict-item]
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_docdb.types.availability_zones

        out["availability_zones"] = (
            capo_docdb.types.availability_zones.deserialize_query(
                child_availability_zones
            )
        )
    child_db_cluster_snapshot_identifier = el.find("DBClusterSnapshotIdentifier")
    if child_db_cluster_snapshot_identifier is not None:
        out["db_cluster_snapshot_identifier"] = str(
            child_db_cluster_snapshot_identifier.text or ""
        )
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_snapshot_create_time = el.find("SnapshotCreateTime")
    if child_snapshot_create_time is not None:
        import capo_docdb.types.t_stamp

        out["snapshot_create_time"] = capo_docdb.types.t_stamp.deserialize_query(
            child_snapshot_create_time
        )
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_cluster_create_time = el.find("ClusterCreateTime")
    if child_cluster_create_time is not None:
        import capo_docdb.types.t_stamp

        out["cluster_create_time"] = capo_docdb.types.t_stamp.deserialize_query(
            child_cluster_create_time
        )
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_snapshot_type = el.find("SnapshotType")
    if child_snapshot_type is not None:
        out["snapshot_type"] = str(child_snapshot_type.text or "")
    child_percent_progress = el.find("PercentProgress")
    if child_percent_progress is not None:
        out["percent_progress"] = int(child_percent_progress.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_db_cluster_snapshot_arn = el.find("DBClusterSnapshotArn")
    if child_db_cluster_snapshot_arn is not None:
        out["db_cluster_snapshot_arn"] = str(child_db_cluster_snapshot_arn.text or "")
    child_source_db_cluster_snapshot_arn = el.find("SourceDBClusterSnapshotArn")
    if child_source_db_cluster_snapshot_arn is not None:
        out["source_db_cluster_snapshot_arn"] = str(
            child_source_db_cluster_snapshot_arn.text or ""
        )
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    return out
