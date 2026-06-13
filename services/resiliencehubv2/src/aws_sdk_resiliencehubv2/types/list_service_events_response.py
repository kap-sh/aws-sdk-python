"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListServiceEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.service_event_list


class ListServiceEventsResponse(TypedDict):
    events: "aws_sdk_resiliencehubv2.types.service_event_list.ServiceEventList"
    """<p>The list of service events.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceEventsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.service_event_list

    out["events"] = aws_sdk_resiliencehubv2.types.service_event_list.serialize_json(
        value["events"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceEventsResponse:
    out: ListServiceEventsResponse = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_resiliencehubv2.types.service_event_list

        out["events"] = (
            aws_sdk_resiliencehubv2.types.service_event_list.deserialize_json(
                data["events"]
            )
        )
    else:
        raise DeserializationError("ListServiceEventsResponse.events required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
