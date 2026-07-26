"""Generated from Smithy shape ``com.amazonaws.docdb#CreateDBSubnetGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.db_subnet_group


class CreateDBSubnetGroupResult(TypedDict, closed=True):
    db_subnet_group: NotRequired["capo_docdb.types.db_subnet_group.DBSubnetGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBSubnetGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_subnet_group" in value:
        import capo_docdb.types.db_subnet_group

        capo_docdb.types.db_subnet_group.serialize_query(
            value["db_subnet_group"], pairs, f"{prefix}.DBSubnetGroup"
        )


def deserialize_query(el: Element) -> CreateDBSubnetGroupResult:
    out: CreateDBSubnetGroupResult = {}  # type: ignore[typeddict-item]
    child_db_subnet_group = el.find("DBSubnetGroup")
    if child_db_subnet_group is not None:
        import capo_docdb.types.db_subnet_group

        out["db_subnet_group"] = capo_docdb.types.db_subnet_group.deserialize_query(
            child_db_subnet_group
        )
    return out
