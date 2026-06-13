"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListMembershipsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_summary_list
    import aws_sdk_cleanrooms.types.pagination_token


class ListMembershipsOutput(TypedDict):
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    membership_summaries: (
        "aws_sdk_cleanrooms.types.membership_summary_list.MembershipSummaryList"
    )
    """<p>The list of memberships returned from the ListMemberships operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanrooms.types.membership_summary_list

    out["membershipSummaries"] = (
        aws_sdk_cleanrooms.types.membership_summary_list.serialize_json(
            value["membership_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMembershipsOutput:
    out: ListMembershipsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "membershipSummaries" in data:
        import aws_sdk_cleanrooms.types.membership_summary_list

        out["membership_summaries"] = (
            aws_sdk_cleanrooms.types.membership_summary_list.deserialize_json(
                data["membershipSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListMembershipsOutput.membership_summaries required"
        )
    return out
