"""Generated from Smithy shape ``com.amazonaws.neptune#DBClusterParameterGroupNameMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string


class DBClusterParameterGroupNameMessage(TypedDict, closed=True):
    db_cluster_parameter_group_name: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name of the DB cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters or numbers.</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <note> <p>This value is stored as a lowercase string.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterParameterGroupNameMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterParameterGroupName",
                str(value["db_cluster_parameter_group_name"]),
            )
        )


def deserialize_query(el: Element) -> DBClusterParameterGroupNameMessage:
    out: DBClusterParameterGroupNameMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group_name = el.find("DBClusterParameterGroupName")
    if child_db_cluster_parameter_group_name is not None:
        out["db_cluster_parameter_group_name"] = str(
            child_db_cluster_parameter_group_name.text or ""
        )
    return out
