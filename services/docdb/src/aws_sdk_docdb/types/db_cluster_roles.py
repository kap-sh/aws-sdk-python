"""Generated from Smithy shape ``com.amazonaws.docdb#DBClusterRoles``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.db_cluster_role

DBClusterRoles: TypeAlias = list["aws_sdk_docdb.types.db_cluster_role.DBClusterRole"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterRoles, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.db_cluster_role

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.db_cluster_role.serialize_query(
            item, pairs, f"{prefix}.DBClusterRole.{n}"
        )


def deserialize_query(el: Element) -> DBClusterRoles:
    import aws_sdk_docdb.types.db_cluster_role

    out: DBClusterRoles = []
    for child in el.findall("DBClusterRole"):
        out.append(aws_sdk_docdb.types.db_cluster_role.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBClusterRoles, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.db_cluster_role

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.db_cluster_role.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterRoles:
    import aws_sdk_docdb.types.db_cluster_role

    out: DBClusterRoles = []
    for child in parent.findall(tag):
        out.append(aws_sdk_docdb.types.db_cluster_role.deserialize_query(child))
    return out
