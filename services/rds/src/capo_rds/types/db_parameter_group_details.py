"""Generated from Smithy shape ``com.amazonaws.rds#DBParameterGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.parameters_list
    import capo_rds.types.string


class DBParameterGroupDetails(TypedDict, closed=True):
    parameters: NotRequired["capo_rds.types.parameters_list.ParametersList"]
    """<p>A list of <code>Parameter</code> values.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBParameterGroupDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "parameters" in value:
        import capo_rds.types.parameters_list

        capo_rds.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DBParameterGroupDetails:
    out: DBParameterGroupDetails = {}  # type: ignore[typeddict-item]
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_rds.types.parameters_list

        out["parameters"] = capo_rds.types.parameters_list.deserialize_query(
            child_parameters
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
