"""Generated from Smithy shape ``com.amazonaws.redshift#ParameterGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_parameter_group

ParameterGroupList: TypeAlias = list[
    "capo_redshift.types.cluster_parameter_group.ClusterParameterGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ParameterGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_parameter_group

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_parameter_group.serialize_query(
            item, pairs, f"{prefix}.ClusterParameterGroup.{n}"
        )


def deserialize_query(el: Element) -> ParameterGroupList:
    import capo_redshift.types.cluster_parameter_group

    out: ParameterGroupList = []
    for child in el.findall("ClusterParameterGroup"):
        out.append(capo_redshift.types.cluster_parameter_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ParameterGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_parameter_group

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_parameter_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ParameterGroupList:
    import capo_redshift.types.cluster_parameter_group

    out: ParameterGroupList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.cluster_parameter_group.deserialize_query(child))
    return out
