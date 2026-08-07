"""Generated from Smithy shape ``com.amazonaws.docdb#DBClusterParameterGroupNameMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.string


class DBClusterParameterGroupNameMessage(TypedDict, closed=True):
    db_cluster_parameter_group_name: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of a cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must be from 1 to 255 letters or numbers.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <note> <p>This value is stored as a lowercase string.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterParameterGroupNameMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterParameterGroupName",
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
