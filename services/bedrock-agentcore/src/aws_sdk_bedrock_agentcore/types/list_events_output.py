"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListEventsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.event_list
    import aws_sdk_bedrock_agentcore.types.pagination_token


class ListEventsOutput(TypedDict, closed=True):
    events: "aws_sdk_bedrock_agentcore.types.event_list.EventList"
    """<p>The list of events that match the specified criteria.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventsOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.event_list

    out["events"] = aws_sdk_bedrock_agentcore.types.event_list.serialize_json(
        value["events"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventsOutput:
    out: ListEventsOutput = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_bedrock_agentcore.types.event_list

        out["events"] = aws_sdk_bedrock_agentcore.types.event_list.deserialize_json(
            data["events"]
        )
    else:
        raise DeserializationError("ListEventsOutput.events required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
