"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeScheduledInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.integer
    import capo_ec2.types.scheduled_instance_id_request_set
    import capo_ec2.types.slot_start_time_range_request
    import capo_ec2.types.string


class DescribeScheduledInstancesRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone (for example, <code>us-west-2a</code>).</p> </li> <li> <p> <code>instance-type</code> - The instance type (for example, <code>c4.large</code>).</p> </li> <li> <p> <code>platform</code> - The platform (<code>Linux/UNIX</code> or <code>Windows</code>).</p> </li> </ul>"""
    max_results: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 100. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token for the next set of results.</p>"""
    scheduled_instance_ids: NotRequired[
        "capo_ec2.types.scheduled_instance_id_request_set.ScheduledInstanceIdRequestSet"
    ]
    """<p>The Scheduled Instance IDs.</p>"""
    slot_start_time_range: NotRequired[
        "capo_ec2.types.slot_start_time_range_request.SlotStartTimeRangeRequest"
    ]
    """<p>The time period for the first schedule to start.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeScheduledInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "scheduled_instance_ids" in value:
        import capo_ec2.types.scheduled_instance_id_request_set

        capo_ec2.types.scheduled_instance_id_request_set.serialize_ec2_query(
            value["scheduled_instance_ids"], pairs, f"{key_prefix}ScheduledInstanceId"
        )
    if "slot_start_time_range" in value:
        import capo_ec2.types.slot_start_time_range_request

        capo_ec2.types.slot_start_time_range_request.serialize_ec2_query(
            value["slot_start_time_range"], pairs, f"{key_prefix}SlotStartTimeRange"
        )


def deserialize_ec2_query(el: Element) -> DescribeScheduledInstancesRequest:
    out: DescribeScheduledInstancesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("ScheduledInstanceId") is not None:
        import capo_ec2.types.scheduled_instance_id_request_set

        out["scheduled_instance_ids"] = (
            capo_ec2.types.scheduled_instance_id_request_set.deserialize_ec2_query(
                el, "ScheduledInstanceId"
            )
        )
    child_slot_start_time_range = el.find("SlotStartTimeRange")
    if child_slot_start_time_range is not None:
        import capo_ec2.types.slot_start_time_range_request

        out["slot_start_time_range"] = (
            capo_ec2.types.slot_start_time_range_request.deserialize_ec2_query(
                child_slot_start_time_range
            )
        )
    return out
