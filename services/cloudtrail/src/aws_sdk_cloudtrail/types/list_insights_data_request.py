"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListInsightsDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.date
    import aws_sdk_cloudtrail.types.list_insights_data_dimensions
    import aws_sdk_cloudtrail.types.list_insights_data_max_results_count
    import aws_sdk_cloudtrail.types.list_insights_data_type
    import aws_sdk_cloudtrail.types.pagination_token
    import aws_sdk_cloudtrail.types.resource_arn


class ListInsightsDataRequest(TypedDict, closed=True):
    insight_source: "aws_sdk_cloudtrail.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name(ARN) of the trail for which you want to retrieve Insights events.</p>"""
    data_type: "aws_sdk_cloudtrail.types.list_insights_data_type.ListInsightsDataType"
    """<p>Specifies the category of events returned. To fetch Insights events, specify <code>InsightsEvents</code> as the value of <code>DataType</code> </p>"""
    dimensions: NotRequired[
        "aws_sdk_cloudtrail.types.list_insights_data_dimensions.ListInsightsDataDimensions"
    ]
    """<p>Contains a map of dimensions. Currently the map can contain only one item.</p>"""
    start_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p>Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.</p>"""
    end_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p>Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.</p>"""
    max_results: NotRequired[
        "aws_sdk_cloudtrail.types.list_insights_data_max_results_count.ListInsightsDataMaxResultsCount"
    ]
    """<p>The number of events to return. Possible values are 1 through 50. The default is 50.</p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.pagination_token.PaginationToken"]
    """<p>The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the original call. For example, if the original call specified a EventName as a dimension with <code>PutObject</code> as a value, the call with NextToken should include those same parameters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInsightsDataRequest) -> dict:
    out: dict = {}
    out["InsightSource"] = value["insight_source"]
    import aws_sdk_cloudtrail.types.list_insights_data_type

    out["DataType"] = (
        aws_sdk_cloudtrail.types.list_insights_data_type.serialize_aws_json_1_1(
            value["data_type"]
        )
    )
    if "dimensions" in value:
        import aws_sdk_cloudtrail.types.list_insights_data_dimensions

        out["Dimensions"] = (
            aws_sdk_cloudtrail.types.list_insights_data_dimensions.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    if "start_time" in value:
        import aws_sdk_cloudtrail.types.date

        out["StartTime"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_cloudtrail.types.date

        out["EndTime"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInsightsDataRequest:
    out: ListInsightsDataRequest = {}  # type: ignore[typeddict-item]
    if "InsightSource" in data:
        out["insight_source"] = data["InsightSource"]
    else:
        raise DeserializationError("ListInsightsDataRequest.insight_source required")
    if "DataType" in data:
        import aws_sdk_cloudtrail.types.list_insights_data_type

        out["data_type"] = (
            aws_sdk_cloudtrail.types.list_insights_data_type.deserialize_aws_json_1_1(
                data["DataType"]
            )
        )
    else:
        raise DeserializationError("ListInsightsDataRequest.data_type required")
    if "Dimensions" in data:
        import aws_sdk_cloudtrail.types.list_insights_data_dimensions

        out["dimensions"] = (
            aws_sdk_cloudtrail.types.list_insights_data_dimensions.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_cloudtrail.types.date

        out["start_time"] = aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_cloudtrail.types.date

        out["end_time"] = aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
