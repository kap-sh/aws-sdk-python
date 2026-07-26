"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2ClientVpnEndpointAuthenticationOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_active_directory_details
    import capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_federated_authentication_details
    import capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_mutual_authentication_details
    import capo_securityhub.types.non_empty_string


class AwsEc2ClientVpnEndpointAuthenticationOptionsDetails(TypedDict, closed=True):
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The authentication type used. </p>"""
    active_directory: NotRequired[
        "capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_active_directory_details.AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails"
    ]
    """<p> Information about the Active Directory, if applicable. With Active Directory authentication, clients are authenticated against existing Active Directory groups. </p>"""
    mutual_authentication: NotRequired[
        "capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_mutual_authentication_details.AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails"
    ]
    """<p> Information about the authentication certificates, if applicable.</p>"""
    federated_authentication: NotRequired[
        "capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_federated_authentication_details.AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails"
    ]
    """<p> Information about the IAM SAML identity provider, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2ClientVpnEndpointAuthenticationOptionsDetails) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "active_directory" in value:
        import capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_active_directory_details

        out["ActiveDirectory"] = (
            capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_active_directory_details.serialize_json(
                value["active_directory"]
            )
        )
    if "mutual_authentication" in value:
        import capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_mutual_authentication_details

        out["MutualAuthentication"] = (
            capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_mutual_authentication_details.serialize_json(
                value["mutual_authentication"]
            )
        )
    if "federated_authentication" in value:
        import capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_federated_authentication_details

        out["FederatedAuthentication"] = (
            capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_federated_authentication_details.serialize_json(
                value["federated_authentication"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2ClientVpnEndpointAuthenticationOptionsDetails:
    out: AwsEc2ClientVpnEndpointAuthenticationOptionsDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "ActiveDirectory" in data:
        import capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_active_directory_details

        out["active_directory"] = (
            capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_active_directory_details.deserialize_json(
                data["ActiveDirectory"]
            )
        )
    if "MutualAuthentication" in data:
        import capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_mutual_authentication_details

        out["mutual_authentication"] = (
            capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_mutual_authentication_details.deserialize_json(
                data["MutualAuthentication"]
            )
        )
    if "FederatedAuthentication" in data:
        import capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_federated_authentication_details

        out["federated_authentication"] = (
            capo_securityhub.types.aws_ec2_client_vpn_endpoint_authentication_options_federated_authentication_details.deserialize_json(
                data["FederatedAuthentication"]
            )
        )
    return out
