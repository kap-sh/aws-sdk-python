"""Generated from Smithy shape ``com.amazonaws.docdb#GlobalClusterMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.boolean
    import capo_docdb.types.global_cluster_member_synchronization_status
    import capo_docdb.types.readers_arn_list
    import capo_docdb.types.string


class GlobalClusterMember(TypedDict, closed=True):
    db_cluster_arn: NotRequired["capo_docdb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for each Amazon DocumentDB cluster.</p>"""
    readers: NotRequired["capo_docdb.types.readers_arn_list.ReadersArnList"]
    """<p>The Amazon Resource Name (ARN) for each read-only secondary cluster associated with the Amazon DocumentDB global cluster.</p>"""
    is_writer: NotRequired["capo_docdb.types.boolean.Boolean"]
    """<p> Specifies whether the Amazon DocumentDB cluster is the primary cluster (that is, has read-write capability) for the Amazon DocumentDB global cluster with which it is associated. </p>"""
    synchronization_status: NotRequired[
        "capo_docdb.types.global_cluster_member_synchronization_status.GlobalClusterMemberSynchronizationStatus"
    ]
    """<p>The status of synchronization of each Amazon DocumentDB cluster in the global cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalClusterMember, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_arn" in value:
        pairs.append((f"{key_prefix}DBClusterArn", str(value["db_cluster_arn"])))
    if "readers" in value:
        import capo_docdb.types.readers_arn_list

        capo_docdb.types.readers_arn_list.serialize_query(
            value["readers"], pairs, f"{key_prefix}Readers"
        )
    if "is_writer" in value:
        pairs.append(
            (f"{key_prefix}IsWriter", "true" if value["is_writer"] else "false")
        )
    if "synchronization_status" in value:
        import capo_docdb.types.global_cluster_member_synchronization_status

        capo_docdb.types.global_cluster_member_synchronization_status.serialize_query(
            value["synchronization_status"], pairs, f"{key_prefix}SynchronizationStatus"
        )


def deserialize_query(el: Element) -> GlobalClusterMember:
    out: GlobalClusterMember = {}  # type: ignore[typeddict-item]
    child_db_cluster_arn = el.find("DBClusterArn")
    if child_db_cluster_arn is not None:
        out["db_cluster_arn"] = str(child_db_cluster_arn.text or "")
    child_readers = el.find("Readers")
    if child_readers is not None:
        import capo_docdb.types.readers_arn_list

        out["readers"] = capo_docdb.types.readers_arn_list.deserialize_query(
            child_readers
        )
    child_is_writer = el.find("IsWriter")
    if child_is_writer is not None:
        out["is_writer"] = (child_is_writer.text or "").lower() == "true"
    child_synchronization_status = el.find("SynchronizationStatus")
    if child_synchronization_status is not None:
        import capo_docdb.types.global_cluster_member_synchronization_status

        out["synchronization_status"] = (
            capo_docdb.types.global_cluster_member_synchronization_status.deserialize_query(
                child_synchronization_status
            )
        )
    return out
