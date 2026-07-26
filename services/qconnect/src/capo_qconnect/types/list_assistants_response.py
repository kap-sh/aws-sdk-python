"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAssistantsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.assistant_list
    import capo_qconnect.types.next_token


class ListAssistantsResponse(TypedDict, closed=True):
    assistant_summaries: "capo_qconnect.types.assistant_list.AssistantList"
    """<p>Information about the assistants.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssistantsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.assistant_list

    out["assistantSummaries"] = capo_qconnect.types.assistant_list.serialize_json(
        value["assistant_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssistantsResponse:
    out: ListAssistantsResponse = {}  # type: ignore[typeddict-item]
    if "assistantSummaries" in data:
        import capo_qconnect.types.assistant_list

        out["assistant_summaries"] = (
            capo_qconnect.types.assistant_list.deserialize_json(
                data["assistantSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAssistantsResponse.assistant_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
