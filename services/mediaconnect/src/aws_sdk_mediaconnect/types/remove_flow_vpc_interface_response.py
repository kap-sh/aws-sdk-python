"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveFlowVpcInterfaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_string


class RemoveFlowVpcInterfaceResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that is associated with the VPC interface you removed.</p>"""
    non_deleted_network_interface_ids: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_string.__listOfString"
    ]
    """<p> IDs of network interfaces associated with the removed VPC interface that MediaConnect was unable to remove.</p>"""
    vpc_interface_name: NotRequired["str"]
    """<p> The name of the VPC interface that was removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveFlowVpcInterfaceResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "non_deleted_network_interface_ids" in value:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["nonDeletedNetworkInterfaceIds"] = (
            aws_sdk_mediaconnect.types.__list_of_string.serialize_json(
                value["non_deleted_network_interface_ids"]
            )
        )
    if "vpc_interface_name" in value:
        out["vpcInterfaceName"] = value["vpc_interface_name"]
    return out


def deserialize_json(data: dict) -> RemoveFlowVpcInterfaceResponse:
    out: RemoveFlowVpcInterfaceResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "nonDeletedNetworkInterfaceIds" in data:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["non_deleted_network_interface_ids"] = (
            aws_sdk_mediaconnect.types.__list_of_string.deserialize_json(
                data["nonDeletedNetworkInterfaceIds"]
            )
        )
    if "vpcInterfaceName" in data:
        out["vpc_interface_name"] = data["vpcInterfaceName"]
    return out
