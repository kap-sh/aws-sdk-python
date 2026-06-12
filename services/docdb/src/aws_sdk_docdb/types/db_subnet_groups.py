"""Generated from Smithy shape ``com.amazonaws.docdb#DBSubnetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.db_subnet_group

DBSubnetGroups: TypeAlias = list["aws_sdk_docdb.types.db_subnet_group.DBSubnetGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSubnetGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.db_subnet_group

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.db_subnet_group.serialize_query(
            item, pairs, f"{prefix}.DBSubnetGroup.{n}"
        )


def deserialize_query(el: Element) -> DBSubnetGroups:
    import aws_sdk_docdb.types.db_subnet_group

    out: DBSubnetGroups = []
    for child in el.findall("DBSubnetGroup"):
        out.append(aws_sdk_docdb.types.db_subnet_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBSubnetGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.db_subnet_group

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.db_subnet_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBSubnetGroups:
    import aws_sdk_docdb.types.db_subnet_group

    out: DBSubnetGroups = []
    for child in parent.findall(tag):
        out.append(aws_sdk_docdb.types.db_subnet_group.deserialize_query(child))
    return out
