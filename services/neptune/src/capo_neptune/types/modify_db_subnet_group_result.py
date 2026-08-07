"""Generated from Smithy shape ``com.amazonaws.neptune#ModifyDBSubnetGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.db_subnet_group


class ModifyDBSubnetGroupResult(TypedDict, closed=True):
    db_subnet_group: NotRequired["capo_neptune.types.db_subnet_group.DBSubnetGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBSubnetGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_subnet_group" in value:
        import capo_neptune.types.db_subnet_group

        capo_neptune.types.db_subnet_group.serialize_query(
            value["db_subnet_group"], pairs, f"{key_prefix}DBSubnetGroup"
        )


def deserialize_query(el: Element) -> ModifyDBSubnetGroupResult:
    out: ModifyDBSubnetGroupResult = {}  # type: ignore[typeddict-item]
    child_db_subnet_group = el.find("DBSubnetGroup")
    if child_db_subnet_group is not None:
        import capo_neptune.types.db_subnet_group

        out["db_subnet_group"] = capo_neptune.types.db_subnet_group.deserialize_query(
            child_db_subnet_group
        )
    return out
