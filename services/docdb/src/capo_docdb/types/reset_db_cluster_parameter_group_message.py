"""Generated from Smithy shape ``com.amazonaws.docdb#ResetDBClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.boolean
    import capo_docdb.types.parameters_list
    import capo_docdb.types.string


class ResetDBClusterParameterGroupMessage(TypedDict, closed=True):
    db_cluster_parameter_group_name: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the cluster parameter group to reset.</p>"""
    reset_all_parameters: NotRequired["capo_docdb.types.boolean.Boolean"]
    """<p>A value that is set to <code>true</code> to reset all parameters in the cluster parameter group to their default values, and <code>false</code> otherwise. You can't use this parameter if there is a list of parameter names specified for the <code>Parameters</code> parameter.</p>"""
    parameters: NotRequired["capo_docdb.types.parameters_list.ParametersList"]
    """<p>A list of parameter names in the cluster parameter group to reset to the default values. You can't use this parameter if the <code>ResetAllParameters</code> parameter is set to <code>true</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResetDBClusterParameterGroupMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterParameterGroupName",
                str(value["db_cluster_parameter_group_name"]),
            )
        )
    if "reset_all_parameters" in value:
        pairs.append(
            (
                f"{key_prefix}ResetAllParameters",
                "true" if value["reset_all_parameters"] else "false",
            )
        )
    if "parameters" in value:
        import capo_docdb.types.parameters_list

        capo_docdb.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
        )


def deserialize_query(el: Element) -> ResetDBClusterParameterGroupMessage:
    out: ResetDBClusterParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group_name = el.find("DBClusterParameterGroupName")
    if child_db_cluster_parameter_group_name is not None:
        out["db_cluster_parameter_group_name"] = str(
            child_db_cluster_parameter_group_name.text or ""
        )
    child_reset_all_parameters = el.find("ResetAllParameters")
    if child_reset_all_parameters is not None:
        out["reset_all_parameters"] = (
            child_reset_all_parameters.text or ""
        ).lower() == "true"
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_docdb.types.parameters_list

        out["parameters"] = capo_docdb.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
