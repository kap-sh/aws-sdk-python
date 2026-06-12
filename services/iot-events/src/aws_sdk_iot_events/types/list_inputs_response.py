"""Generated from Smithy shape ``com.amazonaws.iotevents#ListInputsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.input_summaries
    import aws_sdk_iot_events.types.next_token


class ListInputsResponse(TypedDict):
    input_summaries: NotRequired[
        "aws_sdk_iot_events.types.input_summaries.InputSummaries"
    ]
    """<p>Summary information about the inputs.</p>"""
    next_token: NotRequired["aws_sdk_iot_events.types.next_token.NextToken"]
    """<p>The token that you can use to return the next set of results, or <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInputsResponse) -> dict:
    out: dict = {}
    if "input_summaries" in value:
        import aws_sdk_iot_events.types.input_summaries

        out["inputSummaries"] = aws_sdk_iot_events.types.input_summaries.serialize_json(
            value["input_summaries"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInputsResponse:
    out: ListInputsResponse = {}  # type: ignore[typeddict-item]
    if "inputSummaries" in data:
        import aws_sdk_iot_events.types.input_summaries

        out["input_summaries"] = (
            aws_sdk_iot_events.types.input_summaries.deserialize_json(
                data["inputSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
