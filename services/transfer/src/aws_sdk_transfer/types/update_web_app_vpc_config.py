"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateWebAppVpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.subnet_ids
    import aws_sdk_transfer.types.web_app_vpc_endpoint_ip_address_type


class UpdateWebAppVpcConfig(TypedDict, closed=True):
    subnet_ids: NotRequired["aws_sdk_transfer.types.subnet_ids.SubnetIds"]
    """<p>The list of subnet IDs within the VPC where the web app endpoint should be deployed during the update operation.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_transfer.types.web_app_vpc_endpoint_ip_address_type.WebAppVpcEndpointIpAddressType"
    ]
    """<p>The IP address type for the web app's VPC endpoint. This determines whether the endpoint is accessible over IPv4 only, or over both IPv4 and IPv6.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebAppVpcConfig) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import aws_sdk_transfer.types.subnet_ids

        out["SubnetIds"] = aws_sdk_transfer.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "ip_address_type" in value:
        import aws_sdk_transfer.types.web_app_vpc_endpoint_ip_address_type

        out["IpAddressType"] = (
            aws_sdk_transfer.types.web_app_vpc_endpoint_ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWebAppVpcConfig:
    out: UpdateWebAppVpcConfig = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import aws_sdk_transfer.types.subnet_ids

        out["subnet_ids"] = aws_sdk_transfer.types.subnet_ids.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if "IpAddressType" in data:
        import aws_sdk_transfer.types.web_app_vpc_endpoint_ip_address_type

        out["ip_address_type"] = (
            aws_sdk_transfer.types.web_app_vpc_endpoint_ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    return out
