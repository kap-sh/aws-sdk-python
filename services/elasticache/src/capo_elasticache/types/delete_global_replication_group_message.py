"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteGlobalReplicationGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean
    import capo_elasticache.types.string


class DeleteGlobalReplicationGroupMessage(TypedDict, closed=True):
    global_replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the Global datastore</p>"""
    retain_primary_replication_group: NotRequired[
        "capo_elasticache.types.boolean.Boolean"
    ]
    """<p>The primary replication group is retained as a standalone replication group. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteGlobalReplicationGroupMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "global_replication_group_id" in value:
        pairs.append(
            (
                f"{prefix}.GlobalReplicationGroupId",
                str(value["global_replication_group_id"]),
            )
        )
    if "retain_primary_replication_group" in value:
        pairs.append(
            (
                f"{prefix}.RetainPrimaryReplicationGroup",
                "true" if value["retain_primary_replication_group"] else "false",
            )
        )


def deserialize_query(el: Element) -> DeleteGlobalReplicationGroupMessage:
    out: DeleteGlobalReplicationGroupMessage = {}  # type: ignore[typeddict-item]
    child_global_replication_group_id = el.find("GlobalReplicationGroupId")
    if child_global_replication_group_id is not None:
        out["global_replication_group_id"] = str(
            child_global_replication_group_id.text or ""
        )
    child_retain_primary_replication_group = el.find("RetainPrimaryReplicationGroup")
    if child_retain_primary_replication_group is not None:
        out["retain_primary_replication_group"] = (
            child_retain_primary_replication_group.text or ""
        ).lower() == "true"
    return out
