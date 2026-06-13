"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListMembersOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.member_summary_list
    import aws_sdk_cleanrooms.types.pagination_token


class ListMembersOutput(TypedDict):
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    member_summaries: "aws_sdk_cleanrooms.types.member_summary_list.MemberSummaryList"
    """<p>The list of members returned by the ListMembers operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanrooms.types.member_summary_list

    out["memberSummaries"] = (
        aws_sdk_cleanrooms.types.member_summary_list.serialize_json(
            value["member_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMembersOutput:
    out: ListMembersOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "memberSummaries" in data:
        import aws_sdk_cleanrooms.types.member_summary_list

        out["member_summaries"] = (
            aws_sdk_cleanrooms.types.member_summary_list.deserialize_json(
                data["memberSummaries"]
            )
        )
    else:
        raise DeserializationError("ListMembersOutput.member_summaries required")
    return out
