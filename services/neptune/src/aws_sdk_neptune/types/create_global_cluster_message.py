"""Generated from Smithy shape ``com.amazonaws.neptune#CreateGlobalClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.boolean_optional
    import aws_sdk_neptune.types.global_cluster_identifier
    import aws_sdk_neptune.types.string
    import aws_sdk_neptune.types.tag_list


class CreateGlobalClusterMessage(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "aws_sdk_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The cluster identifier of the new global database cluster.</p>"""
    source_db_cluster_identifier: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>(<i>Optional</i>) The Amazon Resource Name (ARN) of an existing Neptune DB cluster to use as the primary cluster of the new global database.</p>"""
    engine: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name of the database engine to be used in the global database.</p> <p>Valid values: <code>neptune</code> </p>"""
    engine_version: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The Neptune engine version to be used by the global database.</p> <p>Valid values: <code>1.2.0.0</code> or above.</p>"""
    deletion_protection: NotRequired[
        "aws_sdk_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.</p>"""
    database_name: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name for the new global database (up to 64 alpha-numeric characters).</p>"""
    tags: NotRequired["aws_sdk_neptune.types.tag_list.TagList"]
    """<p>Tags to assign to the global cluster.</p>"""
    storage_encrypted: NotRequired[
        "aws_sdk_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>The storage encryption setting for the new global database cluster.</p>"""


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
    if "tags" in value:
        import aws_sdk_neptune.types.tag_list

        aws_sdk_neptune.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
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
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_neptune.types.tag_list

        out["tags"] = aws_sdk_neptune.types.tag_list.deserialize_query(child_tags)
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    return out
