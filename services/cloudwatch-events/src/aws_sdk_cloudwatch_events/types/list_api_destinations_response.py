"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListApiDestinationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.api_destination_response_list
    import aws_sdk_cloudwatch_events.types.next_token


class ListApiDestinationsResponse(TypedDict):
    api_destinations: NotRequired[
        "aws_sdk_cloudwatch_events.types.api_destination_response_list.ApiDestinationResponseList"
    ]
    """<p>An array of <code>ApiDestination</code> objects that include information about an API destination.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_events.types.next_token.NextToken"]
    """<p>A token you can use in a subsequent request to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApiDestinationsResponse) -> dict:
    out: dict = {}
    if "api_destinations" in value:
        import aws_sdk_cloudwatch_events.types.api_destination_response_list

        out["ApiDestinations"] = (
            aws_sdk_cloudwatch_events.types.api_destination_response_list.serialize_aws_json_1_1(
                value["api_destinations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApiDestinationsResponse:
    out: ListApiDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "ApiDestinations" in data:
        import aws_sdk_cloudwatch_events.types.api_destination_response_list

        out["api_destinations"] = (
            aws_sdk_cloudwatch_events.types.api_destination_response_list.deserialize_aws_json_1_1(
                data["ApiDestinations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
