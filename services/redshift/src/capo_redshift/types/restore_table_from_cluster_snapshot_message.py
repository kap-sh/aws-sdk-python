"""Generated from Smithy shape ``com.amazonaws.redshift#RestoreTableFromClusterSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean_optional
    import capo_redshift.types.string


class RestoreTableFromClusterSnapshotMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the Amazon Redshift cluster to restore the table to.</p>"""
    snapshot_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the snapshot to restore the table from. This snapshot must have been created from the Amazon Redshift cluster specified by the <code>ClusterIdentifier</code> parameter.</p>"""
    source_database_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the source database that contains the table to restore from.</p>"""
    source_schema_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the source schema that contains the table to restore from. If you do not specify a <code>SourceSchemaName</code> value, the default is <code>public</code>.</p>"""
    source_table_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the source table to restore from.</p>"""
    target_database_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the database to restore the table to.</p>"""
    target_schema_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the schema to restore the table to.</p>"""
    new_table_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the table to create as a result of the current request.</p>"""
    enable_case_sensitive_identifier: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether name identifiers for database, schema, and table are case sensitive. If <code>true</code>, the names are case sensitive. If <code>false</code> (default), the names are not case sensitive.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreTableFromClusterSnapshotMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
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
    if "enable_case_sensitive_identifier" in value:
        pairs.append(
            (
                f"{prefix}.EnableCaseSensitiveIdentifier",
                "true" if value["enable_case_sensitive_identifier"] else "false",
            )
        )


def deserialize_query(el: Element) -> RestoreTableFromClusterSnapshotMessage:
    out: RestoreTableFromClusterSnapshotMessage = {}  # type: ignore[typeddict-item]
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
    child_enable_case_sensitive_identifier = el.find("EnableCaseSensitiveIdentifier")
    if child_enable_case_sensitive_identifier is not None:
        out["enable_case_sensitive_identifier"] = (
            child_enable_case_sensitive_identifier.text or ""
        ).lower() == "true"
    return out
