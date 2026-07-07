"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.action_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListActionsResponse(TypedDict, closed=True):
    action_summaries: "aws_sdk_iotsitewise.types.action_summaries.ActionSummaries"
    """<p>A list that summarizes the actions associated with the specified asset.</p>"""
    next_token: "aws_sdk_iotsitewise.types.next_token.NextToken"
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.action_summaries

    out["actionSummaries"] = aws_sdk_iotsitewise.types.action_summaries.serialize_json(
        value["action_summaries"]
    )
    out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListActionsResponse:
    out: ListActionsResponse = {}  # type: ignore[typeddict-item]
    if "actionSummaries" in data:
        import aws_sdk_iotsitewise.types.action_summaries

        out["action_summaries"] = (
            aws_sdk_iotsitewise.types.action_summaries.deserialize_json(
                data["actionSummaries"]
            )
        )
    else:
        raise DeserializationError("ListActionsResponse.action_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    else:
        raise DeserializationError("ListActionsResponse.next_token required")
    return out
