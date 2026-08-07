"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeEventSubscriptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string
    import capo_redshift.types.tag_key_list
    import capo_redshift.types.tag_value_list


class DescribeEventSubscriptionsMessage(TypedDict, closed=True):
    subscription_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the Amazon Redshift event notification subscription to be described.</p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeEventSubscriptions request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""
    tag_keys: NotRequired["capo_redshift.types.tag_key_list.TagKeyList"]
    """<p>A tag key or keys for which you want to return all matching event notification subscriptions that are associated with the specified key or keys. For example, suppose that you have subscriptions that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag keys associated with them.</p>"""
    tag_values: NotRequired["capo_redshift.types.tag_value_list.TagValueList"]
    """<p>A tag value or values for which you want to return all matching event notification subscriptions that are associated with the specified tag value or values. For example, suppose that you have subscriptions that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag values associated with them.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEventSubscriptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subscription_name" in value:
        pairs.append((f"{key_prefix}SubscriptionName", str(value["subscription_name"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "tag_keys" in value:
        import capo_redshift.types.tag_key_list

        capo_redshift.types.tag_key_list.serialize_query(
            value["tag_keys"], pairs, f"{key_prefix}TagKeys"
        )
    if "tag_values" in value:
        import capo_redshift.types.tag_value_list

        capo_redshift.types.tag_value_list.serialize_query(
            value["tag_values"], pairs, f"{key_prefix}TagValues"
        )


def deserialize_query(el: Element) -> DescribeEventSubscriptionsMessage:
    out: DescribeEventSubscriptionsMessage = {}  # type: ignore[typeddict-item]
    child_subscription_name = el.find("SubscriptionName")
    if child_subscription_name is not None:
        out["subscription_name"] = str(child_subscription_name.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import capo_redshift.types.tag_key_list

        out["tag_keys"] = capo_redshift.types.tag_key_list.deserialize_query(
            child_tag_keys
        )
    child_tag_values = el.find("TagValues")
    if child_tag_values is not None:
        import capo_redshift.types.tag_value_list

        out["tag_values"] = capo_redshift.types.tag_value_list.deserialize_query(
            child_tag_values
        )
    return out
