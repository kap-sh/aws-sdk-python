"""Generated from Smithy shape ``com.amazonaws.directconnect#ConfirmPublicVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.virtual_interface_id


class ConfirmPublicVirtualInterfaceRequest(TypedDict, closed=True):
    virtual_interface_id: (
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    )
    """<p>The ID of the virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfirmPublicVirtualInterfaceRequest) -> dict:
    out: dict = {}
    out["virtualInterfaceId"] = value["virtual_interface_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfirmPublicVirtualInterfaceRequest:
    out: ConfirmPublicVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceId" in data:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    else:
        raise DeserializationError(
            "ConfirmPublicVirtualInterfaceRequest.virtual_interface_id required"
        )
    return out
