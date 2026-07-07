"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheParameterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.boolean
    import aws_sdk_elasticache.types.string


class CacheParameterGroup(TypedDict, closed=True):
    cache_parameter_group_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the cache parameter group.</p>"""
    cache_parameter_group_family: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the cache parameter group family that this cache parameter group is compatible with.</p> <p>Valid values are: <code>memcached1.4</code> | <code>memcached1.5</code> | <code>memcached1.6</code> | <code>redis2.6</code> | <code>redis2.8</code> | <code>redis3.2</code> | <code>redis4.0</code> | <code>redis5.0</code> | <code>redis6.x</code> | <code>redis7</code> </p>"""
    description: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The description for this cache parameter group.</p>"""
    is_global: NotRequired["aws_sdk_elasticache.types.boolean.Boolean"]
    """<p>Indicates whether the parameter group is associated with a Global datastore</p>"""
    arn: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The ARN (Amazon Resource Name) of the cache parameter group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheParameterGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_parameter_group_name" in value:
        pairs.append(
            (
                f"{prefix}.CacheParameterGroupName",
                str(value["cache_parameter_group_name"]),
            )
        )
    if "cache_parameter_group_family" in value:
        pairs.append(
            (
                f"{prefix}.CacheParameterGroupFamily",
                str(value["cache_parameter_group_family"]),
            )
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "is_global" in value:
        pairs.append((f"{prefix}.IsGlobal", "true" if value["is_global"] else "false"))
    if "arn" in value:
        pairs.append((f"{prefix}.ARN", str(value["arn"])))


def deserialize_query(el: Element) -> CacheParameterGroup:
    out: CacheParameterGroup = {}  # type: ignore[typeddict-item]
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
    child_is_global = el.find("IsGlobal")
    if child_is_global is not None:
        out["is_global"] = (child_is_global.text or "").lower() == "true"
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
