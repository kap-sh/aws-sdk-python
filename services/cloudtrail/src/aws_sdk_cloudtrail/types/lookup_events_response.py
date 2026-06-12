"""Generated from Smithy shape ``com.amazonaws.cloudtrail#LookupEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.events_list
    import aws_sdk_cloudtrail.types.next_token


class LookupEventsResponse(TypedDict):
    events: NotRequired["aws_sdk_cloudtrail.types.events_list.EventsList"]
    """<p>A list of events returned based on the lookup attributes specified and the CloudTrail event. The events list is sorted by time. The most recent event is listed first.</p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.next_token.NextToken"]
    """<p>The token to use to get the next page of results after a previous API call. If the token does not appear, there are no more results to return. The token must be passed in with the same parameters as the previous call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LookupEventsResponse) -> dict:
    out: dict = {}
    if "events" in value:
        import aws_sdk_cloudtrail.types.events_list

        out["Events"] = aws_sdk_cloudtrail.types.events_list.serialize_aws_json_1_1(
            value["events"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LookupEventsResponse:
    out: LookupEventsResponse = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import aws_sdk_cloudtrail.types.events_list

        out["events"] = aws_sdk_cloudtrail.types.events_list.deserialize_aws_json_1_1(
            data["Events"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
