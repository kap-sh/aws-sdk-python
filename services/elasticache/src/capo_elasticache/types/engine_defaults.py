"""Generated from Smithy shape ``com.amazonaws.elasticache#EngineDefaults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_node_type_specific_parameters_list
    import capo_elasticache.types.parameters_list
    import capo_elasticache.types.string


class EngineDefaults(TypedDict, closed=True):
    cache_parameter_group_family: NotRequired["capo_elasticache.types.string.String"]
    """<p>Specifies the name of the cache parameter group family to which the engine default parameters apply.</p> <p>Valid values are: <code>memcached1.4</code> | <code>memcached1.5</code> | <code>memcached1.6</code> | <code>redis2.6</code> | <code>redis2.8</code> | <code>redis3.2</code> | <code>redis4.0</code> | <code>redis5.0</code> | <code>redis6.0</code> | <code>redis6.x</code> | <code>redis7</code> </p>"""
    marker: NotRequired["capo_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    parameters: NotRequired["capo_elasticache.types.parameters_list.ParametersList"]
    """<p>Contains a list of engine default parameters.</p>"""
    cache_node_type_specific_parameters: NotRequired[
        "capo_elasticache.types.cache_node_type_specific_parameters_list.CacheNodeTypeSpecificParametersList"
    ]
    """<p>A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EngineDefaults, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_parameter_group_family" in value:
        pairs.append(
            (
                f"{prefix}.CacheParameterGroupFamily",
                str(value["cache_parameter_group_family"]),
            )
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "parameters" in value:
        import capo_elasticache.types.parameters_list

        capo_elasticache.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )
    if "cache_node_type_specific_parameters" in value:
        import capo_elasticache.types.cache_node_type_specific_parameters_list

        capo_elasticache.types.cache_node_type_specific_parameters_list.serialize_query(
            value["cache_node_type_specific_parameters"],
            pairs,
            f"{prefix}.CacheNodeTypeSpecificParameters",
        )


def deserialize_query(el: Element) -> EngineDefaults:
    out: EngineDefaults = {}  # type: ignore[typeddict-item]
    child_cache_parameter_group_family = el.find("CacheParameterGroupFamily")
    if child_cache_parameter_group_family is not None:
        out["cache_parameter_group_family"] = str(
            child_cache_parameter_group_family.text or ""
        )
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
