"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBClusterParameterGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_parameter_group


class CreateDBClusterParameterGroupResult(TypedDict, closed=True):
    db_cluster_parameter_group: NotRequired[
        "capo_rds.types.db_cluster_parameter_group.DBClusterParameterGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBClusterParameterGroupResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_cluster_parameter_group" in value:
        import capo_rds.types.db_cluster_parameter_group

        capo_rds.types.db_cluster_parameter_group.serialize_query(
            value["db_cluster_parameter_group"],
            pairs,
            f"{prefix}.DBClusterParameterGroup",
        )


def deserialize_query(el: Element) -> CreateDBClusterParameterGroupResult:
    out: CreateDBClusterParameterGroupResult = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group = el.find("DBClusterParameterGroup")
    if child_db_cluster_parameter_group is not None:
        import capo_rds.types.db_cluster_parameter_group

        out["db_cluster_parameter_group"] = (
            capo_rds.types.db_cluster_parameter_group.deserialize_query(
                child_db_cluster_parameter_group
            )
        )
    return out
