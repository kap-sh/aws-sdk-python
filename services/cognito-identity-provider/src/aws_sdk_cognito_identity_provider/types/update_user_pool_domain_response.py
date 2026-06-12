"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateUserPoolDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.domain_type
    import aws_sdk_cognito_identity_provider.types.routing_type
    import aws_sdk_cognito_identity_provider.types.wrapped_integer_type


class UpdateUserPoolDomainResponse(TypedDict):
    managed_login_version: NotRequired[
        "aws_sdk_cognito_identity_provider.types.wrapped_integer_type.WrappedIntegerType"
    ]
    """<p>A version number that indicates the state of managed login for your domain. Version <code>1</code> is hosted UI (classic). Version <code>2</code> is the newer managed login with the branding editor. For more information, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html\">Managed login</a>.</p>"""
    cloud_front_domain: NotRequired[
        "aws_sdk_cognito_identity_provider.types.domain_type.DomainType"
    ]
    """<p>The fully-qualified domain name (FQDN) of the Amazon CloudFront distribution that hosts your managed login or classic hosted UI pages. You domain-name authority must have an alias record that points requests for your custom domain to this FQDN. Amazon Cognito returns this value if you set a custom domain with <code>CustomDomainConfig</code>. If you set an Amazon Cognito prefix domain, this operation returns a blank response.</p>"""
    routing: NotRequired[
        "aws_sdk_cognito_identity_provider.types.routing_type.RoutingType"
    ]
    """<p>The updated routing configuration for the user pool domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserPoolDomainResponse) -> dict:
    out: dict = {}
    if "managed_login_version" in value:
        out["ManagedLoginVersion"] = value["managed_login_version"]
    if "cloud_front_domain" in value:
        out["CloudFrontDomain"] = value["cloud_front_domain"]
    if "routing" in value:
        import aws_sdk_cognito_identity_provider.types.routing_type

        out["Routing"] = (
            aws_sdk_cognito_identity_provider.types.routing_type.serialize_aws_json_1_1(
                value["routing"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserPoolDomainResponse:
    out: UpdateUserPoolDomainResponse = {}  # type: ignore[typeddict-item]
    if "ManagedLoginVersion" in data:
        out["managed_login_version"] = data["ManagedLoginVersion"]
    if "CloudFrontDomain" in data:
        out["cloud_front_domain"] = data["CloudFrontDomain"]
    if "Routing" in data:
        import aws_sdk_cognito_identity_provider.types.routing_type

        out["routing"] = (
            aws_sdk_cognito_identity_provider.types.routing_type.deserialize_aws_json_1_1(
                data["Routing"]
            )
        )
    return out
