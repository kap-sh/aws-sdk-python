"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteCacheParameterGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class DeleteCacheParameterGroupMessage(TypedDict):
    cache_parameter_group_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the cache parameter group to delete.</p> <note> <p>The specified cache security group must not be associated with any clusters.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteCacheParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_parameter_group_name" in value:
        pairs.append(
            (
                f"{prefix}.CacheParameterGroupName",
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
