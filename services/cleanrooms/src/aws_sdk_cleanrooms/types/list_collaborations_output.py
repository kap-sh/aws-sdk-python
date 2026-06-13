"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_summary_list
    import aws_sdk_cleanrooms.types.pagination_token


class ListCollaborationsOutput(TypedDict):
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    collaboration_list: (
        "aws_sdk_cleanrooms.types.collaboration_summary_list.CollaborationSummaryList"
    )
    """<p>The list of collaborations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanrooms.types.collaboration_summary_list

    out["collaborationList"] = (
        aws_sdk_cleanrooms.types.collaboration_summary_list.serialize_json(
            value["collaboration_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationsOutput:
    out: ListCollaborationsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "collaborationList" in data:
        import aws_sdk_cleanrooms.types.collaboration_summary_list

        out["collaboration_list"] = (
            aws_sdk_cleanrooms.types.collaboration_summary_list.deserialize_json(
                data["collaborationList"]
            )
        )
    else:
        raise DeserializationError(
            "ListCollaborationsOutput.collaboration_list required"
        )
    return out
