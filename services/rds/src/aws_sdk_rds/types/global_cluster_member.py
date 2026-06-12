"""Generated from Smithy shape ``com.amazonaws.rds#GlobalClusterMember``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.global_cluster_member_synchronization_status
    import aws_sdk_rds.types.readers_arn_list
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.write_forwarding_status


class GlobalClusterMember(TypedDict):
    db_cluster_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for each Aurora DB cluster in the global cluster.</p>"""
    readers: NotRequired["aws_sdk_rds.types.readers_arn_list.ReadersArnList"]
    """<p>The Amazon Resource Name (ARN) for each read-only secondary cluster associated with the global cluster.</p>"""
    is_writer: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Indicates whether the Aurora DB cluster is the primary cluster (that is, has read-write capability) for the global cluster with which it is associated.</p>"""
    global_write_forwarding_status: NotRequired[
        "aws_sdk_rds.types.write_forwarding_status.WriteForwardingStatus"
    ]
    """<p>The status of write forwarding for a secondary cluster in the global cluster.</p>"""
    synchronization_status: NotRequired[
        "aws_sdk_rds.types.global_cluster_member_synchronization_status.GlobalClusterMemberSynchronizationStatus"
    ]
    """<p>The status of synchronization of each Aurora DB cluster in the global cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalClusterMember, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_arn" in value:
        pairs.append((f"{prefix}.DBClusterArn", str(value["db_cluster_arn"])))
    if "readers" in value:
        import aws_sdk_rds.types.readers_arn_list

        aws_sdk_rds.types.readers_arn_list.serialize_query(
            value["readers"], pairs, f"{prefix}.Readers"
        )
    if "is_writer" in value:
        pairs.append((f"{prefix}.IsWriter", "true" if value["is_writer"] else "false"))
    if "global_write_forwarding_status" in value:
        import aws_sdk_rds.types.write_forwarding_status

        aws_sdk_rds.types.write_forwarding_status.serialize_query(
            value["global_write_forwarding_status"],
            pairs,
            f"{prefix}.GlobalWriteForwardingStatus",
        )
    if "synchronization_status" in value:
        import aws_sdk_rds.types.global_cluster_member_synchronization_status

        aws_sdk_rds.types.global_cluster_member_synchronization_status.serialize_query(
            value["synchronization_status"], pairs, f"{prefix}.SynchronizationStatus"
        )


def deserialize_query(el: Element) -> GlobalClusterMember:
    out: GlobalClusterMember = {}  # type: ignore[typeddict-item]
    child_db_cluster_arn = el.find("DBClusterArn")
    if child_db_cluster_arn is not None:
        out["db_cluster_arn"] = str(child_db_cluster_arn.text or "")
    child_readers = el.find("Readers")
    if child_readers is not None:
        import aws_sdk_rds.types.readers_arn_list

        out["readers"] = aws_sdk_rds.types.readers_arn_list.deserialize_query(
            child_readers
        )
    child_is_writer = el.find("IsWriter")
    if child_is_writer is not None:
        out["is_writer"] = (child_is_writer.text or "").lower() == "true"
    child_global_write_forwarding_status = el.find("GlobalWriteForwardingStatus")
    if child_global_write_forwarding_status is not None:
        import aws_sdk_rds.types.write_forwarding_status

        out["global_write_forwarding_status"] = (
            aws_sdk_rds.types.write_forwarding_status.deserialize_query(
                child_global_write_forwarding_status
            )
        )
    child_synchronization_status = el.find("SynchronizationStatus")
    if child_synchronization_status is not None:
        import aws_sdk_rds.types.global_cluster_member_synchronization_status

        out["synchronization_status"] = (
            aws_sdk_rds.types.global_cluster_member_synchronization_status.deserialize_query(
                child_synchronization_status
            )
        )
    return out
