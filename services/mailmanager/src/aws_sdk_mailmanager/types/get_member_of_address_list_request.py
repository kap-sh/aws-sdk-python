"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetMemberOfAddressListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.address
    import aws_sdk_mailmanager.types.address_list_id


class GetMemberOfAddressListRequest(TypedDict, closed=True):
    address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId"
    """<p>The unique identifier of the address list to retrieve the address from.</p>"""
    address: "aws_sdk_mailmanager.types.address.Address"
    """<p>The address to be retrieved from the address list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMemberOfAddressListRequest) -> dict:
    out: dict = {}
    out["AddressListId"] = value["address_list_id"]
    out["Address"] = value["address"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMemberOfAddressListRequest:
    out: GetMemberOfAddressListRequest = {}  # type: ignore[typeddict-item]
    if "AddressListId" in data:
        out["address_list_id"] = data["AddressListId"]
    else:
        raise DeserializationError(
            "GetMemberOfAddressListRequest.address_list_id required"
        )
    if "Address" in data:
        out["address"] = data["Address"]
    else:
        raise DeserializationError("GetMemberOfAddressListRequest.address required")
    return out
