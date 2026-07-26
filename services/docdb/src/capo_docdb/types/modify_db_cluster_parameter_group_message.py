"""Generated from Smithy shape ``com.amazonaws.docdb#ModifyDBClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.parameters_list
    import capo_docdb.types.string


class ModifyDBClusterParameterGroupMessage(TypedDict, closed=True):
    db_cluster_parameter_group_name: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the cluster parameter group to modify.</p>"""
    parameters: NotRequired["capo_docdb.types.parameters_list.ParametersList"]
    """<p>A list of parameters in the cluster parameter group to modify.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBClusterParameterGroupMessage,
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
    if "parameters" in value:
        import capo_docdb.types.parameters_list

        capo_docdb.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )


def deserialize_query(el: Element) -> ModifyDBClusterParameterGroupMessage:
    out: ModifyDBClusterParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group_name = el.find("DBClusterParameterGroupName")
    if child_db_cluster_parameter_group_name is not None:
        out["db_cluster_parameter_group_name"] = str(
            child_db_cluster_parameter_group_name.text or ""
        )
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_docdb.types.parameters_list

        out["parameters"] = capo_docdb.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
