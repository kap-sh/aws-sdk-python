"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBRecommendationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.filter_list
    import capo_rds.types.integer_optional
    import capo_rds.types.string
    import capo_rds.types.t_stamp


class DescribeDBRecommendationsMessage(TypedDict, closed=True):
    last_updated_after: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>A filter to include only the recommendations that were updated after this specified time.</p>"""
    last_updated_before: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>A filter to include only the recommendations that were updated before this specified time.</p>"""
    locale: NotRequired["capo_rds.types.string.String"]
    """<p>The language that you choose to return the list of recommendations.</p> <p>Valid values:</p> <ul> <li> <p> <code>en</code> </p> </li> <li> <p> <code>en_UK</code> </p> </li> <li> <p> <code>de</code> </p> </li> <li> <p> <code>es</code> </p> </li> <li> <p> <code>fr</code> </p> </li> <li> <p> <code>id</code> </p> </li> <li> <p> <code>it</code> </p> </li> <li> <p> <code>ja</code> </p> </li> <li> <p> <code>ko</code> </p> </li> <li> <p> <code>pt_BR</code> </p> </li> <li> <p> <code>zh_TW</code> </p> </li> <li> <p> <code>zh_CN</code> </p> </li> </ul>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more recommendations to describe.</p> <p>Supported Filters:</p> <ul> <li> <p> <code>recommendation-id</code> - Accepts a list of recommendation identifiers. The results list only includes the recommendations whose identifier is one of the specified filter values.</p> </li> <li> <p> <code>status</code> - Accepts a list of recommendation statuses.</p> <p>Valid values:</p> <ul> <li> <p> <code>active</code> - The recommendations which are ready for you to apply.</p> </li> <li> <p> <code>pending</code> - The applied or scheduled recommendations which are in progress.</p> </li> <li> <p> <code>resolved</code> - The recommendations which are completed.</p> </li> <li> <p> <code>dismissed</code> - The recommendations that you dismissed.</p> </li> </ul> <p>The results list only includes the recommendations whose status is one of the specified filter values.</p> </li> <li> <p> <code>severity</code> - Accepts a list of recommendation severities. The results list only includes the recommendations whose severity is one of the specified filter values.</p> <p>Valid values:</p> <ul> <li> <p> <code>high</code> </p> </li> <li> <p> <code>medium</code> </p> </li> <li> <p> <code>low</code> </p> </li> <li> <p> <code>informational</code> </p> </li> </ul> </li> <li> <p> <code>type-id</code> - Accepts a list of recommendation type identifiers. The results list only includes the recommendations whose type is one of the specified filter values.</p> </li> <li> <p> <code>dbi-resource-id</code> - Accepts a list of database resource identifiers. The results list only includes the recommendations that generated for the specified databases.</p> </li> <li> <p> <code>cluster-resource-id</code> - Accepts a list of cluster resource identifiers. The results list only includes the recommendations that generated for the specified clusters.</p> </li> <li> <p> <code>pg-arn</code> - Accepts a list of parameter group ARNs. The results list only includes the recommendations that generated for the specified parameter groups.</p> </li> <li> <p> <code>cluster-pg-arn</code> - Accepts a list of cluster parameter group ARNs. The results list only includes the recommendations that generated for the specified cluster parameter groups.</p> </li> </ul>"""
    max_records: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of recommendations to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBRecommendations</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBRecommendationsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "last_updated_after" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["last_updated_after"], pairs, f"{prefix}.LastUpdatedAfter"
        )
    if "last_updated_before" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["last_updated_before"], pairs, f"{prefix}.LastUpdatedBefore"
        )
    if "locale" in value:
        pairs.append((f"{prefix}.Locale", str(value["locale"])))
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBRecommendationsMessage:
    out: DescribeDBRecommendationsMessage = {}  # type: ignore[typeddict-item]
    child_last_updated_after = el.find("LastUpdatedAfter")
    if child_last_updated_after is not None:
        import capo_rds.types.t_stamp

        out["last_updated_after"] = capo_rds.types.t_stamp.deserialize_query(
            child_last_updated_after
        )
    child_last_updated_before = el.find("LastUpdatedBefore")
    if child_last_updated_before is not None:
        import capo_rds.types.t_stamp

        out["last_updated_before"] = capo_rds.types.t_stamp.deserialize_query(
            child_last_updated_before
        )
    child_locale = el.find("Locale")
    if child_locale is not None:
        out["locale"] = str(child_locale.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_rds.types.filter_list

        out["filters"] = capo_rds.types.filter_list.deserialize_query(child_filters)
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
