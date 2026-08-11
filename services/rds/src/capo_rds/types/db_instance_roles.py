"""Generated from Smithy shape ``com.amazonaws.rds#DBInstanceRoles``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_instance_role

DBInstanceRoles: TypeAlias = list["capo_rds.types.db_instance_role.DBInstanceRole"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceRoles, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_instance_role

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_instance_role.serialize_query(
            item, pairs, f"{prefix}.DBInstanceRole.{n}"
        )


def deserialize_query(el: Element) -> DBInstanceRoles:
    import capo_rds.types.db_instance_role

    out: DBInstanceRoles = []
    for child in el.findall("DBInstanceRole"):
        out.append(capo_rds.types.db_instance_role.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBInstanceRoles, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_instance_role

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_instance_role.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBInstanceRoles:
    import capo_rds.types.db_instance_role

    out: DBInstanceRoles = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_instance_role.deserialize_query(child))
    return out
