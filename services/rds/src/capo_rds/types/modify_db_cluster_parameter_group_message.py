"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.parameters_list
    import capo_rds.types.string


class ModifyDBClusterParameterGroupMessage(TypedDict, closed=True):
    db_cluster_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB cluster parameter group to modify.</p>"""
    parameters: NotRequired["capo_rds.types.parameters_list.ParametersList"]
    """<p>A list of parameters in the DB cluster parameter group to modify.</p> <p>Valid Values (for the application method): <code>immediate | pending-reboot</code> </p> <note> <p>You can use the <code>immediate</code> value with dynamic parameters only. You can use the <code>pending-reboot</code> value for both dynamic and static parameters.</p> <p>When the application method is <code>immediate</code>, changes to dynamic parameters are applied immediately to the DB clusters associated with the parameter group. When the application method is <code>pending-reboot</code>, changes to dynamic and static parameters are applied after a reboot without failover to the DB clusters associated with the parameter group.</p> </note>"""


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
        import capo_rds.types.parameters_list

        capo_rds.types.parameters_list.serialize_query(
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
        import capo_rds.types.parameters_list

        out["parameters"] = capo_rds.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
