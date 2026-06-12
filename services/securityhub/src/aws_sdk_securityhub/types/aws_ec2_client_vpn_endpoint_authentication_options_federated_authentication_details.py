"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails(
    TypedDict
):
    saml_provider_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the IAM SAML identity provider. </p>"""
    self_service_saml_provider_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the IAM SAML identity provider for the self-service portal. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails,
) -> dict:
    out: dict = {}
    if "saml_provider_arn" in value:
        out["SamlProviderArn"] = value["saml_provider_arn"]
    if "self_service_saml_provider_arn" in value:
        out["SelfServiceSamlProviderArn"] = value["self_service_saml_provider_arn"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails:
    out: AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails = {}  # type: ignore[typeddict-item]
    if "SamlProviderArn" in data:
        out["saml_provider_arn"] = data["SamlProviderArn"]
    if "SelfServiceSamlProviderArn" in data:
        out["self_service_saml_provider_arn"] = data["SelfServiceSamlProviderArn"]
    return out
