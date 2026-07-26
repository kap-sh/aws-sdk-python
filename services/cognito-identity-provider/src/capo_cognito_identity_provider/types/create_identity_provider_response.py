"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateIdentityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.identity_provider_type


class CreateIdentityProviderResponse(TypedDict, closed=True):
    identity_provider: "capo_cognito_identity_provider.types.identity_provider_type.IdentityProviderType"
    """<p>The details of the new user pool IdP.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIdentityProviderResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.identity_provider_type

    out["IdentityProvider"] = (
        capo_cognito_identity_provider.types.identity_provider_type.serialize_aws_json_1_1(
            value["identity_provider"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIdentityProviderResponse:
    out: CreateIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if "IdentityProvider" in data:
        import capo_cognito_identity_provider.types.identity_provider_type

        out["identity_provider"] = (
            capo_cognito_identity_provider.types.identity_provider_type.deserialize_aws_json_1_1(
                data["IdentityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIdentityProviderResponse.identity_provider required"
        )
    return out
