"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeScheduledInstanceAvailabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_scheduled_instance_availability_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.scheduled_instance_recurrence_request
    import aws_sdk_ec2.types.slot_date_time_range_request
    import aws_sdk_ec2.types.string


class DescribeScheduledInstanceAvailabilityRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone (for example, <code>us-west-2a</code>).</p> </li> <li> <p> <code>instance-type</code> - The instance type (for example, <code>c4.large</code>).</p> </li> <li> <p> <code>platform</code> - The platform (<code>Linux/UNIX</code> or <code>Windows</code>).</p> </li> </ul>"""
    first_slot_start_time_range: NotRequired[
        "aws_sdk_ec2.types.slot_date_time_range_request.SlotDateTimeRangeRequest"
    ]
    """<p>The time period for the first schedule to start.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_scheduled_instance_availability_max_results.DescribeScheduledInstanceAvailabilityMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 300. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>"""
    max_slot_duration_in_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum available duration, in hours. This value must be greater than <code>MinSlotDurationInHours</code> and less than 1,720.</p>"""
    min_slot_duration_in_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum available duration, in hours. The minimum required duration is 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next set of results.</p>"""
    recurrence: NotRequired[
        "aws_sdk_ec2.types.scheduled_instance_recurrence_request.ScheduledInstanceRecurrenceRequest"
    ]
    """<p>The schedule recurrence.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeScheduledInstanceAvailabilityRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "first_slot_start_time_range" in value:
        import aws_sdk_ec2.types.slot_date_time_range_request

        aws_sdk_ec2.types.slot_date_time_range_request.serialize_ec2_query(
            value["first_slot_start_time_range"],
            pairs,
            f"{prefix}.FirstSlotStartTimeRange",
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "max_slot_duration_in_hours" in value:
        pairs.append(
            (
                f"{prefix}.MaxSlotDurationInHours",
                str(value["max_slot_duration_in_hours"]),
            )
        )
    if "min_slot_duration_in_hours" in value:
        pairs.append(
            (
                f"{prefix}.MinSlotDurationInHours",
                str(value["min_slot_duration_in_hours"]),
            )
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "recurrence" in value:
        import aws_sdk_ec2.types.scheduled_instance_recurrence_request

        aws_sdk_ec2.types.scheduled_instance_recurrence_request.serialize_ec2_query(
            value["recurrence"], pairs, f"{prefix}.Recurrence"
        )


def deserialize_ec2_query(el: Element) -> DescribeScheduledInstanceAvailabilityRequest:
    out: DescribeScheduledInstanceAvailabilityRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_first_slot_start_time_range = el.find("FirstSlotStartTimeRange")
    if child_first_slot_start_time_range is not None:
        import aws_sdk_ec2.types.slot_date_time_range_request

        out["first_slot_start_time_range"] = (
            aws_sdk_ec2.types.slot_date_time_range_request.deserialize_ec2_query(
                child_first_slot_start_time_range
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_max_slot_duration_in_hours = el.find("MaxSlotDurationInHours")
    if child_max_slot_duration_in_hours is not None:
        out["max_slot_duration_in_hours"] = int(
            child_max_slot_duration_in_hours.text or ""
        )
    child_min_slot_duration_in_hours = el.find("MinSlotDurationInHours")
    if child_min_slot_duration_in_hours is not None:
        out["min_slot_duration_in_hours"] = int(
            child_min_slot_duration_in_hours.text or ""
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_recurrence = el.find("Recurrence")
    if child_recurrence is not None:
        import aws_sdk_ec2.types.scheduled_instance_recurrence_request

        out["recurrence"] = (
            aws_sdk_ec2.types.scheduled_instance_recurrence_request.deserialize_ec2_query(
                child_recurrence
            )
        )
    return out
