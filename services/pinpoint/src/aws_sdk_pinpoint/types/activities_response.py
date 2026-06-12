"""Generated from Smithy shape ``com.amazonaws.pinpoint#ActivitiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.list_of_activity_response


class ActivitiesResponse(TypedDict):
    item: NotRequired[
        "aws_sdk_pinpoint.types.list_of_activity_response.ListOfActivityResponse"
    ]
    """<p>An array of responses, one for each activity that was performed by the campaign.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivitiesResponse) -> dict:
    out: dict = {}
    if "item" in value:
        import aws_sdk_pinpoint.types.list_of_activity_response

        out["Item"] = aws_sdk_pinpoint.types.list_of_activity_response.serialize_json(
            value["item"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ActivitiesResponse:
    out: ActivitiesResponse = {}  # type: ignore[typeddict-item]
    if "Item" in data:
        import aws_sdk_pinpoint.types.list_of_activity_response

        out["item"] = aws_sdk_pinpoint.types.list_of_activity_response.deserialize_json(
            data["Item"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
