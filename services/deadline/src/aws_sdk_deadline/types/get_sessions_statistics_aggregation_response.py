"""Generated from Smithy shape ``com.amazonaws.deadline#GetSessionsStatisticsAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.next_token
    import aws_sdk_deadline.types.sessions_statistics_aggregation_status
    import aws_sdk_deadline.types.statistics_list
    import aws_sdk_deadline.types.string


class GetSessionsStatisticsAggregationResponse(TypedDict, closed=True):
    statistics: NotRequired["aws_sdk_deadline.types.statistics_list.StatisticsList"]
    """<p>The statistics for the specified fleets or queues.</p>"""
    status: "aws_sdk_deadline.types.sessions_statistics_aggregation_status.SessionsStatisticsAggregationStatus"
    """<p>The status of the aggregated results. An aggregation may fail or time out if the results are too large. If this happens, you can call the <code>StartSessionsStatisticsAggregation</code> operation after you reduce the aggregation time frame, reduce the number of queues or fleets in the aggregation, or increase the period length.</p> <p>If you call the <code>StartSessionsStatisticsAggregation </code> operation when the status is <code>IN_PROGRESS</code>, you will receive a <code>ThrottlingException</code>.</p>"""
    status_message: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>A message that describes the status.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionsStatisticsAggregationResponse) -> dict:
    out: dict = {}
    if "statistics" in value:
        import aws_sdk_deadline.types.statistics_list

        out["statistics"] = aws_sdk_deadline.types.statistics_list.serialize_json(
            value["statistics"]
        )
    import aws_sdk_deadline.types.sessions_statistics_aggregation_status

    out["status"] = (
        aws_sdk_deadline.types.sessions_statistics_aggregation_status.serialize_json(
            value["status"]
        )
    )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSessionsStatisticsAggregationResponse:
    out: GetSessionsStatisticsAggregationResponse = {}  # type: ignore[typeddict-item]
    if "statistics" in data:
        import aws_sdk_deadline.types.statistics_list

        out["statistics"] = aws_sdk_deadline.types.statistics_list.deserialize_json(
            data["statistics"]
        )
    if "status" in data:
        import aws_sdk_deadline.types.sessions_statistics_aggregation_status

        out["status"] = (
            aws_sdk_deadline.types.sessions_statistics_aggregation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "GetSessionsStatisticsAggregationResponse.status required"
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
