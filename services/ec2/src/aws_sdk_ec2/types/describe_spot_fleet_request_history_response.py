"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotFleetRequestHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.history_records
    import aws_sdk_ec2.types.string


class DescribeSpotFleetRequestHistoryResponse(TypedDict, closed=True):
    history_records: NotRequired["aws_sdk_ec2.types.history_records.HistoryRecords"]
    """<p>Information about the events in the history of the Spot Fleet request.</p>"""
    last_evaluated_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The last date and time for the events, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). All records up to this time were retrieved.</p> <p>If <code>nextToken</code> indicates that there are more items, this value is not present.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    spot_fleet_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""
    start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The starting date and time for the events, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSpotFleetRequestHistoryResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "history_records" in value:
        import aws_sdk_ec2.types.history_records

        aws_sdk_ec2.types.history_records.serialize_ec2_query(
            value["history_records"], pairs, f"{prefix}.HistoryRecordSet"
        )
    if "last_evaluated_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["last_evaluated_time"], pairs, f"{prefix}.LastEvaluatedTime"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "spot_fleet_request_id" in value:
        pairs.append(
            (f"{prefix}.SpotFleetRequestId", str(value["spot_fleet_request_id"]))
        )
    if "start_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )


def deserialize_ec2_query(el: Element) -> DescribeSpotFleetRequestHistoryResponse:
    out: DescribeSpotFleetRequestHistoryResponse = {}  # type: ignore[typeddict-item]
    if el.find("HistoryRecordSet") is not None:
        import aws_sdk_ec2.types.history_records

        out["history_records"] = (
            aws_sdk_ec2.types.history_records.deserialize_ec2_query(
                el, "HistoryRecordSet"
            )
        )
    child_last_evaluated_time = el.find("LastEvaluatedTime")
    if child_last_evaluated_time is not None:
        import aws_sdk_ec2.types.date_time

        out["last_evaluated_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_last_evaluated_time
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_spot_fleet_request_id = el.find("SpotFleetRequestId")
    if child_spot_fleet_request_id is not None:
        out["spot_fleet_request_id"] = str(child_spot_fleet_request_id.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_ec2.types.date_time

        out["start_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_start_time
        )
    return out
