"""Generated from Smithy shape ``com.amazonaws.rds#DBSubnetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_subnet_group

DBSubnetGroups: TypeAlias = list["capo_rds.types.db_subnet_group.DBSubnetGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSubnetGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_subnet_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_subnet_group.serialize_query(
            item, pairs, f"{prefix}.DBSubnetGroup.{n}"
        )


def deserialize_query(el: Element) -> DBSubnetGroups:
    import capo_rds.types.db_subnet_group

    out: DBSubnetGroups = []
    for child in el.findall("DBSubnetGroup"):
        out.append(capo_rds.types.db_subnet_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBSubnetGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_subnet_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_subnet_group.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBSubnetGroups:
    import capo_rds.types.db_subnet_group

    out: DBSubnetGroups = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_subnet_group.deserialize_query(child))
    return out
