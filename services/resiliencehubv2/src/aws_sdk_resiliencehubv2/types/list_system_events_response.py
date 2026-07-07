"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListSystemEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.system_event_list


class ListSystemEventsResponse(TypedDict, closed=True):
    events: "aws_sdk_resiliencehubv2.types.system_event_list.SystemEventList"
    """<p>The list of system events.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListSystemEventsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.system_event_list

    out["events"] = aws_sdk_resiliencehubv2.types.system_event_list.serialize_json(
        value["events"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSystemEventsResponse:
    out: ListSystemEventsResponse = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_resiliencehubv2.types.system_event_list

        out["events"] = (
            aws_sdk_resiliencehubv2.types.system_event_list.deserialize_json(
                data["events"]
            )
        )
    else:
        raise DeserializationError("ListSystemEventsResponse.events required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
