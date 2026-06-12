"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheSubnetGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_subnet_groups
    import aws_sdk_elasticache.types.string


class CacheSubnetGroupMessage(TypedDict):
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    cache_subnet_groups: NotRequired[
        "aws_sdk_elasticache.types.cache_subnet_groups.CacheSubnetGroups"
    ]
    """<p>A list of cache subnet groups. Each element in the list contains detailed information about one group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "cache_subnet_groups" in value:
        import aws_sdk_elasticache.types.cache_subnet_groups

        aws_sdk_elasticache.types.cache_subnet_groups.serialize_query(
            value["cache_subnet_groups"], pairs, f"{prefix}.CacheSubnetGroups"
        )


def deserialize_query(el: Element) -> CacheSubnetGroupMessage:
    out: CacheSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_cache_subnet_groups = el.find("CacheSubnetGroups")
    if child_cache_subnet_groups is not None:
        import aws_sdk_elasticache.types.cache_subnet_groups

        out["cache_subnet_groups"] = (
            aws_sdk_elasticache.types.cache_subnet_groups.deserialize_query(
                child_cache_subnet_groups
            )
        )
    return out
