"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeRouterConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.router_type_identifier
    import aws_sdk_direct_connect.types.virtual_interface_id


class DescribeRouterConfigurationRequest(TypedDict, closed=True):
    virtual_interface_id: (
        "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    )
    """<p>The ID of the virtual interface.</p>"""
    router_type_identifier: NotRequired[
        "aws_sdk_direct_connect.types.router_type_identifier.RouterTypeIdentifier"
    ]
    """<p>Identifies the router by a combination of vendor, platform, and software version. For example, <code>CiscoSystemsInc-2900SeriesRouters-IOS124</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRouterConfigurationRequest) -> dict:
    out: dict = {}
    out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "router_type_identifier" in value:
        out["routerTypeIdentifier"] = value["router_type_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRouterConfigurationRequest:
    out: DescribeRouterConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceId" in data:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    else:
        raise DeserializationError(
            "DescribeRouterConfigurationRequest.virtual_interface_id required"
        )
    if "routerTypeIdentifier" in data:
        out["router_type_identifier"] = data["routerTypeIdentifier"]
    return out
