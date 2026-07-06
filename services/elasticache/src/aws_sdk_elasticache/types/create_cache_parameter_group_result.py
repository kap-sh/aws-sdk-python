"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateCacheParameterGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_parameter_group


class CreateCacheParameterGroupResult(TypedDict, closed=True):
    cache_parameter_group: NotRequired[
        "aws_sdk_elasticache.types.cache_parameter_group.CacheParameterGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateCacheParameterGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_parameter_group" in value:
        import aws_sdk_elasticache.types.cache_parameter_group

        aws_sdk_elasticache.types.cache_parameter_group.serialize_query(
            value["cache_parameter_group"], pairs, f"{prefix}.CacheParameterGroup"
        )


def deserialize_query(el: Element) -> CreateCacheParameterGroupResult:
    out: CreateCacheParameterGroupResult = {}  # type: ignore[typeddict-item]
    child_cache_parameter_group = el.find("CacheParameterGroup")
    if child_cache_parameter_group is not None:
        import aws_sdk_elasticache.types.cache_parameter_group

        out["cache_parameter_group"] = (
            aws_sdk_elasticache.types.cache_parameter_group.deserialize_query(
                child_cache_parameter_group
            )
        )
    return out
