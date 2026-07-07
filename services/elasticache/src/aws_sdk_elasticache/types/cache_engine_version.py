"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheEngineVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class CacheEngineVersion(TypedDict, closed=True):
    engine: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the cache engine.</p>"""
    engine_version: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The version number of the cache engine.</p>"""
    cache_parameter_group_family: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the cache parameter group family associated with this cache engine.</p> <p>Valid values are: <code>memcached1.4</code> | <code>memcached1.5</code> | <code>memcached1.6</code> | <code>redis2.6</code> | <code>redis2.8</code> | <code>redis3.2</code> | <code>redis4.0</code> | <code>redis5.0</code> | <code>redis6.x</code> | <code>redis7</code> </p>"""
    cache_engine_description: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The description of the cache engine.</p>"""
    cache_engine_version_description: NotRequired[
        "aws_sdk_elasticache.types.string.String"
    ]
    """<p>The description of the cache engine version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheEngineVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "cache_parameter_group_family" in value:
        pairs.append(
            (
                f"{prefix}.CacheParameterGroupFamily",
                str(value["cache_parameter_group_family"]),
            )
        )
    if "cache_engine_description" in value:
        pairs.append(
            (f"{prefix}.CacheEngineDescription", str(value["cache_engine_description"]))
        )
    if "cache_engine_version_description" in value:
        pairs.append(
            (
                f"{prefix}.CacheEngineVersionDescription",
                str(value["cache_engine_version_description"]),
            )
        )


def deserialize_query(el: Element) -> CacheEngineVersion:
    out: CacheEngineVersion = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_cache_parameter_group_family = el.find("CacheParameterGroupFamily")
    if child_cache_parameter_group_family is not None:
        out["cache_parameter_group_family"] = str(
            child_cache_parameter_group_family.text or ""
        )
    child_cache_engine_description = el.find("CacheEngineDescription")
    if child_cache_engine_description is not None:
        out["cache_engine_description"] = str(child_cache_engine_description.text or "")
    child_cache_engine_version_description = el.find("CacheEngineVersionDescription")
    if child_cache_engine_version_description is not None:
        out["cache_engine_version_description"] = str(
            child_cache_engine_version_description.text or ""
        )
    return out
