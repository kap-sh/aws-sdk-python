"""Generated from Smithy shape ``com.amazonaws.redshift#DefaultClusterParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.parameters_list
    import aws_sdk_redshift.types.string


class DefaultClusterParameters(TypedDict):
    parameter_group_family: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the cluster parameter group family to which the engine default parameters apply.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    parameters: NotRequired["aws_sdk_redshift.types.parameters_list.ParametersList"]
    """<p>The list of cluster default parameters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DefaultClusterParameters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "parameter_group_family" in value:
        pairs.append(
            (f"{prefix}.ParameterGroupFamily", str(value["parameter_group_family"]))
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "parameters" in value:
        import aws_sdk_redshift.types.parameters_list

        aws_sdk_redshift.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )


def deserialize_query(el: Element) -> DefaultClusterParameters:
    out: DefaultClusterParameters = {}  # type: ignore[typeddict-item]
    child_parameter_group_family = el.find("ParameterGroupFamily")
    if child_parameter_group_family is not None:
        out["parameter_group_family"] = str(child_parameter_group_family.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import aws_sdk_redshift.types.parameters_list

        out["parameters"] = aws_sdk_redshift.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
