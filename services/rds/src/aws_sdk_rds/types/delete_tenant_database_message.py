"""Generated from Smithy shape ``com.amazonaws.rds#DeleteTenantDatabaseMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.string


class DeleteTenantDatabaseMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The user-supplied identifier for the DB instance that contains the tenant database that you want to delete.</p>"""
    tenant_db_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The user-supplied name of the tenant database that you want to remove from your DB instance. Amazon RDS deletes the tenant database with this name. This parameter isn’t case-sensitive.</p>"""
    skip_final_snapshot: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Specifies whether to skip the creation of a final DB snapshot before removing the tenant database from your DB instance. If you enable this parameter, RDS doesn't create a DB snapshot. If you don't enable this parameter, RDS creates a DB snapshot before it deletes the tenant database. By default, RDS doesn't skip the final snapshot. If you don't enable this parameter, you must specify the <code>FinalDBSnapshotIdentifier</code> parameter.</p>"""
    final_db_snapshot_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The <code>DBSnapshotIdentifier</code> of the new <code>DBSnapshot</code> created when the <code>SkipFinalSnapshot</code> parameter is disabled.</p> <note> <p>If you enable this parameter and also enable <code>SkipFinalShapshot</code>, the command results in an error.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteTenantDatabaseMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{prefix}.DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "tenant_db_name" in value:
        pairs.append((f"{prefix}.TenantDBName", str(value["tenant_db_name"])))
    if "skip_final_snapshot" in value:
        pairs.append(
            (
                f"{prefix}.SkipFinalSnapshot",
                "true" if value["skip_final_snapshot"] else "false",
            )
        )
    if "final_db_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.FinalDBSnapshotIdentifier",
                str(value["final_db_snapshot_identifier"]),
            )
        )


def deserialize_query(el: Element) -> DeleteTenantDatabaseMessage:
    out: DeleteTenantDatabaseMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_tenant_db_name = el.find("TenantDBName")
    if child_tenant_db_name is not None:
        out["tenant_db_name"] = str(child_tenant_db_name.text or "")
    child_skip_final_snapshot = el.find("SkipFinalSnapshot")
    if child_skip_final_snapshot is not None:
        out["skip_final_snapshot"] = (
            child_skip_final_snapshot.text or ""
        ).lower() == "true"
    child_final_db_snapshot_identifier = el.find("FinalDBSnapshotIdentifier")
    if child_final_db_snapshot_identifier is not None:
        out["final_db_snapshot_identifier"] = str(
            child_final_db_snapshot_identifier.text or ""
        )
    return out
