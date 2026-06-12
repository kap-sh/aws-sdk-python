"""Generated from Smithy shape ``com.amazonaws.elasticache#ReplicationGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.replication_group_list
    import aws_sdk_elasticache.types.string


class ReplicationGroupMessage(TypedDict):
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    replication_groups: NotRequired[
        "aws_sdk_elasticache.types.replication_group_list.ReplicationGroupList"
    ]
    """<p>A list of replication groups. Each item in the list contains detailed information about one replication group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReplicationGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "replication_groups" in value:
        import aws_sdk_elasticache.types.replication_group_list

        aws_sdk_elasticache.types.replication_group_list.serialize_query(
            value["replication_groups"], pairs, f"{prefix}.ReplicationGroups"
        )


def deserialize_query(el: Element) -> ReplicationGroupMessage:
    out: ReplicationGroupMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_replication_groups = el.find("ReplicationGroups")
    if child_replication_groups is not None:
        import aws_sdk_elasticache.types.replication_group_list

        out["replication_groups"] = (
            aws_sdk_elasticache.types.replication_group_list.deserialize_query(
                child_replication_groups
            )
        )
    return out
