"""Generated from Smithy shape ``com.amazonaws.elasticache#RebalanceSlotsInGlobalReplicationGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.global_replication_group


class RebalanceSlotsInGlobalReplicationGroupResult(TypedDict):
    global_replication_group: NotRequired[
        "aws_sdk_elasticache.types.global_replication_group.GlobalReplicationGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: RebalanceSlotsInGlobalReplicationGroupResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "global_replication_group" in value:
        import aws_sdk_elasticache.types.global_replication_group

        aws_sdk_elasticache.types.global_replication_group.serialize_query(
            value["global_replication_group"], pairs, f"{prefix}.GlobalReplicationGroup"
        )


def deserialize_query(el: Element) -> RebalanceSlotsInGlobalReplicationGroupResult:
    out: RebalanceSlotsInGlobalReplicationGroupResult = {}  # type: ignore[typeddict-item]
    child_global_replication_group = el.find("GlobalReplicationGroup")
    if child_global_replication_group is not None:
        import aws_sdk_elasticache.types.global_replication_group

        out["global_replication_group"] = (
            aws_sdk_elasticache.types.global_replication_group.deserialize_query(
                child_global_replication_group
            )
        )
    return out
