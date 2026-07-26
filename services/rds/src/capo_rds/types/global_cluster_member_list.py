"""Generated from Smithy shape ``com.amazonaws.rds#GlobalClusterMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.global_cluster_member

GlobalClusterMemberList: TypeAlias = list[
    "capo_rds.types.global_cluster_member.GlobalClusterMember"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalClusterMemberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.global_cluster_member

    for n, item in enumerate(value, 1):
        capo_rds.types.global_cluster_member.serialize_query(
            item, pairs, f"{prefix}.GlobalClusterMember.{n}"
        )


def deserialize_query(el: Element) -> GlobalClusterMemberList:
    import capo_rds.types.global_cluster_member

    out: GlobalClusterMemberList = []
    for child in el.findall("GlobalClusterMember"):
        out.append(capo_rds.types.global_cluster_member.deserialize_query(child))
    return out


def serialize_query_flat(
    value: GlobalClusterMemberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.global_cluster_member

    for n, item in enumerate(value, 1):
        capo_rds.types.global_cluster_member.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> GlobalClusterMemberList:
    import capo_rds.types.global_cluster_member

    out: GlobalClusterMemberList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.global_cluster_member.deserialize_query(child))
    return out
