"""Generated from Smithy shape ``com.amazonaws.securityhub#ListMembersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.member_list
    import aws_sdk_securityhub.types.non_empty_string


class ListMembersResponse(TypedDict):
    members: NotRequired["aws_sdk_securityhub.types.member_list.MemberList"]
    """<p>Member details returned by the operation.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The pagination token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersResponse) -> dict:
    out: dict = {}
    if "members" in value:
        import aws_sdk_securityhub.types.member_list

        out["Members"] = aws_sdk_securityhub.types.member_list.serialize_json(
            value["members"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembersResponse:
    out: ListMembersResponse = {}  # type: ignore[typeddict-item]
    if "Members" in data:
        import aws_sdk_securityhub.types.member_list

        out["members"] = aws_sdk_securityhub.types.member_list.deserialize_json(
            data["Members"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
