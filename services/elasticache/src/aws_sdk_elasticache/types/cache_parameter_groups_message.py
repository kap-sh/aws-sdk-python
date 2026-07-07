"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheParameterGroupsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_parameter_group_list
    import aws_sdk_elasticache.types.string


class CacheParameterGroupsMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    cache_parameter_groups: NotRequired[
        "aws_sdk_elasticache.types.cache_parameter_group_list.CacheParameterGroupList"
    ]
    """<p>A list of cache parameter groups. Each element in the list contains detailed information about one cache parameter group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheParameterGroupsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "cache_parameter_groups" in value:
        import aws_sdk_elasticache.types.cache_parameter_group_list

        aws_sdk_elasticache.types.cache_parameter_group_list.serialize_query(
            value["cache_parameter_groups"], pairs, f"{prefix}.CacheParameterGroups"
        )


def deserialize_query(el: Element) -> CacheParameterGroupsMessage:
    out: CacheParameterGroupsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_cache_parameter_groups = el.find("CacheParameterGroups")
    if child_cache_parameter_groups is not None:
        import aws_sdk_elasticache.types.cache_parameter_group_list

        out["cache_parameter_groups"] = (
            aws_sdk_elasticache.types.cache_parameter_group_list.deserialize_query(
                child_cache_parameter_groups
            )
        )
    return out
