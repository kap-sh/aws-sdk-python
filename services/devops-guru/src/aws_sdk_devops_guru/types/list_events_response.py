"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.events
    import aws_sdk_devops_guru.types.uuid_next_token


class ListEventsResponse(TypedDict):
    events: "aws_sdk_devops_guru.types.events.Events"
    """<p> A list of the requested events. </p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventsResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.events

    out["Events"] = aws_sdk_devops_guru.types.events.serialize_json(value["events"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventsResponse:
    out: ListEventsResponse = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import aws_sdk_devops_guru.types.events

        out["events"] = aws_sdk_devops_guru.types.events.deserialize_json(
            data["Events"]
        )
    else:
        raise DeserializationError("ListEventsResponse.events required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
