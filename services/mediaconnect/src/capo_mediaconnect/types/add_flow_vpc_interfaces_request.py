"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowVpcInterfacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_vpc_interface_request
    import capo_mediaconnect.types.flow_arn


class AddFlowVpcInterfacesRequest(TypedDict, closed=True):
    flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>"""
    vpc_interfaces: NotRequired[
        "capo_mediaconnect.types.__list_of_vpc_interface_request.__listOfVpcInterfaceRequest"
    ]
    """<p> A list of VPC interfaces that you want to add to the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFlowVpcInterfacesRequest) -> dict:
    out: dict = {}
    if "vpc_interfaces" in value:
        import capo_mediaconnect.types.__list_of_vpc_interface_request

        out["vpcInterfaces"] = (
            capo_mediaconnect.types.__list_of_vpc_interface_request.serialize_json(
                value["vpc_interfaces"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddFlowVpcInterfacesRequest:
    out: AddFlowVpcInterfacesRequest = {}  # type: ignore[typeddict-item]
    if "vpcInterfaces" in data:
        import capo_mediaconnect.types.__list_of_vpc_interface_request

        out["vpc_interfaces"] = (
            capo_mediaconnect.types.__list_of_vpc_interface_request.deserialize_json(
                data["vpcInterfaces"]
            )
        )
    return out
