"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2ClientVpnEndpointAuthenticationOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_details

AwsEc2ClientVpnEndpointAuthenticationOptionsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_details.AwsEc2ClientVpnEndpointAuthenticationOptionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2ClientVpnEndpointAuthenticationOptionsList) -> list:
    import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2ClientVpnEndpointAuthenticationOptionsList:
    import aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_details

    out: AwsEc2ClientVpnEndpointAuthenticationOptionsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_details.deserialize_json(
                item
            )
        )
    return out
