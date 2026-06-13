"""Generated from Smithy shape ``com.amazonaws.odb#ServiceNetworkEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.vpc_endpoint_type


class ServiceNetworkEndpoint(TypedDict):
    vpc_endpoint_id: NotRequired["str"]
    """<p>The identifier of the VPC endpoint.</p>"""
    vpc_endpoint_type: NotRequired[
        "aws_sdk_odb.types.vpc_endpoint_type.VpcEndpointType"
    ]
    """<p>The type of the VPC endpoint.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceNetworkEndpoint) -> dict:
    out: dict = {}
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    if "vpc_endpoint_type" in value:
        import aws_sdk_odb.types.vpc_endpoint_type

        out["vpcEndpointType"] = (
            aws_sdk_odb.types.vpc_endpoint_type.serialize_aws_json_1_0(
                value["vpc_endpoint_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceNetworkEndpoint:
    out: ServiceNetworkEndpoint = {}  # type: ignore[typeddict-item]
    if "vpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    if "vpcEndpointType" in data:
        import aws_sdk_odb.types.vpc_endpoint_type

        out["vpc_endpoint_type"] = (
            aws_sdk_odb.types.vpc_endpoint_type.deserialize_aws_json_1_0(
                data["vpcEndpointType"]
            )
        )
    return out
