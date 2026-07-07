"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostReservationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.host_reservation_id_set
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class DescribeHostReservationsRequest(TypedDict, closed=True):
    filter: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>instance-family</code> - The instance family (for example, <code>m4</code>).</p> </li> <li> <p> <code>payment-option</code> - The payment option (<code>NoUpfront</code> | <code>PartialUpfront</code> | <code>AllUpfront</code>).</p> </li> <li> <p> <code>state</code> - The state of the reservation (<code>payment-pending</code> | <code>payment-failed</code> | <code>active</code> | <code>retired</code>).</p> </li> <li> <p> <code>tag:<key></code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    host_reservation_id_set: NotRequired[
        "aws_sdk_ec2.types.host_reservation_id_set.HostReservationIdSet"
    ]
    """<p>The host reservation IDs.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned <code>nextToken</code> value. This value can be between 5 and 500. If <code>maxResults</code> is given a larger value than 500, you receive an error.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeHostReservationsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "filter" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filter"], pairs, f"{prefix}.Filter"
        )
    if "host_reservation_id_set" in value:
        import aws_sdk_ec2.types.host_reservation_id_set

        aws_sdk_ec2.types.host_reservation_id_set.serialize_ec2_query(
            value["host_reservation_id_set"], pairs, f"{prefix}.HostReservationIdSet"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeHostReservationsRequest:
    out: DescribeHostReservationsRequest = {}  # type: ignore[typeddict-item]
    if el.find("Filter") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filter"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filter"
        )
    if el.find("HostReservationIdSet") is not None:
        import aws_sdk_ec2.types.host_reservation_id_set

        out["host_reservation_id_set"] = (
            aws_sdk_ec2.types.host_reservation_id_set.deserialize_ec2_query(
                el, "HostReservationIdSet"
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
