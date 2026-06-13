"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#VpcEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.network_interface_list


class VpcEndpoint(TypedDict):
    vpc_endpoint_id: NotRequired["str"]
    """<p>The connection endpoint ID for connecting to Amazon Redshift Serverless.</p>"""
    vpc_id: NotRequired["str"]
    """<p>The VPC identifier that the endpoint is associated with.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_redshift_serverless.types.network_interface_list.NetworkInterfaceList"
    ]
    """<p>One or more network interfaces of the endpoint. Also known as an interface endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcEndpoint) -> dict:
    out: dict = {}
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "network_interfaces" in value:
        import aws_sdk_redshift_serverless.types.network_interface_list

        out["networkInterfaces"] = (
            aws_sdk_redshift_serverless.types.network_interface_list.serialize_aws_json_1_1(
                value["network_interfaces"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcEndpoint:
    out: VpcEndpoint = {}  # type: ignore[typeddict-item]
    if "vpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "networkInterfaces" in data:
        import aws_sdk_redshift_serverless.types.network_interface_list

        out["network_interfaces"] = (
            aws_sdk_redshift_serverless.types.network_interface_list.deserialize_aws_json_1_1(
                data["networkInterfaces"]
            )
        )
    return out
