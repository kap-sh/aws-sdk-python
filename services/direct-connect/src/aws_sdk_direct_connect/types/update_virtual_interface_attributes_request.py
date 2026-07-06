"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateVirtualInterfaceAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.enable_site_link
    import aws_sdk_direct_connect.types.mtu
    import aws_sdk_direct_connect.types.virtual_interface_id
    import aws_sdk_direct_connect.types.virtual_interface_name


class UpdateVirtualInterfaceAttributesRequest(TypedDict, closed=True):
    virtual_interface_id: (
        "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    )
    """<p>The ID of the virtual private interface.</p>"""
    mtu: NotRequired["aws_sdk_direct_connect.types.mtu.MTU"]
    """<p>The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500.</p>"""
    enable_site_link: NotRequired[
        "aws_sdk_direct_connect.types.enable_site_link.EnableSiteLink"
    ]
    """<p>Indicates whether to enable or disable SiteLink.</p>"""
    virtual_interface_name: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_name.VirtualInterfaceName"
    ]
    """<p>The name of the virtual private interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVirtualInterfaceAttributesRequest) -> dict:
    out: dict = {}
    out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "mtu" in value:
        out["mtu"] = value["mtu"]
    if "enable_site_link" in value:
        out["enableSiteLink"] = value["enable_site_link"]
    if "virtual_interface_name" in value:
        out["virtualInterfaceName"] = value["virtual_interface_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVirtualInterfaceAttributesRequest:
    out: UpdateVirtualInterfaceAttributesRequest = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceId" in data:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    else:
        raise DeserializationError(
            "UpdateVirtualInterfaceAttributesRequest.virtual_interface_id required"
        )
    if "mtu" in data:
        out["mtu"] = data["mtu"]
    if "enableSiteLink" in data:
        out["enable_site_link"] = data["enableSiteLink"]
    if "virtualInterfaceName" in data:
        out["virtual_interface_name"] = data["virtualInterfaceName"]
    return out
