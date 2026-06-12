"""Generated from Smithy shape ``com.amazonaws.docdb#GlobalClusterMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.global_cluster_member

GlobalClusterMemberList: TypeAlias = list[
    "aws_sdk_docdb.types.global_cluster_member.GlobalClusterMember"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalClusterMemberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.global_cluster_member

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.global_cluster_member.serialize_query(
            item, pairs, f"{prefix}.GlobalClusterMember.{n}"
        )


def deserialize_query(el: Element) -> GlobalClusterMemberList:
    import aws_sdk_docdb.types.global_cluster_member

    out: GlobalClusterMemberList = []
    for child in el.findall("GlobalClusterMember"):
        out.append(aws_sdk_docdb.types.global_cluster_member.deserialize_query(child))
    return out


def serialize_query_flat(
    value: GlobalClusterMemberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.global_cluster_member

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.global_cluster_member.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> GlobalClusterMemberList:
    import aws_sdk_docdb.types.global_cluster_member

    out: GlobalClusterMemberList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_docdb.types.global_cluster_member.deserialize_query(child))
    return out
