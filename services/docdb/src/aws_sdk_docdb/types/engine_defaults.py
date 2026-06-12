"""Generated from Smithy shape ``com.amazonaws.docdb#EngineDefaults``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.parameters_list
    import aws_sdk_docdb.types.string


class EngineDefaults(TypedDict):
    db_parameter_group_family: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The name of the cluster parameter group family to return the engine parameter information for.</p>"""
    marker: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    parameters: NotRequired["aws_sdk_docdb.types.parameters_list.ParametersList"]
    """<p>The parameters of a particular cluster parameter group family.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EngineDefaults, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_parameter_group_family" in value:
        pairs.append(
            (
                f"{prefix}.DBParameterGroupFamily",
                str(value["db_parameter_group_family"]),
            )
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "parameters" in value:
        import aws_sdk_docdb.types.parameters_list

        aws_sdk_docdb.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )


def deserialize_query(el: Element) -> EngineDefaults:
    out: EngineDefaults = {}  # type: ignore[typeddict-item]
    child_db_parameter_group_family = el.find("DBParameterGroupFamily")
    if child_db_parameter_group_family is not None:
        out["db_parameter_group_family"] = str(
            child_db_parameter_group_family.text or ""
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import aws_sdk_docdb.types.parameters_list

        out["parameters"] = aws_sdk_docdb.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
