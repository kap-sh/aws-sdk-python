"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetAddressListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.address_list_id


class GetAddressListRequest(TypedDict, closed=True):
    address_list_id: "capo_mailmanager.types.address_list_id.AddressListId"
    """<p>The identifier of an existing address list resource to be retrieved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAddressListRequest) -> dict:
    out: dict = {}
    out["AddressListId"] = value["address_list_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAddressListRequest:
    out: GetAddressListRequest = {}  # type: ignore[typeddict-item]
    if "AddressListId" in data:
        out["address_list_id"] = data["AddressListId"]
    else:
        raise DeserializationError("GetAddressListRequest.address_list_id required")
    return out
