"""Generated from Smithy shape ``com.amazonaws.docdb#DBClusterParameterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.string


class DBClusterParameterGroup(TypedDict, closed=True):
    db_cluster_parameter_group_name: NotRequired["capo_docdb.types.string.String"]
    """<p>Provides the name of the cluster parameter group.</p>"""
    db_parameter_group_family: NotRequired["capo_docdb.types.string.String"]
    """<p>Provides the name of the parameter group family that this cluster parameter group is compatible with.</p>"""
    description: NotRequired["capo_docdb.types.string.String"]
    """<p>Provides the customer-specified description for this cluster parameter group.</p>"""
    db_cluster_parameter_group_arn: NotRequired["capo_docdb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the cluster parameter group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterParameterGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterParameterGroupName",
                str(value["db_cluster_parameter_group_name"]),
            )
        )
    if "db_parameter_group_family" in value:
        pairs.append(
            (
                f"{key_prefix}DBParameterGroupFamily",
                str(value["db_parameter_group_family"]),
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "db_cluster_parameter_group_arn" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterParameterGroupArn",
                str(value["db_cluster_parameter_group_arn"]),
            )
        )


def deserialize_query(el: Element) -> DBClusterParameterGroup:
    out: DBClusterParameterGroup = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group_name = el.find("DBClusterParameterGroupName")
    if child_db_cluster_parameter_group_name is not None:
        out["db_cluster_parameter_group_name"] = str(
            child_db_cluster_parameter_group_name.text or ""
        )
    child_db_parameter_group_family = el.find("DBParameterGroupFamily")
    if child_db_parameter_group_family is not None:
        out["db_parameter_group_family"] = str(
            child_db_parameter_group_family.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_db_cluster_parameter_group_arn = el.find("DBClusterParameterGroupArn")
    if child_db_cluster_parameter_group_arn is not None:
        out["db_cluster_parameter_group_arn"] = str(
            child_db_cluster_parameter_group_arn.text or ""
        )
    return out
