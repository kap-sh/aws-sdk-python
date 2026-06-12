"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_member

DBClusterMemberList: TypeAlias = list[
    "aws_sdk_rds.types.db_cluster_member.DBClusterMember"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterMemberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_cluster_member

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_cluster_member.serialize_query(
            item, pairs, f"{prefix}.DBClusterMember.{n}"
        )


def deserialize_query(el: Element) -> DBClusterMemberList:
    import aws_sdk_rds.types.db_cluster_member

    out: DBClusterMemberList = []
    for child in el.findall("DBClusterMember"):
        out.append(aws_sdk_rds.types.db_cluster_member.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBClusterMemberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_cluster_member

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_cluster_member.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterMemberList:
    import aws_sdk_rds.types.db_cluster_member

    out: DBClusterMemberList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.db_cluster_member.deserialize_query(child))
    return out
