"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteAddressListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.address_list_id


class DeleteAddressListRequest(TypedDict):
    address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId"
    """<p>The identifier of an existing address list resource to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAddressListRequest) -> dict:
    out: dict = {}
    out["AddressListId"] = value["address_list_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAddressListRequest:
    out: DeleteAddressListRequest = {}  # type: ignore[typeddict-item]
    if "AddressListId" in data:
        out["address_list_id"] = data["AddressListId"]
    else:
        raise DeserializationError("DeleteAddressListRequest.address_list_id required")
    return out
