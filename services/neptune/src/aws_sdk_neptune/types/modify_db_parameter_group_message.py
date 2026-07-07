"""Generated from Smithy shape ``com.amazonaws.neptune#ModifyDBParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.parameters_list
    import aws_sdk_neptune.types.string


class ModifyDBParameterGroupMessage(TypedDict, closed=True):
    db_parameter_group_name: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name of the DB parameter group.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBParameterGroup.</p> </li> </ul>"""
    parameters: NotRequired["aws_sdk_neptune.types.parameters_list.ParametersList"]
    """<p>An array of parameter names, values, and the apply method for the parameter update. At least one parameter name, value, and apply method must be supplied; subsequent arguments are optional. A maximum of 20 parameters can be modified in a single request.</p> <p>Valid Values (for the application method): <code>immediate | pending-reboot</code> </p> <note> <p>You can use the immediate value with dynamic parameters only. You can use the pending-reboot value for both dynamic and static parameters, and changes are applied when you reboot the DB instance without failover.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_parameter_group_name" in value:
        pairs.append(
            (f"{prefix}.DBParameterGroupName", str(value["db_parameter_group_name"]))
        )
    if "parameters" in value:
        import aws_sdk_neptune.types.parameters_list

        aws_sdk_neptune.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )


def deserialize_query(el: Element) -> ModifyDBParameterGroupMessage:
    out: ModifyDBParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import aws_sdk_neptune.types.parameters_list

        out["parameters"] = aws_sdk_neptune.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
