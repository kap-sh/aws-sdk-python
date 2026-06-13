"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationChangeRequestsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_change_request_summary_list
    import aws_sdk_cleanrooms.types.pagination_token


class ListCollaborationChangeRequestsOutput(TypedDict):
    collaboration_change_request_summaries: "aws_sdk_cleanrooms.types.collaboration_change_request_summary_list.CollaborationChangeRequestSummaryList"
    """<p>The list of collaboration change request summaries.</p>"""
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationChangeRequestsOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.collaboration_change_request_summary_list

    out["collaborationChangeRequestSummaries"] = (
        aws_sdk_cleanrooms.types.collaboration_change_request_summary_list.serialize_json(
            value["collaboration_change_request_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCollaborationChangeRequestsOutput:
    out: ListCollaborationChangeRequestsOutput = {}  # type: ignore[typeddict-item]
    if "collaborationChangeRequestSummaries" in data:
        import aws_sdk_cleanrooms.types.collaboration_change_request_summary_list

        out["collaboration_change_request_summaries"] = (
            aws_sdk_cleanrooms.types.collaboration_change_request_summary_list.deserialize_json(
                data["collaborationChangeRequestSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListCollaborationChangeRequestsOutput.collaboration_change_request_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
