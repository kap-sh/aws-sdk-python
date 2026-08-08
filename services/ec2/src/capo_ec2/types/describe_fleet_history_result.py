"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetHistoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.fleet_id
    import capo_ec2.types.history_record_set
    import capo_ec2.types.string


class DescribeFleetHistoryResult(TypedDict, closed=True):
    history_records: NotRequired["capo_ec2.types.history_record_set.HistoryRecordSet"]
    """<p>Information about the events in the history of the EC2 Fleet.</p>"""
    last_evaluated_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The last date and time for the events, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). All records up to this time were retrieved.</p> <p>If <code>nextToken</code> indicates that there are more items, this value is not present.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    fleet_id: NotRequired["capo_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC Fleet.</p>"""
    start_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The start date and time for the events, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFleetHistoryResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "history_records" in value:
        import capo_ec2.types.history_record_set

        capo_ec2.types.history_record_set.serialize_ec2_query(
            value["history_records"], pairs, f"{key_prefix}HistoryRecordSet"
        )
    if "last_evaluated_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["last_evaluated_time"], pairs, f"{key_prefix}LastEvaluatedTime"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "fleet_id" in value:
        pairs.append((f"{key_prefix}FleetId", str(value["fleet_id"])))
    if "start_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )


def deserialize_ec2_query(el: Element) -> DescribeFleetHistoryResult:
    out: DescribeFleetHistoryResult = {}  # type: ignore[typeddict-item]
    if el.find("historyRecordSet") is not None:
        import capo_ec2.types.history_record_set

        out["history_records"] = (
            capo_ec2.types.history_record_set.deserialize_ec2_query(
                el, "historyRecordSet"
            )
        )
    child_last_evaluated_time = el.find("lastEvaluatedTime")
    if child_last_evaluated_time is not None:
        import capo_ec2.types.date_time

        out["last_evaluated_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_last_evaluated_time
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_fleet_id = el.find("fleetId")
    if child_fleet_id is not None:
        out["fleet_id"] = str(child_fleet_id.text or "")
    child_start_time = el.find("startTime")
    if child_start_time is not None:
        import capo_ec2.types.date_time

        out["start_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_start_time
        )
    return out
