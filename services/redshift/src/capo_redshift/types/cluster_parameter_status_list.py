"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterParameterStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_parameter_status

ClusterParameterStatusList: TypeAlias = list[
    "capo_redshift.types.cluster_parameter_status.ClusterParameterStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterParameterStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_parameter_status

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_parameter_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ClusterParameterStatusList:
    import capo_redshift.types.cluster_parameter_status

    out: ClusterParameterStatusList = []
    for child in el.findall("member"):
        out.append(
            capo_redshift.types.cluster_parameter_status.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ClusterParameterStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_parameter_status

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_parameter_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ClusterParameterStatusList:
    import capo_redshift.types.cluster_parameter_status

    out: ClusterParameterStatusList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.cluster_parameter_status.deserialize_query(child)
        )
    return out
