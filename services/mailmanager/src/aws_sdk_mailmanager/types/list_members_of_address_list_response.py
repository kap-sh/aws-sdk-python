"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListMembersOfAddressListResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.pagination_token
    import aws_sdk_mailmanager.types.saved_addresses


class ListMembersOfAddressListResponse(TypedDict, closed=True):
    addresses: "aws_sdk_mailmanager.types.saved_addresses.SavedAddresses"
    """<p>The list of addresses.</p>"""
    next_token: NotRequired[
        "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
    ]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMembersOfAddressListResponse) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.saved_addresses

    out["Addresses"] = aws_sdk_mailmanager.types.saved_addresses.serialize_aws_json_1_0(
        value["addresses"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMembersOfAddressListResponse:
    out: ListMembersOfAddressListResponse = {}  # type: ignore[typeddict-item]
    if "Addresses" in data:
        import aws_sdk_mailmanager.types.saved_addresses

        out["addresses"] = (
            aws_sdk_mailmanager.types.saved_addresses.deserialize_aws_json_1_0(
                data["Addresses"]
            )
        )
    else:
        raise DeserializationError(
            "ListMembersOfAddressListResponse.addresses required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
