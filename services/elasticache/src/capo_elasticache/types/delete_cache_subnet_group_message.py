"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteCacheSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class DeleteCacheSubnetGroupMessage(TypedDict, closed=True):
    cache_subnet_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache subnet group to delete.</p> <p>Constraints: Must contain no more than 255 alphanumeric characters or hyphens.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteCacheSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}CacheSubnetGroupName", str(value["cache_subnet_group_name"]))
        )


def deserialize_query(el: Element) -> DeleteCacheSubnetGroupMessage:
    out: DeleteCacheSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_cache_subnet_group_name = el.find("CacheSubnetGroupName")
    if child_cache_subnet_group_name is not None:
        out["cache_subnet_group_name"] = str(child_cache_subnet_group_name.text or "")
    return out
