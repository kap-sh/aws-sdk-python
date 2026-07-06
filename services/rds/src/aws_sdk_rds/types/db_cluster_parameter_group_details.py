"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterParameterGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.parameters_list
    import aws_sdk_rds.types.string


class DBClusterParameterGroupDetails(TypedDict, closed=True):
    parameters: NotRequired["aws_sdk_rds.types.parameters_list.ParametersList"]
    """<p>Provides a list of parameters for the DB cluster parameter group.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBClusterParameters</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterParameterGroupDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "parameters" in value:
        import aws_sdk_rds.types.parameters_list

        aws_sdk_rds.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DBClusterParameterGroupDetails:
    out: DBClusterParameterGroupDetails = {}  # type: ignore[typeddict-item]
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import aws_sdk_rds.types.parameters_list

        out["parameters"] = aws_sdk_rds.types.parameters_list.deserialize_query(
            child_parameters
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
