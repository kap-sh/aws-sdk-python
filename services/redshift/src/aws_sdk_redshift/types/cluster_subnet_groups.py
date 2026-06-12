"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterSubnetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.cluster_subnet_group

ClusterSubnetGroups: TypeAlias = list[
    "aws_sdk_redshift.types.cluster_subnet_group.ClusterSubnetGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterSubnetGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.cluster_subnet_group

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.cluster_subnet_group.serialize_query(
            item, pairs, f"{prefix}.ClusterSubnetGroup.{n}"
        )


def deserialize_query(el: Element) -> ClusterSubnetGroups:
    import aws_sdk_redshift.types.cluster_subnet_group

    out: ClusterSubnetGroups = []
    for child in el.findall("ClusterSubnetGroup"):
        out.append(aws_sdk_redshift.types.cluster_subnet_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ClusterSubnetGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.cluster_subnet_group

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.cluster_subnet_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ClusterSubnetGroups:
    import aws_sdk_redshift.types.cluster_subnet_group

    out: ClusterSubnetGroups = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.cluster_subnet_group.deserialize_query(child))
    return out
