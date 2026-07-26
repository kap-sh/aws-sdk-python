"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2ClientVpnEndpointClientConnectOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_status_details
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsEc2ClientVpnEndpointClientConnectOptionsDetails(TypedDict, closed=True):
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether client connect options are enabled. </p>"""
    lambda_function_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the Lambda function used for connection authorization. </p>"""
    status: NotRequired[
        "capo_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_status_details.AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails"
    ]
    """<p> The status of any updates to the client connect options. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2ClientVpnEndpointClientConnectOptionsDetails) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "lambda_function_arn" in value:
        out["LambdaFunctionArn"] = value["lambda_function_arn"]
    if "status" in value:
        import capo_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_status_details

        out["Status"] = (
            capo_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_status_details.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2ClientVpnEndpointClientConnectOptionsDetails:
    out: AwsEc2ClientVpnEndpointClientConnectOptionsDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "LambdaFunctionArn" in data:
        out["lambda_function_arn"] = data["LambdaFunctionArn"]
    if "Status" in data:
        import capo_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_status_details

        out["status"] = (
            capo_securityhub.types.aws_ec2_client_vpn_endpoint_client_connect_options_status_details.deserialize_json(
                data["Status"]
            )
        )
    return out
