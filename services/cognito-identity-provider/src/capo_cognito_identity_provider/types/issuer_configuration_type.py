"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#IssuerConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.issuer_type


class IssuerConfigurationType(TypedDict, closed=True):
    type: NotRequired["capo_cognito_identity_provider.types.issuer_type.IssuerType"]
    """<p>The type of issuer configuration. Determines the token issuing behavior for the user pool.</p> <dl> <dt>ORIGINAL</dt> <dd> <p>The original issuer configuration for user pools. The issuer URL is hosted in the user pool’s region and provides OIDC endpoints specific to that region.</p> <p>Original issuers have the format of <code>https://cognito-idp.[region].amazonaws.com/[userPoolId]</code> </p> </dd> <dt>UPDATED</dt> <dd> <p>Recommended for all user pools, including for multi-Region replication. Updated issuers host the same JWKS content in multiple regions, resulting in improved resilience and efficiency.</p> <p>Updated issuers have the format of <code>https://issuer-cognito-idp.[region].amazonaws.com/[userPoolId]</code>, where region is the primary Amazon Web Services Region of your user pool.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IssuerConfigurationType) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_cognito_identity_provider.types.issuer_type

        out["Type"] = (
            capo_cognito_identity_provider.types.issuer_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IssuerConfigurationType:
    out: IssuerConfigurationType = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_cognito_identity_provider.types.issuer_type

        out["type"] = (
            capo_cognito_identity_provider.types.issuer_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
