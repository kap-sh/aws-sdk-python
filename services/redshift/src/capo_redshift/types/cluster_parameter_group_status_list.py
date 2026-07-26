"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterParameterGroupStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_parameter_group_status

ClusterParameterGroupStatusList: TypeAlias = list[
    "capo_redshift.types.cluster_parameter_group_status.ClusterParameterGroupStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterParameterGroupStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_parameter_group_status

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_parameter_group_status.serialize_query(
            item, pairs, f"{prefix}.ClusterParameterGroup.{n}"
        )


def deserialize_query(el: Element) -> ClusterParameterGroupStatusList:
    import capo_redshift.types.cluster_parameter_group_status

    out: ClusterParameterGroupStatusList = []
    for child in el.findall("ClusterParameterGroup"):
        out.append(
            capo_redshift.types.cluster_parameter_group_status.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ClusterParameterGroupStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_parameter_group_status

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_parameter_group_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ClusterParameterGroupStatusList:
    import capo_redshift.types.cluster_parameter_group_status

    out: ClusterParameterGroupStatusList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.cluster_parameter_group_status.deserialize_query(child)
        )
    return out
