"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAssistantAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.assistant_association_summary_list
    import aws_sdk_qconnect.types.next_token


class ListAssistantAssociationsResponse(TypedDict):
    assistant_association_summaries: "aws_sdk_qconnect.types.assistant_association_summary_list.AssistantAssociationSummaryList"
    """<p>Summary information about assistant associations.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssistantAssociationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.assistant_association_summary_list

    out["assistantAssociationSummaries"] = (
        aws_sdk_qconnect.types.assistant_association_summary_list.serialize_json(
            value["assistant_association_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssistantAssociationsResponse:
    out: ListAssistantAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "assistantAssociationSummaries" in data:
        import aws_sdk_qconnect.types.assistant_association_summary_list

        out["assistant_association_summaries"] = (
            aws_sdk_qconnect.types.assistant_association_summary_list.deserialize_json(
                data["assistantAssociationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAssistantAssociationsResponse.assistant_association_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
