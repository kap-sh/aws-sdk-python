"""Generated from Smithy shape ``com.amazonaws.redshift#ResetClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean
    import aws_sdk_redshift.types.parameters_list
    import aws_sdk_redshift.types.string


class ResetClusterParameterGroupMessage(TypedDict):
    parameter_group_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the cluster parameter group to be reset.</p>"""
    reset_all_parameters: NotRequired["aws_sdk_redshift.types.boolean.Boolean"]
    """<p>If <code>true</code>, all parameters in the specified parameter group will be reset to their default values. </p> <p>Default: <code>true</code> </p>"""
    parameters: NotRequired["aws_sdk_redshift.types.parameters_list.ParametersList"]
    """<p>An array of names of parameters to be reset. If <i>ResetAllParameters</i> option is not used, then at least one parameter name must be supplied. </p> <p>Constraints: A maximum of 20 parameters can be reset in a single request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResetClusterParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "parameter_group_name" in value:
        pairs.append(
            (f"{prefix}.ParameterGroupName", str(value["parameter_group_name"]))
        )
    if "reset_all_parameters" in value:
        pairs.append(
            (
                f"{prefix}.ResetAllParameters",
                "true" if value["reset_all_parameters"] else "false",
            )
        )
    if "parameters" in value:
        import aws_sdk_redshift.types.parameters_list

        aws_sdk_redshift.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )


def deserialize_query(el: Element) -> ResetClusterParameterGroupMessage:
    out: ResetClusterParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_parameter_group_name = el.find("ParameterGroupName")
    if child_parameter_group_name is not None:
        out["parameter_group_name"] = str(child_parameter_group_name.text or "")
    child_reset_all_parameters = el.find("ResetAllParameters")
    if child_reset_all_parameters is not None:
        out["reset_all_parameters"] = (
            child_reset_all_parameters.text or ""
        ).lower() == "true"
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import aws_sdk_redshift.types.parameters_list

        out["parameters"] = aws_sdk_redshift.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
