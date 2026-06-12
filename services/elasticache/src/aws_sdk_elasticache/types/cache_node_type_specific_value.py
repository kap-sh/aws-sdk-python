"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheNodeTypeSpecificValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class CacheNodeTypeSpecificValue(TypedDict):
    cache_node_type: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The cache node type for which this value applies.</p>"""
    value: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The value for the cache node type.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheNodeTypeSpecificValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_node_type" in value:
        pairs.append((f"{prefix}.CacheNodeType", str(value["cache_node_type"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> CacheNodeTypeSpecificValue:
    out: CacheNodeTypeSpecificValue = {}  # type: ignore[typeddict-item]
    child_cache_node_type = el.find("CacheNodeType")
    if child_cache_node_type is not None:
        out["cache_node_type"] = str(child_cache_node_type.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
