"""Generated from Smithy shape ``com.amazonaws.deadline#ListStepsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.next_token
    import aws_sdk_deadline.types.step_summaries


class ListStepsResponse(TypedDict):
    steps: "aws_sdk_deadline.types.step_summaries.StepSummaries"
    """<p>The steps on the list.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStepsResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.step_summaries

    out["steps"] = aws_sdk_deadline.types.step_summaries.serialize_json(value["steps"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStepsResponse:
    out: ListStepsResponse = {}  # type: ignore[typeddict-item]
    if "steps" in data:
        import aws_sdk_deadline.types.step_summaries

        out["steps"] = aws_sdk_deadline.types.step_summaries.deserialize_json(
            data["steps"]
        )
    else:
        raise DeserializationError("ListStepsResponse.steps required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
