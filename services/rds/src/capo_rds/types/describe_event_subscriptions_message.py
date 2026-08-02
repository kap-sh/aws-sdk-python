"""Generated from Smithy shape ``com.amazonaws.rds#DescribeEventSubscriptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.filter_list
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class DescribeEventSubscriptionsMessage(TypedDict, closed=True):
    subscription_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the RDS event notification subscription you want to describe.</p>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>This parameter isn't currently supported.</p>"""
    max_records: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code> .</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEventSubscriptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subscription_name" in value:
        pairs.append((f"{key_prefix}SubscriptionName", str(value["subscription_name"])))
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeEventSubscriptionsMessage:
    out: DescribeEventSubscriptionsMessage = {}  # type: ignore[typeddict-item]
    child_subscription_name = el.find("SubscriptionName")
    if child_subscription_name is not None:
        out["subscription_name"] = str(child_subscription_name.text or "")
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
