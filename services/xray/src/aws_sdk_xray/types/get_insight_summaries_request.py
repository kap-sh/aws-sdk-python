"""Generated from Smithy shape ``com.amazonaws.xray#GetInsightSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.get_insight_summaries_max_results
    import aws_sdk_xray.types.group_arn
    import aws_sdk_xray.types.group_name
    import aws_sdk_xray.types.insight_state_list
    import aws_sdk_xray.types.timestamp
    import aws_sdk_xray.types.token


class GetInsightSummariesRequest(TypedDict, closed=True):
    states: NotRequired["aws_sdk_xray.types.insight_state_list.InsightStateList"]
    """<p>The list of insight states. </p>"""
    group_arn: NotRequired["aws_sdk_xray.types.group_arn.GroupARN"]
    """<p>The Amazon Resource Name (ARN) of the group. Required if the GroupName isn't provided.</p>"""
    group_name: NotRequired["aws_sdk_xray.types.group_name.GroupName"]
    """<p>The name of the group. Required if the GroupARN isn't provided.</p>"""
    start_time: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p>The beginning of the time frame in which the insights started. The start time can't be more than 30 days old.</p>"""
    end_time: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p>The end of the time frame in which the insights ended. The end time can't be more than 30 days old.</p>"""
    max_results: NotRequired[
        "aws_sdk_xray.types.get_insight_summaries_max_results.GetInsightSummariesMaxResults"
    ]
    """<p>The maximum number of results to display.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.token.Token"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightSummariesRequest) -> dict:
    out: dict = {}
    if "states" in value:
        import aws_sdk_xray.types.insight_state_list

        out["States"] = aws_sdk_xray.types.insight_state_list.serialize_json(
            value["states"]
        )
    if "group_arn" in value:
        out["GroupARN"] = value["group_arn"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    import aws_sdk_xray.types.timestamp

    out["StartTime"] = aws_sdk_xray.types.timestamp.serialize_json(value["start_time"])
    import aws_sdk_xray.types.timestamp

    out["EndTime"] = aws_sdk_xray.types.timestamp.serialize_json(value["end_time"])
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetInsightSummariesRequest:
    out: GetInsightSummariesRequest = {}  # type: ignore[typeddict-item]
    if "States" in data:
        import aws_sdk_xray.types.insight_state_list

        out["states"] = aws_sdk_xray.types.insight_state_list.deserialize_json(
            data["States"]
        )
    if "GroupARN" in data:
        out["group_arn"] = data["GroupARN"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "StartTime" in data:
        import aws_sdk_xray.types.timestamp

        out["start_time"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        raise DeserializationError("GetInsightSummariesRequest.start_time required")
    if "EndTime" in data:
        import aws_sdk_xray.types.timestamp

        out["end_time"] = aws_sdk_xray.types.timestamp.deserialize_json(data["EndTime"])
    else:
        raise DeserializationError("GetInsightSummariesRequest.end_time required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
