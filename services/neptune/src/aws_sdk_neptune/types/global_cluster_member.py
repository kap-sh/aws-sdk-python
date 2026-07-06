"""Generated from Smithy shape ``com.amazonaws.neptune#GlobalClusterMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.boolean
    import aws_sdk_neptune.types.readers_arn_list
    import aws_sdk_neptune.types.string


class GlobalClusterMember(TypedDict, closed=True):
    db_cluster_arn: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p> The Amazon Resource Name (ARN) for each Neptune cluster. </p>"""
    readers: NotRequired["aws_sdk_neptune.types.readers_arn_list.ReadersArnList"]
    """<p> The Amazon Resource Name (ARN) for each read-only secondary cluster associated with the Neptune global database. </p>"""
    is_writer: NotRequired["aws_sdk_neptune.types.boolean.Boolean"]
    """<p> Specifies whether the Neptune cluster is the primary cluster (that is, has read-write capability) for the Neptune global database with which it is associated. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalClusterMember, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_arn" in value:
        pairs.append((f"{prefix}.DBClusterArn", str(value["db_cluster_arn"])))
    if "readers" in value:
        import aws_sdk_neptune.types.readers_arn_list

        aws_sdk_neptune.types.readers_arn_list.serialize_query(
            value["readers"], pairs, f"{prefix}.Readers"
        )
    if "is_writer" in value:
        pairs.append((f"{prefix}.IsWriter", "true" if value["is_writer"] else "false"))


def deserialize_query(el: Element) -> GlobalClusterMember:
    out: GlobalClusterMember = {}  # type: ignore[typeddict-item]
    child_db_cluster_arn = el.find("DBClusterArn")
    if child_db_cluster_arn is not None:
        out["db_cluster_arn"] = str(child_db_cluster_arn.text or "")
    child_readers = el.find("Readers")
    if child_readers is not None:
        import aws_sdk_neptune.types.readers_arn_list

        out["readers"] = aws_sdk_neptune.types.readers_arn_list.deserialize_query(
            child_readers
        )
    child_is_writer = el.find("IsWriter")
    if child_is_writer is not None:
        out["is_writer"] = (child_is_writer.text or "").lower() == "true"
    return out
