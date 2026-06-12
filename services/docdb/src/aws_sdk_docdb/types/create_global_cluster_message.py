"""Generated from Smithy shape ``com.amazonaws.docdb#CreateGlobalClusterMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.boolean_optional
    import aws_sdk_docdb.types.global_cluster_identifier
    import aws_sdk_docdb.types.string


class CreateGlobalClusterMessage(TypedDict):
    global_cluster_identifier: NotRequired[
        "aws_sdk_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The cluster identifier of the new global cluster.</p>"""
    source_db_cluster_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) to use as the primary cluster of the global cluster. This parameter is optional.</p>"""
    engine: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The name of the database engine to be used for this cluster.</p>"""
    engine_version: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The engine version of the global cluster.</p>"""
    deletion_protection: NotRequired[
        "aws_sdk_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>The deletion protection setting for the new global cluster. The global cluster can't be deleted when deletion protection is enabled. </p>"""
    database_name: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The name for your database of up to 64 alpha-numeric characters. If you do not provide a name, Amazon DocumentDB will not create a database in the global cluster you are creating.</p>"""
    storage_encrypted: NotRequired[
        "aws_sdk_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>The storage encryption setting for the new global cluster. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateGlobalClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "source_db_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.SourceDBClusterIdentifier",
                str(value["source_db_cluster_identifier"]),
            )
        )
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{prefix}.DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "database_name" in value:
        pairs.append((f"{prefix}.DatabaseName", str(value["database_name"])))
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{prefix}.StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )


def deserialize_query(el: Element) -> CreateGlobalClusterMessage:
    out: CreateGlobalClusterMessage = {}  # type: ignore[typeddict-item]
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_source_db_cluster_identifier = el.find("SourceDBClusterIdentifier")
    if child_source_db_cluster_identifier is not None:
        out["source_db_cluster_identifier"] = str(
            child_source_db_cluster_identifier.text or ""
        )
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_database_name = el.find("DatabaseName")
    if child_database_name is not None:
        out["database_name"] = str(child_database_name.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    return out
