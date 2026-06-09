"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockExtensionHistoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_id_set
    import aws_sdk_ec2.types.describe_future_capacity_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeCapacityBlockExtensionHistoryRequest(TypedDict):
    capacity_reservation_ids: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id_set.CapacityReservationIdSet"
    ]
    """<p>The IDs of Capacity Block reservations that you want to display the history for.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_future_capacity_max_results.DescribeFutureCapacityMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone of the extension.</p> </li> <li> <p> <code>availability-zone-id</code> - The Availability Zone ID of the extension.</p> </li> <li> <p> <code>capacity-block-extension-offering-id</code> - The ID of the extension offering.</p> </li> <li> <p> <code>capacity-block-extension-status</code> - The status of the extension (<code>payment-pending</code> | <code>payment-failed</code> | <code>payment-succeeded</code>).</p> </li> <li> <p> <code>capacity-reservation-id</code> - The reservation ID of the extension.</p> </li> <li> <p> <code>instance-type</code> - The instance type of the extension.</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityBlockExtensionHistoryRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_reservation_ids" in value:
        import aws_sdk_ec2.types.capacity_reservation_id_set

        aws_sdk_ec2.types.capacity_reservation_id_set.serialize_ec2_query(
            value["capacity_reservation_ids"], pairs, f"{prefix}.CapacityReservationIds"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeCapacityBlockExtensionHistoryRequest:
    out: DescribeCapacityBlockExtensionHistoryRequest = {}  # type: ignore[typeddict-item]
    if el.find("CapacityReservationIds") is not None:
        import aws_sdk_ec2.types.capacity_reservation_id_set

        out["capacity_reservation_ids"] = (
            aws_sdk_ec2.types.capacity_reservation_id_set.deserialize_ec2_query(
                el, "CapacityReservationIds"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
