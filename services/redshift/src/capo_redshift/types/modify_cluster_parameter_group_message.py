"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.parameters_list
    import capo_redshift.types.string


class ModifyClusterParameterGroupMessage(TypedDict, closed=True):
    parameter_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the parameter group to be modified.</p>"""
    parameters: NotRequired["capo_redshift.types.parameters_list.ParametersList"]
    """<p>An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.</p> <p>For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional.</p> <p>For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "parameter_group_name" in value:
        pairs.append(
            (f"{key_prefix}ParameterGroupName", str(value["parameter_group_name"]))
        )
    if "parameters" in value:
        import capo_redshift.types.parameters_list

        capo_redshift.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
        )


def deserialize_query(el: Element) -> ModifyClusterParameterGroupMessage:
    out: ModifyClusterParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_parameter_group_name = el.find("ParameterGroupName")
    if child_parameter_group_name is not None:
        out["parameter_group_name"] = str(child_parameter_group_name.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_redshift.types.parameters_list

        out["parameters"] = capo_redshift.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
