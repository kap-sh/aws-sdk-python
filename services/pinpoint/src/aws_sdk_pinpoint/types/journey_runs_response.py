"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyRunsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.list_of_journey_run_response


class JourneyRunsResponse(TypedDict):
    item: NotRequired[
        "aws_sdk_pinpoint.types.list_of_journey_run_response.ListOfJourneyRunResponse"
    ]
    """<p>An array of responses, one for each run of the journey</p>"""
    next_token: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneyRunsResponse) -> dict:
    out: dict = {}
    if "item" in value:
        import aws_sdk_pinpoint.types.list_of_journey_run_response

        out["Item"] = (
            aws_sdk_pinpoint.types.list_of_journey_run_response.serialize_json(
                value["item"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> JourneyRunsResponse:
    out: JourneyRunsResponse = {}  # type: ignore[typeddict-item]
    if "Item" in data:
        import aws_sdk_pinpoint.types.list_of_journey_run_response

        out["item"] = (
            aws_sdk_pinpoint.types.list_of_journey_run_response.deserialize_json(
                data["Item"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
