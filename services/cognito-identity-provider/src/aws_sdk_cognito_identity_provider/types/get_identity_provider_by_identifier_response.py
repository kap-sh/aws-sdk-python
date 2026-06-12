"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetIdentityProviderByIdentifierResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.identity_provider_type


class GetIdentityProviderByIdentifierResponse(TypedDict):
    identity_provider: "aws_sdk_cognito_identity_provider.types.identity_provider_type.IdentityProviderType"
    """<p>The configuration of the IdP in your user pool. Includes additional identifiers, the IdP name and type, and trust-relationship details like the issuer URL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIdentityProviderByIdentifierResponse) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.identity_provider_type

    out["IdentityProvider"] = (
        aws_sdk_cognito_identity_provider.types.identity_provider_type.serialize_aws_json_1_1(
            value["identity_provider"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIdentityProviderByIdentifierResponse:
    out: GetIdentityProviderByIdentifierResponse = {}  # type: ignore[typeddict-item]
    if "IdentityProvider" in data:
        import aws_sdk_cognito_identity_provider.types.identity_provider_type

        out["identity_provider"] = (
            aws_sdk_cognito_identity_provider.types.identity_provider_type.deserialize_aws_json_1_1(
                data["IdentityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "GetIdentityProviderByIdentifierResponse.identity_provider required"
        )
    return out
