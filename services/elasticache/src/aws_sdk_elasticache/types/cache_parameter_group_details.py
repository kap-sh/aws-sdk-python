"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheParameterGroupDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_node_type_specific_parameters_list
    import aws_sdk_elasticache.types.parameters_list
    import aws_sdk_elasticache.types.string


class CacheParameterGroupDetails(TypedDict):
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    parameters: NotRequired["aws_sdk_elasticache.types.parameters_list.ParametersList"]
    """<p>A list of <a>Parameter</a> instances.</p>"""
    cache_node_type_specific_parameters: NotRequired[
        "aws_sdk_elasticache.types.cache_node_type_specific_parameters_list.CacheNodeTypeSpecificParametersList"
    ]
    """<p>A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheParameterGroupDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "parameters" in value:
        import aws_sdk_elasticache.types.parameters_list

        aws_sdk_elasticache.types.parameters_list.serialize_query(
            value["parameters"], pairs, f"{prefix}.Parameters"
        )
    if "cache_node_type_specific_parameters" in value:
        import aws_sdk_elasticache.types.cache_node_type_specific_parameters_list

        aws_sdk_elasticache.types.cache_node_type_specific_parameters_list.serialize_query(
            value["cache_node_type_specific_parameters"],
            pairs,
            f"{prefix}.CacheNodeTypeSpecificParameters",
        )


def deserialize_query(el: Element) -> CacheParameterGroupDetails:
    out: CacheParameterGroupDetails = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import aws_sdk_elasticache.types.parameters_list

        out["parameters"] = aws_sdk_elasticache.types.parameters_list.deserialize_query(
            child_parameters
        )
    child_cache_node_type_specific_parameters = el.find(
        "CacheNodeTypeSpecificParameters"
    )
    if child_cache_node_type_specific_parameters is not None:
        import aws_sdk_elasticache.types.cache_node_type_specific_parameters_list

        out["cache_node_type_specific_parameters"] = (
            aws_sdk_elasticache.types.cache_node_type_specific_parameters_list.deserialize_query(
                child_cache_node_type_specific_parameters
            )
        )
    return out
