"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateCacheParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string
    import capo_elasticache.types.tag_list


class CreateCacheParameterGroupMessage(TypedDict, closed=True):
    cache_parameter_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>A user-specified name for the cache parameter group. This value is stored as a lowercase string.</p>"""
    cache_parameter_group_family: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache parameter group family that the cache parameter group can be used with.</p> <p>Valid values are: <code>valkey8</code> | <code>valkey7</code> | <code>memcached1.4</code> | <code>memcached1.5</code> | <code>memcached1.6</code> | <code>redis2.6</code> | <code>redis2.8</code> | <code>redis3.2</code> | <code>redis4.0</code> | <code>redis5.0</code> | <code>redis6.x</code> | <code>redis7</code> </p>"""
    description: NotRequired["capo_elasticache.types.string.String"]
    """<p>A user-specified description for the cache parameter group.</p>"""
    tags: NotRequired["capo_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateCacheParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}CacheParameterGroupName",
                str(value["cache_parameter_group_name"]),
            )
        )
    if "cache_parameter_group_family" in value:
        pairs.append(
            (
                f"{key_prefix}CacheParameterGroupFamily",
                str(value["cache_parameter_group_family"]),
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tags" in value:
        import capo_elasticache.types.tag_list

        capo_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateCacheParameterGroupMessage:
    out: CreateCacheParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_cache_parameter_group_name = el.find("CacheParameterGroupName")
    if child_cache_parameter_group_name is not None:
        out["cache_parameter_group_name"] = str(
            child_cache_parameter_group_name.text or ""
        )
    child_cache_parameter_group_family = el.find("CacheParameterGroupFamily")
    if child_cache_parameter_group_family is not None:
        out["cache_parameter_group_family"] = str(
            child_cache_parameter_group_family.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elasticache.types.tag_list

        out["tags"] = capo_elasticache.types.tag_list.deserialize_query(child_tags)
    return out
