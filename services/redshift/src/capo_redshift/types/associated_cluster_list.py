"""Generated from Smithy shape ``com.amazonaws.redshift#AssociatedClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_associated_to_schedule

AssociatedClusterList: TypeAlias = list[
    "capo_redshift.types.cluster_associated_to_schedule.ClusterAssociatedToSchedule"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AssociatedClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_associated_to_schedule

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_associated_to_schedule.serialize_query(
            item, pairs, f"{prefix}.ClusterAssociatedToSchedule.{n}"
        )


def deserialize_query(el: Element) -> AssociatedClusterList:
    import capo_redshift.types.cluster_associated_to_schedule

    out: AssociatedClusterList = []
    for child in el.findall("ClusterAssociatedToSchedule"):
        out.append(
            capo_redshift.types.cluster_associated_to_schedule.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AssociatedClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_associated_to_schedule

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_associated_to_schedule.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AssociatedClusterList:
    import capo_redshift.types.cluster_associated_to_schedule

    out: AssociatedClusterList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.cluster_associated_to_schedule.deserialize_query(child)
        )
    return out
