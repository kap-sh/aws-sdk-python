"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowVpcInterfacesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_vpc_interface


class AddFlowVpcInterfacesResponse(TypedDict):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that these VPC interfaces were added to.</p>"""
    vpc_interfaces: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_vpc_interface.__listOfVpcInterface"
    ]
    """<p> The details of the newly added VPC interfaces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFlowVpcInterfacesResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "vpc_interfaces" in value:
        import aws_sdk_mediaconnect.types.__list_of_vpc_interface

        out["vpcInterfaces"] = (
            aws_sdk_mediaconnect.types.__list_of_vpc_interface.serialize_json(
                value["vpc_interfaces"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddFlowVpcInterfacesResponse:
    out: AddFlowVpcInterfacesResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "vpcInterfaces" in data:
        import aws_sdk_mediaconnect.types.__list_of_vpc_interface

        out["vpc_interfaces"] = (
            aws_sdk_mediaconnect.types.__list_of_vpc_interface.deserialize_json(
                data["vpcInterfaces"]
            )
        )
    return out
