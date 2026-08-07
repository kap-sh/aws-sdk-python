"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheParameterGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_node_type_specific_parameters_list
    import capo_elasticache.types.parameters_list
    import capo_elasticache.types.string


class CacheParameterGroupDetails(TypedDict, closed=True):
    marker: NotRequired["capo_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    parameters: NotRequired["capo_elasticache.types.parameters_list.ParametersList"]
    """<p>A list of <a>Parameter</a> instances.</p>"""
    cache_node_type_specific_parameters: NotRequired[
        "capo_elasticache.types.cache_node_type_specific_parameters_list.CacheNodeTypeSpecificParametersList"
    ]
    """<p>A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheParameterGroupDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "parameters" in value:
        import capo_elasticache.types.parameters_list

        capo_elasticache.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
        )
    if "cache_node_type_specific_parameters" in value:
        import capo_elasticache.types.cache_node_type_specific_parameters_list

        capo_elasticache.types.cache_node_type_specific_parameters_list.serialize_query(
            value["cache_node_type_specific_parameters"],
            pairs,
            f"{key_prefix}CacheNodeTypeSpecificParameters",
        )


def deserialize_query(el: Element) -> CacheParameterGroupDetails:
    out: CacheParameterGroupDetails = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_elasticache.types.parameters_list

        out["parameters"] = capo_elasticache.types.parameters_list.deserialize_query(
            child_parameters
        )
    child_cache_node_type_specific_parameters = el.find(
        "CacheNodeTypeSpecificParameters"
    )
    if child_cache_node_type_specific_parameters is not None:
        import capo_elasticache.types.cache_node_type_specific_parameters_list

        out["cache_node_type_specific_parameters"] = (
            capo_elasticache.types.cache_node_type_specific_parameters_list.deserialize_query(
                child_cache_node_type_specific_parameters
            )
        )
    return out
