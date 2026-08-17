"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FilterLogEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.filtered_log_events
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.searched_log_streams


class FilterLogEventsResponse(TypedDict, closed=True):
    events: NotRequired[
        "capo_cloudwatch_logs.types.filtered_log_events.FilteredLogEvents"
    ]
    """<p>The matched events.</p>"""
    searched_log_streams: NotRequired[
        "capo_cloudwatch_logs.types.searched_log_streams.SearchedLogStreams"
    ]
    """<p> <b>Important</b> As of May 15, 2020, this parameter is no longer supported. This parameter returns an empty list.</p> <p>Indicates which log streams have been searched and whether each has been searched completely.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. The token expires after 24 hours.</p> <p>If the results don't include a <code>nextToken</code>, then pagination is finished. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterLogEventsResponse) -> dict:
    out: dict = {}
    if "events" in value:
        import capo_cloudwatch_logs.types.filtered_log_events

        out["events"] = (
            capo_cloudwatch_logs.types.filtered_log_events.serialize_aws_json_1_1(
                value["events"]
            )
        )
    if "searched_log_streams" in value:
        import capo_cloudwatch_logs.types.searched_log_streams

        out["searchedLogStreams"] = (
            capo_cloudwatch_logs.types.searched_log_streams.serialize_aws_json_1_1(
                value["searched_log_streams"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterLogEventsResponse:
    out: FilterLogEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_cloudwatch_logs.types.filtered_log_events

        out["events"] = (
            capo_cloudwatch_logs.types.filtered_log_events.deserialize_aws_json_1_1(
                data["events"]
            )
        )
    if data.get("searchedLogStreams") is not None:
        import capo_cloudwatch_logs.types.searched_log_streams

        out["searched_log_streams"] = (
            capo_cloudwatch_logs.types.searched_log_streams.deserialize_aws_json_1_1(
                data["searchedLogStreams"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
