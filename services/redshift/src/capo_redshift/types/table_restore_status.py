"""Generated from Smithy shape ``com.amazonaws.redshift#TableRestoreStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.long_optional
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp
    import capo_redshift.types.table_restore_status_type


class TableRestoreStatus(TypedDict, closed=True):
    table_restore_request_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier for the table restore request.</p>"""
    status: NotRequired[
        "capo_redshift.types.table_restore_status_type.TableRestoreStatusType"
    ]
    """<p>A value that describes the current state of the table restore request.</p> <p>Valid Values: <code>SUCCEEDED</code>, <code>FAILED</code>, <code>CANCELED</code>, <code>PENDING</code>, <code>IN_PROGRESS</code> </p>"""
    message: NotRequired["capo_redshift.types.string.String"]
    """<p>A description of the status of the table restore request. Status values include <code>SUCCEEDED</code>, <code>FAILED</code>, <code>CANCELED</code>, <code>PENDING</code>, <code>IN_PROGRESS</code>.</p>"""
    request_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The time that the table restore request was made, in Universal Coordinated Time (UTC).</p>"""
    progress_in_mega_bytes: NotRequired[
        "capo_redshift.types.long_optional.LongOptional"
    ]
    """<p>The amount of data restored to the new table so far, in megabytes (MB).</p>"""
    total_data_in_mega_bytes: NotRequired[
        "capo_redshift.types.long_optional.LongOptional"
    ]
    """<p>The total amount of data to restore to the new table, in megabytes (MB).</p>"""
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the Amazon Redshift cluster that the table is being restored to.</p>"""
    snapshot_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the snapshot that the table is being restored from.</p>"""
    source_database_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the source database that contains the table being restored.</p>"""
    source_schema_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the source schema that contains the table being restored.</p>"""
    source_table_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the source table being restored.</p>"""
    target_database_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the database to restore the table to.</p>"""
    target_schema_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the schema to restore the table to.</p>"""
    new_table_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the table to create as a result of the table restore request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TableRestoreStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "table_restore_request_id" in value:
        pairs.append(
            (f"{prefix}.TableRestoreRequestId", str(value["table_restore_request_id"]))
        )
    if "status" in value:
        import capo_redshift.types.table_restore_status_type

        capo_redshift.types.table_restore_status_type.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))
    if "request_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["request_time"], pairs, f"{prefix}.RequestTime"
        )
    if "progress_in_mega_bytes" in value:
        pairs.append(
            (f"{prefix}.ProgressInMegaBytes", str(value["progress_in_mega_bytes"]))
        )
    if "total_data_in_mega_bytes" in value:
        pairs.append(
            (f"{prefix}.TotalDataInMegaBytes", str(value["total_data_in_mega_bytes"]))
        )
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "snapshot_identifier" in value:
        pairs.append(
            (f"{prefix}.SnapshotIdentifier", str(value["snapshot_identifier"]))
        )
    if "source_database_name" in value:
        pairs.append(
            (f"{prefix}.SourceDatabaseName", str(value["source_database_name"]))
        )
    if "source_schema_name" in value:
        pairs.append((f"{prefix}.SourceSchemaName", str(value["source_schema_name"])))
    if "source_table_name" in value:
        pairs.append((f"{prefix}.SourceTableName", str(value["source_table_name"])))
    if "target_database_name" in value:
        pairs.append(
            (f"{prefix}.TargetDatabaseName", str(value["target_database_name"]))
        )
    if "target_schema_name" in value:
        pairs.append((f"{prefix}.TargetSchemaName", str(value["target_schema_name"])))
    if "new_table_name" in value:
        pairs.append((f"{prefix}.NewTableName", str(value["new_table_name"])))


def deserialize_query(el: Element) -> TableRestoreStatus:
    out: TableRestoreStatus = {}  # type: ignore[typeddict-item]
    child_table_restore_request_id = el.find("TableRestoreRequestId")
    if child_table_restore_request_id is not None:
        out["table_restore_request_id"] = str(child_table_restore_request_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_redshift.types.table_restore_status_type

        out["status"] = capo_redshift.types.table_restore_status_type.deserialize_query(
            child_status
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_request_time = el.find("RequestTime")
    if child_request_time is not None:
        import capo_redshift.types.t_stamp

        out["request_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_request_time
        )
    child_progress_in_mega_bytes = el.find("ProgressInMegaBytes")
    if child_progress_in_mega_bytes is not None:
        out["progress_in_mega_bytes"] = int(child_progress_in_mega_bytes.text or "")
    child_total_data_in_mega_bytes = el.find("TotalDataInMegaBytes")
    if child_total_data_in_mega_bytes is not None:
        out["total_data_in_mega_bytes"] = int(child_total_data_in_mega_bytes.text or "")
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_source_database_name = el.find("SourceDatabaseName")
    if child_source_database_name is not None:
        out["source_database_name"] = str(child_source_database_name.text or "")
    child_source_schema_name = el.find("SourceSchemaName")
    if child_source_schema_name is not None:
        out["source_schema_name"] = str(child_source_schema_name.text or "")
    child_source_table_name = el.find("SourceTableName")
    if child_source_table_name is not None:
        out["source_table_name"] = str(child_source_table_name.text or "")
    child_target_database_name = el.find("TargetDatabaseName")
    if child_target_database_name is not None:
        out["target_database_name"] = str(child_target_database_name.text or "")
    child_target_schema_name = el.find("TargetSchemaName")
    if child_target_schema_name is not None:
        out["target_schema_name"] = str(child_target_schema_name.text or "")
    child_new_table_name = el.find("NewTableName")
    if child_new_table_name is not None:
        out["new_table_name"] = str(child_new_table_name.text or "")
    return out
