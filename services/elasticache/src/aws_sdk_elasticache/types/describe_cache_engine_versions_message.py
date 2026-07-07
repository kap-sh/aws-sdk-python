"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeCacheEngineVersionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.boolean
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.string


class DescribeCacheEngineVersionsMessage(TypedDict, closed=True):
    engine: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The cache engine to return. Valid values: <code>memcached</code> | <code>redis</code> </p>"""
    engine_version: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The cache engine version to return.</p> <p>Example: <code>1.4.14</code> </p>"""
    cache_parameter_group_family: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of a specific cache parameter group family to return details for.</p> <p>Valid values are: <code>memcached1.4</code> | <code>memcached1.5</code> | <code>memcached1.6</code> | <code>redis2.6</code> | <code>redis2.8</code> | <code>redis3.2</code> | <code>redis4.0</code> | <code>redis5.0</code> | <code>redis6.x</code> | <code>redis6.2</code> | <code>redis7</code> | <code>valkey7</code> </p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul>"""
    max_records: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>"""
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    default_only: NotRequired["aws_sdk_elasticache.types.boolean.Boolean"]
    """<p>If <code>true</code>, specifies that only the default version of the specified engine or engine and major version combination is to be returned.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeCacheEngineVersionsMessage, pairs: list[tuple[str, str]], prefix: str
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
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "default_only" in value:
        pairs.append(
            (f"{prefix}.DefaultOnly", "true" if value["default_only"] else "false")
        )


def deserialize_query(el: Element) -> DescribeCacheEngineVersionsMessage:
    out: DescribeCacheEngineVersionsMessage = {}  # type: ignore[typeddict-item]
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
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_default_only = el.find("DefaultOnly")
    if child_default_only is not None:
        out["default_only"] = (child_default_only.text or "").lower() == "true"
    return out
