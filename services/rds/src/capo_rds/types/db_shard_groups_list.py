"""Generated from Smithy shape ``com.amazonaws.rds#DBShardGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_shard_group

DBShardGroupsList: TypeAlias = list["capo_rds.types.db_shard_group.DBShardGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBShardGroupsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_shard_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_shard_group.serialize_query(
            item, pairs, f"{prefix}.DBShardGroup.{n}"
        )


def deserialize_query(el: Element) -> DBShardGroupsList:
    import capo_rds.types.db_shard_group

    out: DBShardGroupsList = []
    for child in el.findall("DBShardGroup"):
        out.append(capo_rds.types.db_shard_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBShardGroupsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_shard_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_shard_group.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBShardGroupsList:
    import capo_rds.types.db_shard_group

    out: DBShardGroupsList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_shard_group.deserialize_query(child))
    return out
