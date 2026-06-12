"""Generated from Smithy shape ``com.amazonaws.neptune#CopyDBClusterParameterGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.db_cluster_parameter_group


class CopyDBClusterParameterGroupResult(TypedDict):
    db_cluster_parameter_group: NotRequired[
        "aws_sdk_neptune.types.db_cluster_parameter_group.DBClusterParameterGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CopyDBClusterParameterGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_parameter_group" in value:
        import aws_sdk_neptune.types.db_cluster_parameter_group

        aws_sdk_neptune.types.db_cluster_parameter_group.serialize_query(
            value["db_cluster_parameter_group"],
            pairs,
            f"{prefix}.DBClusterParameterGroup",
        )


def deserialize_query(el: Element) -> CopyDBClusterParameterGroupResult:
    out: CopyDBClusterParameterGroupResult = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group = el.find("DBClusterParameterGroup")
    if child_db_cluster_parameter_group is not None:
        import aws_sdk_neptune.types.db_cluster_parameter_group

        out["db_cluster_parameter_group"] = (
            aws_sdk_neptune.types.db_cluster_parameter_group.deserialize_query(
                child_db_cluster_parameter_group
            )
        )
    return out
