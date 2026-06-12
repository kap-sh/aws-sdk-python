"""Generated from Smithy shape ``com.amazonaws.docdb#GlobalCluster``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.boolean_optional
    import aws_sdk_docdb.types.failover_state
    import aws_sdk_docdb.types.global_cluster_identifier
    import aws_sdk_docdb.types.global_cluster_member_list
    import aws_sdk_docdb.types.string
    import aws_sdk_docdb.types.tag_list


class GlobalCluster(TypedDict):
    global_cluster_identifier: NotRequired[
        "aws_sdk_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>Contains a user-supplied global cluster identifier. This identifier is the unique key that identifies a global cluster. </p>"""
    global_cluster_resource_id: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The Amazon Web Services RegionRegion-unique, immutable identifier for the global database cluster. This identifier is found in CloudTrail log entries whenever the KMS customer master key (CMK) for the cluster is accessed. </p>"""
    global_cluster_arn: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the global cluster.</p>"""
    status: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>Specifies the current state of this global cluster.</p>"""
    engine: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The Amazon DocumentDB database engine used by the global cluster. </p>"""
    engine_version: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>Indicates the database engine version.</p>"""
    database_name: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The default database name within the new global cluster.</p>"""
    storage_encrypted: NotRequired[
        "aws_sdk_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>The storage encryption setting for the global cluster.</p>"""
    deletion_protection: NotRequired[
        "aws_sdk_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>The deletion protection setting for the new global cluster.</p>"""
    global_cluster_members: NotRequired[
        "aws_sdk_docdb.types.global_cluster_member_list.GlobalClusterMemberList"
    ]
    """<p>The list of cluster IDs for secondary clusters within the global cluster. Currently limited to one item. </p>"""
    failover_state: NotRequired["aws_sdk_docdb.types.failover_state.FailoverState"]
    """<p>A data object containing all properties for the current state of an in-process or pending switchover or failover process for this global cluster. This object is empty unless the <code>SwitchoverGlobalCluster</code> or <code>FailoverGlobalCluster</code> operation was called on this global cluster.</p>"""
    tag_list: NotRequired["aws_sdk_docdb.types.tag_list.TagList"]
    """<p>A list of global cluster tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalCluster, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "global_cluster_resource_id" in value:
        pairs.append(
            (
                f"{prefix}.GlobalClusterResourceId",
                str(value["global_cluster_resource_id"]),
            )
        )
    if "global_cluster_arn" in value:
        pairs.append((f"{prefix}.GlobalClusterArn", str(value["global_cluster_arn"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "database_name" in value:
        pairs.append((f"{prefix}.DatabaseName", str(value["database_name"])))
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{prefix}.StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{prefix}.DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "global_cluster_members" in value:
        import aws_sdk_docdb.types.global_cluster_member_list

        aws_sdk_docdb.types.global_cluster_member_list.serialize_query(
            value["global_cluster_members"], pairs, f"{prefix}.GlobalClusterMembers"
        )
    if "failover_state" in value:
        import aws_sdk_docdb.types.failover_state

        aws_sdk_docdb.types.failover_state.serialize_query(
            value["failover_state"], pairs, f"{prefix}.FailoverState"
        )
    if "tag_list" in value:
        import aws_sdk_docdb.types.tag_list

        aws_sdk_docdb.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{prefix}.TagList"
        )


def deserialize_query(el: Element) -> GlobalCluster:
    out: GlobalCluster = {}  # type: ignore[typeddict-item]
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_global_cluster_resource_id = el.find("GlobalClusterResourceId")
    if child_global_cluster_resource_id is not None:
        out["global_cluster_resource_id"] = str(
            child_global_cluster_resource_id.text or ""
        )
    child_global_cluster_arn = el.find("GlobalClusterArn")
    if child_global_cluster_arn is not None:
        out["global_cluster_arn"] = str(child_global_cluster_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_database_name = el.find("DatabaseName")
    if child_database_name is not None:
        out["database_name"] = str(child_database_name.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_global_cluster_members = el.find("GlobalClusterMembers")
    if child_global_cluster_members is not None:
        import aws_sdk_docdb.types.global_cluster_member_list

        out["global_cluster_members"] = (
            aws_sdk_docdb.types.global_cluster_member_list.deserialize_query(
                child_global_cluster_members
            )
        )
    child_failover_state = el.find("FailoverState")
    if child_failover_state is not None:
        import aws_sdk_docdb.types.failover_state

        out["failover_state"] = aws_sdk_docdb.types.failover_state.deserialize_query(
            child_failover_state
        )
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import aws_sdk_docdb.types.tag_list

        out["tag_list"] = aws_sdk_docdb.types.tag_list.deserialize_query(child_tag_list)
    return out
