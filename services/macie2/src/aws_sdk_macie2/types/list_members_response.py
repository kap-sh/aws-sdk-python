"""Generated from Smithy shape ``com.amazonaws.macie2#ListMembersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_member
    import aws_sdk_macie2.types.__string


class ListMembersResponse(TypedDict, closed=True):
    members: NotRequired["aws_sdk_macie2.types.__list_of_member.__listOfMember"]
    """<p>An array of objects, one for each account that's associated with the administrator account and matches the criteria specified in the request.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersResponse) -> dict:
    out: dict = {}
    if "members" in value:
        import aws_sdk_macie2.types.__list_of_member

        out["members"] = aws_sdk_macie2.types.__list_of_member.serialize_json(
            value["members"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembersResponse:
    out: ListMembersResponse = {}  # type: ignore[typeddict-item]
    if "members" in data:
        import aws_sdk_macie2.types.__list_of_member

        out["members"] = aws_sdk_macie2.types.__list_of_member.deserialize_json(
            data["members"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
