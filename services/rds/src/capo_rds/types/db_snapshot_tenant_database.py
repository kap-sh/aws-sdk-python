"""Generated from Smithy shape ``com.amazonaws.rds#DBSnapshotTenantDatabase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list


class DBSnapshotTenantDatabase(TypedDict, closed=True):
    db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the snapshot of the DB instance.</p>"""
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The ID for the DB instance that contains the tenant databases.</p>"""
    dbi_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The resource identifier of the source CDB instance. This identifier can't be changed and is unique to an Amazon Web Services Region.</p>"""
    engine_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the database engine.</p>"""
    snapshot_type: NotRequired["capo_rds.types.string.String"]
    """<p>The type of DB snapshot.</p>"""
    tenant_database_create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The time the DB snapshot was taken, specified in Coordinated Universal Time (UTC). If you copy the snapshot, the creation time changes.</p>"""
    tenant_db_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the tenant database.</p>"""
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>The master username of the tenant database.</p>"""
    tenant_database_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The resource ID of the tenant database.</p>"""
    character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the character set of a tenant database.</p>"""
    db_snapshot_tenant_database_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the snapshot tenant database.</p>"""
    nchar_character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>The <code>NCHAR</code> character set name of the tenant database.</p>"""
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshotTenantDatabase, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_snapshot_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBSnapshotIdentifier", str(value["db_snapshot_identifier"]))
        )
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "dbi_resource_id" in value:
        pairs.append((f"{key_prefix}DbiResourceId", str(value["dbi_resource_id"])))
    if "engine_name" in value:
        pairs.append((f"{key_prefix}EngineName", str(value["engine_name"])))
    if "snapshot_type" in value:
        pairs.append((f"{key_prefix}SnapshotType", str(value["snapshot_type"])))
    if "tenant_database_create_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["tenant_database_create_time"],
            pairs,
            f"{key_prefix}TenantDatabaseCreateTime",
        )
    if "tenant_db_name" in value:
        pairs.append((f"{key_prefix}TenantDBName", str(value["tenant_db_name"])))
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "tenant_database_resource_id" in value:
        pairs.append(
            (
                f"{key_prefix}TenantDatabaseResourceId",
                str(value["tenant_database_resource_id"]),
            )
        )
    if "character_set_name" in value:
        pairs.append(
            (f"{key_prefix}CharacterSetName", str(value["character_set_name"]))
        )
    if "db_snapshot_tenant_database_arn" in value:
        pairs.append(
            (
                f"{key_prefix}DBSnapshotTenantDatabaseARN",
                str(value["db_snapshot_tenant_database_arn"]),
            )
        )
    if "nchar_character_set_name" in value:
        pairs.append(
            (
                f"{key_prefix}NcharCharacterSetName",
                str(value["nchar_character_set_name"]),
            )
        )
    if "tag_list" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{key_prefix}TagList"
        )


def deserialize_query(el: Element) -> DBSnapshotTenantDatabase:
    out: DBSnapshotTenantDatabase = {}  # type: ignore[typeddict-item]
    child_db_snapshot_identifier = el.find("DBSnapshotIdentifier")
    if child_db_snapshot_identifier is not None:
        out["db_snapshot_identifier"] = str(child_db_snapshot_identifier.text or "")
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_dbi_resource_id = el.find("DbiResourceId")
    if child_dbi_resource_id is not None:
        out["dbi_resource_id"] = str(child_dbi_resource_id.text or "")
    child_engine_name = el.find("EngineName")
    if child_engine_name is not None:
        out["engine_name"] = str(child_engine_name.text or "")
    child_snapshot_type = el.find("SnapshotType")
    if child_snapshot_type is not None:
        out["snapshot_type"] = str(child_snapshot_type.text or "")
    child_tenant_database_create_time = el.find("TenantDatabaseCreateTime")
    if child_tenant_database_create_time is not None:
        import capo_rds.types.t_stamp

        out["tenant_database_create_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_tenant_database_create_time
        )
    child_tenant_db_name = el.find("TenantDBName")
    if child_tenant_db_name is not None:
        out["tenant_db_name"] = str(child_tenant_db_name.text or "")
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_tenant_database_resource_id = el.find("TenantDatabaseResourceId")
    if child_tenant_database_resource_id is not None:
        out["tenant_database_resource_id"] = str(
            child_tenant_database_resource_id.text or ""
        )
    child_character_set_name = el.find("CharacterSetName")
    if child_character_set_name is not None:
        out["character_set_name"] = str(child_character_set_name.text or "")
    child_db_snapshot_tenant_database_arn = el.find("DBSnapshotTenantDatabaseARN")
    if child_db_snapshot_tenant_database_arn is not None:
        out["db_snapshot_tenant_database_arn"] = str(
            child_db_snapshot_tenant_database_arn.text or ""
        )
    child_nchar_character_set_name = el.find("NcharCharacterSetName")
    if child_nchar_character_set_name is not None:
        out["nchar_character_set_name"] = str(child_nchar_character_set_name.text or "")
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    return out
