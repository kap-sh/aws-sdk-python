"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowVpcInterfacesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_vpc_interface_request
    import aws_sdk_mediaconnect.types.flow_arn

class AddFlowVpcInterfacesRequest(TypedDict):
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>"""
    vpc_interfaces: NotRequired["aws_sdk_mediaconnect.types.__list_of_vpc_interface_request.__listOfVpcInterfaceRequest"]
    """<p> A list of VPC interfaces that you want to add to the flow.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AddFlowVpcInterfacesRequest) -> dict:
    out: dict = {}
    if "vpc_interfaces" in value:
        import aws_sdk_mediaconnect.types.__list_of_vpc_interface_request
        out["vpcInterfaces"] = aws_sdk_mediaconnect.types.__list_of_vpc_interface_request.serialize_json(value["vpc_interfaces"])
    return out


def deserialize_json(data: dict) -> AddFlowVpcInterfacesRequest:
    out: AddFlowVpcInterfacesRequest = {}  # type: ignore[typeddict-item]
    if "vpcInterfaces" in data:
        import aws_sdk_mediaconnect.types.__list_of_vpc_interface_request
        out["vpc_interfaces"] = aws_sdk_mediaconnect.types.__list_of_vpc_interface_request.deserialize_json(data["vpcInterfaces"])
    return out