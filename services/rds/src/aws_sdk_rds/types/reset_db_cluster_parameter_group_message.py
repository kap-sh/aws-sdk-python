"""Generated from Smithy shape ``com.amazonaws.rds#ResetDBClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.parameters_list
    import aws_sdk_rds.types.string


class ResetDBClusterParameterGroupMessage(TypedDict):
    db_cluster_parameter_group_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the DB cluster parameter group to reset.</p>"""
    reset_all_parameters: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Specifies whether to reset all parameters in the DB cluster parameter group to their default values. You can't use this parameter if there is a list of parameter names specified for the <code>Parameters</code> parameter.</p>"""
    parameters: NotRequired["aws_sdk_rds.types.parameters_list.ParametersList"]
    """<p>A list of parameter names in the DB cluster parameter group to reset to the default values. You can't use this parameter if the <code>ResetAllParameters</code> parameter is enabled.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResetDBClusterParameterGroupMessage,
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
        import aws_sdk_rds.types.parameters_list

        out["parameters"] = aws_sdk_rds.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
