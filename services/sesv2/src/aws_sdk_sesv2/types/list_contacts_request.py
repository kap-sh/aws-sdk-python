"""Generated from Smithy shape ``com.amazonaws.sesv2#ListContactsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.contact_list_name
    import aws_sdk_sesv2.types.list_contacts_filter
    import aws_sdk_sesv2.types.max_items
    import aws_sdk_sesv2.types.next_token


class ListContactsRequest(TypedDict, closed=True):
    contact_list_name: "aws_sdk_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""
    filter: NotRequired["aws_sdk_sesv2.types.list_contacts_filter.ListContactsFilter"]
    """<p>A filter that can be applied to a list of contacts.</p>"""
    page_size: NotRequired["aws_sdk_sesv2.types.max_items.MaxItems"]
    """<p>The number of contacts that may be returned at once, which is dependent on if there are more or less contacts than the value of the PageSize. Use this parameter to paginate results. If additional contacts exist beyond the specified limit, the <code>NextToken</code> element is sent in the response. Use the <code>NextToken</code> value in subsequent requests to retrieve additional contacts.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A string token indicating that there might be additional contacts available to be listed. Use the token provided in the Response to use in the subsequent call to ListContacts with the same parameters to retrieve the next page of contacts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_sesv2.types.list_contacts_filter

        out["Filter"] = aws_sdk_sesv2.types.list_contacts_filter.serialize_json(
            value["filter"]
        )
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContactsRequest:
    out: ListContactsRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import aws_sdk_sesv2.types.list_contacts_filter

        out["filter"] = aws_sdk_sesv2.types.list_contacts_filter.deserialize_json(
            data["Filter"]
        )
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
