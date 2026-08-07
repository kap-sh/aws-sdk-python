"""Generated from Smithy shape ``com.amazonaws.docdb#DBClusterParameterGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.parameters_list
    import capo_docdb.types.string


class DBClusterParameterGroupDetails(TypedDict, closed=True):
    parameters: NotRequired["capo_docdb.types.parameters_list.ParametersList"]
    """<p>Provides a list of parameters for the cluster parameter group.</p>"""
    marker: NotRequired["capo_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterParameterGroupDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "parameters" in value:
        import capo_docdb.types.parameters_list

        capo_docdb.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DBClusterParameterGroupDetails:
    out: DBClusterParameterGroupDetails = {}  # type: ignore[typeddict-item]
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_docdb.types.parameters_list

        out["parameters"] = capo_docdb.types.parameters_list.deserialize_query(
            child_parameters
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
