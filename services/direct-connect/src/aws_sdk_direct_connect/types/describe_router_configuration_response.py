"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeRouterConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.router_config
    import aws_sdk_direct_connect.types.router_type
    import aws_sdk_direct_connect.types.virtual_interface_id
    import aws_sdk_direct_connect.types.virtual_interface_name


class DescribeRouterConfigurationResponse(TypedDict):
    customer_router_config: NotRequired[
        "aws_sdk_direct_connect.types.router_config.RouterConfig"
    ]
    """<p>The customer router configuration.</p>"""
    router: NotRequired["aws_sdk_direct_connect.types.router_type.RouterType"]
    """<p>The details about the router.</p>"""
    virtual_interface_id: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID assigned to the virtual interface.</p>"""
    virtual_interface_name: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_name.VirtualInterfaceName"
    ]
    """<p>Provides the details about a virtual interface's router.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRouterConfigurationResponse) -> dict:
    out: dict = {}
    if "customer_router_config" in value:
        out["customerRouterConfig"] = value["customer_router_config"]
    if "router" in value:
        import aws_sdk_direct_connect.types.router_type

        out["router"] = aws_sdk_direct_connect.types.router_type.serialize_aws_json_1_1(
            value["router"]
        )
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "virtual_interface_name" in value:
        out["virtualInterfaceName"] = value["virtual_interface_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRouterConfigurationResponse:
    out: DescribeRouterConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "customerRouterConfig" in data:
        out["customer_router_config"] = data["customerRouterConfig"]
    if "router" in data:
        import aws_sdk_direct_connect.types.router_type

        out["router"] = (
            aws_sdk_direct_connect.types.router_type.deserialize_aws_json_1_1(
                data["router"]
            )
        )
    if "virtualInterfaceId" in data:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if "virtualInterfaceName" in data:
        out["virtual_interface_name"] = data["virtualInterfaceName"]
    return out
