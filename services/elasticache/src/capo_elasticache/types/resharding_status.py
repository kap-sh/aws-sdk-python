"""Generated from Smithy shape ``com.amazonaws.elasticache#ReshardingStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.slot_migration


class ReshardingStatus(TypedDict, closed=True):
    slot_migration: NotRequired["capo_elasticache.types.slot_migration.SlotMigration"]
    """<p>Represents the progress of an online resharding operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReshardingStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "slot_migration" in value:
        import capo_elasticache.types.slot_migration

        capo_elasticache.types.slot_migration.serialize_query(
            value["slot_migration"], pairs, f"{prefix}.SlotMigration"
        )


def deserialize_query(el: Element) -> ReshardingStatus:
    out: ReshardingStatus = {}  # type: ignore[typeddict-item]
    child_slot_migration = el.find("SlotMigration")
    if child_slot_migration is not None:
        import capo_elasticache.types.slot_migration

        out["slot_migration"] = capo_elasticache.types.slot_migration.deserialize_query(
            child_slot_migration
        )
    return out
