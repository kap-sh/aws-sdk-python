"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheSecurityGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_security_groups
    import capo_elasticache.types.string


class CacheSecurityGroupMessage(TypedDict, closed=True):
    marker: NotRequired["capo_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    cache_security_groups: NotRequired[
        "capo_elasticache.types.cache_security_groups.CacheSecurityGroups"
    ]
    """<p>A list of cache security groups. Each element in the list contains detailed information about one group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheSecurityGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "cache_security_groups" in value:
        import capo_elasticache.types.cache_security_groups

        capo_elasticache.types.cache_security_groups.serialize_query(
            value["cache_security_groups"], pairs, f"{key_prefix}CacheSecurityGroups"
        )


def deserialize_query(el: Element) -> CacheSecurityGroupMessage:
    out: CacheSecurityGroupMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_cache_security_groups = el.find("CacheSecurityGroups")
    if child_cache_security_groups is not None:
        import capo_elasticache.types.cache_security_groups

        out["cache_security_groups"] = (
            capo_elasticache.types.cache_security_groups.deserialize_query(
                child_cache_security_groups
            )
        )
    return out
