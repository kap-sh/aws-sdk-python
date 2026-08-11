"""Generated from Smithy shape ``com.amazonaws.rds#DBSecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_security_group

DBSecurityGroups: TypeAlias = list["capo_rds.types.db_security_group.DBSecurityGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSecurityGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_security_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_security_group.serialize_query(
            item, pairs, f"{prefix}.DBSecurityGroup.{n}"
        )


def deserialize_query(el: Element) -> DBSecurityGroups:
    import capo_rds.types.db_security_group

    out: DBSecurityGroups = []
    for child in el.findall("DBSecurityGroup"):
        out.append(capo_rds.types.db_security_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBSecurityGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_security_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_security_group.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBSecurityGroups:
    import capo_rds.types.db_security_group

    out: DBSecurityGroups = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_security_group.deserialize_query(child))
    return out
