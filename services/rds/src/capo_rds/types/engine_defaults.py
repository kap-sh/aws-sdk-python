"""Generated from Smithy shape ``com.amazonaws.rds#EngineDefaults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.parameters_list
    import capo_rds.types.string


class EngineDefaults(TypedDict, closed=True):
    db_parameter_group_family: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the name of the DB parameter group family that the engine default parameters apply to.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous EngineDefaults request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code> .</p>"""
    parameters: NotRequired["capo_rds.types.parameters_list.ParametersList"]
    """<p>Contains a list of engine default parameters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EngineDefaults, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_parameter_group_family" in value:
        pairs.append(
            (
                f"{key_prefix}DBParameterGroupFamily",
                str(value["db_parameter_group_family"]),
            )
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "parameters" in value:
        import capo_rds.types.parameters_list

        capo_rds.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
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
        import capo_rds.types.parameters_list

        out["parameters"] = capo_rds.types.parameters_list.deserialize_query(
            child_parameters
        )
    return out
