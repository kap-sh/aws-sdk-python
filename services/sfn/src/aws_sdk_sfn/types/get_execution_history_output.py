"""Generated from Smithy shape ``com.amazonaws.sfn#GetExecutionHistoryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.history_event_list
    import aws_sdk_sfn.types.page_token


class GetExecutionHistoryOutput(TypedDict):
    events: "aws_sdk_sfn.types.history_event_list.HistoryEventList"
    """<p>The list of events that occurred in the execution.</p>"""
    next_token: NotRequired["aws_sdk_sfn.types.page_token.PageToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetExecutionHistoryOutput) -> dict:
    out: dict = {}
    import aws_sdk_sfn.types.history_event_list

    out["events"] = aws_sdk_sfn.types.history_event_list.serialize_aws_json_1_0(
        value["events"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetExecutionHistoryOutput:
    out: GetExecutionHistoryOutput = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_sfn.types.history_event_list

        out["events"] = aws_sdk_sfn.types.history_event_list.deserialize_aws_json_1_0(
            data["events"]
        )
    else:
        raise DeserializationError("GetExecutionHistoryOutput.events required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
