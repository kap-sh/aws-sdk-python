"""Generated from Smithy shape ``com.amazonaws.elasticache#FailoverGlobalReplicationGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.global_replication_group


class FailoverGlobalReplicationGroupResult(TypedDict, closed=True):
    global_replication_group: NotRequired[
        "capo_elasticache.types.global_replication_group.GlobalReplicationGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: FailoverGlobalReplicationGroupResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "global_replication_group" in value:
        import capo_elasticache.types.global_replication_group

        capo_elasticache.types.global_replication_group.serialize_query(
            value["global_replication_group"], pairs, f"{prefix}.GlobalReplicationGroup"
        )


def deserialize_query(el: Element) -> FailoverGlobalReplicationGroupResult:
    out: FailoverGlobalReplicationGroupResult = {}  # type: ignore[typeddict-item]
    child_global_replication_group = el.find("GlobalReplicationGroup")
    if child_global_replication_group is not None:
        import capo_elasticache.types.global_replication_group

        out["global_replication_group"] = (
            capo_elasticache.types.global_replication_group.deserialize_query(
                child_global_replication_group
            )
        )
    return out
