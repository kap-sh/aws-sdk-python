"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListApiDestinationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.api_destination_name
    import capo_cloudwatch_events.types.connection_arn
    import capo_cloudwatch_events.types.limit_max100
    import capo_cloudwatch_events.types.next_token


class ListApiDestinationsRequest(TypedDict, closed=True):
    name_prefix: NotRequired[
        "capo_cloudwatch_events.types.api_destination_name.ApiDestinationName"
    ]
    """<p>A name prefix to filter results returned. Only API destinations with a name that starts with the prefix are returned.</p>"""
    connection_arn: NotRequired[
        "capo_cloudwatch_events.types.connection_arn.ConnectionArn"
    ]
    """<p>The ARN of the connection specified for the API destination.</p>"""
    next_token: NotRequired["capo_cloudwatch_events.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""
    limit: NotRequired["capo_cloudwatch_events.types.limit_max100.LimitMax100"]
    """<p>The maximum number of API destinations to include in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApiDestinationsRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApiDestinationsRequest:
    out: ListApiDestinationsRequest = {}  # type: ignore[typeddict-item]
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
