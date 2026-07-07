"""Generated from Smithy shape ``com.amazonaws.neptune#DeleteDBClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string


class DeleteDBClusterParameterGroupMessage(TypedDict, closed=True):
    db_cluster_parameter_group_name: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name of the DB cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must be the name of an existing DB cluster parameter group.</p> </li> <li> <p>You can't delete a default DB cluster parameter group.</p> </li> <li> <p>Cannot be associated with any DB clusters.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBClusterParameterGroupMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterParameterGroupName",
                str(value["db_cluster_parameter_group_name"]),
            )
        )


def deserialize_query(el: Element) -> DeleteDBClusterParameterGroupMessage:
    out: DeleteDBClusterParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group_name = el.find("DBClusterParameterGroupName")
    if child_db_cluster_parameter_group_name is not None:
        out["db_cluster_parameter_group_name"] = str(
            child_db_cluster_parameter_group_name.text or ""
        )
    return out
