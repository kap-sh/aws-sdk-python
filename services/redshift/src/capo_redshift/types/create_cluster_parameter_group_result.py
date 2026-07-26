"""Generated from Smithy shape ``com.amazonaws.redshift#CreateClusterParameterGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_parameter_group


class CreateClusterParameterGroupResult(TypedDict, closed=True):
    cluster_parameter_group: NotRequired[
        "capo_redshift.types.cluster_parameter_group.ClusterParameterGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateClusterParameterGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_parameter_group" in value:
        import capo_redshift.types.cluster_parameter_group

        capo_redshift.types.cluster_parameter_group.serialize_query(
            value["cluster_parameter_group"], pairs, f"{prefix}.ClusterParameterGroup"
        )


def deserialize_query(el: Element) -> CreateClusterParameterGroupResult:
    out: CreateClusterParameterGroupResult = {}  # type: ignore[typeddict-item]
    child_cluster_parameter_group = el.find("ClusterParameterGroup")
    if child_cluster_parameter_group is not None:
        import capo_redshift.types.cluster_parameter_group

        out["cluster_parameter_group"] = (
            capo_redshift.types.cluster_parameter_group.deserialize_query(
                child_cluster_parameter_group
            )
        )
    return out
