"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheParameterGroupNameMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class CacheParameterGroupNameMessage(TypedDict, closed=True):
    cache_parameter_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache parameter group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheParameterGroupNameMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_parameter_group_name" in value:
        pairs.append(
            (
                f"{prefix}.CacheParameterGroupName",
                str(value["cache_parameter_group_name"]),
            )
        )


def deserialize_query(el: Element) -> CacheParameterGroupNameMessage:
    out: CacheParameterGroupNameMessage = {}  # type: ignore[typeddict-item]
    child_cache_parameter_group_name = el.find("CacheParameterGroupName")
    if child_cache_parameter_group_name is not None:
        out["cache_parameter_group_name"] = str(
            child_cache_parameter_group_name.text or ""
        )
    return out
