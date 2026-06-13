"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Endpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.vpc_endpoint_list


class Endpoint(TypedDict):
    address: NotRequired["str"]
    """<p>The DNS address of the VPC endpoint.</p>"""
    port: NotRequired["int"]
    """<p>The port that Amazon Redshift Serverless listens on.</p>"""
    vpc_endpoints: NotRequired[
        "aws_sdk_redshift_serverless.types.vpc_endpoint_list.VpcEndpointList"
    ]
    """<p>An array of <code>VpcEndpoint</code> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Endpoint) -> dict:
    out: dict = {}
    if "address" in value:
        out["address"] = value["address"]
    if "port" in value:
        out["port"] = value["port"]
    if "vpc_endpoints" in value:
        import aws_sdk_redshift_serverless.types.vpc_endpoint_list

        out["vpcEndpoints"] = (
            aws_sdk_redshift_serverless.types.vpc_endpoint_list.serialize_aws_json_1_1(
                value["vpc_endpoints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if "address" in data:
        out["address"] = data["address"]
    if "port" in data:
        out["port"] = data["port"]
    if "vpcEndpoints" in data:
        import aws_sdk_redshift_serverless.types.vpc_endpoint_list

        out["vpc_endpoints"] = (
            aws_sdk_redshift_serverless.types.vpc_endpoint_list.deserialize_aws_json_1_1(
                data["vpcEndpoints"]
            )
        )
    return out
