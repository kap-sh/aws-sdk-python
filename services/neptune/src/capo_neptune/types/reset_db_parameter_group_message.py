"""Generated from Smithy shape ``com.amazonaws.neptune#ResetDBParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.boolean
    import capo_neptune.types.parameters_list
    import capo_neptune.types.string


class ResetDBParameterGroupMessage(TypedDict, closed=True):
    db_parameter_group_name: NotRequired["capo_neptune.types.string.String"]
    """<p>The name of the DB parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must match the name of an existing DBParameterGroup.</p> </li> </ul>"""
    reset_all_parameters: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Specifies whether (<code>true</code>) or not (<code>false</code>) to reset all parameters in the DB parameter group to default values.</p> <p>Default: <code>true</code> </p>"""
    parameters: NotRequired["capo_neptune.types.parameters_list.ParametersList"]
    """<p>To reset the entire DB parameter group, specify the <code>DBParameterGroup</code> name and <code>ResetAllParameters</code> parameters. To reset specific parameters, provide a list of the following: <code>ParameterName</code> and <code>ApplyMethod</code>. A maximum of 20 parameters can be modified in a single request.</p> <p>Valid Values (for Apply method): <code>pending-reboot</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResetDBParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_parameter_group_name" in value:
        pairs.append(
            (f"{prefix}.DBParameterGroupName", str(value["db_parameter_group_name"]))
        )
    if "reset_all_parameters" in value:
        pairs.append(
            (
                f"{prefix}.ResetAllParameters",
                "true" if value["reset_all_parameters"] else "false",
            )
        )
    if "parameters" in value:
        import capo_neptune.types.parameters_list

        capo_neptune.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )


def deserialize_query(el: Element) -> ResetDBParameterGroupMessage:
    out: ResetDBParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
    child_reset_all_parameters = el.find("ResetAllParameters")
    if child_reset_all_parameters is not None:
        out["reset_all_parameters"] = (
            child_reset_all_parameters.text or ""
        ).lower() == "true"
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_neptune.types.parameters_list

        out["parameters"] = capo_neptune.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
