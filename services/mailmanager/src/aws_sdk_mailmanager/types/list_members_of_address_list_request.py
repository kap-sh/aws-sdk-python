"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListMembersOfAddressListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.address_filter
    import aws_sdk_mailmanager.types.address_list_id
    import aws_sdk_mailmanager.types.address_page_size
    import aws_sdk_mailmanager.types.pagination_token


class ListMembersOfAddressListRequest(TypedDict):
    address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId"
    """<p>The unique identifier of the address list to list the addresses from.</p>"""
    filter: NotRequired["aws_sdk_mailmanager.types.address_filter.AddressFilter"]
    """<p>Filter to be used to limit the results.</p>"""
    next_token: NotRequired[
        "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
    ]
    """<p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>"""
    page_size: NotRequired[
        "aws_sdk_mailmanager.types.address_page_size.AddressPageSize"
    ]
    """<p>The maximum number of address list members that are returned per call. You can use NextToken to retrieve the next page of members.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMembersOfAddressListRequest) -> dict:
    out: dict = {}
    out["AddressListId"] = value["address_list_id"]
    if "filter" in value:
        import aws_sdk_mailmanager.types.address_filter

        out["Filter"] = aws_sdk_mailmanager.types.address_filter.serialize_aws_json_1_0(
            value["filter"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMembersOfAddressListRequest:
    out: ListMembersOfAddressListRequest = {}  # type: ignore[typeddict-item]
    if "AddressListId" in data:
        out["address_list_id"] = data["AddressListId"]
    else:
        raise DeserializationError(
            "ListMembersOfAddressListRequest.address_list_id required"
        )
    if "Filter" in data:
        import aws_sdk_mailmanager.types.address_filter

        out["filter"] = (
            aws_sdk_mailmanager.types.address_filter.deserialize_aws_json_1_0(
                data["Filter"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    return out
