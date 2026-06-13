"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateAddressListResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.address_list_id


class CreateAddressListResponse(TypedDict):
    address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId"
    """<p>The identifier of the created address list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAddressListResponse) -> dict:
    out: dict = {}
    out["AddressListId"] = value["address_list_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAddressListResponse:
    out: CreateAddressListResponse = {}  # type: ignore[typeddict-item]
    if "AddressListId" in data:
        out["address_list_id"] = data["AddressListId"]
    else:
        raise DeserializationError("CreateAddressListResponse.address_list_id required")
    return out
