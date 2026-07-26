"""Generated from Smithy shape ``com.amazonaws.neptune#CopyDBClusterParameterGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.db_cluster_parameter_group


class CopyDBClusterParameterGroupResult(TypedDict, closed=True):
    db_cluster_parameter_group: NotRequired[
        "capo_neptune.types.db_cluster_parameter_group.DBClusterParameterGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CopyDBClusterParameterGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_parameter_group" in value:
        import capo_neptune.types.db_cluster_parameter_group

        capo_neptune.types.db_cluster_parameter_group.serialize_query(
            value["db_cluster_parameter_group"],
            pairs,
            f"{prefix}.DBClusterParameterGroup",
        )


def deserialize_query(el: Element) -> CopyDBClusterParameterGroupResult:
    out: CopyDBClusterParameterGroupResult = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group = el.find("DBClusterParameterGroup")
    if child_db_cluster_parameter_group is not None:
        import capo_neptune.types.db_cluster_parameter_group

        out["db_cluster_parameter_group"] = (
            capo_neptune.types.db_cluster_parameter_group.deserialize_query(
                child_db_cluster_parameter_group
            )
        )
    return out
