"""Generated from Smithy shape ``com.amazonaws.securityir#ListMembershipsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.list_membership_items


class ListMembershipsResponse(TypedDict):
    next_token: NotRequired["str"]
    """<p>An optional string that, if supplied on subsequent calls to ListMemberships, allows the API to fetch the next page of results. </p>"""
    items: NotRequired[
        "aws_sdk_security_ir.types.list_membership_items.ListMembershipItems"
    ]
    """<p>Request element for ListMemberships including the accountID, membershipARN, membershipID, membershipStatus, and region for each response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "items" in value:
        import aws_sdk_security_ir.types.list_membership_items

        out["items"] = aws_sdk_security_ir.types.list_membership_items.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> ListMembershipsResponse:
    out: ListMembershipsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import aws_sdk_security_ir.types.list_membership_items

        out["items"] = aws_sdk_security_ir.types.list_membership_items.deserialize_json(
            data["items"]
        )
    return out
