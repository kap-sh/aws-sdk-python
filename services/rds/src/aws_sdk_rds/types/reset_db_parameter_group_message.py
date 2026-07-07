"""Generated from Smithy shape ``com.amazonaws.rds#ResetDBParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.parameters_list
    import aws_sdk_rds.types.string


class ResetDBParameterGroupMessage(TypedDict, closed=True):
    db_parameter_group_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the DB parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must match the name of an existing <code>DBParameterGroup</code>.</p> </li> </ul>"""
    reset_all_parameters: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Specifies whether to reset all parameters in the DB parameter group to default values. By default, all parameters in the DB parameter group are reset to default values.</p>"""
    parameters: NotRequired["aws_sdk_rds.types.parameters_list.ParametersList"]
    """<p>To reset the entire DB parameter group, specify the <code>DBParameterGroup</code> name and <code>ResetAllParameters</code> parameters. To reset specific parameters, provide a list of the following: <code>ParameterName</code> and <code>ApplyMethod</code>. A maximum of 20 parameters can be modified in a single request.</p> <p> <b>MySQL</b> </p> <p>Valid Values (for Apply method): <code>immediate</code> | <code>pending-reboot</code> </p> <p>You can use the immediate value with dynamic parameters only. You can use the <code>pending-reboot</code> value for both dynamic and static parameters, and changes are applied when DB instance reboots.</p> <p> <b>MariaDB</b> </p> <p>Valid Values (for Apply method): <code>immediate</code> | <code>pending-reboot</code> </p> <p>You can use the immediate value with dynamic parameters only. You can use the <code>pending-reboot</code> value for both dynamic and static parameters, and changes are applied when DB instance reboots.</p> <p> <b>Oracle</b> </p> <p>Valid Values (for Apply method): <code>pending-reboot</code> </p>"""


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
        import aws_sdk_rds.types.parameters_list

        aws_sdk_rds.types.parameters_list.serialize_query(
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
        import aws_sdk_rds.types.parameters_list

        out["parameters"] = aws_sdk_rds.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
