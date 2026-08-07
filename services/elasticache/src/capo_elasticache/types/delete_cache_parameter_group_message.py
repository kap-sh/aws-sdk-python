"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteCacheParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class DeleteCacheParameterGroupMessage(TypedDict, closed=True):
    cache_parameter_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache parameter group to delete.</p> <note> <p>The specified cache security group must not be associated with any clusters.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteCacheParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}CacheParameterGroupName",
                str(value["cache_parameter_group_name"]),
            )
        )


def deserialize_query(el: Element) -> DeleteCacheParameterGroupMessage:
    out: DeleteCacheParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_cache_parameter_group_name = el.find("CacheParameterGroupName")
    if child_cache_parameter_group_name is not None:
        out["cache_parameter_group_name"] = str(
            child_cache_parameter_group_name.text or ""
        )
    return out
