"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetIdentityProviderByIdentifierResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.identity_provider_type


class GetIdentityProviderByIdentifierResponse(TypedDict, closed=True):
    identity_provider: "capo_cognito_identity_provider.types.identity_provider_type.IdentityProviderType"
    """<p>The configuration of the IdP in your user pool. Includes additional identifiers, the IdP name and type, and trust-relationship details like the issuer URL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIdentityProviderByIdentifierResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.identity_provider_type

    out["IdentityProvider"] = (
        capo_cognito_identity_provider.types.identity_provider_type.serialize_aws_json_1_1(
            value["identity_provider"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIdentityProviderByIdentifierResponse:
    out: GetIdentityProviderByIdentifierResponse = {}  # type: ignore[typeddict-item]
    if "IdentityProvider" in data:
        import capo_cognito_identity_provider.types.identity_provider_type

        out["identity_provider"] = (
            capo_cognito_identity_provider.types.identity_provider_type.deserialize_aws_json_1_1(
                data["IdentityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "GetIdentityProviderByIdentifierResponse.identity_provider required"
        )
    return out
