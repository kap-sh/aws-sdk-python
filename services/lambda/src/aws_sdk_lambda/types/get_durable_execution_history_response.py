"""Generated from Smithy shape ``com.amazonaws.lambda#GetDurableExecutionHistoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.events
    import aws_sdk_lambda.types.string


class GetDurableExecutionHistoryResponse(TypedDict):
    events: "aws_sdk_lambda.types.events.Events"
    """<p>An array of execution history events, ordered chronologically unless <code>ReverseOrder</code> is set to <code>true</code>. Each event represents a significant occurrence during the execution, such as step completion or callback resolution.</p>"""
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>If present, indicates that more history events are available. Use this value as the <code>Marker</code> parameter in a subsequent request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDurableExecutionHistoryResponse) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.events

    out["Events"] = aws_sdk_lambda.types.events.serialize_json(value["events"])
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> GetDurableExecutionHistoryResponse:
    out: GetDurableExecutionHistoryResponse = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import aws_sdk_lambda.types.events

        out["events"] = aws_sdk_lambda.types.events.deserialize_json(data["Events"])
    else:
        raise DeserializationError("GetDurableExecutionHistoryResponse.events required")
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
