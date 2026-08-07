"""Generated from Smithy shape ``com.amazonaws.elasticache#CompleteMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.replication_group


class CompleteMigrationResponse(TypedDict, closed=True):
    replication_group: NotRequired[
        "capo_elasticache.types.replication_group.ReplicationGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CompleteMigrationResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "replication_group" in value:
        import capo_elasticache.types.replication_group

        capo_elasticache.types.replication_group.serialize_query(
            value["replication_group"], pairs, f"{key_prefix}ReplicationGroup"
        )


def deserialize_query(el: Element) -> CompleteMigrationResponse:
    out: CompleteMigrationResponse = {}  # type: ignore[typeddict-item]
    child_replication_group = el.find("ReplicationGroup")
    if child_replication_group is not None:
        import capo_elasticache.types.replication_group

        out["replication_group"] = (
            capo_elasticache.types.replication_group.deserialize_query(
                child_replication_group
            )
        )
    return out
