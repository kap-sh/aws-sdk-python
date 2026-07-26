"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_version

ClusterVersionList: TypeAlias = list[
    "capo_redshift.types.cluster_version.ClusterVersion"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterVersionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_version

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_version.serialize_query(
            item, pairs, f"{prefix}.ClusterVersion.{n}"
        )


def deserialize_query(el: Element) -> ClusterVersionList:
    import capo_redshift.types.cluster_version

    out: ClusterVersionList = []
    for child in el.findall("ClusterVersion"):
        out.append(capo_redshift.types.cluster_version.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ClusterVersionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_version

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_version.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ClusterVersionList:
    import capo_redshift.types.cluster_version

    out: ClusterVersionList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.cluster_version.deserialize_query(child))
    return out
