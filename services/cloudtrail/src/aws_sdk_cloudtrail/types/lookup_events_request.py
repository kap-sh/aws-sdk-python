"""Generated from Smithy shape ``com.amazonaws.cloudtrail#LookupEventsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.date
    import aws_sdk_cloudtrail.types.event_category
    import aws_sdk_cloudtrail.types.lookup_attributes_list
    import aws_sdk_cloudtrail.types.max_results
    import aws_sdk_cloudtrail.types.next_token


class LookupEventsRequest(TypedDict):
    lookup_attributes: NotRequired[
        "aws_sdk_cloudtrail.types.lookup_attributes_list.LookupAttributesList"
    ]
    """<p>Contains a list of lookup attributes. Currently the list can contain only one item.</p>"""
    start_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p>Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.</p>"""
    end_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p>Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.</p>"""
    event_category: NotRequired["aws_sdk_cloudtrail.types.event_category.EventCategory"]
    """<p>Specifies the event category. If you do not specify an event category, events of the category are not returned in the response. For example, if you do not specify <code>insight</code> as the value of <code>EventCategory</code>, no Insights events are returned.</p>"""
    max_results: NotRequired["aws_sdk_cloudtrail.types.max_results.MaxResults"]
    """<p>The number of events to return. Possible values are 1 through 50. The default is 50.</p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.next_token.NextToken"]
    """<p>The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the original call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LookupEventsRequest) -> dict:
    out: dict = {}
    if "lookup_attributes" in value:
        import aws_sdk_cloudtrail.types.lookup_attributes_list

        out["LookupAttributes"] = (
            aws_sdk_cloudtrail.types.lookup_attributes_list.serialize_aws_json_1_1(
                value["lookup_attributes"]
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
    if "event_category" in value:
        import aws_sdk_cloudtrail.types.event_category

        out["EventCategory"] = (
            aws_sdk_cloudtrail.types.event_category.serialize_aws_json_1_1(
                value["event_category"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LookupEventsRequest:
    out: LookupEventsRequest = {}  # type: ignore[typeddict-item]
    if "LookupAttributes" in data:
        import aws_sdk_cloudtrail.types.lookup_attributes_list

        out["lookup_attributes"] = (
            aws_sdk_cloudtrail.types.lookup_attributes_list.deserialize_aws_json_1_1(
                data["LookupAttributes"]
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
    if "EventCategory" in data:
        import aws_sdk_cloudtrail.types.event_category

        out["event_category"] = (
            aws_sdk_cloudtrail.types.event_category.deserialize_aws_json_1_1(
                data["EventCategory"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
