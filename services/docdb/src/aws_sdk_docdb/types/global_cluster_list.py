"""Generated from Smithy shape ``com.amazonaws.docdb#GlobalClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.global_cluster

GlobalClusterList: TypeAlias = list["aws_sdk_docdb.types.global_cluster.GlobalCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.global_cluster

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.global_cluster.serialize_query(
            item, pairs, f"{prefix}.GlobalClusterMember.{n}"
        )


def deserialize_query(el: Element) -> GlobalClusterList:
    import aws_sdk_docdb.types.global_cluster

    out: GlobalClusterList = []
    for child in el.findall("GlobalClusterMember"):
        out.append(aws_sdk_docdb.types.global_cluster.deserialize_query(child))
    return out


def serialize_query_flat(
    value: GlobalClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.global_cluster

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.global_cluster.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> GlobalClusterList:
    import aws_sdk_docdb.types.global_cluster

    out: GlobalClusterList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_docdb.types.global_cluster.deserialize_query(child))
    return out
