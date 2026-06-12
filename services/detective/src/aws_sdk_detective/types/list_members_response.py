"""Generated from Smithy shape ``com.amazonaws.detective#ListMembersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.member_detail_list
    import aws_sdk_detective.types.pagination_token


class ListMembersResponse(TypedDict):
    member_details: NotRequired[
        "aws_sdk_detective.types.member_detail_list.MemberDetailList"
    ]
    """<p>The list of member accounts in the behavior graph.</p> <p>For invited accounts, the results include member accounts that did not pass verification and member accounts that have not yet accepted the invitation to the behavior graph. The results do not include member accounts that were removed from the behavior graph.</p> <p>For the organization behavior graph, the results do not include organization accounts that the Detective administrator account has not enabled as member accounts.</p>"""
    next_token: NotRequired["aws_sdk_detective.types.pagination_token.PaginationToken"]
    """<p>If there are more member accounts remaining in the results, then use this pagination token to request the next page of member accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersResponse) -> dict:
    out: dict = {}
    if "member_details" in value:
        import aws_sdk_detective.types.member_detail_list

        out["MemberDetails"] = (
            aws_sdk_detective.types.member_detail_list.serialize_json(
                value["member_details"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembersResponse:
    out: ListMembersResponse = {}  # type: ignore[typeddict-item]
    if "MemberDetails" in data:
        import aws_sdk_detective.types.member_detail_list

        out["member_details"] = (
            aws_sdk_detective.types.member_detail_list.deserialize_json(
                data["MemberDetails"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
