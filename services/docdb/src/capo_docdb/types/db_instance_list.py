"""Generated from Smithy shape ``com.amazonaws.docdb#DBInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.db_instance

DBInstanceList: TypeAlias = list["capo_docdb.types.db_instance.DBInstance"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_docdb.types.db_instance

    for n, item in enumerate(value, 1):
        capo_docdb.types.db_instance.serialize_query(
            item, pairs, f"{prefix}.DBInstance.{n}"
        )


def deserialize_query(el: Element) -> DBInstanceList:
    import capo_docdb.types.db_instance

    out: DBInstanceList = []
    for child in el.findall("DBInstance"):
        out.append(capo_docdb.types.db_instance.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBInstanceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_docdb.types.db_instance

    for n, item in enumerate(value, 1):
        capo_docdb.types.db_instance.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBInstanceList:
    import capo_docdb.types.db_instance

    out: DBInstanceList = []
    for child in parent.findall(tag):
        out.append(capo_docdb.types.db_instance.deserialize_query(child))
    return out
