"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListParticipantEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.event_list
    import aws_sdk_ivs_realtime.types.pagination_token


class ListParticipantEventsResponse(TypedDict):
    events: "aws_sdk_ivs_realtime.types.event_list.EventList"
    """<p>List of the matching events.</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>If there are more events than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListParticipantEventsResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs_realtime.types.event_list

    out["events"] = aws_sdk_ivs_realtime.types.event_list.serialize_json(
        value["events"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListParticipantEventsResponse:
    out: ListParticipantEventsResponse = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_ivs_realtime.types.event_list

        out["events"] = aws_sdk_ivs_realtime.types.event_list.deserialize_json(
            data["events"]
        )
    else:
        raise DeserializationError("ListParticipantEventsResponse.events required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
