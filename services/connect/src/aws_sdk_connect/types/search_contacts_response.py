"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contacts
    import aws_sdk_connect.types.large_next_token
    import aws_sdk_connect.types.total_count


class SearchContactsResponse(TypedDict):
    contacts: "aws_sdk_connect.types.contacts.Contacts"
    """<p>Information about the contacts.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.large_next_token.LargeNextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    total_count: NotRequired["aws_sdk_connect.types.total_count.TotalCount"]
    """<p>The total number of contacts which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.contacts

    out["Contacts"] = aws_sdk_connect.types.contacts.serialize_json(value["contacts"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    return out


def deserialize_json(data: dict) -> SearchContactsResponse:
    out: SearchContactsResponse = {}  # type: ignore[typeddict-item]
    if "Contacts" in data:
        import aws_sdk_connect.types.contacts

        out["contacts"] = aws_sdk_connect.types.contacts.deserialize_json(
            data["Contacts"]
        )
    else:
        raise DeserializationError("SearchContactsResponse.contacts required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    return out
