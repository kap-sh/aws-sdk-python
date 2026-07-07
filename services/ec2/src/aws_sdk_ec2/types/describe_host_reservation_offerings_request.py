"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostReservationOfferingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_host_reservations_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.string


class DescribeHostReservationOfferingsRequest(TypedDict, closed=True):
    filter: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>instance-family</code> - The instance family of the offering (for example, <code>m4</code>).</p> </li> <li> <p> <code>payment-option</code> - The payment option (<code>NoUpfront</code> | <code>PartialUpfront</code> | <code>AllUpfront</code>).</p> </li> </ul>"""
    max_duration: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>This is the maximum duration of the reservation to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 94608000 for three years.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_host_reservations_max_results.DescribeHostReservationsMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned <code>nextToken</code> value. This value can be between 5 and 500. If <code>maxResults</code> is given a larger value than 500, you receive an error.</p>"""
    min_duration: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>This is the minimum duration of the reservation you'd like to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 31536000 for one year.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    offering_id: NotRequired["aws_sdk_ec2.types.offering_id.OfferingId"]
    """<p>The ID of the reservation offering.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeHostReservationOfferingsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "filter" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filter"], pairs, f"{prefix}.Filter"
        )
    if "max_duration" in value:
        pairs.append((f"{prefix}.MaxDuration", str(value["max_duration"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "min_duration" in value:
        pairs.append((f"{prefix}.MinDuration", str(value["min_duration"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "offering_id" in value:
        pairs.append((f"{prefix}.OfferingId", str(value["offering_id"])))


def deserialize_ec2_query(el: Element) -> DescribeHostReservationOfferingsRequest:
    out: DescribeHostReservationOfferingsRequest = {}  # type: ignore[typeddict-item]
    if el.find("Filter") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filter"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filter"
        )
    child_max_duration = el.find("MaxDuration")
    if child_max_duration is not None:
        out["max_duration"] = int(child_max_duration.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_min_duration = el.find("MinDuration")
    if child_min_duration is not None:
        out["min_duration"] = int(child_min_duration.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_offering_id = el.find("OfferingId")
    if child_offering_id is not None:
        out["offering_id"] = str(child_offering_id.text or "")
    return out
