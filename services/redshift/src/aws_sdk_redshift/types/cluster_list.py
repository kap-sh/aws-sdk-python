"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.cluster

ClusterList: TypeAlias = list["aws_sdk_redshift.types.cluster.Cluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.cluster

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.cluster.serialize_query(
            item, pairs, f"{prefix}.Cluster.{n}"
        )


def deserialize_query(el: Element) -> ClusterList:
    import aws_sdk_redshift.types.cluster

    out: ClusterList = []
    for child in el.findall("Cluster"):
        out.append(aws_sdk_redshift.types.cluster.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.cluster

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.cluster.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ClusterList:
    import aws_sdk_redshift.types.cluster

    out: ClusterList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.cluster.deserialize_query(child))
    return out
