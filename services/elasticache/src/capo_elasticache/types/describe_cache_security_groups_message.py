"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeCacheSecurityGroupsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.string


class DescribeCacheSecurityGroupsMessage(TypedDict, closed=True):
    cache_security_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache security group to return details for.</p>"""
    max_records: NotRequired["capo_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>"""
    marker: NotRequired["capo_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeCacheSecurityGroupsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_security_group_name" in value:
        pairs.append(
            (
                f"{prefix}.CacheSecurityGroupName",
                str(value["cache_security_group_name"]),
            )
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeCacheSecurityGroupsMessage:
    out: DescribeCacheSecurityGroupsMessage = {}  # type: ignore[typeddict-item]
    child_cache_security_group_name = el.find("CacheSecurityGroupName")
    if child_cache_security_group_name is not None:
        out["cache_security_group_name"] = str(
            child_cache_security_group_name.text or ""
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
