"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListApiDestinationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.api_destination_response_list
    import aws_sdk_eventbridge.types.next_token


class ListApiDestinationsResponse(TypedDict, closed=True):
    api_destinations: NotRequired[
        "aws_sdk_eventbridge.types.api_destination_response_list.ApiDestinationResponseList"
    ]
    """<p>An array that includes information about each API destination.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApiDestinationsResponse) -> dict:
    out: dict = {}
    if "api_destinations" in value:
        import aws_sdk_eventbridge.types.api_destination_response_list

        out["ApiDestinations"] = (
            aws_sdk_eventbridge.types.api_destination_response_list.serialize_aws_json_1_1(
                value["api_destinations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApiDestinationsResponse:
    out: ListApiDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "ApiDestinations" in data:
        import aws_sdk_eventbridge.types.api_destination_response_list

        out["api_destinations"] = (
            aws_sdk_eventbridge.types.api_destination_response_list.deserialize_aws_json_1_1(
                data["ApiDestinations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
