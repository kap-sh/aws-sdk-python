"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBClusterParameterGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_parameter_group


class CreateDBClusterParameterGroupResult(TypedDict):
    db_cluster_parameter_group: NotRequired[
        "aws_sdk_rds.types.db_cluster_parameter_group.DBClusterParameterGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBClusterParameterGroupResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_cluster_parameter_group" in value:
        import aws_sdk_rds.types.db_cluster_parameter_group

        aws_sdk_rds.types.db_cluster_parameter_group.serialize_query(
            value["db_cluster_parameter_group"],
            pairs,
            f"{prefix}.DBClusterParameterGroup",
        )


def deserialize_query(el: Element) -> CreateDBClusterParameterGroupResult:
    out: CreateDBClusterParameterGroupResult = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group = el.find("DBClusterParameterGroup")
    if child_db_cluster_parameter_group is not None:
        import aws_sdk_rds.types.db_cluster_parameter_group

        out["db_cluster_parameter_group"] = (
            aws_sdk_rds.types.db_cluster_parameter_group.deserialize_query(
                child_db_cluster_parameter_group
            )
        )
    return out
